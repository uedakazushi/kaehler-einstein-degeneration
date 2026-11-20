# 研究ノート：一般型超曲面のKE退化
更新：2026-11-20 / v1.2

## KE尺度とLagrangian fibrationの比較
標準規格化 $\operatorname{Ric}(\omega_t)=-\omega_t$ では体積 $2\pi^2d(d-4)^2$ は固定され、成分内部の基点からは $d$ 個の配置補空間の四実次元完備KE極限が残る（Song, arXiv:1706.01518v1, Theorem 1.2；Song–Sturm–Wang, arXiv:2003.04709v1, Theorem 6.1）。径の尺度 $R_t=\log(-\log|t|^2)$ のcubical候補とは異なる極限である。

Zhang, MRL 22 (2015), 1843–1869, DOI 10.4310/MRL.2015.v22.n6.a16, arXiv:1505.04728v2, Theorem 2.4の局所collapseにはQ-factorialなsimple toroidal全空間と相対canonicalのamplenessを仮定する。Source germ $xy=tz$ とそのcrepant small resolutionでは両条件を同時には満たさず、局所型の類似だけで直接適用しない。詳細な先行比較・仮定の適用計算の正本は[関連Lagrangian研究ノート](https://github.com/uedakazushi/lagrangian-torus-fibration/blob/main/research/notes.md)。

Part Vの写像 $\Phi_t$ と選んだLagrangian fibration $\pi_t:X_t\to B_d(T)$ を対応させるには、$b_t=\sup_xd_\square(\Phi_t(x),p_T\pi_t(x))\to0$ を別途検証する。$\operatorname{dis}(\Phi_t)\le a_t$ なら $\operatorname{dis}(p_T\pi_t)\le a_t+2b_t$、全fiberのambient直径も同じ量以下となる。証明は関連主原稿の `topo:ke-map-compatibility`。これは三角不等式による比較であって、(CP)$_d$+(PBE)$_d$やactual適合性を証明したことではない。五次では $p_T$ は同相、六次以上では基底の木も収縮する。

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
## 人工基底計量とactual退化計量の比較
$p_T:B_d(T)\to\mathcal C_d$ の人工PL長さ計量 $|v|_\varepsilon^2=|dp_T(v)|_\square^2+\varepsilon^2|v|_h^2$ によるgraph correspondenceのdistortionは、$d=5$ で $\Theta(\varepsilon^2)$、$d\ge6$ で $\Theta(\varepsilon)$ と鋭い（関連Lagrangian研究の topo:metric-collapse-sharp）。従ってGH収束には各々対応する上界がある。これは人工的な基底計量についての結果であり、actual KE退化やaction-affine metricの収束の証明ではない。

実際の長さ計量へ適用するための三入力（topo:finite-portal-criterion）は、(N) no-shortcut、(S) square path lifts、(F) fiber/portal connector diameterの消失であり、有限square数 $N_d=d\binom{d-1}{2}$ による距離誤差上界が得られる。(N),(S)だけでは(F)は導けない。二つのunit squareを頂点で貼った折り畳み模型は(N),(S)を厳密に満たすのにGH距離が$\sqrt2/2$以上となる反例。Part IV–Vの$(CP)_d+(PBE)_d$へ接続する際は、no-shortcutの定量化とglobal portal費用を区別して検証する。一般的新規性は未確認。
