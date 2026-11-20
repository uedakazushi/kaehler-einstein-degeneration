# 研究ノート：一般型超曲面のKE退化
更新：2026-11-20 / v1.4

## 開正方形内部の actual KE 比較と局所collapse
五次族について、主稿 `coarse:thm:moving-triple-tensor` / `coarse:cor:open-square-tensor` に新しい証明を置いた。正確な三重点座標 ζ0ζ1ζ2=t、L=−log|t|²、R=log L、独立深度 a,b とし、0<η<1/2 を固定する。a,b∈[L^η/2,2L^(1−η)] 上で actual g_t は二つの cusp の積 h_prod に全固定階で O(L^(−η/4)) 近づく。全角度について一様であり、(TC)_5、(PBE)_5、actual metric buffer を仮定しない。依存する大域入力は既存の capped volume 下界 `coarse:cor:global-volume-lower` である。

証明は、三重点内の expanding product annuli、shifted-sinh 型の負KE下barrier、finite complete annuli の上barrierから volume ratio→1 を得て、Savin (2007), Theorem 1.3 の small-perturbation regularity を適用する。bounded densityだけの旧推論とは異なり、small C0 potential が入力である。明示式・境界比較・Savinの仮定・Schauderによる誤差率を今回点検した。新規性の網羅的確認は未完了。

関連 Lagrangian 主稿 `ke:open-cell-collapse` により、各開正方形の固定長方形 Kη=[η,1−η]² 上に actual KE–Lagrangian torus fibration を構成できる。Fiberのintrinsic/ambient diameterは O(L^(−η))、raw cubical mapとの値の誤差は O(1/R)。Moser像領域に内在距離を入れれば R^−2 g_t のGH極限は平坦な Kη であり、projection distortion は O(L^(−η/4)+L^(−η)/R)。領域外のshortcutを許すambient距離、大域fibrationとの接着、singular fibersは未解決。

## 局所windowと残るtensor仮定
三つの深度が同程度のとき、一つの独立二座標product windowで任意半径のconstrained-cusp ballを覆うことはできない（`coarse:prop:triple-product-obstruction`）。最大深度を従属座標にする小さい相対箱は有効であり、全deep triple上のvolume上下界とbounded potentialは `coarse:cor:triple-volume-comparison` で証明する。これだけではfull tripleのtensor比較は得られない。

Source gateのfixed model ballはoriented half-armを越える。Full source-coordinate extension上でdensity比較を行い、(TC)_5は**その点で有効なorientation**のmodelに対する下界として定式化する。全ての拡大窓で同じmodelのtensor比較を要求しない。任意半径のexhaustionはcoarse小窓構成の結論に含めず、dominant tripleでの証明と一般の(PBE)_dを分ける。

## 体積密度とtensor比較：現行の解析条件
主稿 `coarse:prop:density-counterexample` は、固定ball上で滑らかな負KE計量列の体積密度が正に一様有界でも、内側ballでtensorが一様有界とは限らないことを証明する。したがってvolume lower/upper estimatesだけを用いた局所tensor比較は使えない。

五次のexterior comparisonには独立な仮定 $(\mathrm{TC})_5$（`coarse:hyp:TC5`）を置く。これに依存するraw submetry、actual connectors、source diameter、粗い距離二側比較、$(\mathrm{CP})_5$ の検証も条件付きである。Raw coordinatesの代数的構成、閉セルの実現、determinant/volume評価、actual metric ballsを用いたsource inradius/escapeの議論、抽象有限距離論は、このtensor比較の推論から分離する。旧来の全証明を今回独立監査したことにはしない。

修復の具体的な十分条件は、各点にactual metric ballが入る一様bufferと、そこから負のholomorphic sectional curvatureを持つcomplete productへの正則写像である。`coarse:lem:actual-buffer-comparison` によりlocalized Chern–Luから一方向の比較を得て、volume upper boundと合わせる。Model metricでのbufferだけではactual bufferを証明したことにならず、欲しいcoarse distanceを先に使う循環を避ける。

### 反例の要点と参照先
$\Omega=B(0,1/4)\subset\mathbf C^2$、$r=|w|$ として
\[
 \varphi(z,w)=-2\log(1-|z|^2r)-2\log(1-r)
\]
は有界連続plurisubharmonicであり、$w\ne0$ では正則局所写像 $(z,w)\mapsto(z\sqrt w,\sqrt w)$ によるproduct-disc KE potentialのpullbackである。Jacobianは $1/2$ なので $\det(\varphi_{a\bar b})=e^\varphi$。Bedford–Taylor measureはdivisor $w=0$ にmassを持たず、方程式は弱い意味で全域に成立する。滑らかな境界値を一様近似しDirichlet問題を解くと、滑らかなstrictly psh $u_j\to\varphi$ が得られる。従って $\omega_j=\mathrm i\partial\bar\partial u_j$ は $\operatorname{Ric}(\omega_j)=-\omega_j$ と一様なdensity上下界を満たす。しかし $z=0,w\ne0$ で
\[
\varphi_{z\bar z}=2r,\qquad
\varphi_{w\bar w}=\frac1{2r(1-r)^2},
\]
なので一様tensor上界は存在しない。完全背景をより大きなbidiscに選んでも、その内側の固定ball上では同じ反例になる。**対象compact退化族に対する反例ではなく、一般的な局所推論を排除する反例**である。完全な証明は主稿 `coarse:prop:density-counterexample` に置く。

依存する一次資料：

- B. Guan, *The Dirichlet Problem for Complex Monge–Ampère Equations and Regularity of the Pluri-Complex Green Function*, CAG 6 (1998), 687–703, Theorem 1.1。https://people.math.osu.edu/guan.19/Papers/guan1998b-cag.pdf 。球上で境界値を延長した $\widetilde b_j$ に $A_j(|Z|^2-1/16)$ を足すと、$A_j$ 大で必要なstrict psh subsolutionを得る。2000年のcorrectionはLemma 3.1/Theorem 1.3とGreen functionのTheorem 1.2の問題を扱い、ここで使うTheorem 1.1を撤回していない。https://people.math.osu.edu/guan.19/Papers/guan1998b-cagapp.pdf 。
- E. Bedford and B. A. Taylor, *A new capacity for plurisubharmonic functions*, Acta Math. 149 (1982), 1–40, DOI 10.1007/BF02392348。Theorem 4.1の比較とTheorem 6.9のpluripolar capacity零を使う。https://www.math.stonybrook.edu/~ebedford/PapersForM655/BTNewCapacity.pdf 。

### Lagrangian側で得た局所結果
関連主稿 `lagrangian-torus-fibration/papers/sections/paper/ke_fiber_compatibility.tex` の `ke:short-torus-averaging` と `ke:triple-moving-fibration` が証明の正本。Full-orbit moving domainで $c h_t\le g_t\le C h_t$ を仮定すると、torus平均の短いprimitiveから一つのMoser flowを構成し、全局所fibersを同時にLagrangian化する。$\min\ell_a>m_t$ でambient diameter $O(m_t^{-1})$、raw cubical mapのtarget誤差 $O((1+\log m_t)/R_t)$。$m_t=R_t$ と選べる。高階比較やPBEはこの局所symplectic構成の入力ではないが、全閉cornerのtensor比較と大域的なmetric近似は未証明である。開正方形の固定compact部分については上記の新定理で解析比較を証明した。Ruan, arXiv:math/0309177v2, §3のaveraging–Moser機構に先行研究があり、新規性は未確認。

## KE尺度とLagrangian fibrationの比較
標準規格化 $\operatorname{Ric}(\omega_t)=-\omega_t$ では体積 $2\pi^2d(d-4)^2$ は固定され、成分内部の基点からは $d$ 個の配置補空間の四実次元完備KE極限が残る（Song, arXiv:1706.01518v1, Theorem 1.2；Song–Sturm–Wang, arXiv:2003.04709v1, Theorem 6.1）。径の尺度 $R_t=\log(-\log|t|^2)$ のcubical候補とは異なる極限である。

Zhang, MRL 22 (2015), 1843–1869, DOI 10.4310/MRL.2015.v22.n6.a16, arXiv:1505.04728v2, Theorem 2.4の局所collapseにはQ-factorialなsimple toroidal全空間と相対canonicalのamplenessを仮定する。Source germ $xy=tz$ とそのcrepant small resolutionでは両条件を同時には満たさず、局所型の類似だけで直接適用しない。詳細な先行比較・仮定の適用計算の正本は[関連Lagrangian研究ノート](https://github.com/uedakazushi/lagrangian-torus-fibration/blob/main/research/notes.md)。

Part Vの写像 $\Phi_t$ と選んだLagrangian fibration $\pi_t:X_t\to B_d(T)$ を対応させるには、$b_t=\sup_xd_\square(\Phi_t(x),p_T\pi_t(x))\to0$ を別途検証する。$\operatorname{dis}(\Phi_t)\le a_t$ なら $\operatorname{dis}(p_T\pi_t)\le a_t+2b_t$、全fiberのambient直径も同じ量以下となる。証明は関連主原稿の `topo:ke-map-compatibility`。これは三角不等式による比較であって、(CP)$_d$+(PBE)$_d$やactual適合性を証明したことではない。五次では $p_T$ は同相、六次以上では基底の木も収縮する。

## 固定領域の収束から径の尺度へ移る際の障害
三重点の $x_a=\ell_a/L_t$ に関して全 $x_a\ge\eta>0$ である固定compact集合では、$q_a=1+R_t^{-1}\log\min(x_a,1/2)+O((L_tR_t)^{-1})$ であり、cubical像はtriple vertexに縮む。正方形内部の $w_i=1$、$w_j,w_k\in[\eta,1-\eta]$ は $x_j\asymp L_t^{w_j-1}$、$x_k\asymp L_t^{w_k-1}$ に対応する。厳密な証明とsoftmax全閉corner実現は関連Lagrangian主稿 `ke:triple-hexagon`、`ke:fixed-simplex-scale`。固定compacta上の局所収束だけでは、この速度で境界に近づく領域を制御できない。

### 一様な粗比較を加えても係数1は決まらない例
$R=\log L$、$s=-\log x$、$x\in[L^{-1},1]$ とする。滑らかな $0\le\chi\le1$ を、$u\le0$ で0、$u\ge1$ で1となるよう取り、
\[
g_L=(1+\chi(s-R/2))^2\,ds^2
\]
と置く。任意の固定compact集合 $K\subset(0,1]$ 上で、十分大きい $L$ に対して $g_L=dx^2/x^2$ が完全に一致する。全領域でも $dx^2/x^2\le g_L\le4dx^2/x^2$。しかし $R\ge2$ のとき全長は
\[
\int_0^R(1+\chi(s-R/2))\,ds
=\frac32R-c_\chi,\qquad
c_\chi=1-\int_0^1\chi(u)\,du.
\]
従って $R^{-2}g_L$ は長さ $3/2-c_\chi/R$ の区間であり、GH極限は $[0,3/2]$。固定領域での完全な一致と全体の粗い比較からは、depth写像 $q=1-s/R$ の値域 $[0,1]$ における係数1の距離は得られない。これはKE計量の反例ではなく、moving-windowの鋭い評価が必要なことを示す長さ空間の例である。

### Cusp Hermitian模型とKE模型の区別
Zhang, arXiv:1505.04728v2, Proposition 3.1は、同論文のQ-factorial・相対ample仮定の下でactual/background metricの一様比較を与える。Lemma 3.2(ii)の最深stratum背景とLemma 3.3の極限比較は、制約付きcusp Hermitian模型と整合する。等深度で模型が退化するわけではない。他方、$\psi=-\log(x_0x_1x_2)$、$x_0=1-x_1-x_2$ に対し
\[
\det\operatorname{Hess}\psi
=\frac{x_0^2+x_1^2+x_2^2}{x_0^2x_1^2x_2^2}
\]
であり、分子は非定数なので、この模型potential自体を $\det\operatorname{Hess}\psi=\kappa e^{2\psi}$ の解と同一視できない。模型との二側比較と、sharp係数を持つKE漸近は異なる入力である。一次資料：https://arxiv.org/pdf/1505.04728 。

## 背景capped formをtensor比較に使う際の障害
Density Ω_low とそのcurvature h_low=ddc log Ω_lowは区別する。Tripleの深度 (L/2,L/4,L/4) では、cap係数μ0がO(L^−1)、μ1,μ2がO(L^−2)となり、h_lowとconstrained cuspの最大固有値比はLの程度に増える。一変数capを z=√|t| Z、B=A0+L/2 で書くと、係数は
\[
c_B(Z)=\frac{2(B-\log(1+|Z|^2)+|Z|^2)}{(B-\log(1+|Z|^2))^2(1+|Z|^2)^2}.
\]
c_B(0)=2/B、−c_B(0)^−1∂Z∂barZ log c_B(0)=B−1。したがって一様な曲率上界を持つreferenceとしてh_lowをそのまま使えない。これはΩ_lowのdensity比較やglobal determinant下界への反例ではない。今回のvolume-barrier法はh_lowのtensor/curvature比較を用いない。

## 今回確認した解析文献
- O. Savin, *Small Perturbation Solutions for Elliptic Equations*, CPDE 32 (2007), 557–578, DOI 10.1080/03605300500394405, Theorem 1.3、pp.558–560のH1/H2/H4。https://www.math.columbia.edu/~savin/Small_pert.pdf 。ゼロ次項依存を許し、全域の退化楕円性とHessian原点近傍の一様楕円性で足りる。正のcone外でdetを0に延長した F(M,u,x)=det_+(H(x)+P(M))/det H(x)−e^u に適用する。
- Y. Wang, *A Liouville Theorem for the Complex Monge–Ampère Equation*, arXiv:1303.2403、Lemmas 2.1/2.4。https://arxiv.org/pdf/1303.2403 。Complex Hessianの実Hessianへの埋込みとcone外延長を参照。主適用はSavin原典を用いる。
- J. Cheng and Y. Xu, *Interior W^{2,p} estimate for small perturbations to the complex Monge–Ampère equation*, Calc. Var. PDE 62 (2023), 231, DOI 10.1007/s00526-023-02571-x、Lemma 2.1/Theorem 1.4。https://arxiv.org/pdf/2301.00940 。関連するsmall-perturbation regularityであり、今回の証明ではSavinを直接使う。
- E. Di Nezza, V. Guedj, H. Guenancia, *Corrigendum to “Families of singular Kähler–Einstein metrics”*, JEMS 28 (2026), no.11, 5107–5111, DOI 10.4171/JEMS/1801。https://ems.press/content/serial-article-files/54000?nt=1 。元のProposition D/Theorem E（Prop.5.9/Thm.5.11）のpotential下界を訂正。訂正版Theorem 4はX0 irreducibleを仮定し、我々の可約中心fiberへ直接は適用しない。

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
