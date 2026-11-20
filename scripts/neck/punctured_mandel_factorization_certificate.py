#!/usr/bin/env python3
"""Exact symbolic certificate for the punctured Mandel linear operator.

Checks only finite symbolic identities used in the manuscript:
- Pöschl--Teller conjugation and supersymmetric factorization;
- longitudinal zero modes, Wronskian, and Jordan partners;
- the distributional constant-mode Green profile and T-scaling;
- a numerical sanity check of the high-frequency Green bound.

It does not replace the functional-analytic proofs concerning spectral calculus,
cusp-weighted spaces, or nonlinear gluing.
"""
from __future__ import annotations

import math
from pathlib import Path

import sympy as sp
from scipy.integrate import solve_ivp


def assert_zero(expr: sp.Expr, name: str) -> None:
    value = sp.simplify(sp.trigsimp(expr))
    if value != 0:
        raise AssertionError(f"{name} failed: {value}")


def main() -> None:
    s, w, z, T = sp.symbols("s w z T", real=True, positive=False)
    y = sp.Function("y")(s)
    c = sp.cosh(s)

    # d/dw after w=sinh(s)
    def d_w(expr: sp.Expr) -> sp.Expr:
        return sp.simplify(sp.diff(expr, s) / c)

    f = c ** (-sp.Rational(5, 2)) * y
    h0_conjugated = sp.simplify(
        (1 + sp.sinh(s) ** 2) * d_w(d_w(f))
        + 6 * sp.sinh(s) * d_w(f)
        + 4 * f
    )
    target = c ** (-sp.Rational(5, 2)) * (
        sp.diff(y, s, 2)
        - sp.Rational(9, 4) * y
        + sp.Rational(15, 4) * sp.sech(s) ** 2 * y
    )
    assert_zero(h0_conjugated - target, "Pöschl--Teller conjugation")

    # Q^*Q = -d_s^2 + 9/4 - 15/4 sech^2(s)
    a = sp.Rational(3, 2) * sp.tanh(s)
    potential_from_qstarq = sp.simplify(a**2 - sp.diff(a, s))
    assert_zero(
        potential_from_qstarq
        - (sp.Rational(9, 4) - sp.Rational(15, 4) * sp.sech(s) ** 2),
        "Q-star-Q potential",
    )

    w = sp.symbols("w", real=True)

    def H0(expr: sp.Expr) -> sp.Expr:
        return sp.simplify((1 + w**2) * sp.diff(expr, w, 2) + 6 * w * sp.diff(expr, w) + 4 * expr)

    u0 = (1 + w**2) ** -2
    u1 = (w + w**3 / sp.Integer(3)) / (1 + w**2) ** 2
    assert_zero(H0(u0), "H0 u0")
    assert_zero(H0(u1), "H0 u1")
    assert_zero(
        u0 * sp.diff(u1, w) - u1 * sp.diff(u0, w) - (1 + w**2) ** -3,
        "Wronskian",
    )

    v0 = (
        w**3 * sp.atan(w)
        + w**2
        + 3 * w * sp.atan(w)
        - sp.log(1 + w**2)
        + 2
    ) / (6 * (1 + w**2) ** 2)
    v1 = (
        -2 * w**3
        + 3 * w * (w**2 + 3) * sp.log(1 + w**2)
        - 30 * w
        + 12 * sp.atan(w)
    ) / (54 * (1 + w**2) ** 2)
    assert_zero(H0(v0) - u0, "H0 v0 = u0")
    assert_zero(H0(v1) - u1, "H0 v1 = u1")

    # Even Green profile for the base-constant source.  Away from zero it is u1
    # up to sign; the derivative jump is 2*pi.
    m0_plus = sp.pi * u1
    m0_minus = -sp.pi * u1
    assert_zero(H0(m0_plus), "m0 on w>0")
    assert_zero(H0(m0_minus), "m0 on w<0")
    jump = sp.simplify(sp.limit(sp.diff(m0_plus, w), w, 0, dir="+") - sp.limit(sp.diff(m0_minus, w), w, 0, dir="-"))
    assert_zero(jump - 2 * sp.pi, "m0 derivative jump")

    # T-rescaling identity, away from the source.
    z, T = sp.symbols("z T", real=True, positive=True)
    m = sp.Function("m")
    scaled = T * m(T * z)
    lhs_scaled = sp.simplify(
        (z**2 + T**-2) * sp.diff(scaled, z, 2)
        + 6 * z * sp.diff(scaled, z)
        + 4 * scaled
    )
    W = sp.symbols("W", real=True)
    expected = T * (
        (1 + W**2) * sp.diff(m(W), W, 2)
        + 6 * W * sp.diff(m(W), W)
        + 4 * m(W)
    )
    expected = expected.subs(W, T * z)
    assert_zero(lhs_scaled - expected, "T scaling")

    # Numerical sanity check of the bound -m_lambda(0) <= pi/sqrt(lambda^2-4)
    # using the resolvent kernel of the conjugated Pöschl--Teller operator.
    def green_at_zero(lam: float) -> float:
        S = 18.0
        k = math.sqrt(lam * lam + 9.0 / 4.0)

        def rhs(sv, Y):
            yy, yp = Y
            pot = 9.0 / 4.0 - 15.0 / 4.0 / (math.cosh(sv) ** 2) + lam * lam
            return [yp, pot * yy]

        initial = [math.exp(-k * S), -k * math.exp(-k * S)]
        sol = solve_ivp(rhs, (S, 0.0), initial, rtol=1e-11, atol=1e-14, method="DOP853")
        if not sol.success:
            raise RuntimeError(sol.message)
        y0, yp0 = sol.y[0, -1], sol.y[1, -1]
        # For an even Green kernel, 2*y'(0+)=-2*pi.
        scale = -math.pi / yp0
        return scale * y0

    checked = []
    for lam in (2.25, 3.0, 5.0, 9.0):
        value = green_at_zero(lam)
        bound = math.pi / math.sqrt(lam * lam - 4.0)
        if not (0.0 <= value <= bound * (1 + 2e-6)):
            raise AssertionError((lam, value, bound))
        checked.append((lam, value, bound))

    output = Path(__file__).with_suffix(".txt")
    output.write_text(
        "Punctured Mandel factorization certificate passed.\n"
        "Verified: conjugation, Q*Q, zero/Jordan modes, Wronskian, "
        "distributional jump, T-scaling, and numerical high-frequency bounds.\n"
        + "\n".join(f"lambda={lam:.2f}: -m(0)={val:.12g}, bound={bd:.12g}" for lam, val, bd in checked)
        + "\n",
        encoding="utf-8",
    )
    print(output.read_text(encoding="utf-8"), end="")


if __name__ == "__main__":
    main()
