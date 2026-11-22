"""Symbolic identities for the fixed capped-volume KE barrier.

This is NOT a proof of analytic positivity, cover, or actual KE convergence.
Requires Python 3 and sympy.
"""
import sympy as sp

b, eps, s, alpha, X, L = sp.symbols("b eps s alpha X L", positive=True)
chi = s / (s + eps)
mu = 2 * (chi * (1 - chi) / alpha + chi ** 2 / alpha ** 2)
Q = 2 * b * (eps * alpha + s) / (alpha ** 2 * (s + eps) ** 2)
assert sp.simplify(mu * b / s - Q) == 0

# Central source (x,y,z)=(sqrt(t)*X,sqrt(t)*Y,XY).
Qcentral = sp.factor((eps * Q).subs(s, b * eps * X ** 2))
expected = 2 * b * (alpha + b * X ** 2) / (alpha ** 2 * (1 + b * X ** 2) ** 2)
assert sp.simplify(Qcentral - expected) == 0
assert sp.simplify(Qcentral.subs(X, 0) - 2 * b / alpha) == 0

beta = sp.symbols("beta", real=True)
assert sp.simplify(L ** (-2) / L ** (beta - 4) - L ** (2 - beta)) == 0

m1, m2, m3, B1, B2 = sp.symbols("m1 m2 m3 B1 B2", positive=True)
v1, v2, v3 = sp.Matrix([[1, 0]]), sp.Matrix([[0, 1]]), sp.Matrix([[-B1, -B2]])
H = m1 * (v1.T * v1) + m2 * (v2.T * v2) + m3 * (v3.T * v3)
assert sp.simplify(H.det() - (m1 * m2 + m1 * m3 * B2 ** 2 + m2 * m3 * B1 ** 2)) == 0

print("PASS: cap coefficient, source rescaling, beta exponent, triple minors")
