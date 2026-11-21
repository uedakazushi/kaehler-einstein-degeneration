# 研究ノート：一般型超曲面のKE退化

更新：2026-11-22 / v1.11（Part IV–V本文はv1.9）

## 共同編集の正本と共有局所入力

`multiscale-kaehler-einstein` は固定配置補空間のPart I–III、本repoは退化族局所解析のPart IVと条件付き距離論のPart V、`surface-lagrangian-torus-fibration` はactual KE Lagrangian構成と同じ射影の全曲面GH実現を所有する。三研究の方針・Introduction・証明依存を共同で点検するが、証明全文を相互に複製しない。共有する結果を変更したら、利用側の定理ラベルと仮定も照合し、各repoの保存後にhubへ反映する。

2026-11-22に照合した外部正本は、[固定配置Part I](https://github.com/uedakazushi/multiscale-kaehler-einstein/blob/de1bd02daf78105c60ae9e9f4b1dac2d8e3c88e6/papers/multiscale-kaehler-einstein.tex) v1.3の統合ソースと、[曲面稿・改訂33](https://github.com/uedakazushi/surface-lagrangian-torus-fibration/tree/68c7e3751e2de8f44c9ade062461fe150f21265c)。Part Iの確認commitは `de1bd02daf78105c60ae9e9f4b1dac2d8e3c88e6`で、main保存後のbranch/tree読戻しの一致も共同確認した。以下の利用条件の照合と指定証明鎖の内部点検を、外部全文の包括的再検証と区別する。

| 本repoの共有入力 | 仮定・量化と証明の所在 | 曲面稿での利用と適用限界 |
| --- | --- | --- |
| `coarse:cor:degree-d-volume-lower` | `ass:Gd`、固定d・固定族。主稿のweighted cap・六型minor・adjunction residueから全X_tでω_t²≥c_dΩ_low。Source軸でも正cap方向を保持する。 | K1のPoisson/Schwarz bufferとsource volume、full tripleの固定face入力。Density単独からtensor比較は結論しない。 |
| `coarse:thm:full-triple-tensor` | `full_triple_comparison.tex`。m₁≤m<L_t/3、全深度比・全phaseでC^q誤差O(1/m)。固定m₀のface下界→内外simplex→small Ricci potentialの順。 | `ke:actual-closed-corner` と有限cut版、二active co-Gram。保護領域を出る全曲面の下距離は曲面側のscalar評価を要する。 |
| `simplex:lem:rank-one-schwarz`、`simplex:cor:active-cogram` | `simplex_boundary_geometry.tex`。Complete simplex模型で係数1、actual tripleではO(1/min ell)を加える。 | Triple上のscalar下界。Source-inclusiveな一active領域のsharp normal評価と混同しない。 |
| `pair:prop:bundle-conic`、`pair:cor:global-primitive` | `source_free_neck_coordinates.tex`。Source・tripleを除く固定K上。射影を先に固定したexact uv=t、Ω=dlog v∧τと単一λを保持。 | Canonical normal action・momentの共通化。独立に指定した第二actionやorbit partitionは供給しない。 |
| `pair:thm:fixed-end-moment`、`pair:cor:actual-common-moment` | 同節。固定K→小さい固定r→全小複素t。Period 1で±4π/s_r+O_K(s_r^(−1−δ))+o_(t;r,K)(1)。Songの固定gaugeとRZのSNC Theorem 5.1を使う。 | K1–K2の固定段階のend符号。新補題 `pair:lem:diagonal-fixed-end` で選んだ遅いexhaustionへ移せるが、任意速度の一様性やbufferは与えない。 |
| `coarse:lem:pair-arm-density`、`coarse:lem:complete-volume-upper` | Oriented annulus–disc。Complete上比較はlog-volume ratioの上有界性が必要。Finite quotientの境界発散でその仮定を確認する。 | Source全moment退出の前段volume入力。Source軸を含むarm tensor比較は曲面稿 `ke:source-arm-uniform-tensor` の別証明。 |

**重点点検の結論。** Capped densityについて、Hermitian frame errorを正backgroundへ吸収してから正のminorを取る順序、sourceで元のplane座標を保持すること、residueのt依存scalarを固定することを再読した。Full tripleについて固定face・compact phase quotient・内外barrierの大小関係と、small log-volume自体がRicci potentialとなることを照合した。Fixed-endについて、固定componentがP²からd−1本の直線を除いたもの、log canonical classがO(d−4)、period 1の係数が4πであること、Kとrをtより先に固定する量化を照合した。一次文献の全証明や全高階正則性の再監査を今回完了したとはしない。

**固定段階からの新しい接続補題。** `pair:lem:diagonal-fixed-end` は、K_jを固定してr_jを選び、有限個の既証誤差E_j(t)→0とt閾値前の有限費用B_jを確定した後、j(t)→∞を十分遅く選べばE_j(t)≤ε_jかつB_j/R_t≤ε_jとend符号を同時に保てることを証明する。共通moment intervalは±π/s_jで段階ごとに縮んでよい。固定段階のbuffer・matchingの存在や、費用のj依存成長率を証明する補題ではない。原稿に証明を置き、ここでは量化だけを記す。

**二つの大域経路。** Part Vの全曲面適用はCP/PBE付きで、quinticのCP検証はTC5に依存する。曲面稿 `ke:global-metric-realization` には同じf_t=p_Tπ_tの直接scalar/portal証明があり、neck/core/sourceの接続もそこで別に扱う。したがって全曲面のGH問題自体を本稿の局所入力だけから「未解決」と記さず、CP/PBE/TCという追加packageの未検証部分を明記する。Part Vの特定のΦ_tとf_tとの一様近接性を新たに示したことにもならない。Part IIのsecondary complex periodsと第二symplectic action、Part IIIのH_loc/H_ancもそれぞれ別の入力である。

**固定補空間のexact collar入力。** Part Iの `lem:SNC-compatible-collars` は同一Hermitian depthsを保つ実有向collarsと段階的商を構成し、`lem:fc-collar-transfer` はRZの局所正則射影による延長とそのexact pullbackの全残余一様な比較を与える。`lem:RZ-collar-tensor` がRZ Theorem 5.1を選んだcollarの一面tensor評価へ移す。一般のlog-smooth collarだけでは不十分な障害は `rem:log-collar-obstruction`。証明の正本は上記Part Iであり、指定collar構成と延長比較を独立内部点検した。これらは固定SNC空間の結果で、退化parameterに一様なbuffer、任意速度で指定した退化族のmoving比較、CP/PBE/TCの証明を与えるものではない。

**固定補空間の全射収縮と閉球近似。** Part I v1.3の `prop:cogram`、`lem:lambda-choice`、`thm:contract`、`thm:rough` は、clean finite-depth構造とmetric-IRFAの下で、properな1-Lipschitz全射 $S:X\to\mathcal C$ と $d_{\mathcal C}(Sp,Sq)\le d_g(p,q)\le d_{\mathcal C}(Sp,Sq)+K$ を与える。`cor:based-ball-approximation` は、固定したSについて全中心o・全半径A・全R>0で、ambient距離を制限した閉球 $\overline B_{(X,R^{-1}d_g)}(o,A)$ と $\overline B_{\mathcal C}(S(o)/R,A)$ の間に基点対を含む歪み3K/R以下の対応を構成する。通常のGH距離は3K/(2R)以下である。`cor:GH` と `thm:moving` はその帰結で、指定compact集合を零へ送る選択ではKがその集合に依存してよい。今回の独立内部点検は、十分深い共通collar、全逆計量と残余covector norm、可積分収縮、局所一セル化、全射性、fiberのambient直径と閉球対応を対象とした。固定空間内では任意のmoving centerに一様だが、退化族に一様なKや中間尺度の有効な速度を与えない。

**LDPとexact tailの共同監査。** Part Iの `thm:LDP` はmetric-IRFAとvolume-IRFAを仮定する。`lem:deep-sector-partition` の深いnormal directionsによる可測分割、`lem:cellwise-LDP` のcompact上界・ambient-open下界、`lem:exp-tight` の一面評価によるexponential tightnessを用い、LDP本体に追加仮定を置かない。下界は正の質量を持つ固定residual compactを使い、exact-support sectorへの制限だけで全ての下位faceの正の質量を要求しない。`lem:level`、`lem:calibration`、`lem:vertex-tightness`、`thm:tail` の指定鎖では、level crossing、固定residual compactでの距離校正、残余無限遠のtightnessとactual metric-ball tailへの移行を直接監査した。Exact-tail係数にはexponential volume-IRFAを用いる。これらは三研究の共同監査として記録し、今回co-Gramから閉球近似を再読した読み手が測度節全体も独立再検証したとはしない。証明・修復の詳細と確認状態の正本はPart Iおよび同repoの研究ノートである。

**固定補空間との尺度接続と基点の範囲。** 曲面改訂33の `topo:component-cone-germ` は、cubical targetの成分頂点e_iの小球を$C_{2,d-1}$の小球と等長同定する。`ke:intermediate-component-cone` は同じP0のdistortion $\epsilon_t\to0$ と、非空領域 $A_t$ のtarget変位 $\eta_t=\sup_{y\in A_t}d_\square(f_t(y),e_i)\to0$ に対し、$a_t\to\infty$、$a_t/R_t\to0$、$R_t(\epsilon_t+\eta_t)/a_t\to0$ なら、任意の $y_t\in A_t$ を基点として $(X_t,a_t^{-1}d_{g_t},y_t)\to(C_{2,d-1},0)$ となることを示す。固定半径の球の近似誤差は基点の選択に一様で、$a_t=R_t\sqrt{\epsilon_t+\eta_t+R_t^{-1}}$ と選べる。$A_t=f_t^{-1}(e_i)$ は $\eta_t=0$ の場合である。

同じP0の共通anchorで選んだ一成分のcoreと変更collarには、`ke:global-base-parameterization` から $\eta_t\le Cq_t$、$q_t=(1+\log(N_{j(t)}+1))/R_t\to0$ が成り立つ。従って $a_t=R_t\sqrt{\epsilon_t+q_t}$ はその全領域の任意基点に使える。距離は全曲面ambient距離であり、core内在距離やLiouville軌道長の評価を要求しない。これはPart Iの固定成分の漸近錐との接点だが、Part Iの証明を退化族へ直接適用せず、任意の中間尺度・極限交換・tensor収束・有効な収束速度を結論しない。証明は曲面稿 `ke_global_metric_realization.tex` に置き、本repoには利用条件だけを記す。

**K2/K3の限定した接続監査。** 曲面改訂33の [研究ノート](https://github.com/uedakazushi/surface-lagrangian-torus-fibration/blob/68c7e3751e2de8f44c9ade062461fe150f21265c/research/notes.md) と [依存表](https://github.com/uedakazushi/surface-lagrangian-torus-fibration/blob/68c7e3751e2de8f44c9ade062461fe150f21265c/research/ke-dependencies.md) を正本とする。K2は `ke:quantitative-order-hamiltonian` と `ke:neck-corner-saturated-union` のcutoff・逆flow・moment・同じ全torusの順序、K3は `ke:closed-component-link`、`ke:star-cover-adapted-primitive`、`ke:saddle-moving-relative-interpolation`、`ke:link-relative-collar-gluing`、`ke:actual-global-fibration` の支持と選択順序を独立内部点検した。全K2交わりを含む恒等collar、補間後partitionに対するwhole-fiber trim、固定compactを保持した全域被覆を確認し、対象内で訂正を要するギャップは見つからなかった。任意に指定したcore germの延長や任意の第二actionの一致を仮定した議論ではない。全上流入力・全文献の再検証やCP/PBE/TCの検証とは区別する。

## Source-free neck：正則作用とactual metricの接続

現在の証明の正本は主稿の `source_free_neck_coordinates.tex` と `source_free_neck_comparison.tex`。固定次数d≥5、sourceとtriple pointsを避ける固定compact base Kに限る。前者の `pair:prop:bundle-conic` がexplicit normal form、`pair:cor:global-primitive` が単一primitive、`pair:thm:fixed-end-moment` / `pair:cor:actual-common-moment` が円平均η_tの共通moment stripを与える。

**座標の障害と修復。** 局所conic overlapをcomplete C*の自己同型と分類してはならない。例えば(u,v)↦(ue^u,ve^(−u))は原点近くで正則可逆、uvとlabelled axesを保つが、base-only乗数ではない。この例はnormal formの不存在を示さない。射影P(V)からD=P(W)へのprojectionを先に固定すると、P(V)＼P(U)=Tot(O_D(1)⊕O_D(1))でtransitionは初めからbase-onlyである。h=−F_d/G、h0=h|Dを用いるx_i'=x_i h0/h、x_j'=x_jがexact方程式へ移す。旧 `sharp:prop:conic-normal-form` の証明をこの構成へ置き換えた。

**Momentの規約。** d^c=(i/2)(bar∂−∂)、circleのperiodは1、ι_Vη=−dμとする。Ω=dlogv∧τに対するλ=d^c log(ω²/|Ω|²)を固定するとμ=(Aλ)(V)。τ'=bτの場合のλの差はbaseからの閉形式−d^c log|b|²であり、normal momentは不変だがresidual action periodsのためには選択を固定する。各conic fibreでdμ(−JV)=η(V,JV)>0。

**固定endとmoving end。** s_r=−log r²についてμの両end値は±4π/s_r+O(s_r^(−1−δ))+o_{t→0;r,K}(1)。まずrを固定し、その後tを小さくする。Song (arXiv:1706.01518, Definition 2.3, Lemmas 4.4–4.5)の固定gauge収束とRochon–Zhang (arXiv:1106.0873, (5.5)–(5.6), Theorem 5.1)のSNC potential remainderを使う。Period 2πのgeneratorなら主項は±2/s_rとなるので規約を混ぜない。Smooth-divisor full expansionをSNCへ無断で適用していない。共通intervalからradial derivativeの一様下界や全neckのMoser生存は従わない。

**平均の順序とperiods。** 関連Lagrangian主稿 `ke:staged-neck-averaging` ではη=A1ω、κ=A2η、φ*ω=η、ψ*η=κとし、Θ=φψを使う。第二flowはnormal S¹にequivariantで、Θ*λ=A2A1λ+dq、μ∘ψ=A2μが厳密に成り立つ。原primitiveと整数cycleを共通に固定すれば全periodを追跡できる。同じnormal actionだけでは、独立に指定したneckの第二periodやreduced leavesの一致は得られない。共通bufferの下で一段階bundleとのHamiltonian比較があり、指定subgroupのactual closed cornerにも従来と同じGH率がある。

**解析の残り。** `neck:prop:volume-envelope` は固定residual compact上でc h²≤ω²≤h²のみを与える。拡幅annulus×D₂と同じannulus×D₃のcomplete product metricsの制限は、全人工境界を越えて滑らかで、normal depthが発散しても中心volume比9/4を保つ（`neck:prop:residual-boundary-obstruction`）。これはactual compact familyの反例ではなく、local residual boundary情報の不足を示す。Zhang (arXiv:1505.04728v2, Lemma 3.3, (3.10)–(3.12))の正次元stratumの極限もpotential φ₀(x,z)とmixed termsを残す。

固定baseの補題からactual circle長へ進むための解析入力は `neck:lem:rank-one-circle` のp*h_D≤Aωである。曲面稿の `ke:fixed-base-neck-moser` は必要な固定段階bufferを別に証明する。Volume上界と合わせれば、Hermitian matrix G=[[a,c],[c̄,b]]に対しdetG≥a/A、従ってa≤ABとなり、mixed coefficientsがあってもnormal circle長を抑えられる。Actual metric ball bufferがあればlocalized Chern–Luでこのrank-one下界を得るが、そのbufferを欲しいtensor比較から逆算しない。Full tensor比較にはsmall log-densityと一様smooth背景、あるいは別の解析が必要。Complete strip×curveへのglobal延長・完備性・bounded log-ratioを仮定すればOmori–Yauによる一意性でproductを同定できるが、fixed residual discの極限だけではこれらの条件を満たさない。

## 全深部三重点の比較と大域density入力

正確な三重点座標ζ0ζ1ζ2=t、ell_i=−log|ζ_i|²、L=−log|t|²、R=log Lを用いる。固定次数d≥5の一般位置全平面退化について、min ell_i≥mで
\[
 \left|\log(\omega_t^2/k_L^2)\right|\le C/m,\qquad
 \|g_t-g_L^{\mathrm{sf}}\|_{C^q(g_L^{\mathrm{sf}})}\le C_q/m
\]
を証明した。全深度比・全位相・固定族の全三重点に一様であり、定数は固定した次数と族に依存してよい。正本は主稿 `coarse:thm:full-triple-tensor`。次数一様性、sourceのtensor比較、大域GHはこの定理の主張に含まれない。

固定toric模型k_Lの存在・一意性・完備性にはZhang (2015), 第2.1節、Theorem 2.1 / Proposition 2.2を用いる。退化族のTheorem 2.4やQ-factorial仮定は使わない。ψ_L=log L−Σlog ell_iと内外translated-simplex barriersによりψ_L−(log3)/2≤φ_L≤ψ_L、V_L/3≤k_L²≤V_Lを得る。半平面へのSchwarz評価とdeterminant上界からtensor二側比較を先に確保し、内部正則性で全高階を制御する。Log-densityの凸性から固定量のfacet shiftによる誤差O(1/min ell)を得て、actual volumeを内外の模型で挟み、小さいpotentialへSavinを適用する。証明の所在は `coarse:lem:simplex-model` / `coarse:lem:simplex-shift` / `coarse:lem:small-volume-tensor`。

Actual側の大域入力 `coarse:cor:degree-d-volume-lower` は、adjunction residueによるcanonical densityの規格化、backgroundによるHermitian frame errorの吸収、各正のcap方向のminorから得る六型のdeterminant下界である。固定dについてh0=(d−4)FS、A0をdに対し十分大きく取り、active supportは高々三つ、inactive capsは有界となる。Sourceでは元のplane coordinatesを保つexact xy=tzとrescalingを用い、二つのcap係数≥c_d/Lを確保する。Compact minimum原理からactual volume下界へ進む。この入力は全固定次数について点検済みであり、三重点のtensor比較に(TC)/(PBE)やactual metric bufferを仮定しない。

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

- O. Savin, *Small Perturbation Solutions for Elliptic Equations*, CPDE 32 (2007), 557–578, DOI 10.1080/03605300500394405, Theorem 1.3、pp.558–560のH1/H2/H4。https://www.math.columbia.edu/~savin/Small_pert.pdf 。ゼロ次項依存を許し、全域の退化楕円性とHessian原点近傍の一様楕円性で足りる。正のcone外でdetを0に延長した F(M,u,x)=det_+(H(x)+P(M))/det H(x)−e^u に適用する。
- Y. Wang, *A Liouville Theorem for the Complex Monge–Ampère Equation*, arXiv:1303.2403、Lemmas 2.1/2.4。https://arxiv.org/pdf/1303.2403 。Complex Hessianの実Hessianへの埋込みとcone外延長を参照。主適用はSavin原典を用いる。
- J. Cheng and Y. Xu, *Interior W^{2,p} estimate for small perturbations to the complex Monge–Ampère equation*, Calc. Var. PDE 62 (2023), 231, DOI 10.1007/s00526-023-02571-x、Lemma 2.1/Theorem 1.4。https://arxiv.org/pdf/2301.00940 。関連するsmall-perturbation regularityであり、今回の証明ではSavinを直接使う。
- E. Di Nezza, V. Guedj, H. Guenancia, *Corrigendum to “Families of singular Kähler–Einstein metrics”*, JEMS 28 (2026), no.11, 5107–5111, DOI 10.4171/JEMS/1801。https://ems.press/content/serial-article-files/54000?nt=1 。元のProposition D/Theorem E（Prop.5.9/Thm.5.11）のpotential下界を訂正。訂正版Theorem 4はX0 irreducibleを仮定し、我々の可約中心fiberへ直接は適用しない。

- S.-T. Yau, *A general Schwarz lemma for Kähler manifolds*, Amer. J. Math. 100 (1978), 197–203, Theorem 2, DOI 10.2307/2373880。https://archive.ymsc.tsinghua.edu.cn/pacm_download/59/11034-Shing-Tung_Yau_30.pdf 。Complete modelから半平面へのSchwarz評価に用いる。Rank oneでの係数1は本文の局所Bochner計算でも確認した。
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

保存された16本の旧原稿由来の検算と統合稿の5本は、2026-11-20に再実行され、元入力のSHA-256も照合されている。現在も有効な再現資産を保持するが、v1.9で再実行していない。出典・ハッシュは `source-manifest.json`、実行状態は `validation.json` に記す。

本repoの数学的点検は冒頭の共有局所入力表の量化・規格化と、`pair:lem:diagonal-fixed-end` の証明を対象とし、同補題は別の読み手も独立内部点検した。管理文書v1.11ではPart I v1.3の全射収縮・閉球近似とLDP・exact tailの共同監査を同期し、既存のcollar/延長比較と曲面改訂33の基点拡張・指定K2/K3鎖の確認状態を保持する。今回独立に再読した指定鎖はco-Gram→収縮写像→閉球近似である。Part IV–Vの本文は変更しておらず、この同期に伴う組版・有限検算の再実行はしていない。既存の全高階解析証明・一次文献全体の再監査、新規性の包括的確認、外部査読、形式証明とは区別する。

2026-11-22にv1.9のPart IVを117頁、Part Vを37頁へ `latexmk` で組版し、PDFとSyncTeXをbuildに生成した。最終logの未解決参照・引用、重複ラベル、欠字、overfull/underfull boxは0。日本語フォントの代替・featureとbookmark数式に関する警告は残る。IVの1、6–7、70–71、117頁、Vの2、4–5、37頁を画像化して、本文・数式・新補題・文献の欠落、重なり、はみ出しがないことを確認した。全頁の画像点検ではない。初期環境のformat/font map不足は利用可能なTeX Live環境で補い、主稿の設定は保持した。GitHubへの反映とhub更新は組版から独立に確認する。

## 人工基底計量とactual退化計量の比較

$p_T:B_d(T)\to\mathcal C_d$ の人工PL長さ計量 $|v|_\varepsilon^2=|dp_T(v)|_\square^2+\varepsilon^2|v|_h^2$ によるgraph correspondenceのdistortionは、$d=5$ で $\Theta(\varepsilon^2)$、$d\ge6$ で $\Theta(\varepsilon)$ と鋭い（関連Lagrangian研究の topo:metric-collapse-sharp）。従ってGH収束には各々対応する上界がある。これは人工的な基底計量についての結果であり、actual KE退化やaction-affine metricの収束の証明ではない。

実際の長さ計量へ適用するための三入力（topo:finite-portal-criterion）は、(N) no-shortcut、(S) square path lifts、(F) fiber/portal connector diameterの消失であり、有限square数 $N_d=d\binom{d-1}{2}$ による距離誤差上界が得られる。(N),(S)だけでは(F)は導けない。二つのunit squareを頂点で貼った折り畳み模型は(N),(S)を厳密に満たすのにGH距離が$\sqrt2/2$以上となる反例。Part IV–Vの$(CP)_d+(PBE)_d$へ接続する際は、no-shortcutの定量化とglobal portal費用を区別して検証する。一般的新規性は未確認。
