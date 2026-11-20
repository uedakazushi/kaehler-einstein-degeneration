# 現行研究方針：一般型超曲面の負Kähler–Einstein退化

更新：2026-11-20 / v1.7・現行研究方針

## 研究固有の目標

固定次数d≥5の一般型曲面の全平面退化について、径の尺度のactual KE極限をcubical複体と同定し、Lagrangian torus fibrationのfiber収縮として実現することを目指す。全深部三重点の解析比較と全閉cornerの局所GH収縮は証明済みであり、Source-freeな固定compact baseで正則normal action、canonical primitive、円平均後の共通moment intervalを得た。次の核心はneck全体のMoser flow bufferと複数のtriple endsの同時整合、sourceでの解析、全曲面のshortcut制御である。高次元の超平面退化は、mixed source–higher-stratum modelsの解析を含む後続課題とする。

## 論文と証明の状態

- `papers/kaehler-einstein-degeneration.tex`：Part IV、66頁（回収時）。局所模型、source packing、固定次数d≥5の代数・残差packageに、全深部三重点のactual tensor比較、simplex境界の積漸近、全閉cornerのGH定理を統合。Sourceを含むquintic exteriorのcoarse metric geometryは独立な(TC)_5付き。全域のsharp co-Gramは粗い比較に加えて(PBE)_d付きであり、証明済みの三重点内のactive co-Gramと区別する。Bounded-densityからtensor比較を導く一般的推論は反例により排除した。
- `papers/cubical-gh-limit.tex`：Part V、34頁（回収時）。Abstract pruning–transportとdiam(C_5)=sqrt(13)は解析仮定と独立。全曲面のactual degree-d GH適用は(CP)_d+(PBE)_d付きであり、無条件の大域actual GH収束は未証明。
- 高次元ではmixed source–higher-stratum modelsの解析が残るためGH極限は予想。
- Fixed arrangement complement側Part I–IIIの正本は[multiscale-kaehler-einstein](https://github.com/uedakazushi/multiscale-kaehler-einstein)。固定空間の結果から族の一様性を自動的に導かない。

## 全深部三重点の actual semi-flat 比較

任意の固定次数 d≥5 の一般位置全平面退化で、三重点の全深度比・全角度に一様な actual KE 比較を証明した。正確な座標 ζ0ζ1ζ2=t、ell_i=−log|ζ_i|²、L=−log|t|²、R=log L とし、k_Lをlogarithmic simplex上のcomplete toric KE form、その実計量をg_L^sfとする。十分大きい固定m1と各qのCqについて、m≥m1、min ell_i≥mで
\[
\left|\log\frac{\omega_t^2}{k_L^2}\right|\le C/m,\qquad
\|g_t-g_L^{sf}\|_{C^q}\le C_q/m.
\]
定数は固定dと族に依存してよい。次数一様性は主張しない。証明の正本はKE主稿 `coarse:thm:full-triple-tensor`。

固定toric模型の存在・完備性にはZhang (2015), §2.1, Theorem 2.1 / Proposition 2.2を用いる（退化族のTheorem 2.4とQ-factorial仮定は使わない）。ψ_L=log L−Σlog ell_iに対してψ_L−(log3)/2≤φ_L≤ψ_L、V_L/3≤k_L²≤V_Lを内外にずらした障壁で証明する。Complete模型から三つの半平面へのYau Schwarz lemma、determinant比較、内部正則性により一様cusp geometryを得る。凸性からfacet shiftのlog-density差をO(1/min ell)とし、actual計量を内外のsimplex KE metricsでvolume比較する。Savinの小摂動定理でtensor・全高階誤差へ移る。Actual metric bufferや(TC)/(PBE)を前提としない。

Actual側の大域入力は `coarse:cor:degree-d-volume-lower`。Adjunction residueでcanonical densityを固定し、backgroundによるHermitian frame errorの吸収と各正のcap方向のminorから六型のdeterminant下界を証明する。Sourceでは元のplane coordinatesを保つexact xy=tzとrescalingにより二つのcap係数≥c_d/Lを使う。Compact minimum原理からactual volume下界を得る。今回この依存部分も再点検して明示化した。

## 全閉cornerの距離と同じLagrangian bundleによるGH収縮

三つのlabelsからなるJについて、C_J={w∈[0,1]^J:max w_i=1}を三枚のunit squaresからなる閉cornerとし、d_JはC_J自身の内在距離とする。Softmax hexagonの全phase preimage H_{t,R}にR^−2 g_tを入れると、projectionのdistortionはO(log R/R)である。H_{t,R}内の曲線だけを用いる内在距離と、外側保護領域{min ell_i>R/2}内の全曲線を許すprotected-ambient距離の双方で成立する。正本は `simplex:thm:closed-corner-model` / `simplex:cor:actual-closed-corner-metric`。

関連Lagrangian主稿 `ke:closed-corner-gh` / `ke:closed-corner-protected-gh` は、`ke:actual-closed-corner` と同じactual Lagrangian torus bundleと同じ射影に、このO(log R/R)のGH近似を与える。全fiberの非正規化intrinsic/ambient diameterはO(1/R)、正規化後はO(1/R²)、raw cubical mapとの誤差はO(log R/R)。Squareの継目・共通頂点でもfiberはregular T²である。模型のLie derivativeを評価したMoser pullback比較を使うため、粗い比較だけからGH距離を推論していない。

距離下界は両端をclippingしたdepth写像をcomplete simplex全体で定義し、active coordinateが一つなら係数1のSchwarz評価、二つならdominant product漸近を用いて全経路を制御する。上界は高々三枚のsquaresを通るgeodesicを内部へずらし、固定位相で持ち上げる。Seam collarが狭いという事実だけに依存しない。

C_Jの距離はfull complex C_dの他のcellsを経由する距離ではなく、protected-ambient距離は全曲面X_tの距離ではない。X_t全体のshortcut、異なる三重点・neckとの接着、source・branch・coreのsingular fibersとの同定は未解決である。新規性の包括的確認と外部査読・形式証明は未実施。

## Simplex境界の鋭い積漸近とactive co-Gram

主稿 `papers/sections/simplex_boundary_geometry.tex` に次を証明する。全固定階のnormはangular universal coverの正規化された正則座標、または同値な模型covariant normで取り、全phaseに一様である。

- `simplex:lem:rank-one-schwarz`：各iについて |d log ell_i|_{g_L^sf}≤1。半平面へのrank-one Schwarz計算で正確な係数1を得る。
- `simplex:prop:dominant-product`：独立深度a,b、δ=(a+b)/L→0なら、二重cusp productに対してmodel誤差O(δ²)。Expanded quadrantとinner rectangleにより1≤k_L²/ω_prod²≤(πδ/sin πδ)^4を得て、Savinと線形化後のSchauder評価を用いる。Pure modelには深度の絶対的下限を置かない。
- `simplex:cor:actual-dominant-product`：actual誤差はO(1/min ell_i+δ²)。特に0<η<1/2、a,b∈[L^η/2,2L^(1−η)]の開正方形領域ではO(L^−η)。関連Lagrangian主稿 `ke:open-cell-collapse` は固定長方形Kη=[η,1−η]²への内在GH収束とprojection distortion O(L^−η)、fiber径O(L^−η)、raw誤差O(1/R)を与える。
- `simplex:prop:facet-product`：b=ell_0、a=ell_1、d_*=min(a,L−a)、b/d_*→0なら、cusp(b)×finite-annulus(a,width L)へのmodel誤差O((b/d_*)^(2/3))。Actual側にはO(1/b)を加える。比較rectangleの幅β=(b²d_*)^(1/3)で二つの誤差を釣り合わせる。
- `simplex:cor:active-cogram`：ell_i≤Le^−Aのactive indicesが一つまたは二つなら、d log ell_iのco-GramはId+O(e^(−A/2))。二つならO(e^−2A)へ改善し、actualにはO(1/min ell_i)を加える。

Actual chart内でexpanding product annuliとshifted-sinh下barrierを直接使う別の比較法も、`coarse:thm:moving-triple-tensor` / `coarse:cor:open-square-tensor` に保持する。いずれも有界densityだけでなく、小さいC0 potentialをSavinへ入力する。三重点内のこれらの結論には(TC)/(PBE)を仮定しない。

## 局所windowと残るtensor仮定

三つの深度が同程度のとき、一つの独立二座標product windowで任意半径のconstrained-cusp ballを覆うことはできない（`coarse:prop:triple-product-obstruction`）。最大深度を従属座標にする小さい相対箱は有効であり、全deep triple上のvolume上下界とbounded potentialは `coarse:cor:triple-volume-comparison` で証明する。このvolume比較単独ではtensor比較は得られず、上記のcomplete simplex barriersとSavinを組み合わせてfull tripleの比較を証明する。

Source gateのfixed model ballはoriented half-armを越える。Full source-coordinate extension上でdensity比較を行い、(TC)_5は**その点で有効なorientation**のmodelに対する下界として定式化する。全ての拡大窓で同じmodelのtensor比較を要求しない。任意半径のexhaustionはcoarse小窓構成の結論に含めず、dominant tripleでの証明と一般の(PBE)_dを分ける。

## 体積密度とtensor比較：現行の解析条件

主稿 `coarse:prop:density-counterexample` は、固定ball上で滑らかな負KE計量列の体積密度が正に一様有界でも、内側ballでtensorが一様有界とは限らないことを証明する。したがってvolume lower/upper estimatesだけを用いた局所tensor比較は使えない。

五次のexterior comparisonには独立な仮定 $(\mathrm{TC})_5$（`coarse:hyp:TC5`）を置く。これに依存するraw submetry、actual connectors、source diameter、粗い距離二側比較、$(\mathrm{CP})_5$ の検証も条件付きである。Raw coordinatesの代数的構成、閉セルの実現、determinant/volume評価、actual metric ballsを用いたsource inradius/escapeの議論、抽象有限距離論は、このtensor比較の推論から分離する。旧来の全証明を今回独立監査したことにはしない。

修復の具体的な十分条件は、各点にactual metric ballが入る一様bufferと、そこから負のholomorphic sectional curvatureを持つcomplete productへの正則写像である。`coarse:lem:actual-buffer-comparison` によりlocalized Chern–Luから一方向の比較を得て、volume upper boundと合わせる。Model metricでのbufferだけではactual bufferを証明したことにならず、欲しいcoarse distanceを先に使う循環を避ける。

## 位相・人工計量とactual metricの区別

候補\(\mathcal C_d\)の一般次数のセル数・\(\operatorname{Sk}_2\Delta^{d-1}\)との同相・整数ホモロジーはPart Vに証明がある。Lagrangian分岐基底\(B_d(T)\)からのcell-like写像は\(d\ge6\)では同相でないが、人工PL長さ距離によるdistortionは\(d=5\)で\(\Theta(\varepsilon^2)\)、\(d\ge6\)で\(\Theta(\varepsilon)\)であり、GH距離には各々対応する上界がある。証明の正本はLagrangian repoの`topo:metric-collapse-sharp`。
Actual計量への大域適用には(N) global no-shortcut、(S) square path lifts、(F) small fiber/portal connectorsを全域で検証する必要があり、(F)は前二条件からは従わない（同repoの`topo:portal-counterexample`）。三重点内の(N),(S)とregular fibersの径評価は上記の閉corner定理で得たが、他の領域との大域的な接続は含まれない。Part IV–Vの\((CP)_d+(PBE)_d\)は依然未証明。六次Petersen木系は6点の\(S_6\)軌道をなすが、これはrealized KE計量の対称性を決めない。

## Lagrangian fibrationとの接続

標準負KE尺度での四実次元非崩壊極限と、$R_t^{-2}g_t$ のcubical候補を区別する。Zhang (MRL, 2015)の局所torus collapse定理はQ-factorialなtoroidal全空間を仮定するため、我々のsource $xy=tz$ へ直接適用しない。主稿序論に先行比較を統合した。閉corner内では同じactual Lagrangian fibrationの射影がGH近似となることを証明した。一方、Part Vの大域GH近似を既存大域fibrationのfiber収縮と同定するには、$\sup_x d_\square(\Phi_t(x),p_T\pi_t(x))\to0$ を全X_tで検証する必要がある。関連Lagrangian主原稿の `topo:ke-map-compatibility` がその十分性を示すが、この大域適合性は未証明である。

## Source-free neckの座標・作用周期・解析条件

正本は主稿の `papers/sections/source_free_neck_coordinates.tex` と `papers/sections/source_free_neck_comparison.tex`。二重線のsourceと三重点を避ける固定compact baseに対して次を証明した。Moving baseやmoving endの一様性は別問題である。

- `pair:prop:bundle-conic`：射影的法線束の表示を先に固定し、h=−F_d/∏_{k≠i,j}L_k、h0=h|Dとしてx_i'=x_i h0/h、x_j'=x_jでexact uv=tを得る。Base、labelled axes、normal first jetを保ち、固定compact上で一様な正則逆を持つ。局所conic overlapをcomplete C*の自己同型と扱う旧証明をこの明示構成で置き換えた。
- `pair:cor:normal-circle` / `pair:prop:canonical-normal-moment`：同じ正則normal S¹と、η_t=Aω_tに対するcanonical μ_tを構成。ι_Vη_t=−dμ_t、dμ_t(−JV)=η_t(V,JV)>0。周期は1で、patchごとの加法定数はない。
- `pair:cor:global-primitive`：open base上の非消滅正則1-form τを選び、Ω=dlog v∧τ、λ_t=d^c log(ω_t²/|Ω|²)を一つの大域primitiveとする。τの変更ではnormal momentは不変だが、residual periodsのためにprimitiveの選択は保持する。
- `pair:thm:fixed-end-moment` / `pair:cor:actual-common-moment`：s_r=−log r²として両固定endのmomentは±4π/s_r+O(s_r^(−1−δ))+o_t(1)。rを小さく固定した後でt→0とする。Song, arXiv:1706.01518, Definition 2.3 / Lemmas 4.4–4.5とRochon–Zhang, arXiv:1106.0873, (5.5)–(5.6) / Theorem 5.1を用い、η_tのreductionsに共通のintervalを得る。
- `neck:prop:volume-envelope`：固定residual compact上でc h_t²≤ω_t²≤h_t²。ただし誤差はO(1)である。`neck:prop:residual-boundary-obstruction`はexact negative KE productでも固定residual境界の影響が消えないことを示す。Actual compact familyへの反例ではない。
- `neck:lem:rank-one-circle`：p*h_D≤Aωかつω²≤B(h_A+h_D)²ならnormal real vectorsについてg_ω≤AB g_A。Mixed termsを許す。Actual metric ballの一様bufferを別途仮定すればnormal circleの長さはO(1/min(s,M−s))となる。Buffer自体は未証明。
- `neck:prop:small-density-coupled`：一般のsmooth negative KE背景h_tに対しsmall log-volume errorから同率のtensor誤差を得る。積分離は要求しない。Complete strip×curve上への延長・完備性・global bounded log-ratioがあればproductを同定できるが、そのglobal仮定は未検証である。

関連Lagrangian主稿 `ke:staged-neck-averaging` は、一つのnormal circleを先に平均し、endで残る円を平均することで、同じactual normal actionと全marked action periodsを保つ。共通のdomain/image bufferの下で一段階構成や整数基底変更とHamiltonian比較できる。`ke:staged-closed-corner-gh` は指定primitive subgroupに適合するactual triple bundleにも同じGH誤差O(log R/R)を与える。旧bundleと同一のfiber分割は主張しない。固定base上のprimitiveとmoment intervalがあっても、neck全体のflow生存、tripleとの同一作用、reduced foliationの同時整合はまだ必要である。

## 次の課題

1. 最優先はsource-free neck全体のnormal Moser flowの生存と一様buffer。まず `neck:lem:rank-one-circle` に必要なresidual方向の下界を、欲しい距離比較を先取りせず証明する。指定productへの漸近を仮定せずcoupledな背景も許す。同時に射影的normal actionとtriple側の指定subgroupの実際のoverlapを比較し、複数endの作用・reduced leaves・primitive markingsを合わせる。二段階構成はこの入力があれば同じnormal circleとperiodsを保つが、非定数unitによるorbit partitionの変化は別に処理する。
2. Sourceの正しいorientationでactual tensor・connector評価を進め、source・branch・coreと既存大域fibrationへの相対接着を扱う。三重点のcusp–annulus漸近は利用できるが、sourceでの比較やsingular fibersのmetric制御を代替しない。
3. 全曲面のno-shortcutとglobal portal費用を検証する。(PBE)_dのquantitative terminal trivialization、protected rectangular inclusion、uniform comparison、two-metric escapeをactual metricsで証明し、一般次数の(CP)_dのconnectorsを監査する。C_J内の距離と、他のlabelsを通るC_dの距離を明確に分ける。

## 保存・検証

全文TeXのSHA-256は `research/source-manifest.json`、元監査は `research/source-audit.md`。回収時に3原稿のLuaLaTeX組版と、統合稿5 scripts・旧v0.12の16 scriptsの再実行を行った。検査は有限組合せ・式・bookkeepingに限られ、未完成の解析証明を代替しない。詳細は `research/migration.md`。

今回追加したexplicit bundle coordinates、canonical momentのpatchingと周期1の係数、Songのstable-family仮定、Rochon–ZhangのSNC potential remainder、rank-one determinant、residual-boundary例、complete KE uniquenessを原典および証明で点検した。二段階averageのexact primitive transport、Hamiltonian path homotopy、指定subgroupでのclosed-corner GHも関連稿で独立に再読した。現行の解析監査では、全固定次数のweighted cap determinant、source residue規格化、complete simplexの内外barriers、convex shift評価、expanding product domains、shifted-sinh barriers、Savinの原典のH1/H2/H4とTheorem 1.3を点検した。さらに正確な係数1のBochner計算、積領域の包含と内部近似によるvolume比較、dominant/facetの誤差率、active co-Gram、全閉cornerのpruningと有限gallery、modelを基準とするMoser pullbackおよびprotected-ambient GHの証明を独立に再読した。Bounded-density推論の反例とその依存先、GuanのDirichlet存在定理、Bedford–Taylorの比較・pluripolar massの一次資料も確認した。局所GH定理の原稿内の証明・今回の監査と、未完成の大域解析、新規性の未確認、未実施の形式証明を区別する。現環境では `lualatex.fmt`・LuaTeX-ja等の基本資産がなく、LuaLaTeX組版の試行は本文処理前に停止した。回収時の組版成功と現行改訂の未組版を区別する。

## 共通研究原則と保存許可（研究固有方針から独立）

数学的重要性・新規性・理解の深化・応用可能性・正確性・実現可能性を総合して方針を更新する。証明済み・仮定付き・未完成・予想・計算観察、既知結果と独自結果、草稿の証明と今回の監査を区別する。重要文献は一次資料の正確な定理と仮定を確認する。日本語LuaLaTeXで公表原稿と十分な証明を保持し、有効なアイデア・反例・計算は現行ノートに統合する。再現コード・証明書・入力を残すが旧版/中間出力は蓄積しない。区切りごと承諾なしに通常コミットで `main` へpush、15–30分を目安に切り良く保存する。force pushとGitHub Actions追加/起動はしない。Library旧資料は削除しないがGitHub移行後は定常二重保存しない。先に対象repoへ保存してからresearch-hubを更新し、数学検証・組版・GitHub・hubを別々に確認する。
