# 研究ノート：一般型超曲面のKE退化

更新：2026-11-23 / v1.29（Part IV本文はv1.16、Part V本文はv1.10）

## Capped density の最大前因子と検証資産

**Capped barrier の前因子は鋭い。** Part IV `coarse:prop:capped-prefactor-sharp` で、同じ α_i と canonical density に対する Ω^(β)=L_t^β∏α_i^(−2)Ω_0 を考えると、h^(β)=dd^c log Ω^(β)=h^low はβに依らず、β≤2では全域 determinant lower が成り立つが、β>2では source中央点で (h^low)^2/Ω^(β)≈L_t^(2−β)→0 のため失敗することを直接証明した。中央rescalingでactive二方向はL_t^(−1)、背景・inactiveはO(|t|)であり、canonical residueは非零である。これはこのcap ansatzの最適性であり、一般の別障壁やactual KE metricそのものに対する最適性を主張しない。Part IVのglobal capped lowerを変更せず、これを利用する曲面稿の仮定も変えない。

直接計算は主稿の命題に置く。基本恒等式 `Q_i\vert f_i\vert^2=\mu_i`、central rescalingでの `|t|Q_x=2b_x(α_x+b_x|X|²)/[α_x²(1+b_x|X|²)²]` と三capの二次minorを、再現可能な `research/check_capped_prefactor.py` のsympy検算でも照合した。ただしスクリプトは幾何学的coverや係数の一様性、Monge–Ampère最小値原理を自動証明するものではない。

Savinの原著 `Small Perturbation Solutions for Elliptic Equations`, *Commun. PDE* 32 (2007), 557–578, Theorem 1.3 pp.559–560のH1/H2/H4を一次PDF本文・ページ画像で確認した。局所lemma `coarse:lem:small-volume-tensor` では、PSD順序に関して単調な `det_+` を用いたH1、基準正定値行列近傍の一様楕円性H2、零解の周囲のC²条件H4を明示している。H3はTheorem 1.3の仮定ではない。この監査は定理文とoperatorへの適合に限り、原著全証明や曲面原稿の局所安定性全体の形式検証ではない。

## 固定比較模型に対する局所安定性率の最適性

`simplex:prop:boundary-floor-sharpness` は、固定深度座標と既定のcomplete simplex模型k_Lに対する局所定理 `coarse:thm:boundary-to-triple` のO(1/m)を、一般にo(1/m)へ改善できないことを示す。固定m₀,b>0に対する一つの族 \(\omega_{b,L}=F_b^*k_{L+3b}\)、\(F_b(w)=w+b\mathbf1\) が、同じdensity floor c_*=(1/3)(m₀/(m₀+b))⁶を満たす。Balanced点L=3m、ell_i=mでは相対実計量が正確に(m/(m+b))² Id、体積対数比が−4log(1+b/m)である。L=m²、ell=(m²−2m,m,m)では、それぞれId−(2b/m)Id+O_b(m⁻²)、−4b/m+O_b(m⁻²)となり、正規化単体の境界へ向かう領域でも一次誤差が残る。証明は現行本文に一回だけ置く。Balanced例はscaling、境界例はpure-modelのdominant-product漸近だけに依存する。

**Lだけの率がないこと。** 同じ積比較を一般のL、m→∞、m/L→0へ適用すると、p=(L−2m,m,m)で
\[
v_{b,L}(p):=\log\frac{\omega_{b,L}^2}{k_L^2}(p)
=-\frac{4b}{m}+O_b\!\left(m^{-2}+(m/L)^2\right).
\]
任意の正関数r(L)→0に対し、m(L)=min{r(L)^(−1/2),L^(1/2)}と選ぶ。このときm→∞、m/L→0、m r(L)≤sqrt(r(L))→0、m³/L²≤L^(−1/2)→0だから、m v_b,L→−4bであり、|v_b,L|/r(L)→∞となる。同じ固定bの局所族で評価点だけを選び直すため、最小深度の発散速度を指定しない全ての深部点列に共通する、Lだけによる消失率は存在しない。この結論も固定した座標・模型と局所仮定クラスに限り、compact射影族の実際の誤差下界ではない。

**次の精度問題。** この例はfacetの固定平行移動を比較模型に吸収すれば消える。従ってcoordinate-invariantな最適性、又は補正済み模型に対する最適性は示さない。Actual familyのfixed-end情報から有界なfacet shiftを選べるか、その後の剰余をo(1/m)に抑える追加境界条件は何か、が次の候補である。一般の境界入力を三つの平行移動定数だけで記述できるとは仮定しない。既存のfixed-end moment則だけから、全深度域の二次漸近を推論しない。

**先行比較の範囲。** Zhangのcanonical semi-flat比較は正規化座標x_i=ell_i/Lの固定compact集合上で、全phaseを含められる。Ruan I/IIには全域の粗いquasi-isometryがあり、H-minimal論文には固定縮小領域上のtorus-averageとの定量比較がある。本稿で比較するのは、指定したcomplete simplex解への相対小誤差を最小深度で定量化し、深度比に一様にする点と局所境界入力である。確認した定理・量化・版は `research/source-audit.md` を参照する。優先権の網羅的確認は未了である。

## Complete simplexの存在入力と直接比較

**Complete simplex模型の最小入力。** Part IV `coarse:lem:simplex-model` は、Zhang Theorem 2.1に明記されたCheng–Yauの標準実単体上の凸解存在・境界発散・実Hessian完備性を入力とする。一意性は内側homothety比較、tube完備性は有限長曲線の実射影、格子商の完備性は等長作用から直接証明する。w/Lはuniversal cover上の等長写像だが、4πの角度格子を4π/Lへ変える。固定周期商のinjectivity radius下界は結論しない。全深度比の正規化窓でpotentialとtensorの規格化を明示した。Zhangの定理文と適用条件は実読済みだが、CY1982 Theorem 4.4の原文・証明は未取得であり、原典確認済みとはしない。正確な書誌・係数点検・確認範囲は `research/source-audit.md`、直接証明は現行本文が正本である。

Zhang, arXiv:1505.04728v2, pp.4–6では、σ=R_{≥0}³とu_σ=(1,1,1)に対するB_σがΔ_1である。境界の滑らかさを要求せず、任意L>0はscalingで得る。Cheng–Yau 1982の書誌は *The real Monge-Ampère equation and affine flat structures*, Beijing Symposium proceedings, Science Press, pp.339–370。原典Theorem 4.4の本文は未取得で、存在入力の確認箇所はZhang Theorem 2.1である。Zhang p.6の一意性は別のCY1980 Proposition 5.5に帰属するが、本稿では下記の比較により直接得る。

**有界凸領域での一意性。** Ω⊂Rⁿを有界凸領域、x₀∈Ω、0<a<1とし、u,vがdetD²u=e^{2u}、detD²v=e^{2v}と境界発散を満たす滑らかな凸解なら、Ω_a=x₀+a(Ω−x₀)上のv_a(x)=v(x₀+(x−x₀)/a)−n log aも同じ方程式を満たす。Ω_aの閉包はΩ内にcompactに入り、uは有限、v_aは境界で発散するので、正の内部最大値の排除によりu≤v_a。a↑1と役割交換からu=v。第2解の完備性や境界発散率は不要である。これは標準的な比較原理の直接帰結であり、新規性を主張しない。主稿は必要なn=2の単体の場合を証明する。

**複素係数の確認。** w=x+iyではφ_{w_j bar w_k}=φ_{x_jx_k}/4なので、det(φ_{w bar w})=4^{−n}detD²φ。Zhang v2 p.6の式(2.2)直後には4^nと印刷されていることをPDF画像で実表示して確認した。この定数はRicciには影響しない。本稿のk=(i/2)Hessφ dw∧dbarw、k²=(1/2)e^{2φ}dV_w=8e^{2φ}dV_logは独立に再計算して正しい。参照: https://arxiv.org/pdf/1505.04728v2 。

## 共同編集の正本と共有局所入力

`multiscale-kaehler-einstein` は固定配置補空間のPart I–III、本repoは退化族局所解析のPart IVと条件付き距離論のPart V、`surface-lagrangian-torus-fibration` はactual KE Lagrangian構成と同じ射影の全曲面GH実現を所有する。三研究の方針・Introduction・証明依存を共同で点検するが、証明全文を相互に複製しない。共有する結果を変更したら、利用側の定理ラベルと仮定も照合し、各repoの保存後にhubへ反映する。

Part IV–Vが使う曲面の数学入力は、[改訂37・commit 32c67ae](https://github.com/uedakazushi/surface-lagrangian-torus-fibration/tree/32c67aefe6beb47c2955923e2b6eb2471d48af31)に固定する。局所actual K4、全moment・五次同時実現と同じ射影の測度系の正本は曲面稿であり、指定箇所の内部点検と現行版の保存確認は科学引用pinとは別に管理する。

現行Part IV v1.15は、固定end・normal winding・Schwarz半径依存、complete simplexの最小存在入力と直接証明に、固定比較模型での局所安定性率の最適性と先行結果との具体的比較を統合する。曲面の五次と標準等重み六次の同時実現・測度系は曲面repoに証明を置く。既存の科学引用pinと今回の確認範囲を分け、Part V本文は不変である。

固定補空間側は[Part I v1.10・総説v1.14・研究資料v1.19](https://github.com/uedakazushi/multiscale-kaehler-einstein/tree/2926300c2425c7e68550ac08ee81a2afa639a0c6)を確認版とする。尖点付き有限面積双曲曲線Sと境界のないコンパクト連結Riemann因子Yの積で、距離Laplace変換をRe s<3の切断半平面上でW/(1−s)−H(s)Log(1−s)+G(s)と表示する。Hはentire、GはRe s<3で正則であり、WとmonodromyからYの正規化基点距離分布を回収する。通常volume-IRFA一般への解析接続・等長型・族一様性は主張しない。総説はこの積の結果、Part IV v1.12の固定end/winding、曲面改訂44の同じ射影による確率体積極限を統合する。これらは固定補空間側の成果・共同編集であり、Part IV/Vへの新しい解析仮定やCP/PBE/TCの検証ではない。 既存の裾係数・compact基点一様性・非可積分cusp・gauge・K5 linkの指定点検は保持するが、新しい積の命題・系は別に作成担当・統合担当・独立担当が実本文を読んで照合した。 新しい `cor:CW-fixed-cutoff-budget` は固定SNC cutoffの脱落質量とStokes defectをCe^{-A}で抑える。統合担当がこの追加証明を実読し、固定対の予算とtの有効収束率を区別している。

本稿の公表入口は無条件の局所解析を中心とし、Part IVの最小入力表 `tab:surface-minimal-inputs` に曲面P0が使う四群をまとめる。局所安定性は `coarse:thm:boundary-to-triple`、全平面族への適用は既存の `coarse:thm:full-triple-tensor` とし、証明を一回だけ置く。Part Vの抽象pruning–transportと有限targetの直径計算は独立の成果で、CP/PBEを仮定するactual raw-pruning経路、曲面側の直接scalar/portal経路を区別する。

| 本repoの共有入力 | 仮定・量化と証明の所在 | 曲面稿での利用と適用限界 |
| --- | --- | --- |
| `coarse:cor:degree-d-volume-lower` | `ass:Gd`、固定d・固定族。主稿のweighted cap・六型minor・adjunction residueから全X_tでω_t²≥c_dΩ_low。Source軸でも正cap方向を保持する。 | K1のPoisson/Schwarz bufferとsource volume、full tripleの固定face入力。Density単独からtensor比較は結論しない。 |
| `coarse:thm:boundary-to-triple` → `coarse:thm:full-triple-tensor` | `full_triple_comparison.tex`。Exact tripleの各固定tのcompact radial閉包×全phaseに滑らかなKE metric、全faceの一様density下界。m₁≤m<L_t/3、全深度比・全phaseでC^q誤差O(1/m)。族への適用だけにcapped下界を使う。 | `ke:actual-closed-corner` と有限cut版、二active co-Gram。保護領域を出る全曲面の下距離は曲面側のscalar評価を要する。 |
| `simplex:cor:actual-closed-corner-metric` | `closed_triple_metric.tex`。H_{t,R}の内在距離と、min ell>R/2内のprotected距離に対するO(log R/R)。 | 曲面稿 `ke:slow-cut-closed-corner-gh` は固定mも許す有限条件を確認してm/2でfull-tripleを使う。全X_tの下距離へ直接読み替えない。 |
| `simplex:lem:rank-one-schwarz`、`simplex:cor:active-cogram` | `simplex_boundary_geometry.tex`。Complete simplex模型で係数1、actual tripleではO(1/min ell)を加える。 | Triple上のscalar下界。Source-inclusiveな一active領域のsharp normal評価と混同しない。 |
| `pair:prop:bundle-conic`、`pair:cor:global-primitive`、`pair:rem:normal-frame-winding` | `source_free_neck_coordinates.tex`。Source・tripleを除く固定K上。Exact uv=t、Ω=dlog v∧τと単一λ。Frame変更bのnormal windingでmomentの整数定数差を追跡する。 | Canonical normal action・momentの共通化。Zero windingでも残余periodは別データであり、第二actionやorbit partitionは供給しない。 |
| `pair:prop:fixed-end-transfer` → `pair:thm:fixed-end-moment`、`pair:cor:actual-common-moment` | 同節。固定collarのlog-densityのC¹収束と極限成分のradial derivativeを分ける。固定K→小さい固定r→全小複素t、全phaseで±4π/s_r+O_K(s_r^(−1−δ))+o_(t;r,K)(1)。SongとRZのSNC定理が二条件を検証する。 | K1–K2のend符号。`pair:lem:diagonal-fixed-end` で選んだ遅いexhaustionへ移せるが、任意速度の一様性やbufferは与えない。 |
| `coarse:lem:pair-arm-density`、`coarse:lem:complete-volume-upper` | Oriented annulus–disc。Complete上比較はlog-volume ratioの上有界性が必要。Finite quotientの境界発散でその仮定を確認する。 | Source全moment退出の前段volume入力。Source軸を含むarm tensor比較は曲面稿 `ke:source-arm-uniform-tensor` の別証明。 |

**対象を限定した解析入力監査。** Capped densityのweighted minor・六型cover・residue規格化から、full-tripleの固定face下界・内外barrier・small Ricci potential・Savin、closed-cornerの内在/protected距離への移行までを再読した。Full-tripleはsource-free triple chartの全深度比・全phaseに一様で、m自体の発散を仮定しないため曲面の有限cut版にも使える。Source中央では元のplane座標を保ち、rescaleされたcap係数とresidueのt因子を照合した。Fixed-end/diagonalは固定componentのlog canonical class O(d−4)、period 1の係数4π、K_j→r_j→既証誤差E_j・有限費用B_j→全複素tの閾値の順を確認した。指定範囲では結論を妨げるgapは見つからなかったが、全高階解析証明・全原稿・一次文献全証明の包括的な再監査ではない。

**Source armとsharp scalarの三境界。** 曲面稿 `ke:source-arm-uniform-tensor` の固定normal境界にはcapped projective lower、固定residual境界にはsource-free neckのtensor比較、moving normal境界s=κLにはpositive-Poisson potential・actual ball buffer・localized Schwarzを使う。Full-triple、全moment退出、後続のglobal scalar障壁を入力にしない。`ke:sharp-normal-boundary-inputs` の残余境界∂P_jだけが、sourceから離れたtripleのmin ell≈b_jでfull-tripleとrank-one Schwarzを使い、係数1+O(1/b_j)を得る。Sourceを含むs=κLでは独立の粗いC_j、外側s=𝔫_jでは粗いA_jで足りる。この依存鎖と定数の選択順序を直接点検した。

**固定endの最小解析とvolume frame。** `pair:prop:fixed-end-transfer` の二入力は固定end collar上のlog-densityのC¹収束と、極限成分のradial derivativeが4/s+O(s^(−1−δ))となることである。共通frame Ω=dlog v∧τ=−dlog u∧τとperiod 1のVの向きを固定すると、momentは±π倍のradial derivativeの円平均になる。Hermitian normのcutにはs=s_r+O_K(1)を用い、主項の差O_K(s_r^−2)を吸収する。実際にはC¹収束のうちradial微分の収束だけで足り、moving内部のtensor/bufferは不要である。`pair:rem:normal-frame-winding` は、全orbitを含むpatchの非消滅正則unit bに対しμ′=μ−2π wind_V(b)を与える。Nonbasicでもzero windingなら同じmomentを保つが、λ′−λ=−d arg bの残余periodとprimitiveの同一性は別である。新しい式と適用順を作成担当と統合担当が点検した。

**Actual bufferの半径と円周収縮。** `coarse:lem:localized-chern-lu` は、actual球の半径σとtargetの負曲率κに対して tr_g(F*h)≤C_n κ⁻¹(1+σ⁻²)を与える。正則写像のrank低下、潰れたinjectivity radius、targetの非完備性を許す。`neck:cor:shrinking-buffer-circle` はrank-one下界と体積上界を組み合わせ、normal深度m=min(s,M−s)に対しlength≤C(1+σ⁻¹)/mを得る。0<σ≤1ならmσ→∞が非正規化の収縮、Rmσ→∞がRで割った収縮の十分条件となる。半径は別の幾何的議論で確保する入力であり、bufferの存在、全tensor比較、Moser flow生存、CP/PBE/TCは証明しない。証明は距離cutoffの勾配・Laplacian bounds、正の最大点、mixed coefficientsを含むdeterminant比較を明記する。これは古典的なSchwarz評価の定量的帰結であり、新しいSchwarz lemmaとしての優先権は主張しない。

**固定段階からの接続補題。** `pair:lem:diagonal-fixed-end` は、K_jを固定してr_jを選び、有限個の既証誤差E_j(t)→0とt閾値前の有限費用B_jを確定した後、j(t)→∞を十分遅く選べばE_j(t)≤ε_jかつB_j/R_t≤ε_jとend符号を同時に保てることを証明する。共通moment intervalは±π/s_jで段階ごとに縮んでよい。固定段階のbuffer・matchingの存在や、費用のj依存成長率を証明する補題ではない。原稿に証明を置き、ここでは量化だけを記す。

**Sourceを含むfixed-shellの証明正本。** 曲面稿 [ke_staged_neck_averaging.tex](https://github.com/uedakazushi/surface-lagrangian-torus-fibration/blob/32c67aefe6beb47c2955923e2b6eb2471d48af31/papers/sections/paper/ke_staged_neck_averaging.tex) の `ke:source-inclusive-fixed-shell` は、source-inclusive正規形x′y′=t h_t(p)と固定compact P^+を用いる。各固定rのendとr²≤|x′|≤rのshellは、h_0(p)=0でも中央成分のsmooth locusのcompactにあり、全複素tの固定gauge収束を使える。同じΩ_t=dlog x′∧dp=−dlog y′∧dpはsourceでdx′∧dy′/(t h′_t(p))と非零正則に延びる。したがって全phaseのend値±4π/s_rと、rに共通な正のshell横断費用c log2を得る。t閾値のr依存を許し、shellを通る経路部分の費用を全曲面二点間距離と同一視しない。異なるvolume frameのprimitiveには閉形式差が残り、residual periodの消滅や異なる正規形間のprimitiveの一致は結論しない。証明と別の読み手による内部点検は曲面側に置き、Part IVのsource-free定理には新たな適用範囲を付け足さない。

**二つの大域経路。** Part Vの全曲面適用はCP/PBE付きで、quinticのCP検証はTC5に依存する。曲面稿 `ke:global-metric-realization` には同じf_t=p_Tπ_tの直接scalar/portal証明があり、neck/core/sourceの接続もそこで別に扱う。したがって全曲面のGH問題自体を本稿の局所入力だけから「未解決」と記さず、CP/PBE/TCという追加packageの未検証部分を明記する。Part Vの特定のΦ_tとf_tとの一様近接性を新たに示したことにもならない。Part IIのsecondary complex periodsと第二symplectic action、Part IIIのH_loc/H_ancもそれぞれ別の入力である。

**同じ射影での確率体積測度。** 曲面改訂44の保存稿 `papers/sections/paper/ke_global_metric_realization.tex` の `ke:global-volume-measure` と `ke:global-volume-scope` が証明の正本である。固定d≥5と既存の一般位置族について、dV_t=ω_t²/2、V_d=2π²d(d−4)²、ν_t=dV_t/V_dと置くと、同じf_t=p_Tπ_tの押し出しはd^−1Σδ_{e_i}、π_tの押し出しはd^−1Σδ_{v_i}へ弱収束する。前者は全cubical計量空間と同じGH近似写像を用いるmeasured GH収束であり、極限測度に全台性を要求しない。

各固定成分W_iの体積は、Part I `lem:CW`・`thm:facemass` のbounded primitiveによるStokesとK_{H_i}+D_i=(d−4)Hから2π²(d−4)²である。固定compact上の成分収束と `ke:global-clipped-depth-map`・`ke:global-depth-base-comparison` により、その像はe_iへ一様に近づく。成分体積の和と全体積が一致するため、固定compactを大きく取った後のt→0で補集合の質量を抑えられる。p_T^−1(e_i)={v_i}とcompact性がπ_t側の弱収束を与え、五次の作用指定射影には `ke:relative-replacement-gh` の一様値比較を使う。Moving coreへの包含や対角列の選び直し、moving neckの一様体積漸近は追加しない。

証明本文を実読して量化・規格化・像の位置を照合したが、曲面全主稿やPart Iの全Stokes証明を今回再監査したという意味ではない。改訂44の数学保存版は `d39270ec79ad973551f67c740682dbb06bac48e5` である。Part IV/V本文の改訂37入力pinは保持し、現行の表示確認は別に記す。距離極限の辺・squareは残り、確率測度の台だけへ空間を取り替えない。R_t^−2g_tの未正規化体積はR_t^−4dV_tで総量が零へ向かう。成分体積保存やexhaustion原理自体の新規性は主張しない。

**公表範囲と仮定の接続。** Part Iの `thm:intro-metric` は連結smooth projective pair・reduced SNC境界・K+D ampleを仮定し、`prop:RZ` が `def:clean` と `def:metricIRFA` を検証する。n≥1であり、空境界はcompact spaceと一点錐の自明な距離定理に含める。固定基点でのconeの一意性と、移動基点の複数の極限型を区別する。Exact tailには非空境界が必要で、一般multidegree配置では超平面用の単一skeletonではなくcomponent-labelled dual complexを用いる。既存の直接点検では、この導入から定義・距離定理・KE適用・配置例へ渡る仮定と量化を照合した。Rochon–Zhang §5, pp.38–39, Theorem 5.1の対象とnormal coefficient c_i=1、および同論文p.2の複素次元1の場合を一次資料で確認した。距離定理の結論やPart IV/Vへの入力を強めたわけではない。

| 外部の結論 | 利用する入力と適用範囲 | 証明の正本 |
| --- | --- | --- |
| 距離・moving・metric link | Clean finite-depth構造とmetric-IRFA。固定空間のK、linkは等長型まで。 | Part I `thm:rough`、`cor:based-ball-approximation`、`prop:cone-limits`、`prop:link` |
| LDP・測度付き平行移動・tail | Ordinary volume-IRFAは全faceで再帰的に整合。距離を使う結論にはmetric-IRFAと各定理の基点条件を加える。 | Part I `thm:LDP`、`thm:translation`、`thm:tail` |
| Face massの交点数 | 非正規化KE体積、有限体積、有界primitiveとadjunction。確率版は全体積で除す。 | Part I `lem:CW`、`thm:facemass`、`rem:probability-face-mass` |
| Abel係数・複素有理型延長 | 一側Abelはordinary volume-IRFA。有理型延長には角・残余方向でL1制御したjoint polyhomogeneityを追加。 | Part I `thm:Mellin-recursion`、`rem:Mellin-continuation`、`ex:Abel-not-meromorphic` |
| Secondary period | Component/cusp labelsを伴う残余曲線。Complex periodにはKähler orientationも保持し、一般WP completionにはcontrolled push-off。 | Part II `prop:partI-translation`、`thm:intro-unoriented`、`hyp:controlled-pushoff` |

**固定補空間のexact collar入力。** Part Iの `lem:SNC-compatible-collars` は同一Hermitian depthsを保つ実有向collarsと段階的商を構成し、`lem:fc-collar-transfer` はRZの局所正則射影による延長とそのexact pullbackの全残余一様な比較を与える。`lem:RZ-collar-tensor` がRZ Theorem 5.1を選んだcollarの一面tensor評価へ移す。一般のlog-smooth collarだけでは不十分な障害は `rem:log-collar-obstruction`。証明の正本は上記Part Iであり、指定collar構成と延長比較を独立内部点検した。これらは固定SNC空間の結果で、退化parameterに一様なbuffer、任意速度で指定した退化族のmoving比較、CP/PBE/TCの証明を与えるものではない。

**固定補空間の全射収縮と閉球近似。** Part Iの `prop:cogram`、`lem:lambda-choice`、`thm:contract`、`thm:rough` は、clean finite-depth構造とmetric-IRFAの下で、properな1-Lipschitz全射 $S:X\to\mathcal C$ と $d_{\mathcal C}(Sp,Sq)\le d_g(p,q)\le d_{\mathcal C}(Sp,Sq)+K$ を与える。`cor:based-ball-approximation` は、固定したSについて全中心o・全半径A・全R>0で、ambient距離を制限した閉球 $\overline B_{(X,R^{-1}d_g)}(o,A)$ と $\overline B_{\mathcal C}(S(o)/R,A)$ の間に基点対を含む歪み3K/R以下の対応を構成する。通常のGH距離は3K/(2R)以下である。`cor:GH` と `thm:moving` はその帰結で、指定compact集合を零へ送る選択ではKがその集合に依存してよい。独立内部点検では、十分深い共通collar、全逆計量と残余covector norm、可積分収縮、局所一セル化、全射性、fiberのambient直径と閉球対応を対象とした。固定空間内では任意のmoving centerに一様だが、退化族に一様なKや中間尺度の有効な速度を与えない。

**移動基点とincidence linkの分類。** Part Iの `thm:moving` は任意のx_jとR_j→∞について、S(x_j)/R_jを中心とするconeのambient閉球へ3K/(2R_j)のGH評価を与える。`def:incidence-link` は面αを保つcofacesとface mapsだけで残余cone L_αを作り、重複するlabelsのcoface copiesを保持する。`lem:positive-star-product` の正の面座標の領域で積表示を得て、m=min_{i∈α}√c_i u_i>2Aなら `lem:star-ball-isometry` によりambient閉A球が厳密にR^α_c×L_αの閉球となる。外部へ退出する経路は最初の退出と最後の再入で2(m−A)>2Aを要するため短絡できない。Closed star全体の積は一般に誤りで、三辺cycleのambient shortcutと二edge copiesの境界同一視を `rem:closed-star-obstruction` に保持する。

`prop:cone-limits` は有限個のcell copiesと各座標の有限極限/発散への部分列抽出により、有界基点極限またはR^α_c×L_αの積を全てのpointed limitsとして分類する。残余基点z_j→zによる追加の閉球GH誤差はd_{L_α}(z_j,z)以下で、αがmaximalならL_α={0}とする。`cor:moving-limit-classification` はSの全射性により、任意に指定したR_j→∞に対して全ての型を実現する。移動基点の独立点検では、このincidence・壁までの距離・ambient距離・基点と実現の量化を確認した。一つの固定空間の結論であり、退化族の任意速度でのmoving解析を与えない。

**Metric linkと先行研究の範囲。** `lem:cone-link-metric` と `prop:link` はcoarse sectionによるradial divergenceの一様O(1/r)評価と、πで切った角距離からのpath metric回復を与える。異なるlink成分間のlength距離は∞として扱う。復元するのはmetric linkの等長型であり、指定cell分割・component labels・normal depth重み、genuine geodesic-ray boundaryは結論に含めない（`rem:link-metric-scope`）。これはcomponent-labelled mixed Mellin transformsからのincidence検出と異なる入力データを使う主張である。

Leuzinger (2004), Lemma 5.1・Theorem 5.2・Corollary 6.3には有限体積locally symmetric spacesのbounded-additive cone比較・Tits quotient上のasymptotic cone・radial公式があり、Bridson–Haefliger, I.5, Definition 5.6・Remarks 5.7（59–60頁）はcone距離と角距離の標準事項を与える。これらを独自成果として扱わず、SNC KEへの適用範囲と既知部分をPart I Introductionで区別する。本文の書誌と同repoの `research/source-audit.md` を詳細な一次資料照合の正本とし、ここでは共同監査を同期する。網羅的な優先権・新規性確認は未了である。

**LDPとexact tailの共同監査。** Part Iの `thm:LDP` はmetric-IRFAとvolume-IRFAを仮定する。`lem:deep-sector-partition` の深いnormal directionsによる可測分割、`lem:cellwise-LDP` のcompact上界・ambient-open下界、`lem:exp-tight` の一面評価によるexponential tightnessを用い、LDP本体に追加仮定を置かない。下界は正の質量を持つ固定residual compactを使い、exact-support sectorへの制限だけで全ての下位faceの正の質量を要求しない。`lem:level`、`lem:calibration`、`lem:vertex-tightness`、`thm:tail` の指定鎖では、level crossing、固定residual compactでの距離校正、残余無限遠のtightnessとactual metric-ball tailへの移行を直接監査した。全faceのconditional residual momentsを共通入力とすれば通常のvolume-IRFAでvertex tightnessが閉じ、exact tail、joint law、distance Laplace transformにも指数的volume remainderは不要となる（`thm:joint`、`cor:Laplace`）。これらは三研究の共同監査として記録し、距離・平行移動極限を担当した読み手が測度節全体も独立再検証したとはしない。証明・修復の詳細と確認状態の正本はPart Iおよび同repoの研究ノートである。

**固定空間の測度付き平行移動。** Part I v1.6の `thm:translation` は、非空face Iについてmin T_i→∞であれば中心vectorの相対速度によらず、重みe^{ΣT_i}と平行移動射影Π_Tによる測度が $e^{-\sum s_i}\,ds_I\otimes\lambda_F$ へ収束することを示す。通常volume-IRFAのL1支配により、固定normal strip×全residual space上で全変動誤差を明示する（`eq:translation-TV-strip`）。Metric-IRFAに加えnormal offsetとresidual basepointが収束すれば、固定gのscale-one極限は $\mathbb R^I_{\boldsymbol c}\times F^\circ$ で、全半径のambient閉球の押出し測度も全変動収束する（`eq:translation-TV-ball`）。Smooth volume-IRFAは不要である。この極限の直接点検は、全残余上で深部1となるcutoff、短いambient経路のnormal/residual退出排除、段階的torus connectionと終点補正、基点offset、およびnormal Lebesgue方向による全球面の零測度性である。退化族のt一様な測度極限やtensor比較の証明としては使わない。

**Stokesとface massの規格化の共同点検。** Part Iの `lem:CW` は、滑らかなHermitian基準曲率Θに対するω−Θ=dβと、Poincaré型計量でのω・βの有界性を仮定する。有限体積cutoffを用いる直接Stokesで積分を滑らかな基準曲率へ戻し、potential自体の有界性は要求しない。KE pairへの適用条件は `app:CW`、残余strataへのadjunctionとnormal torusの規格化は `thm:facemass` が正本である。Period 2πのnormal circlesを既に積分した $\lambda_F=(2\pi)^{|I|}dV_{g_F}$ を用いるため、face massの式にnormal torus係数を二重に掛けない。非正規化体積μ=dV_gに対して、L=K+D、k=codim Fとすると $\mathfrak m_F=(2\pi)^n(L^{n-k}\cdot F)/(n-k)!$ である。確率測度μ/vol_g(X)からは $\widehat{\mathfrak m}_F=\mathfrak m_F/\mathrm{vol}_g(X)$ を得る（`rem:probability-face-mass`）。異なるfaceへの拡大極限の質量であり、互いに素な分割の確率として全faceの和を1にしない。この適用条件と規格化は共同点検として記録し、本repo担当者による全一次文献の独立再検証とは区別する。

**全faceのvolume-IRFAとMellinの共同点検。** Part Iの `lem:Mellin-conditional-moments` は全full faceの整合するvolume-IRFAから、条件付き残余測度のsubcritical exponential momentsを、normal深度Tに関するessential supremumで一様に抑える。この共通入力は上記のvertex tightnessにも用いる。`lem:Mellin-weighted-TV` は非加重TV誤差δ(T)とHölder補間から、compact subcritical parameter set上で $C\delta(T)^{1-\tau_*/q}$（$\tau_*<q<1$）のweighted TV評価を与える。任意に選んだ支配関数b_F自体のweighted momentを追加仮定せず、`thm:Mellin` と `thm:Mellin-recursion` のAbel residueとadjunction recursionを得る。一様性はcritical boundaryから離したparameter集合についてのもので、残余parameterもcriticalへ動かす場合の極限順序は正本に従う。

Component-labelled mixed transformの係数は、I⊂J、F⊂D_I、G⊂D_Jについて $\mathfrak m_G\mathbf1_{\{G\subset F\}}$ であり、正のface massesとともにincidenceを検出する（`prop:Mellin-incidence`）。Face massの数値列だけからincidenceを決める主張ではない。複素meromorphic continuationには、角・残余方向のL1 coefficient/remainder評価を伴うjoint polyhomogeneityを追加する（`rem:Mellin-continuation`）。`ex:Abel-not-meromorphic` のabstract cusp measure $e^{-t}(1+1/t)\,dt\,d\theta/(2\pi)$ はordinary volume-IRFAとAbel極限を満たすが、transformのsimple poleを引いた後にlog(1/ε)が残り、有理型延長しない。これはKE体積の反例ではなく、ordinary volume入力だけからの推論の限界である。これらは共同点検として同期し、一面だけの非加重L1評価や退化族の評価へ適用範囲を広げない。

**測度の先行結果と標識付きperiod。** Chambert–Loir–Tschinkel, *Igusa integrals and volume asymptotics in analytic and adelic geometry* (2010) のresidue measures・Clemens complex・Igusa leading coefficientによる層上の質量の解釈と重なる部分は、Part I Introductionの一次比較に従う。本稿のlog-log depthとordinary recursive L1漸近による一側Abel極限に、同論文のsmooth heightに対する有理型延長を無条件に移さない。書誌・正確な引用箇所と共同監査の範囲は固定配置repoの本文・`research/source-audit.md`を正本とする。

Part II v2.1の `prop:partI-translation` はn≥2の非空faceについてPart Iの測度付き平行移動をcomponent-labelled collarとdeeper-face labels付きで利用し、factorと各cuspの標識を保つ。n=1は原空間自身のperiodという別の自明な場合として扱う。複素periodを得るにはKähler orientationも保持する。`thm:intro-unoriented` で忘れるのは向きだけであり、裸の距離極限からlabelsが復元されるという主張ではない。一般secondary WP completionの `hyp:controlled-pushoff` は残る。この標識・向き・条件付き完成化の整理は共同点検の同期であり、Part IIの代数・Torelli・WP証明全体を本repoで独立再検証したものではない。曲面側の第二symplectic actionとの同一視もしない。

**曲面の中間尺度における全移動基点の四型。** 曲面改訂36の `topo:cubical-local-models` / `topo:cubical-moving-blowups` は有限cubical targetのambient小球と移動基点の拡大極限を分類する。`ke:intermediate-moving-classification` はP0の同じ全射f_tとそのdistortion ε_tについて、a_t→∞、a_t/R_t→0、R_t ε_t/a_t→0なら、任意の退化列・任意の移動基点の中間尺度の極限が部分列上で存在し、次の四型に尽きることを示す。

| 極限の型 | 基点と模型 |
| --- | --- |
| 成分錐 | (C_{2,d−1},z)。zは任意の有限点。 |
| 分岐する半平面の積 | (R×Y_{d−2},(0,z))。Y_mは原点を共有するm本の半直線、zはその任意の有限点。 |
| 全角3π/2のEuclidean錐 | (K_{3π/2},z)。三つのquadrantsを循環的に貼った錐、zは任意の有限点。 |
| 平面 | (R²,0)。 |

条件を満たす任意の尺度・退化列に対して各型と各有限基点を実現できる。証明は既存の全域歪みをR_t/a_t倍して閉球を比較し、有限targetの分類とf_tの全射性を使う。曲面側の共同点検を同期したもので、Part IV/Vの新しいtensor解析入力ではない。R_t ε_t/a_t→0を外した全中間尺度、labelsの追加復元、tensor収束、CP/PBE/TCの検証は結論しない。

**成分錐の頂点を指定する場合。** `topo:component-cone-germ` は、cubical targetの成分頂点e_iの小球を$C_{2,d-1}$の小球と等長同定する。`ke:intermediate-component-cone` は同じP0のdistortion $\epsilon_t\to0$ と、非空領域 $A_t$ のtarget変位 $\eta_t=\sup_{y\in A_t}d_\square(f_t(y),e_i)\to0$ に対し、$a_t\to\infty$、$a_t/R_t\to0$、$R_t(\epsilon_t+\eta_t)/a_t\to0$ なら、任意の $y_t\in A_t$ を基点として $(X_t,a_t^{-1}d_{g_t},y_t)\to(C_{2,d-1},0)$ となることを示す。固定半径の球の近似誤差は基点の選択に一様で、$a_t=R_t\sqrt{\epsilon_t+\eta_t+R_t^{-1}}$ と選べる。$A_t=f_t^{-1}(e_i)$ は $\eta_t=0$ の場合である。

同じP0の共通anchorで選んだ一成分のcoreと変更collarには、`ke:global-base-parameterization` から $\eta_t\le Cq_t$、$q_t=(1+\log(N_{j(t)}+1))/R_t\to0$ が成り立つ。従って $a_t=R_t\sqrt{\epsilon_t+q_t}$ はその全領域の任意基点に使える。距離は全曲面ambient距離であり、core内在距離やLiouville軌道長の評価を要求しない。これはPart Iの固定成分の漸近錐との接点だが、Part Iの証明を退化族へ直接適用せず、任意の中間尺度・極限交換・tensor収束・有効な収束速度を結論しない。証明は曲面稿 `ke_global_metric_realization.tex` に置き、本repoには利用条件だけを記す。

**K2/K3の限定した接続監査。** 曲面稿の [研究ノート](https://github.com/uedakazushi/surface-lagrangian-torus-fibration/blob/c056ecba5d25a55f135e739faab5993582814484/research/notes.md) と [依存表](https://github.com/uedakazushi/surface-lagrangian-torus-fibration/blob/c056ecba5d25a55f135e739faab5993582814484/research/ke-dependencies.md) を正本とする。K2は `ke:quantitative-order-hamiltonian` と `ke:neck-corner-saturated-union` のcutoff・逆flow・moment・同じ全torusの順序、K3は `ke:closed-component-link`、`ke:star-cover-adapted-primitive`、`ke:saddle-moving-relative-interpolation`、`ke:link-relative-collar-gluing`、`ke:actual-global-fibration` の支持と選択順序を独立内部点検した。全K2交わりを含む恒等collar、補間後partitionに対するwhole-fiber trim、固定compactを保持した全域被覆を確認し、対象内で訂正を要するギャップは見つからなかった。任意に指定したcore germの延長や任意の第二actionの一致を仮定した議論ではない。全上流入力・全文献の再検証やCP/PBE/TCの検証とは区別する。

## K5のactual相対接着・五次の同時実現と残る条件

全域主定理から逆向きに実読した範囲を次に集約する。証明の正本は曲面稿であり、この表は新たなPart IV/Vの解析入力を主張しない。

| 対象 | 確認した条件と結論 |
| --- | --- |
| `ke:fixed-component-transfer`、`ke:component-relative-flux`、`ke:component-exact-collar-germ` | 固定graph gaugeの明示的な小さいprimitive差を用い、全flow bufferを先に固定してexact Moserを行う。二形式の収束だけからprimitive periodsの一致を推論しない。任意の点固定collar germには相対flux条件があり、全域P0はactual linkの葉から構成するため任意germの延長を要求しない。 |
| `snc:reeb-leaf-kernel`、`snc:fixed-holonomy`、`snc:minimal-holonomy-controls` | 固定coupling chartsでbasic＋exact cutoffを行えることは、各成分のg_a個の独立regular-leaf periodsの消滅と同値。Holonomyで障害を消す際は一般に元のfull saddle collarsのliftを固定できず、障害消去後のbasic補正とは区別する。 |
| `ke:actual-limit-weinstein-core`、`ke:actual-centered-primitive-weighted`、`ke:star-cover-adapted-primitive` | 一つのprimitiveのcentered scalar averagesをexactに貼り、core近傍では補正を零にする。Cusp重み付き評価でZΨ>0を保ち、新しいtrappingを防ぐ。 |
| `ke:component-meridian-normalization`、`ke:component-shell-primitive-support` | 正residue gaugeとcanonical momentの加法定数をwindingとexact transportで固定する。Cutoffの全支持・全円軌道・flow buffersを一つの固定component compactに入れ、最後にt閾値を取る。 |
| `ke:saddle-moving-relative-interpolation`、`ke:link-relative-collar-gluing`、`ke:actual-global-fibration` | Anchorの同じmarked partitionから相対Diff0自明化を作る。全K2交わりを含むend collarsでは恒等、sourceのμ=0近傍は支持外である。第二作用やcritical valuesの独立指定は結論しない。 |

これらの指定鎖では、現在のP0の結論を妨げるgapは見つからなかった。固定次数・族・weights、残余compactとstage、normal cutsと共通moment interval、component cutと有限bufferを順に決め、その後に全ての小さい複素tの閾値を取る。任意速度のmoving領域や未証明の相対実現を対角選択で代用しない。共有解析や外部文献の以前の対象限定監査は保持するが、今回その全体を再監査したという意味ではない。

### 固定fiberのfree bandとsourceの面積wall

曲面稿 [neck_action_matching.tex](https://github.com/uedakazushi/surface-lagrangian-torus-fibration/blob/c056ecba5d25a55f135e739faab5993582814484/papers/sections/paper/neck_action_matching.tex) の `ng8:fixed-fiber-relative-dh` は、一つの固定t≠0、freeなHamiltonian circle band、E_t/S¹≃J×P、作用不変primitive dλ_t=ω_t・λ_t(V)=μを仮定する。Pは非空境界を持つcompact connected surfaceである。境界のtoric actionsがaffineなら、λ_t−μdθの降下と境界framingの整数windingからStokesによりtotal reduced areaはμ-affineとなる。Reference constantsはtに依存してよく、t=0までのsmooth total-space extensionと中央成分からのtransportは不要である。

`ng8:source-dh-wall` は、周期2π、I_k=|z_k|²/2、重み(1,−1)、μ=I₁−I₂、I₁+I₂≤cという局所模型でreduced areaがπ(c−|μ|)となることを示す。μ=0ではregular partの面積を用い、両側の連続極限に一致する。外側toric cutがaffineでも、source固定点を横切る全intervalのaffine性は従わない。これはactual P0全体の面積計算やatlas不存在の反例ではない。P0の周期1規約からはgeneratorとcanonical momentをともに2πで割って用いる。

`ng8:fixed-fiber-area-scope` のとおり、`ng8:parametric-moser`にはmarked identifications、端のopen germs、positive target areas、総量一致、保存する全collars/capsを含むprotected-area marginを別に確認する。Sourceの近傍を固定するなら変更支持をそこから離し、core collar適合も別入力とする。上の補題・例の直接証明はこの担当が作成し、主担当と別の読み手がH²=0・basic性・windingの符号・面積積分・周期換算を独立に点検した。

### 保持領域の補集合ごとの有限面積配分

曲面稿 `ng8:componentwise-primitive` / `ng8:componentwise-critical-area` は、保持領域Kをdiskの和に限定せず、自由部分の連結成分U_αとcritical regions D_hの実際のincidenceを用いる。新しい固定領域の下で初期のmarked interpolationとrelative Diff0同定が既に与えられた範囲の定理であり、抽象Reeb graphの一致だけからは適用しない。

K内の質量をκ_h、各U_αの面積をM_αとし、r_h=a_h−κ_hをtargetの可動部分とする。非空のfree cell D_h∩U_αにだけ正のx_hαを置いて
\[
\sum_\alpha x_{h\alpha}=r_h,\qquad
\sum_h x_{h\alpha}=M_\alpha
\]
とできることが、同じrelative orbit内で全target areasを実現できる必要十分条件である。差のprimitiveを各U_α内にcompact supportで取り、成分ごとにMoserを行う。K内のmeasureとκ_h自体がparameterに滑らかである必要はなく、自由部分のarea forms・cell massesとr_hの滑らかさを用いる。

`ng8:strict-area-cuts` は、各連結incidence componentの総量一致と、非空properなregion集合Sについてのstrict Hall条件
\[
\sum_{h\in S}r_h<\sum_{\alpha\in N(S)}M_\alpha
\]
を同値な有限判定として与える。孤立regionにはr_h=0を要求する。固定graph・compact parameter上で全条件が成立すれば正の余裕は一様になるが、これは退化tに一様な評価ではない。一般の有限輸送原理を新規成果とはせず、本文の直接証明とmax-flow/min-cutの一次引用に従う。

`ng8:annular-protection-obstruction` は、保持annulusの内側の質量を別regionへ運べないため、全総量と個別marginだけでは足りないことを示す。`ng8:interior-area-cut-obstruction` は両端で正の配分があっても内部parameterでcutが破れる模型である。`ng8:affine-area-cuts` は、r_hとM_αが全てaffineなら両端の確認で十分であることを示す。一般のsmooth familyというだけでは、その端点判定の十分性は従わない。これらはactual KE族の不存在例ではなく、指定の固定領域と入力からの無条件な推論を排除する。

### Sourceの全近傍を保つactual P0の微小実現

`ng8:p0-source-protected-reduction` は、sourceが相異なるregular閉葉上にある既存P0構成から、その葉の小さい飽和annuliをcritical leavesとend collarsから離して保護する。逆像はsource点だけでなくfull compact pinched torusとその近傍を含む。これらを除いた自由部分では、μ=0を跨いでもreduced formsが滑らかである。K内のreduced areaの特異性は変更支持から隔離される。

`ng8:p0-small-area-flexibility` は、固定stage・t≠0・小さいcompact moment区間Jについて、総和零の十分小さいsmooth increments δa_hを実現する。端の指定open intervalsではδa_h=0とする。Source annulusは一つのD_h内部にあるため、補集合が分断されてもincidence graphは連結である。Spanning-treeでrow sum δa_h・column sum0の線形右逆Lを作り、各free cellの積分1のbump φ_hαからρ=1+Σ(Lδa)_hα φ_hαを取れば、十分小さい増分についてρ≥1/2となる。成分別Moserと自由部分のcircle liftを用いて、同じactual形式・canonical moment・normal circle・marked tree・source全近傍・end germs・whole-fiber商を保つ。

元の絶対面積a_h^0やprotected mass κ_hのsmoothnessは不要で、a_h=a_h^0+δa_hの相対増分だけを扱う。小ささの定数は固定stage・t・保護領域に依存する。Critical leavesの全近傍まで追加固定する場合にはincidence graphが分断され得るため、この零総和だけの結論へは含めない。この証明はこの担当が起草し、主担当と別担当が指定範囲を点検した。所定の大きいaffine targetsや退化一様な予算、全intervalのabsolute areaのaffine性を結論しない。

### Actual anchor periodsと五次の限定core chart

曲面稿 [global_action_atlas.tex](https://github.com/uedakazushi/surface-lagrangian-torus-fibration/blob/c056ecba5d25a55f135e739faab5993582814484/papers/sections/paper/global_action_atlas.tex) の `ke:anchor-liouville-actions` は、同じLiouville primitiveと**周期1のcycles**で M=δ−ρ<0、A=∫_βλを固定し、critical rayのperiodsを(rM,rA)とする。Canonical normal actionが実際に存在する共通collarではq=ρ+rMなので、第二作用はA(q−ρ)/Mとなる。Neckの直線c+pqとの一致には
\[
A=p(\delta-\rho),\qquad c=-p\rho
\]
が必要十分である。Core全体へ元のcanonical circleが延びるという主張ではない。Primitive差の残余periodをκ、framing変更をβ_N=εβ+kαとすれば、p=k+εA/M、c+ρ(p−k)=εκとなる。Exact primitive補正でこのperiod差を自動的に消すことはできない。

`ke:actual-anchor-fan-criterion` はactual anchor葉が所定のperiodを持つことを仮定する。五次では有向四角形fに沿うtarget A_b=−M 1_{b=f(a)}、六次Petersenではexternal critical periods0、内部annulusの両端periods0と−Mを使う。Actual overlapsのcycle marking、meridianの負符号、reduced annulusのStokes同定も入力である。この下で同じdomain・skeleton・保持corner葉を用いたLiouville fillingにK4／Petersen作用chartを得る。Faceとbranch格子は飽和し、denominatorは1となる。これは主担当の条件付き構成と共同点検を同期したもので、この担当による追加の全core証明の独立監査とはしない。

`ke:anchor-stokes-budget` は、所定clutching relationと同じ周期1のframingを確認した上で、reference periods c_bに対しArea(P)=−Σc_b−Mを与える。K4のbasin targetsはA_b−c_b、Petersenのexternal targetsは−c_b、内部annulusは−Mであり、総量は厳密に一致する。保持集合がpuncture collarsだけで内側referenceも負ならpositive marginを得る。しかしsource annuli等を追加固定する場合には全有限cutを確認する必要がある。反対側neckの切片・残余period差・整数framing、sourceを含むmarked interpolationと全open overlapsのwhole-fiber一致は、このStokes式だけでは得られない。五次でこれらを満たす新構成は次節に分ける。CP/PBE/TCやPart IV/Vのtensor定理には新たな結論を加えない。

**五次の標準K2 end collarsへのactual適用。** 曲面稿 `ke:k4-actual-end-anchor`（改訂39に統合済み）は、anchor上に追加保持annuliを置かない選択で上の条件を満たす。既存証明鎖の `ke:component-meridian-normalization`、`ke:eq:component-two-action-estimate`、`ke:neck-corner-saturated-union`、`ke:link-relative-collar-gluing` と `ng8:p0-source-protected-reduction` を独立に読んだ。Primitive切替えがB/b_j=5.4までに終わり、全actual K2交わりはb_res/b_j>5.5に入る。Bはsource torus labelで、b_res=B(1+O(b_j^−2))だから、保持collarの最内境界をB=5.45b_jに選べる。Retained cornerの6b_j cutだけでなく、min ell>3b_jの広いconstruction domainと5b_j<B<9b_jの共通reduced葉族を使う。

同じtransported positive meridianでQ_ab=ν_b−ρ_bは厳密である。正のρ_minを固定し、j大→N大→t小の順に取る。q_a=δ=4π/Nのanchorではnormal depthが[N/2,2N]、残余depthが5.45b_jと比較可能であり、深度比に一様な二作用評価とL≫Nからν_b=O(b_j^−1)を得る。従って全十二境界でQ_ab<−ρ_b/2<0となり、任意の有向四角形のK4 targetsを選べる。同じ正meridiansのclutchingは、component内の直線のnormal bundle O(1)を使い、有限chartのxと無限遠chartのx'=x/zのtransitionからΣ[β_ab]=−[α_a]と確認する。P0のgraph・averaging・Hamiltonian isotopiesを通じてこのframingを移す。各βを独立にβ+kαへ変更した基底にはこの確認を流用しない。

Sourceのfull compact pinched fibersはμ=0にあり、各固定j,N,tの後に、それら全体の飽和近傍を|μ|<δ/2へ選べる。Anchor変更を|q_a−δ|<δ/4に支持させれば両者は離れ、sourceを点だけでなく全fiberと近傍ごと保持する。近傍幅のt一様下界やtに関するsmooth choiceは不要である。この選択は、既指定の大きいsource近傍まで保存する主張ではない。この局所coreの証明と、追加保持annuli・全neck interval・反対側germsの面積とframing整合は分ける。局所系の独立点検はこの指定経路に限り、全P0・全core証明・外部一次文献の包括的再監査ではない。五次の全intervalへの拡張は以下の別証明を使う。

### 五次の両端period条件と全moment作用実現

曲面改訂42の [global_action_atlas.tex](https://github.com/uedakazushi/surface-lagrangian-torus-fibration/blob/497b241898bc91787aacb09a97754fa2ea0fccf8/papers/sections/paper/global_action_atlas.tex) の `ke:k4-actual-neck-periods` は、正weights \(w_{i,j}\)、row sum 1、\(\rho_{i,j}=2\pi w_{i,j}\)、有向四角形 \(f_i\) に対して \(x_{i;jk}=\mathbf1_{\{k=f_i(j)\}}\) と置き、両端の整合を
\[
 n_{ij;k}=1+x_{i;jk}+x_{j;ik},\qquad
 \rho_{i,k}+x_{i;jk}\rho_{i,j}
 =\rho_{j,k}+x_{j;ik}\rho_{j,i}
\]
へ帰着する。同じK2 tube上の閉差とnormal periodの零値から共通残余定数 \(\chi_{ij;k}\) を得て、閉差にclutching relationを適用し \(\sum_k\chi_{ij;k}=-2\pi\) を示す。Actual source normal formのargument principleはcritical側のshear \(n_{ij;k}-1\)、K2 end側のshear \(-1\) を与える。非閉primitiveをambient homology relationへ積分していない。`ke:k4-equal-weight-periods` の等重みと対称六系は配分(3,1,1)を与え、`ke:k4-cyclic-weight-periods` には非対称な正weightsの明示族もある。

全intervalの正本は [neck_action_matching.tex](https://github.com/uedakazushi/surface-lagrangian-torus-fibration/blob/497b241898bc91787aacb09a97754fa2ea0fccf8/papers/sections/paper/neck_action_matching.tex) の `ng8:uniform-k2-end-periods`、`ng8:thin-source-tail-choice` と `ng8:quintic-full-moment` である。共通左frameのend actionを \(R_k=\chi_k+\nu_k\) とすると、全intervalのcappingとStokesからtarget reduced areaは厳密に
\[
 a_k^{\mathrm{tar}}(\mu)=\rho_{i,k}+x_{i;jk}\rho_{i,j}
 -x_{i;jk}\mu-\nu_k(\mu)+n_{ij;k}\min(\mu,0)
\]
となる。Criticalとendの異なるshearを引くため、負側の補正は \(n_{ij;k}\mu\) である。全面積は \(-\sum_kR_k-\mu+5\min(\mu,0)\) となり、target総和と一致する。Full-tripleの同じlogarithmic primitiveとexact transportから全momentで \(|\nu_k|\le C/b_r\) を得て、正residueの最小値を先に固定すれば全targetに正の余裕がある。ここでrは解析stageであり、成分標識jと区別する。

Source-freeの `ng8:relative-dh`・`ng8:straight-neck`・`ng8:central-criterion` は全moment band上の自由作用を仮定し、source-inclusive neckの \(\mu=0\) へそのまま適用しない。`ng8:actual-source-area-wall` はcritical region内の全source数を \(n_h\) として、元の面積と保護質量をそれぞれ \(a_h^0=A_h-n_h|\mu|/2\)、\(\kappa_h=K_h-n_h|\mu|/2\)（\(A_h,K_h\) は滑らか）と書く。各sourceの保護領域内に取ったequivariant Darboux ballsの厳密な寄与と、その外のcompact free quotientの積分を分けるため、全marked quotientの通常の滑らかさや元の残余座標を保つDarboux chartを仮定しない。`ng8:source-corrected-area-demand` の条件は \(a_h^{\mathrm{tar}}-n_h\min(\mu,0)\in C^\infty\) である。Targetと保護質量の全source-wallが相殺し、自由需要 \(a_h^{\mathrm{tar}}-\kappa_h\) は全intervalで滑らかになる。面積自体をaffineにする要求とは異なる。

初期source allocationと順序を指定したrooted treesを使い、全区間で同じP・source marks・K2 end collarsを固定する。SourceとK2補正の支持を避ける小さい内部saddle diskを先に確保し、treesを避けさせる。Graphはsource外のsmooth densityとsource点の零質量により面積零であり、Darboux-ball除去とfree部分の積分から近傍質量は \(\mu=0\) を含めて連続である。固定end massを除いた追加近傍の質量にDiniを用い、sourceの全tailをtargetより小さくして全strict cutsを満たす。Source annulusの幅だけを縮めてtailが消えると推論していない。Saddleを先のdisk内へ移せば、sourceとsaddleの点近傍では局所葉が \(\mu\) に依存しない。初期葉とannuliは引戻し座標で取り、\(D_{r,\mu,t}\circ S_t\) による像を用いる。新しいannuliをS_tが集合として保つことは要求しない。

両coreとの接着は、marked interpolationの後に同じtargetへのparameter-relative面積Moserを施す。両open germsは既にtargetを満たすため保持できる。最後のfree bandでも補助primitiveのfirst jetsを有限source sections上で零にし、点を全Moser時刻で固定してallocationとframingを保つ。実際に保持するfull compact nodal neighborhoodsは \(|\mu|<\delta/2\) 内に先に凍結し、anchor変更の支持から離す。

量化は、正weights・有限compatible data・rooted treesのmarked class、残余compactと解析cuts、十分小さいt、thin葉の幅と支持、source全近傍の凍結の順である。S_tはsource disksとsingle-valued source sectionsから先に固定し、DはK2 radial collarsだけで決める。Thin葉の微分に応じて解析領域・写像を再定義しない。固定基準葉が必要なら \(\mu\) に依存しない \(H_{r,t}\in\mathrm{Diff}_0\) を先に合成できるが、そのC^k一様性やt方向の滑らかさは使わない。同じ初期葉から通常P0と作用指定版をそれぞれ構成し、同じP_rの外へ支持を拡大しない。Connector boundsは全同一moment集合に対するambient費用で、clipped-depth mapも同じ形式・cutsで決まるため、fixed Tと同じ遅い対角選択を保ち、thin幅の選択後に新たなt閾値を課さない。既固定の任意P0や大きいsource tailsに対する変更ではない。保持tailがあるmomentでtarget以上なら、ordered cutsが相対実現を妨げる。

指定証明鎖の内部点検では、新実文と既存面積定理・source wall・全moment connector・相対置換を照合した。全intervalのprimitive bound、正負cappingと全量、Diniの連続性と固定end mass、最後のfirst-jet補正、初期葉からの二構成は担当・統合担当・別の読み手が確認している。改訂42ではsource-freeな旧補題の適用範囲、thin葉より先に固定する解析データ、全三面共通の実数平行移動を明示し、本資料はその指定箇所を同期した。全主稿・全格子接着・全一次文献の包括的再監査、形式証明、外部査読又は新規性の網羅的確認とは区別する。

### 共通momentを保つ変更のGH安定性

曲面稿 [ke_global_base_compatibility.tex](https://github.com/uedakazushi/surface-lagrangian-torus-fibration/blob/c056ecba5d25a55f135e739faab5993582814484/papers/sections/paper/ke_global_base_compatibility.tex) の `ke:moment-relative-replacement` は、変更後のactual局所fibrationが既に得られた場合の条件付き定理である。同じ保持cornerと全K2 end collars、sourceのcompact nodal neighborhoods、canonical normal momentの向きと加法定数、anchor cutsとcore/変更collarを保つ。実際のmarked product自明化・compatibleなcore cone商・全overlapでのwhole-fiber一致も要求する。木の抽象同型やnormal circleの一致だけでは足りない。

この下で、同じcubical targetへのparameter化を保持corner上で厳密に一致させ、sup_x d_square(f̂_{j,t}(x),f_{j,t}(x))≤Cη_{j,t}、η_{j,t}=A(1+log(N_j+1))/R_tとできる。Cは固定次数・族と有限targetに依存し、reduced葉を変更するdiffeomorphismの微分には依存しない。`ke:relative-replacement-gh` は同じ遅い対角列でdistortionと、各coarse fiber（一つのp_T-fiber上の葉の合併）のambient径の消失を与える。主担当の証明と別担当の独立点検を同期したもので、この担当による追加の全証明再監査とは区別する。曲面稿の `ke:quintic-simultaneous-realization` は上の全moment構成にこの評価を適用し、同じactual Lagrangian射影に作用適合matroidal atlas、全域distortionの消失、全coarse fibersの正規化ambient径の消失を同時に与える。Focus valuesには穿孔focus affine structureを用いる。等重みと対称六系は有限条件の明示解であり、五次の存在に追加の未検証解析仮定はない。結論は各tでの同時実現であって、atlas自体のt方向の収束、固定した極限affine structure、極限距離のHessian性・Monge–Ampère性を主張しない。任意の追加保持annuli・大きいtailsの相対可解性、t方向に滑らかなfibration族は含まない。六次の標準等重み同時実現は別定理による。

Atlas接続は `ke:eq:quintic-branch-action-coordinates`・`ke:eq:quintic-core-branch-extension`・`ke:eq:quintic-affine-full-transition` に実数切片まで記載する。全periodsを同時に2πで割り、四角形のpredecessor指標を \(y_k=\mathbf1_{\{f_i(k)=j\}}\)、\(y'_k=\mathbf1_{\{f_j(k)=i\}}\) とすれば、両core faceの座標は
\[
 \zeta'=\zeta,\qquad
 s'=-s+(y_k+y'_k)\zeta+w_{i,j}+w_{j,i}
\]
で結ばれる。三面共通の平行移動は \((w_{i,j}+w_{j,i})r_{ji}\) で、非対称な正weightsにも適用できる。残余定数χが相殺するのは同じneck primitiveで比較するためである。全開collarで既に一致する実際の葉と作用を入力とし、整数行列だけから葉の接着を推論しない。

先行研究との直接の比較では、[Fernández de Bobadilla–Pełka, arXiv:2312.13248v4](https://arxiv.org/html/2312.13248v4) Remark 5.9はramification locusとouter boundaryを除く部分にaction-affine構造を与え、Theorem 6.14は構成された補助symplectic形式の計量により、properな場合に全fiberのGH収束を含む。局所・部分的GHだけの結果と記述してはならない。[Evans–Mauri, arXiv:1905.09229v3](https://arxiv.org/html/1905.09229v3), Remarks 2.11–2.12はcontact actionとLiouville radial方向の作用の斉次性を述べ、Lemma 2.16はcone extensionを与える。これらの既知の構成原理と正則部分の作用座標を認めた上で、actual負KE形式上のbranch/coreを含むatlasと同じ射影の全域GH実現という本稿の接続を比較する。Atlasのt極限やHessian性はこの差分の主張に加えない。

`ke:raw-moment-error-insufficient` の障害はprofileの尺度にある。固定stageと0<α<β<1についてμ_t=−L_t^(−α)、ν_t=−L_t^(−β)なら|μ_t−ν_t|→0だが、共通longitudeはそれぞれα、βへ収束し、target差は消えない。近似matchingにはraw momentのo(1)ではなく、longitude profileの一様誤差制御が必要である。この例は実際のatlasの不存在を意味しない。五次の同時実現も、Part IV/Vのtensor結論、CP/PBE/TC又はPart IIIのH_loc/H_ancの未検証状態を変更しない。

## Source-free neck：正則作用とactual metricの接続

現在の証明の正本は主稿の `source_free_neck_coordinates.tex` と `source_free_neck_comparison.tex`。固定次数d≥5、sourceとtriple pointsを避ける固定compact base Kに限る。前者の `pair:prop:bundle-conic` がexplicit normal form、`pair:cor:global-primitive` が単一primitive、`pair:thm:fixed-end-moment` / `pair:cor:actual-common-moment` が円平均η_tの共通moment stripを与える。

**座標の障害と修復。** 局所conic overlapをcomplete C*の自己同型と分類してはならない。例えば(u,v)↦(ue^u,ve^(−u))は原点近くで正則可逆、uvとlabelled axesを保つが、base-only乗数ではない。この例はnormal formの不存在を示さない。射影P(V)からD=P(W)へのprojectionを先に固定すると、P(V)＼P(U)=Tot(O_D(1)⊕O_D(1))でtransitionは初めからbase-onlyである。h=−F_d/G、h0=h|Dを用いるx_i'=x_i h0/h、x_j'=x_jがexact方程式へ移す。旧 `sharp:prop:conic-normal-form` の証明をこの構成へ置き換えた。

**Momentの規約。** d^c=(i/2)(bar∂−∂)、circleのperiodは1、ι_Vη=−dμとする。Ω=dlogv∧τに対するλ=d^c log(ω²/|Ω|²)を固定するとμ=(Aλ)(V)。τ'=bτの場合のλの差はbaseからの閉形式−d^c log|b|²であり、normal momentは不変だがresidual action periodsのためには選択を固定する。各conic fibreでdμ(−JV)=η(V,JV)>0。

**固定endとmoving end。** s_r=−log r²についてμの両end値は±4π/s_r+O(s_r^(−1−δ))+o_{t→0;r,K}(1)。まずrを固定し、その後tを小さくする。Song (arXiv:1706.01518, Definition 2.3, Lemmas 4.4–4.5)の固定gauge収束とRochon–Zhang (arXiv:1106.0873, (5.5)–(5.6), Theorem 5.1)のSNC potential remainderを使う。Period 2πのgeneratorなら主項は±2/s_rとなるので規約を混ぜない。Smooth-divisor full expansionをSNCへ無断で適用していない。共通intervalからradial derivativeの一様下界や全neckのMoser生存は従わない。

**平均の順序とperiods。** 関連Lagrangian主稿 `ke:staged-neck-averaging` ではη=A1ω、κ=A2η、φ*ω=η、ψ*η=κとし、Θ=φψを使う。第二flowはnormal S¹にequivariantで、Θ*λ=A2A1λ+dq、μ∘ψ=A2μが厳密に成り立つ。原primitiveと整数cycleを共通に固定すれば全periodを追跡できる。同じnormal actionだけでは、独立に指定したneckの第二periodやreduced leavesの一致は得られない。共通bufferの下で一段階bundleとのHamiltonian比較があり、指定subgroupのactual closed cornerにも従来と同じGH率がある。

**解析の残り。** `neck:prop:volume-envelope` は固定residual compact上でc h²≤ω²≤h²のみを与える。拡幅annulus×D₂と同じannulus×D₃のcomplete product metricsの制限は、全人工境界を越えて滑らかで、normal depthが発散しても中心volume比9/4を保つ（`neck:prop:residual-boundary-obstruction`）。これはactual compact familyの反例ではなく、local residual boundary情報の不足を示す。Zhang (arXiv:1505.04728v2, Lemma 3.3, (3.10)–(3.12))の正次元stratumの極限もpotential φ₀(x,z)とmixed termsを残す。

固定baseの補題からactual circle長へ進むための解析入力は `neck:lem:rank-one-circle` のp*h_D≤Aωである。曲面稿の `ke:fixed-base-neck-moser` は必要な固定段階bufferを別に証明する。Volume上界と合わせれば、Hermitian matrix G=[[a,c],[c̄,b]]に対しdetG≥a/A、従ってa≤ABとなり、mixed coefficientsがあってもnormal circle長を抑えられる。Actual metric ball bufferがあればlocalized Chern–Luでこのrank-one下界を得るが、そのbufferを欲しいtensor比較から逆算しない。Full tensor比較にはsmall log-densityと一様smooth背景、あるいは別の解析が必要。Complete strip×curveへのglobal延長・完備性・bounded log-ratioを仮定すればOmori–Yauによる一意性でproductを同定できるが、fixed residual discの極限だけではこれらの条件を満たさない。

## 境界密度からの局所安定性と全平面族への適用

正確な三重点座標ζ0ζ1ζ2=t、ell_i=−log|ζ_i|²、L=−log|t|²、R=log Lを用いる。`coarse:thm:boundary-to-triple` は大域compactificationや全平面退化を仮定しない。固定m₀,c_*>0について、全phaseを含むD_{t,m₀}={min ell_i>m₀}の閉包近傍で各ω_tが滑らかな負KE metricであり、全ての固定faceでω_t²≥c_* V_Lを満たすことを入力とする。m₀,c_*に依存するm₁,L_*と各qのC_qを用い、L≥L_*、m₁≤m<L/3で
\[
 \left|\log(\omega_t^2/k_L^2)\right|\le C/m,\qquad
 \|g_t-g_L^{\mathrm{sf}}\|_{C^q(g_L^{\mathrm{sf}})}\le C_q/m
\]
を得る。全深度比・全位相に一様で、normはnormalized holomorphic covering chartsまたはmodel covariant normで計算する。各固定tでsmoothであればよく、tに関する正則性や境界上界のt一様性は要しない。

**最小入力と証明の向き。** 下barrierは固定c=M m₀で外へずらす。境界の一因子が(1+M)^(−2)となるため、L≥6cと9/4(1+M)^(−2)≤c_*から境界volume下比較を得る。負の内部最小値を排除して全域へ延長する。上barrierはm₀だけ内へずらし、complete模型のdensityが全人工境界で発散する。Actual densityは各固定tのcompact閉包で有限なので比は境界で0へ向かい、その上界をt一様に取らずに最大値原理が閉じる。Phaseのcompact quotientを外して非周期無限coverへ一般化することはできない。Coverはこの比較の後、局所正則性のために用いる。

Shift評価により小さくなるv=log(ω_t²/k_L²)自身が、同じRicci規格化によるdd^c v=ω_t−k_Lを満たす。m₁≥4cを取ると、最大深度を従属にした固定相対窓の全深度は3m/4以上となり、Savinの閾値をqと独立に固定した後にSchauderで各qを得る。Interiorのdensity下界、actual tensor buffer、actual境界逃避を入力に加えていない。

全平面退化への適用は `coarse:thm:full-triple-tensor` に分ける。一般性 `ass:Gd`、固定d≥5・固定族に対し、`coarse:cor:degree-d-volume-lower` とlocal residue比較が上記のfixed-face下界を与える。三重点の有限性から定数を共通にする。次数一様性、source全体のtensor比較、大域GHはこの局所適用の主張ではない。

**局所安定性核の独立内部点検。** 別の読み手が局所定理と単一証明、small-volume-tensor、全平面への適用を読み、compact phase quotient、内外barrierの符号と全境界、t一様上界の不要性、coverへの移行順序、Savin/Schauderの量化を確認した。Savinのauthor PDFのH1/H2/H4・Theorem 1.3もその担当が再読した。指定鎖に新たな結論阻害gapは見つからなかった。この点検は以下のcapped determinantの指定鎖の監査と範囲を分ける。全一次原著の包括的な再監査、新規性確認、外部査読・形式証明ではない。

固定toric模型k_Lの存在・一意性・完備性にはZhang (2015), 第2.1節、Theorem 2.1 / Proposition 2.2を用いる。退化族のTheorem 2.4やQ-factorial仮定は使わない。ψ_L=log L−Σlog ell_iと内外translated-simplex barriersによりψ_L−(log3)/2≤φ_L≤ψ_L、V_L/3≤k_L²≤V_Lを得る。半平面へのSchwarz評価とdeterminant上界からtensor二側比較を先に確保し、内部正則性で全高階を制御する。Log-densityの凸性から固定量のfacet shiftによる誤差O(1/min ell)を得て、actual volumeを内外の模型で挟み、小さいpotentialへSavinを適用する。証明の所在は `coarse:lem:simplex-model` / `coarse:lem:simplex-shift` / `coarse:lem:small-volume-tensor`。

**Capped volume入力の監査と定量化。** Part IV v1.11では `coarse:lem:capped-positivity` → `coarse:lem:weighted-cap-lower` → pair/triple数値補題 → `coarse:thm:global-determinant` → `coarse:cor:degree-d-volume-lower` の全指定証明鎖を直接点検した。結論を妨げる誤りは認めず、Chern derivativeによる軸上も滑らかな式、吸収の明示的閾値、residueの規格化と有限coverの量化を本文へ補った。固定positive backgroundに対しΘ_i≤k_i h0、α_*≤α_iと取ると、`coarse:eq:intrinsic-cap-curvature` は
\[
 dd^c(-2\log\alpha_i)
 =-\frac{2\chi_i}{\alpha_i}\Theta_i
  +\frac{2(\epsilon\alpha_i+s_i)}{\alpha_i^2(s_i+\epsilon)^2}
       \sqrt{-1}\langle\nabla' L_i\wedge\overline{\nabla' L_i}\rangle,
 \qquad \epsilon=|t|
\]
を与える。α_*≥max(1,4Σk_i)でhlow≥h0/2となる。Holomorphic directionsへ移す際はμ_i≤1/(2α_*)+2/α_*²と固定frame定数K_bを用い、`coarse:eq:cap-absorption-budget` の全誤差≤1/2を先に課す。FS metricsなら正値性だけの十分条件はα_*≥4d/(d−4)だが、frame吸収とdeterminantの定数は別に固定する。

Pairではχ_u≥(1+√C0)^−1かつ反対capのα_v≥L/2+A0−log(1+C0^(3/2))、tripleでは二つのχ≥(2C0+1)^−1かつ残るα≥L/3+A0−log(C0^(1/3)+1)を用いる。これらは深度比・全phaseに一様である。六型のambient領域とA0を固定し、有限個のunit/Jacobian/minor下界とLの下限を選んだ後に、全小複素tの共通閾値を取る。中央fiber近傍の外のcompact領域ではplane積のnormが正数以上なので、小tの全X_tが六型coverへ入る。

Canonical densityは固定adjunction frameのnorm逆数とresidueの二乗であり、局所方程式のunit Pと座標Jacobianを保持する（`coarse:eq:residue-density-normalization`）。Sourceでは元のplane coordinates x,yを保つz=−F_d/Pによりxy=tzを正確に得る。Central rescaling x=τX,y=τY,t=τ²では、|t|Q_xと|t|Q_yが軸上もc_d/L以上であり、residueの1/tはdx∧dyで相殺して−dX∧dYとなる。Oriented armsではcapとdzの二方向を使う。Fixed dのinactive capsは一様有界で、三重点以上の新模型は生じない。各smooth compact fiberでlog(ω²/Ωlow)の最小点を取り、ddc log(ω²/Ωlow)=ω−hlowの符号から全域下界を得る。Sourceの軸や全phaseを取り除いた非compact領域へ最大値原理を移していない。大域potentialと下界の範囲は `coarse:rem:capped-global-potential` に明記した。

上の補強は直接微分、正のrank-one formsのminor、adjunction residue、compact最小値原理による。新たな外部解析定理は加えておらず、Aubin–Yauの存在論を含む原著全証明の再監査ではない。指定鎖に(TC)/(PBE)、actual tensor比較又はactual metric bufferへの循環依存はない。次数一様性、global potential上界、source全域tensor漸近、任意速度のmoving域へは結論を広げない。

**Complete envelopeの上比較。** `coarse:lem:complete-volume-upper` の一般形は、complete負KE形式hに対するlog-volume ratio uが上に有界であることを仮定する。Ricci下界によるLaplacian型Omori–Yauを使い、複素次元2でtr_hω=2+Δ_huと算術幾何平均からω²≤h²を得る。Hessian型原理は不要で、完備性だけからsup u<∞を推論しない。本稿のfinite ball、annulus–disc、product-annulus windowsでは、各固定tでactual densityが人工境界を越えて有限に延長し、explicit complete modelのdensityが全人工境界で発散するためu→−∞となる。Angular coversは周期性で同じ上界を持ち、residual universal coverには内部のfinite disc windowを使う。Source xy=tzのenlarged annulus–discはy=tz/xにより固定chartへ延長するので、有限quotient上の直接の最大値原理だけでも上比較が閉じる。非周期な無限coverへ適用する場合の上有界性は別の確認事項である。

## Simplexの境界における鋭い模型

証明の正本は `papers/sections/simplex_boundary_geometry.tex`。角度θ_iの周期は2π、w_i=ell_i−2iθ_iのimaginary periodは4πである。各cuspの実計量は(d ell_i²+4dθ_i²)/ell_i²、logarithmic volumeの係数は8。以下のCq評価はangular universal coverの固定半径ball上、同値な模型covariant normで行う。Pure modelでは深度に絶対的下限を置かない。

### Rank-oneの正確な係数とactive co-Gram

`simplex:lem:rank-one-schwarz` は各iについて
\[
 \frac{d\ell_i^2+4d\theta_i^2}{\ell_i^2}
 \le g_L^{\mathrm{sf}},\qquad |d\log\ell_i|_{g_L^{\mathrm{sf}}}\le1
\]
を与える。Target formをiq(z)dz∧dbar zとするとRic=−ωから∂z∂bar z log q=q。u=tr_k f*ω_Hに対してΔ log(q∘f)=u、source Ric=−kのholomorphic one-form Bochner計算からΔ log|df|²≥−1なので、Δ log u≥u−1となる。既存の粗い比較でuは有界、complete Ricci下界のmaximum principleでu≤1を得る。実計量へ戻す際の余分な因子2はない。

`simplex:cor:active-cogram` により、ell_i≤Le^−Aのactive indices I、1≤|I|≤2、に対して
\[
 G_I=\bigl(\langle d\log\ell_i,d\log\ell_j
                 \rangle_{(g_L^{\mathrm{sf}})^{-1}}\bigr)
      =\mathrm{Id}+O(e^{-A/2}).
\]
二つがactiveなら誤差はO(e^−2A)。一つなら、残る二深度の小さい方aについてa≤Le^(−A/4)の場合をdominant比較、それ以外をfacet比較で覆う。Actual metricにはO(1/min ell_i)を加える。これは三重点内の結果であり、sourceを含む全域の(PBE)_d付きsharp co-Gramを無条件化したものではない。

### Dominant領域の二重cusp

独立深度a,bとδ=(a+b)/Lについて、`simplex:prop:dominant-product` は
\[
 1\le k_L^2/\omega_{\mathrm{prod}}^2
 \le\left(\frac{\pi\delta}{\sin(\pi\delta)}\right)^4
\]
を全点で与える。下比較にはexpanded quadrant (−c,∞)²を使いc↓0、上比較にはA=La/(a+b)、B=Lb/(a+b)のrectangle (0,A)×(0,B)を使う。上側cornerがtriangleの境界にあるため、先に(τ,A−τ)×(τ,B−τ)へ縮め、τ↓0とする。これにより共有境界でdensityの発散率を比較する必要がなくなる。

固定product ballsでsmall potentialはO(δ²)、Savinと線形化後のSchauder評価により全固定階のtensor誤差もO(δ²)となる。`simplex:cor:actual-dominant-product` はactual誤差
\[
 O\bigl((\min_i\ell_i)^{-1}+\delta^2\bigr)
\]
を与える。特に0<η<1/2、a,b∈[L^η/2,2L^(1−η)]の開正方形領域ではO(L^−η)。関連Lagrangian主稿 `ke:open-cell-collapse` は固定長方形Kη=[η,1−η]²への内在GH収束とprojection distortion O(L^−η)、fiber径O(L^−η)、raw mapとの誤差O(1/R)を与える。

Actual chart内のexpanding annuliにshifted-sinh lower barrierとcomplete-annulus upper barrierを直接適用する方法も `coarse:thm:moving-triple-tensor` に保持する。保護条件e^−ρ min(a,b)≥m0、e^ρ(a+b)≤L/2の下でsmall potential O(e^−ρ)を得る。この方法はglobal density floorを有限境界値として使う。一方、pure modelの領域包含法にはこの絶対深度条件が不要である。

### Facet領域のcusp–annulus

b=ell_0、a=ell_1、d_*=min(a,L−a)、ε=b/d_*→0と置く。幅Lのfinite annulus coefficient
\[
 K_L(a)=(\pi/L)^2\csc^2(\pi a/L)
\]
を用いたproduct p_L=cusp(b)⊕K_L(a)(da²+4dθ_1²)に対し、
`simplex:prop:facet-product` はmodel error O(ε^(2/3))を与える。Actualではb→∞を加えてO(b^−1+ε^(2/3))となる。a/Lが固定compact subsetにある仮定は不要である。

下比較はtriangleを含むexpanded strip productからc↓0、上比較は(0,β)×(0,L−β)のcomplete productから得る。Volume log-ratioの上界はO((b/β)²+β/d_*)であり、β=(b²d_*)^(1/3)で釣り合う。固定product ballsのendpoint距離は中心のd_*と一様に比較可能なのでSavinを適用できる。外側rectangleは固定模型上だけで用い、actualの比較は深い内側balls上で行う。従って外側rectangleそのものをactual chartに入れる追加条件はない。

## 全閉cornerの距離とLagrangian fiberによる実現

三つのlabels Jについて
\[
 \mathcal C_J=\{w\in[0,1]^J:\max_i w_i=1\}
\]
に三枚のunit squares自身の内在距離d_Jを入れる。m=R、softmax深度
\[
 \ell_a=R+(L-3R)\frac{L^{w_a}}{\sum_bL^{w_b}}
\]
の像をH_{L,R}とし、その全phase preimageをH_{t,R}とする。主稿 `simplex:thm:closed-corner-model` / `simplex:cor:actual-closed-corner-metric` により、R^−2 g_tの距離とd_Jのprojection distortionはO(log R/R)。対象となるactual距離は次の二つである。

- H_{t,R}内に留まる全曲線で定める内在距離。
- 外側保護領域{min ell_i>R/2}内の全曲線の距離をH_{t,R}へ制限したprotected-ambient距離。

Complete modelでは、さらに全simplexの経路を許す距離にも同じ評価がある。Actualについて保護領域外へ出る曲線を許したとは主張しない。

### 全経路の下界と有限galleryの上界

下界の要点は
\[
 \Psi_a(\ell)=\left[
 \frac{\log(\ell_a/R)}{R-2\log R}\right]_0^1
\]
をcomplete simplex全体で定義することである。少なくとも一つの成分が1なので像はC_Jに入る。微分が非零となるactive indicesは高々二つ。一つならexact1 Schwarz、二つならell_j+ell_k≤2L/Rにおけるdominant error O(R^−2)を使う。従ってclipping levelやseamsに長く留まる経路も一様に制御する。幅の小さいseam collarを捨てるだけではこの下界は得られない。

上界ではC_Jのgeodesicを高々三枚の相異なるsquares内の直線分で実現する。各線分を幅4log R/Rだけ内部へ移してsharp product比較で持ち上げ、portalのずれを粗いsoftmax Lipschitz評価で接続する。最後のphase調整費用は正規化後O(R^−2)。証明の所在は `simplex:lem:closed-corner-no-shortcut` と `simplex:thm:closed-corner-model`。

### 同じactual Lagrangian bundleの射影がGH近似となる

関連Lagrangian主稿 `ke:closed-corner-gh` / `ke:closed-corner-protected-gh` は、`ke:actual-closed-corner` と同じMoser像W_{t,J}、同じprojection π_{t,J}について、上記二つの距離でdistortion O(log R/R)を証明する。模型のLie derivativeを直接評価し、Moser pullbackとg_L^sfの相対差O(1/R)を得ることがmetric transferの入力である。

全fiberの非正規化intrinsic/ambient diameterはO(1/R)、R^−2 g_tでのdiameterはO(1/R²)、raw cubical mapとの誤差はO(log R/R)。継目・共通頂点にもregular T² fibersが存在する。これは既存大域fibrationのsource・branch・coreのsingular fibersの同定ではない。C_Jには三枚自身の距離を入れる。曲面稿の `topo:coordinate-retraction` がtarget距離の制限との一致を与えるが、全X_tのshortcutはその局所結論とは独立で、曲面稿のglobal scalar評価で扱う。

## Neck collarの相対接着：利用可能な補題と残る条件

関連Lagrangian主稿 `ke:relative-fiber-preserving` は、torus-saturated collarの元のphase toriが既にω-Lagrangianなら、chain homotopy primitive β=Hωがvertical tangent distribution上で零になることを用いる。Moser vector fieldはそのdistributionに接し、各fiberを集合として保つ。ωのtorus不変性や各点の固定を仮定する必要はない。

`ke:relative-neck-matching` は、別のactual neck fibrationとorbit partitionが一致するcollarで、基底座標をその分割によって同定すれば両fibrationが一致して接着できることを示す。定数係数monomial変更ζ'=c(t)ζ^A、A∈GL(2,Z)は分割を保つが、非定数holomorphic unitを含む変更は一般に分割を変える。同じoverlapに二つのtorus actionsがあるだけでは適用できない。任意の別のprimitiveへ取り替えてもverticalでの消滅は自動的に保たれない。

共同監査ではactual neck–triple overlapの全fiber一致と、source・branch・coreへ至る指定K2/K3鎖の支持・量化を重点点検した。具体的なラベルと確認範囲は冒頭の「K2/K3の限定した接続監査」を参照する。これらの構成の正本は曲面稿であり、閉cornerの局所結果単独から大域接着が従うという意味ではない。大域(CP)_d+(PBE)_dの検証と、新結果の新規性の包括的確認は未完了である。

## 局所windowと残るtensor仮定

三つの深度が同程度のとき、一つの独立二座標product windowで任意半径のconstrained-cusp ballを覆うことはできない（`coarse:prop:triple-product-obstruction`）。最大深度を従属座標にする小さい相対箱は有効であり、全deep triple上のvolume上下界とbounded potentialは `coarse:cor:triple-volume-comparison` で証明する。このvolume比較単独ではtensor比較は得られず、上記のcomplete simplex barriersとSavinを組み合わせてfull tripleの比較を証明する。

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

### Lagrangian化の一般的入力

関連主稿 `surface-lagrangian-torus-fibration/papers/sections/paper/ke_fiber_compatibility.tex` の `ke:short-torus-averaging` と `ke:triple-moving-fibration` が証明の正本。Full-orbit moving domainで $c h_t\le g_t\le C h_t$ を仮定すると、torus平均の短いprimitiveから一つのMoser flowを構成し、全局所fibersを同時にLagrangian化する。$\min\ell_a>m_t$ でambient diameter $O(m_t^{-1})$、raw cubical mapのtarget誤差 $O((1+\log m_t)/R_t)$。$m_t=R_t$ と選べる。高階比較やPBEはこの局所symplectic構成自体の入力ではない。全閉cornerのGH結論には、上記のsharp tensor比較とMoser flowのC1評価を加える。全X_tでのmetric近似と相対接着はこの局所定理には含まれず、曲面稿の別の大域定理で扱う。Ruan, arXiv:math/0309177v2, §3のaveraging–Moser機構に先行研究があり、新規性は未確認。

## KE尺度とLagrangian fibrationの比較

標準規格化 $\operatorname{Ric}(\omega_t)=-\omega_t$ では体積 $2\pi^2d(d-4)^2$ は固定され、成分内部の基点からは $d$ 個の配置補空間の四実次元完備KE極限が残る（Song, arXiv:1706.01518v1, Theorem 1.2；Song–Sturm–Wang, arXiv:2003.04709v1, Theorem 6.1）。径の尺度 $R_t=\log(-\log|t|^2)$ のcubical候補とは異なる極限である。

Zhang, MRL 22 (2015), 1843–1869, DOI 10.4310/MRL.2015.v22.n6.a16, arXiv:1505.04728v2, Theorem 2.4の局所collapseにはQ-factorialなsimple toroidal全空間と相対canonicalのamplenessを仮定する。Source germ $xy=tz$ とそのcrepant small resolutionでは両条件を同時には満たさず、局所型の類似だけで直接適用しない。詳細な先行比較・仮定の適用計算の正本は[関連Lagrangian研究ノート](https://github.com/uedakazushi/surface-lagrangian-torus-fibration/blob/main/research/notes.md)。

Part Vの写像 $\Phi_t$ と選んだLagrangian fibration $\pi_t:X_t\to B_d(T)$ を対応させるには、$b_t=\sup_xd_\square(\Phi_t(x),p_T\pi_t(x))\to0$ を別途検証する。$\operatorname{dis}(\Phi_t)\le a_t$ なら $\operatorname{dis}(p_T\pi_t)\le a_t+2b_t$、全fiberのambient直径も同じ量以下となる。証明は関連主原稿の `topo:ke-map-compatibility`。これは三角不等式による比較であって、(CP)$_d$+(PBE)$_d$や大域actual適合性を証明したことではない。五次では $p_T$ は同相、六次以上では基底の木も収縮する。

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
c_B(0)=2/B、−c_B(0)^−1∂Z∂barZ log c_B(0)=B−1。したがって一様な曲率上界を持つreferenceとしてh_lowをそのまま使えない。これはΩ_lowのdensity比較やglobal determinant下界への反例ではない。現行のvolume-barrier法はh_lowのtensor/curvature比較を用いない。

## 確認済みの解析文献と未確認の比較先

- J. Song, *Degeneration of Kähler–Einstein manifolds of negative scalar curvature*, [arXiv:1706.01518v1](https://arxiv.org/pdf/1706.01518)。Definition 2.3（PDF8頁）のstable family条件、Lemmas 4.4–4.5（PDF22–23頁）の固定compact評価と一意な極限、Lemma 3.7（PDF15–16頁）の成長条件付き一意性を確認した。固定rのsource-inclusive shellは中央成分のsmooth locusへ入るので適用できる。任意速度のmoving領域の一様収束を引用したものではない。
- F. Rochon and Z. Zhang, *Asymptotics of complete Kähler metrics of finite volume on quasiprojective manifolds*, [arXiv:1106.0873v2](https://arxiv.org/pdf/1106.0873)。§5 (5.5)–(5.6)（PDF38–39頁）とTheorem 5.1（PDF39頁）のSNC potential remainderを確認した。固定end移送の入力整理では、§2のextension map (2.44)–(2.46)（PDF17–18頁）も照合し、深いcornerから離れた固定compact上でのradial微分のO(s^−2)+O(|q|)を確認した。固定residual compactのradial微分からperiod 1の係数4πを得る。Sourceの零点はcomponent上の新しいboundary divisorではない。Smooth-divisor限定のfull expansionを入力にしていない。
- O. Savin, *Small Perturbation Solutions for Elliptic Equations*, CPDE 32 (2007), 557–578, DOI 10.1080/03605300500394405, Theorem 1.3、pp.558–560のH1/H2/H4。https://www.math.columbia.edu/~savin/Small_pert.pdf 。ゼロ次項依存を許し、全域の退化楕円性とHessian原点近傍の一様楕円性で足りる。正のcone外でdetを0に延長した F(M,u,x)=det_+(H(x)+P(M))/det H(x)−e^u に適用する。
- Y. Wang, *A Liouville Theorem for the Complex Monge–Ampère Equation*, arXiv:1303.2403、Lemmas 2.1/2.4。https://arxiv.org/pdf/1303.2403 。Complex Hessianの実Hessianへの埋込みとcone外延長を参照。主適用はSavin原典を用いる。
- J. Cheng and Y. Xu, *Interior W^{2,p} estimate for small perturbations to the complex Monge–Ampère equation*, Calc. Var. PDE 62 (2023), 231, DOI 10.1007/s00526-023-02571-x、Lemma 2.1/Theorem 1.4。https://arxiv.org/pdf/2301.00940 。関連するsmall-perturbation regularityであり、今回の証明ではSavinを直接使う。
- E. Di Nezza, V. Guedj, H. Guenancia, *Corrigendum to “Families of singular Kähler–Einstein metrics”*, JEMS 28 (2026), no.11, 5107–5111, DOI 10.4171/JEMS/1801。https://ems.press/content/serial-article-files/54000?nt=1 。元のProposition D/Theorem E（Prop.5.9/Thm.5.11）のpotential下界を訂正。訂正版Theorem 4はX0 irreducibleを仮定し、我々の可約中心fiberへ直接は適用しない。

- S.-T. Yau, *A general Schwarz lemma for Kähler manifolds*, Amer. J. Math. 100 (1978), 197–203, Theorem 2, DOI 10.2307/2373880。https://archive.ymsc.tsinghua.edu.cn/pacm_download/59/11034-Shing-Tung_Yau_30.pdf 。Complete modelから半平面へのSchwarz評価に用いる。Rank oneでの係数1は本文の局所Bochner計算でも確認した。 今回は一次PDFの§1 (10)–(16)（p.199）とTheorem 2（p.201）を実読し、正則射影に対する局所化の入力を確認した。Buffer半径依存は主稿 `coarse:lem:localized-chern-lu` に直接証明する。Roydenの既存引用全体の再監査はしていない。
- Gontard, arXiv:1807.02002v2。https://arxiv.org/abs/1807.02002v2 。一次PDFの冒頭とTheorems 1–2を確認した。Finite-type convex tube / Thullen domainの境界におけるcurvature pinchingを扱い、polyhedral simplexのLevi-flat facetsとcornersへの直接の適用結果ではない。本研究の新結果はこの文献に依存せず、定量的な優先権比較は未確認。
- Fox, arXiv:1206.3176, DOI 10.1007/s10231-013-0362-6。https://arxiv.org/abs/1206.3176 。一次metadataとabstractのみ確認し、本文は未取得。具体的な定理・仮定との比較は未了であり、本研究の証明の入力に使わない。優先権について結論しない。

## Cubical modelと有限計算

\(\mathcal C_5=\{w\in[0,1]^5:\max_iw_i=1,\ |\operatorname{supp}w|\le3\}\)。
25 vertices、50 edges、30 squares、Euler characteristic 5、\(H_2=\mathbb Z^4\)。標準cubical metricのdiameter \(\sqrt{13}\) はPart Vに有限gallery証明があり、対応するexact gallery scriptも再実行した。下限・等号分類と解析全体を機械検証したことは意味しない。

## 任意次数の候補複体とLagrangian基底

固定次数 \(d\ge5\) について
\[
\mathcal C_d=\{w\in[0,1]^d:\max_i w_i=1,\ |\operatorname{supp}w|\le3\}
\]
は \(w\mapsto w/(\sum_iw_i)\) で \(\operatorname{Sk}_2\Delta^{d-1}\) に同相であり、逆は \(x\mapsto x/\max_i x_i\)。セル数は
\[
(f_0,f_1,f_2)=\left(\binom d1+\binom d2+\binom d3,\ d\binom d2,\ d\binom{d-1}{2}\right),
\quad \widetilde H_2(\mathcal C_d;\mathbb Z)=\mathbb Z^{\binom{d-1}{3}}.
\]
一般次数の証明は `papers/cubical-gh-limit.tex` の `prop:degree-d-cubical-topology` に統合した。Lagrangian研究の \(B_d(T)\) からは、分岐木を収縮するcell-like homotopy equivalence \(B_d(T)\to\mathcal C_d\) が得られるが、\(d\ge6\) で同相ではない。これは構成の**位相的比較**であり、KE距離、action atlas、special Lagrangianを同一視しない。有限次数 \(d=5,6,7,8\) の境界行列の独立検算（有理数体の階数および有限体の階数）は関連研究 `surface-lagrangian-torus-fibration/verification/verify_ke_base_topology.py` と対応する。

**六次の標準Petersen同時実現。** 曲面改訂44の `ke:petersen-full-moment` と `ke:sextic-simultaneous-realization` は、六つの標準Petersen系の一つ、等重みw_i,j=2/5、各二重線のsource配分(1,1,1,1;2)を固定し、初期source葉を構成中に選ぶ範囲で、同じactual射影に作用atlas・全域GH実現・確率体積極限を与える。内部二端cutの累積位置はbalanced separatorとthin blockで調整し、正marginの後に中央parameterをfreezeしてからfull source annuliを固定する。Core domain・primitiveは先に固定し、anchor葉は全moment構成後に選ぶ。現在の同期では定理の仮定・結論、全開接着・相対GHへの接続を実読し、曲面側の指定独立点検の記録を確認した。全六次証明の新たな包括監査ではない。任意の非等重み、先指定された大きいsource近傍、t方向に滑らかなfibration族、atlasのparameter極限とHessian性は含まない。

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

保存された16本の旧原稿由来の検算と統合稿の5本は、2026-11-20に再実行され、元入力のSHA-256も照合されている。現在も有効な再現資産を保持するが、現行の研究資料v1.27では再実行していない。出典・ハッシュは `source-manifest.json`、実行状態は `validation.json` に記す。

保持する局所解析には、独立した局所安定性定理、全平面への適用、公表入口の四入力表と大域volume入力の証明がある。Capped positivityからpair/triple比較、六つの局所型のdeterminant、compact最小値原理、固定次数系までをPart IV v1.11の改訂時に実読した。追加したChern恒等式、曲率とframe errorの吸収予算、pair/tripleの定数、sourceのcapとresidue、有限coverから定数を選ぶ順序、大域potentialの範囲は別の読み手も独立に確認した。この第二点検が既存の全capped証明や全原著を再監査したことは意味しない。局所安定性核の既存内部点検も保持する。Part IV v1.12の固定end移送とframe windingについては、式・符号・半径差・固定段階の量化を作成担当と統合担当が点検した。曲面・固定補空間の既存理論はその正本へ参照を保ち、全てを再検証したとはしない。全原稿・全外部入力の包括的監査、新規性の網羅的確認、外部査読、形式証明は未了である。

Part IV v1.14は124頁に組版し、未定義参照・引用、重複label、欠字、LaTeX error、overfull/underfullの六分類は全て0。1・7–8・49–53・123頁の9頁を150dpiで実表示し、表題、Introduction、simplex模型の全証明とCheng–Yau書誌に欠字・重なり・切断・数式のはみ出しを認めない。全124頁の逐頁表示ではない。内容不変のPart V v1.10は既存37頁・指定5頁表示の記録を保持し、今回は再組版・再表示していない。有限計算証明書も今回再実行していない。各source/PDF hashと実行環境はvalidation.jsonに記す。

研究資料v1.27は、曲面改訂44の等重みPetersen同時実現と測度系の適用範囲を同期する。確認した保存commitは曲面 `d39270ec79ad973551f67c740682dbb06bac48e5`、固定側 `2926300c2425c7e68550ac08ee81a2afa639a0c6`（Part I v1.10・総説v1.14・資料v1.19）である。曲面側の既存の組版・表示記録と、本repoで今回行った確認を区別する。IV/Vの既存の科学引用pin（曲面改訂37・`32c67aefe6beb47c2955923e2b6eb2471d48af31`）は維持し、新しい六次の証明は曲面側を正本とする。保存・hub更新は別に確認する。

実行環境にはLuaTeX-ja、Harano Aji、CM/AMS/RSFSのvector font mapを含むuser-local TeX設定を用いた。通常のLuaLaTeX/latexmk・SyncTeXのrepo設定は保持し、PDFとcacheはGit追跡しない。現行source/PDFのSHA-256、頁と実行範囲は検証JSONに集約する。GitHubへの反映とhub更新は組版から独立に確認する。

## 人工基底計量とactual退化計量の比較

$p_T:B_d(T)\to\mathcal C_d$ の人工PL長さ計量 $|v|_\varepsilon^2=|dp_T(v)|_\square^2+\varepsilon^2|v|_h^2$ によるgraph correspondenceのdistortionは、$d=5$ で $\Theta(\varepsilon^2)$、$d\ge6$ で $\Theta(\varepsilon)$ と鋭い（関連Lagrangian研究の topo:metric-collapse-sharp）。従ってGH収束には各々対応する上界がある。これは人工的な基底計量についての結果であり、actual KE退化やaction-affine metricの収束の証明ではない。

実際の長さ計量へ適用するための三入力（topo:finite-portal-criterion）は、(N) no-shortcut、(S) square path lifts、(F) fiber/portal connector diameterの消失であり、有限square数 $N_d=d\binom{d-1}{2}$ による距離誤差上界が得られる。(N),(S)だけでは(F)は導けない。二つのunit squareを頂点で貼った折り畳み模型は(N),(S)を厳密に満たすのにGH距離が$\sqrt2/2$以上となる反例。Part IV–Vの$(CP)_d+(PBE)_d$へ接続する際は、no-shortcutの定量化とglobal portal費用を区別して検証する。一般的新規性は未確認。
