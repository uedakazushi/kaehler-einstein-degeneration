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

## 六次基底の対称性の区別
$\mathcal C_6$ は全 $S_6$ の座標置換で不変だが、六つの同時Petersen分岐木系は $S_6$ の一軌道をなし、単独の選択の安定化群は指数6（位数120）。従って、位相上の比較 $B_6(T)\to \mathcal C_6$ をラベル付きで全 $S_6$ 対称にするなら、一つの固定木系だけでは不十分で、六つの選択をともに管理する。厳密な組合せ証明は Lagrangianの base_topology.tex。これはactual KE計量の対称性や極限解析の証明ではない。

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
## 人工基底計量の定量的GH収縮
分岐木の系 T を固定し、Lagrangian基底の p_T:B_d(T)→C_d に対し、任意の補助PL Euclidean計量 h と \varepsilon>0 から
\[
|v|_\varepsilon^2=|dp_T(v)|_\square^2+\varepsilon^2|v|_h^2
\]
という内在的長さ計量を構成できる。有限木fiberの一様径と、unit squareがambient R^dで凸であることを用いる有限gallery liftingから
\[
0\le d_\varepsilon(x,y)-d_\square(p_Tx,p_Ty)\le C(d,T,h)\varepsilon
\]
が得られ、d_GH≤C\varepsilon/2。d≥6でも基底の非同相性と収束が両立する。厳密な証明は lagrangian-torus-fibration/papers/sections/paper/base_topology.tex の topo:metric-collapse。本研究Part Vには帰結と出典を示した。これは人工的な距離についての定理であり、actual KE距離と作用アフィン基底距離の比較のための解析入力を与えない。一般的な新規性は未確認。

