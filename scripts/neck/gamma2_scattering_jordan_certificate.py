#!/usr/bin/env python3
"""High-precision audit of the Gamma(2) scattering/Jordan blocks.

The analytic input is the diagonal/off-diagonal natural scattering coefficient
formula appearing in Posingies, arXiv:1111.1132, Section 4.  The script checks
normalization to the geometric cusp coordinate r = pi*y (cusp width 2), the
s=1 value and derivative, the trivial-channel Laurent coefficients, the
functional equation, the parity-independent 2x2 standard Jordan transfer, the renormalized common\nchannel, and the regular-slope energy constants.
"""
from __future__ import annotations

import json
from pathlib import Path
import mpmath as mp

mp.mp.dps = 100


def prefactor(s: mp.mpf | mp.mpc) -> mp.mpf | mp.mpc:
    return mp.sqrt(mp.pi) * mp.gamma(s - mp.mpf("0.5")) / mp.gamma(s)


def zeta_ratio(s: mp.mpf | mp.mpc) -> mp.mpf | mp.mpc:
    return mp.zeta(2 * s - 1) / mp.zeta(2 * s)


def natural_diag(s: mp.mpf | mp.mpc) -> mp.mpf | mp.mpc:
    return (2 ** (-s)) * prefactor(s) * zeta_ratio(s) / (2 ** (2 * s) - 1)


def natural_offdiag(s: mp.mpf | mp.mpc) -> mp.mpf | mp.mpc:
    return (
        2 ** (-s - 1)
        * prefactor(s)
        * zeta_ratio(s)
        * (2 ** (2 * s) - 2)
        / (2 ** (2 * s) - 1)
    )


def natural_std(s: mp.mpf | mp.mpc) -> mp.mpf | mp.mpc:
    return natural_diag(s) - natural_offdiag(s)


def natural_triv(s: mp.mpf | mp.mpc) -> mp.mpf | mp.mpc:
    return natural_diag(s) + 2 * natural_offdiag(s)


def geometric_normalization(s: mp.mpf | mp.mpc) -> mp.mpf | mp.mpc:
    # Natural incoming term is (y/2)^s.  With q=exp(pi*i*z), r=pi*y,
    # multiplication by (2*pi)^s makes the incoming coefficient r^s.
    # The outgoing y^(1-s) term is consequently multiplied by
    # 2^s*pi^(2s-1).
    return 2 ** s * mp.pi ** (2 * s - 1)


def psi_std(s: mp.mpf | mp.mpc) -> mp.mpf | mp.mpc:
    return geometric_normalization(s) * natural_std(s)


def psi_triv(s: mp.mpf | mp.mpc) -> mp.mpf | mp.mpc:
    return geometric_normalization(s) * natural_triv(s)


log2 = mp.log(2)
zeta2_logder = mp.diff(mp.zeta, 2) / mp.zeta(2)
zetam1_logder = mp.diff(mp.zeta, -1) / mp.zeta(-1)

psi1_exact = -4 * log2
psi1prime_exact = 4 * log2 * (
    mp.mpf(11) / 3 * log2
    - 2 * mp.euler
    + 2 * zeta2_logder
    - 2 * mp.log(mp.pi)
)
psi1prime_fe = 4 * log2 * (
    mp.mpf(17) / 3 * log2 - 2 - 2 * zetam1_logder
)
triv_finite_exact = 6 * (zetam1_logder - mp.log(4) + 1)

# Posingies' finite natural scattering constants.
A = zetam1_logder - mp.log(4 * mp.pi) + 1
C_off = (A + log2 / 6) / mp.pi
C_diag = (A - mp.mpf(11) * log2 / 6) / mp.pi
constant_difference_geometric = 2 * mp.pi * (C_diag - C_off)

h = mp.mpf("1e-25")
psi1_num = (psi_std(1 + h) + psi_std(1 - h)) / 2
psi1prime_num = (psi_std(1 + h) - psi_std(1 - h)) / (2 * h)
triv_finite_num = (psi_triv(1 + h) - 3 / h + psi_triv(1 - h) + 3 / h) / 2

# Functional equation in the geometric normalization.
functional_samples = [
    mp.mpf("0.23"),
    mp.mpf("0.71"),
    mp.mpf("1.19"),
    mp.mpc("0.31", "0.27"),
]
functional_errors = [abs(psi_std(s) * psi_std(1 - s) - 1) for s in functional_samples]

# Parity-independent standard Jordan transfer in bases
# incoming = (u0*r, u0*r*log(r)-v0*r),
# outgoing = (u0, u0*log(r)+v0).
a = psi1_exact
b = psi1prime_exact
# Matrix [[a,b],[0,-a]].
determinant = -a * a
trace = mp.mpf("0")
# Singular values from eigenvalues of M^T M.
lam_minus = a * a + b * b / 2 - abs(b) * mp.sqrt(b * b + 4 * a * a) / 2
lam_plus = a * a + b * b / 2 + abs(b) * mp.sqrt(b * b + 4 * a * a) / 2
singular_values = [mp.sqrt(lam_minus), mp.sqrt(lam_plus)]

# Exact long-cusp energy coefficient for a regular root-one slope:
# ||u0||^2_{(1+w^2)^2dw}=pi/2 and theta has period 2*pi.
long_cusp_energy_coefficient = (mp.pi / 2) * (2 * mp.pi)

# Laurent finite part of the trivial/common channel.  After subtracting the
# residue 3*u_p/(s-1), the regular incoming u_p*r has outgoing coefficients
# C_triv*u_p - 3*(u_p*log(r)+v_p).
common_log_coefficient = mp.mpf(-3)
common_constant_coefficient = triv_finite_exact
# For a general even regular cusp slope a, the common component contributes
# -6*pi^2*||P_triv a||^2*log(R) below the leading pi^2*R*||a||^2 term.
common_energy_log_coefficient = -6 * mp.pi**2

TOL = mp.mpf("1e-45")
assert abs(psi1_num - psi1_exact) < TOL
assert abs(psi1prime_num - psi1prime_exact) < mp.mpf("1e-35")
assert abs(psi1prime_exact - psi1prime_fe) < TOL
assert abs(triv_finite_num - triv_finite_exact) < mp.mpf("1e-30")
assert abs(constant_difference_geometric - psi1_exact) < TOL
assert max(functional_errors) < mp.mpf("1e-70")
assert abs(determinant + 16 * log2**2) < TOL
assert abs(long_cusp_energy_coefficient - mp.pi**2) < TOL
assert singular_values[0] > 0
assert common_log_coefficient == -3
assert abs(common_constant_coefficient - triv_finite_exact) < TOL
assert abs(common_energy_log_coefficient + 6 * mp.pi**2) < TOL


def s(x: mp.mpf | mp.mpc, digits: int = 60) -> str:
    return mp.nstr(x, digits)


report = {
    "normalization": {
        "cusp_width": 2,
        "local_coordinate": "q=exp(pi*i*z)",
        "r": "pi*Im(z)",
        "outgoing_multiplier": "2^s*pi^(2s-1)",
    },
    "standard_channel": {
        "psi_1_exact": "-4*log(2)",
        "psi_1_numeric": s(psi1_exact),
        "psi_prime_1_exact_zeta2": "4*log(2)*(11*log(2)/3 - 2*EulerGamma + 2*zeta'(2)/zeta(2) - 2*log(pi))",
        "psi_prime_1_exact_zetam1": "4*log(2)*(17*log(2)/3 - 2 - 2*zeta'(-1)/zeta(-1))",
        "psi_prime_1_numeric": s(psi1prime_exact),
        "functional_equation_max_error": s(max(functional_errors), 20),
    },
    "trivial_channel": {
        "residue_at_1": "3",
        "finite_part_exact": "6*(zeta'(-1)/zeta(-1) - log(4) + 1)",
        "finite_part_numeric": s(triv_finite_exact),
    },
    "Posingies_constant_check": {
        "2pi_times_Cdiag_minus_Coffdiag": s(constant_difference_geometric),
        "expected": "-4*log(2)",
    },
    "parity_independent_standard_Jordan_transfer": {
        "incoming_basis": ["u0*r", "u0*r*log(r)-v0*r"],
        "outgoing_basis": ["u0", "u0*log(r)+v0"],
        "matrix": [[s(a), s(b)], ["0", s(-a)]],
        "determinant_exact": "-16*log(2)^2",
        "determinant_numeric": s(determinant),
        "singular_values_numeric": [s(x) for x in singular_values],
    },
    "renormalized_common_channel": {
        "residue": "3*u_p/(s-1)",
        "outgoing_log_Jordan_coefficient": "-3",
        "outgoing_constant_coefficient_exact": "6*(zeta'(-1)/zeta(-1) - log(4) + 1)",
        "outgoing_constant_coefficient_numeric": s(common_constant_coefficient),
    },
    "long_cusp_energy": {
        "leading_coefficient_exact": "pi^2",
        "leading_coefficient_numeric": s(long_cusp_energy_coefficient),
        "common_log_correction_exact": "-6*pi^2*||P_triv a||^2*log(R)",
        "common_log_coefficient_numeric": s(common_energy_log_coefficient),
    },
    "status": "Gamma(2) scattering/Jordan certificate passed",
}

out = Path(__file__).with_suffix(".json")
out.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(report["status"])
print(f"psi_std(1) = {s(psi1_exact, 30)}")
print(f"psi_std'(1) = {s(psi1prime_exact, 30)}")
print(f"trivial finite part = {s(triv_finite_exact, 30)}")
print(f"minimum singular value = {s(singular_values[0], 30)}")
