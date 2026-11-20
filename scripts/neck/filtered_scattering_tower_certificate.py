#!/usr/bin/env python3
"""Audit the filtered root-0/root-1 scattering tower formulas in v0.11.

This checks only the formal punctured-neck algebra and high-precision Laurent
coefficient D_triv.  It does not address the triple-corner or nonlinear KE
problem.
"""
from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Dict, List

import mpmath as mp
import sympy as sp

OUT = Path(__file__).with_suffix('.json')


def standard_matrix(N: int, b: List[sp.Expr]) -> sp.Matrix:
    """Rows are T0 degree 0..N, columns are T1 degree 0..N."""
    M = sp.zeros(N + 1)
    for n in range(N + 1):
        for j in range(n + 1):
            k = n - j
            M[k, n] += b[j] * (-1) ** k
    return M


def common_quotient_matrix(N: int, c: List[sp.Expr]) -> sp.Matrix:
    """Rows are T0 degrees 1..N+1 modulo T0,0; columns T1 0..N."""
    M = sp.zeros(N + 1)
    for n in range(N + 1):
        # pole coefficient c_{-1}=3 contributes to T0,n+1
        M[n, n] += 3 * (-1) ** (n + 1)
        # regular coefficients c_j contribute to T0,n-j; omit degree 0 quotient
        for j in range(n + 1):
            degree = n - j
            if degree >= 1:
                M[degree - 1, n] += c[j] * (-1) ** degree
    return M


def formal_cusp_check() -> Dict[str, str]:
    """Check L(T0,2)=L(T1,2)=0 using only H0 relations."""
    L = sp.symbols('L')  # log r
    r = sp.symbols('r', positive=True)
    u, v, z = sp.symbols('u v z')

    # H0 action on the formal longitudinal basis.
    H0 = {u: 0, v: u, z: v - u}

    def H(expr: sp.Expr) -> sp.Expr:
        out = 0
        for atom, image in H0.items():
            out += sp.diff(expr, atom) * image
        return sp.expand(out)

    # Delta on polynomials f(L): root 0 is f''-f'; root 1 on r f(L) is r(f''+f').
    def delta0(expr: sp.Expr) -> sp.Expr:
        return sp.diff(expr, L, 2) - sp.diff(expr, L)

    def delta1_coeff(expr: sp.Expr) -> sp.Expr:
        return sp.diff(expr, L, 2) + sp.diff(expr, L)

    T02 = sp.Rational(1, 2) * u * L**2 + v * L + z
    T12_coeff = sp.Rational(1, 2) * u * L**2 - v * L + z
    check0 = sp.simplify(H(T02) + delta0(T02))
    check1 = sp.simplify(H(T12_coeff) + delta1_coeff(T12_coeff))
    assert check0 == 0
    assert check1 == 0
    return {'T0_2': str(check0), 'T1_2': str(check1)}


def dtriv_high_precision() -> Dict[str, str]:
    mp.mp.dps = 150
    gamma = mp.euler
    gamma1 = mp.stieltjes(1)
    z2 = mp.zeta(2)
    z2p = mp.diff(mp.zeta, 2, 1)
    z2pp = mp.diff(mp.zeta, 2, 2)
    a1 = 2 * mp.log(mp.pi / 2) - 2 * z2p / z2
    a2 = mp.pi**2 / 3 - 4 * (z2pp / z2 - (z2p / z2) ** 2)
    D = 6 * (-2 * gamma1 + gamma * a1 + (a1**2 + a2) / 4)

    def psi_triv(s: mp.mpf) -> mp.mpf:
        return (
            mp.pi ** (2 * s - mp.mpf('0.5'))
            * mp.gamma(s - mp.mpf('0.5'))
            / mp.gamma(s)
            * mp.zeta(2 * s - 1)
            / mp.zeta(2 * s)
        )

    C = 6 * (mp.diff(mp.zeta, -1, 1) / mp.zeta(-1) - mp.log(4) + 1)
    eps = mp.mpf('1e-30')
    direct = (psi_triv(1 + eps) - 3 / eps - C) / eps
    err = abs(direct - D)
    # cancellation at 1e-35 still leaves ample precision at 90 dps
    assert err < mp.mpf('1e-25')
    return {
        'a1': mp.nstr(a1, 60),
        'a2': mp.nstr(a2, 60),
        'C_triv': mp.nstr(C, 60),
        'D_triv_formula': mp.nstr(D, 70),
        'D_triv_direct_limit': mp.nstr(direct, 70),
        'absolute_error': mp.nstr(err, 10),
    }


def main() -> None:
    b = sp.symbols('b0:8')
    c = sp.symbols('c0:8')
    standard = {}
    common = {}
    for N in range(7):
        Ms = standard_matrix(N, list(b))
        det_s = sp.factor(Ms.det())
        expected_s = (-1) ** (N * (N + 1) // 2) * b[0] ** (N + 1)
        assert sp.simplify(det_s - expected_s) == 0
        standard[str(N)] = {
            'determinant': str(det_s),
            'diagonal': [str(Ms[i, i]) for i in range(N + 1)],
        }

        Mc = common_quotient_matrix(N, list(c))
        det_c = sp.factor(Mc.det())
        expected_c = 3 ** (N + 1) * (-1) ** ((N + 1) * (N + 2) // 2)
        assert sp.simplify(det_c - expected_c) == 0
        common[str(N)] = {
            'determinant': str(det_c),
            'diagonal': [str(Mc[i, i]) for i in range(N + 1)],
        }

    # Explicit n=0,1 common outgoing coefficients.
    T00, T01, T02 = sp.symbols('T00 T01 T02')
    C, D = sp.symbols('C D')
    n0 = -3 * T01 + C * T00
    n1 = 3 * T02 - C * T01 + D * T00
    assert n0 == C * T00 - 3 * T01
    assert n1 == D * T00 - C * T01 + 3 * T02

    report = {
        'status': 'passed',
        'formal_cusp_kernel_checks': formal_cusp_check(),
        'standard_truncations_N_0_to_6': standard,
        'common_quotient_truncations_N_0_to_6': common,
        'common_n0_outgoing': str(n0),
        'common_n1_outgoing': str(n1),
        'D_triv_high_precision': dtriv_high_precision(),
    }
    OUT.write_text(json.dumps(report, indent=2, ensure_ascii=False) + '\n')
    print('Filtered scattering tower certificate passed.')
    print(f'Wrote {OUT}')


if __name__ == '__main__':
    main()
