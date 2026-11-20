# 研究ノート：一般型超曲面のKE退化
更新：2026-11-20 / v1.1

## Cubical modelと有限計算
\(\mathcal C_5=\{w\in[0,1]^5:\max_iw_i=1,\ |\operatorname{supp}w|\le3\}\)。
25 vertices、50 edges、30 squares、Euler characteristic 5、\(H_2=\mathbb Z^4\)。標準cubical metricのdiameter \(\sqrt{13}\) はLibrary v0.12内の計算結果であり、今回回収したPart Vに有限gallery証明があり、対応するexact gallery scriptを再実行した。下限・等号分類と解析全体を機械検証したことは意味しない。

## 任意次数の候補複体とLagrangian基底（新しい横断検証）
固定次数 \(d\ge5\) について
\[
\mathcal C_d=\{w\in[0,1]^d:\max_i w_i=1,\ |\operatorname{supp}w|\le3\}
\]
は \(w\mapsto w/(\sum_iw_i)\) で \(\operatorname{Sk}_2\Delta^{d-1}\) に同相であり、逆は \(x\mapsto x/\max_i x_i\)。セル数は
\[
(f_0,f_1,f_2)=\left(\binom d1+\binom d2+\binom d3,\ d\binom d2,\ d\binom{d-1}{2}\right),
\quad \widetilde H_2(\mathcal C_d;\mathbb Z)=\mathbb Z^{\binom{d-1}{3}}.
\]
一般次数の証明は `papers/cubical-gh-limit.tex` の `prop:degree-d-cubical-topology` に統合した。Lagrangian研究の \(B_d(T)\) からは、分岐木を収縮するcell-like homotopy equivalence \(B_d(T)\to\mathcal C_d\) が得られるが、\(d\ge6\) で同相ではない。これは構成の**位相的比較**であり、KE距離、action atlas、special Lagrangianを同一視しない。有限次数 \(d=5,6,7,8\) の境界行列の独立検算（有理数体の階数および有限体の階数）は関連研究 `lagrangian-torus-fibration/verification/verify_ke_base_topology.py` と対応する。

## Leading synchronization
\(L_t=-\log|t|^2,\ R_t=\log L_t\)。三重点の \(xyz=t\vartheta\) から \(\ell_x+\ell_y+\ell_z=L_t+O(1)\)。Neck/corner incidenceでは
\[
\log\Lambda_{xy}=R_t+\log(1-p_z)+O(L_t^{-1})
\]
が成立する範囲を特定する。Overlap-compatibleで \(\max_e|\tau_{e,t}|=o(R_t)\) ならfirst-scale cubical modelのdistortionは消える。ただしactual KE metricでsublinear correctionを示すことが残る。

## Mandel zero modes、degree jumpと解析障害
\(u_0(w)=(1+w^2)^{-2}\) はscale、\(u_1(w)=(w+w^3/3)(1+w^2)^{-2}\) はend-degree/asymmetryのJacobi方向。Five-source relative jump \(a_+-a_-=5\) はcusp trivializationに依存し、balance \(5=2+3\) と整合させる。Filtered root-1 tracesを含むnonlinear Lyapunov–Schmidt/scattering matchingのuniform controlが主障害。

## 再現性
旧v0.12原稿の16検算は元の配布ZIPに基づきSHA-256を照合し、全件再実行した。統合稿の補助検算5本も再実行済み。出典・ハッシュは `source-manifest.json`、結果は `validation.json`。
