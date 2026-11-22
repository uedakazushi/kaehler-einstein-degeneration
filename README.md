# Kähler–Einstein degeneration

更新：2026-11-23 / v1.27（研究資料。Part IV v1.14、Part V v1.10）

**公表計画：** 数学的価値の最大化を基準に、曲面P0・Part IVの最小局所解析・Part Iの距離と実球体積漸近を優先する。[研究方針](00_research_plan.md)に実行順序・達成基準・担当を記した。中心定理の構成、入力の範囲、先行研究との差を確定し、五次の同時atlas/GH実現を公表範囲へ加える。六次の標準等重み同時実現も公表範囲へ加え、追加保持集合や条件付き解析拡張は独立した完成基準で進める。

最初に[現行研究方針](00_research_plan.md)、次に[研究ノート](research/notes.md)を読む。固定次数d≥5の一般型曲面の全平面退化について、actual KE計量の径の尺度の極限とLagrangian torus fibrationによる実現を研究する。正本はGitHubのmain、研究全体の入口は[research-hub](https://github.com/uedakazushi/research-hub)。

**公表準備で明確にした解析核：** `coarse:thm:boundary-to-triple` はexact triple領域、全angular phasesのcompact quotient、各固定tのsmooth radial閉包、固定faceの一様なdensity下界から、全深度比に一様なC^q誤差O(1/m)を導く。境界上界のt一様性は不要。`coarse:thm:full-triple-tensor` を全平面退化への適用として分け、証明は一度だけ置いた。Part IVの入口を無条件の局所成果中心へ改め、曲面P0への最小四入力表を設けた。固定endについては `pair:prop:fixed-end-transfer` がlog-densityの固定collar収束と成分cusp微分を切り分け、normal windingがmomentの加法定数を決めることを明示する。

**Capped-volume入力の確認：** Part IV v1.11では、正値性からweighted cap minors、pair/triple、六つの局所型、compact最小値原理、固定次数の大域下界までの指定証明鎖を実読した。結論を妨げる誤りは見つからず、零点を含むChern微分の正確なcap恒等式、曲率・frame誤差の明示的吸収条件、固定adjunction residue、有限coverから最後に小さい複素parameterを取る順序を補った。追加式と定数依存は別担当も独立点検した。全原著・全主稿の包括的検証とは区別する。

**五次の同じ射影による同時実現：** 曲面稿の `ke:quintic-simultaneous-realization` は、初期source葉・allocation・全保持近傍を構成中に選ぶ範囲で、actual負KE形式に関する一つの大域Lagrangian fibrationに作用適合matroidal atlasと全曲面ambient GH実現を同時に与える。Source-freeな旧neck補題と全source-wallを用いる構成を区別し、両端periodの有限整合、全momentの自由需要とstrict cuts、coreとの全開collarの葉・作用および平行移動を含むatlas接続を証明する。等重みと対称六系が整合データの実例を与える。Focus valuesには穿孔focus affine structureを用いる。各tでの同時実現であり、atlas自体のt方向の極限や極限距離のHessian性は含まない。六次には別に標準等重みの同時実現がある。既指定の大きいsource近傍を保つ相対存在、CP/PBE/TC・H_loc/H_ancの検証は未解決。証明の正本と限定した内部点検の範囲を研究ノート・検証JSONに記す。

**同じ射影上の確率体積測度：** 曲面改訂44の保存稿 `ke:global-volume-measure` は、同じGH近似写像とLagrangian射影による確率体積の押し出しが、各成分頂点に重み1/dを置く原子測度へ弱収束することを示す。固定成分の体積と固定compact上の収束、既存の全域値比較を使い、moving neckの体積漸近は追加しない。計量極限の辺・squareは残り、極限測度の台だけに空間を縮めない。本文と証明を確認し、数学保存版は `d39270ec79ad973551f67c740682dbb06bac48e5` である。数学保存と現行の表示確認は個別に記す。

**Actual bufferの半径と円周収縮。** `coarse:lem:localized-chern-lu` は、actual球の半径σとtargetの負曲率κに対して tr_g(F*h)≤C_n κ⁻¹(1+σ⁻²)を与える。正則写像のrank低下、潰れたinjectivity radius、targetの非完備性を許す。`neck:cor:shrinking-buffer-circle` はrank-one下界と体積上界を組み合わせ、normal深度m=min(s,M−s)に対しlength≤C(1+σ⁻¹)/mを得る。0<σ≤1ならmσ→∞が非正規化の収縮、Rmσ→∞がRで割った収縮の十分条件となる。半径は別の幾何的議論で確保する入力であり、bufferの存在、全tensor比較、Moser flow生存、CP/PBE/TCは証明しない。証明は距離cutoffの勾配・Laplacian bounds、正の最大点、mixed coefficientsを含むdeterminant比較を明記する。これは古典的なSchwarz評価の定量的帰結であり、新しいSchwarz lemmaとしての優先権は主張しない。

**六次の標準Petersen同時実現。** 曲面改訂44の `ke:petersen-full-moment` と `ke:sextic-simultaneous-realization` は、六つの標準Petersen系の一つ、等重みw_i,j=2/5、各二重線のsource配分(1,1,1,1;2)を固定し、初期source葉を構成中に選ぶ範囲で、同じactual射影に作用atlas・全域GH実現・確率体積極限を与える。内部二端cutの累積位置はbalanced separatorとthin blockで調整し、正marginの後に中央parameterをfreezeしてからfull source annuliを固定する。Core domain・primitiveは先に固定し、anchor葉は全moment構成後に選ぶ。現在の同期では定理の仮定・結論、全開接着・相対GHへの接続を実読し、曲面側の指定独立点検の記録を確認した。全六次証明の新たな包括監査ではない。任意の非等重み、先指定された大きいsource近傍、t方向に滑らかなfibration族、atlasのparameter極限とHessian性は含まない。

**Complete simplex模型の最小入力。** Part IV `coarse:lem:simplex-model` は、Zhang Theorem 2.1に明記されたCheng–Yauの標準実単体上の凸解存在・境界発散・実Hessian完備性を入力とする。一意性は内側homothety比較、tube完備性は有限長曲線の実射影、格子商の完備性は等長作用から直接証明する。w/Lはuniversal cover上の等長写像だが、4πの角度格子を4π/Lへ変える。固定周期商のinjectivity radius下界は結論しない。全深度比の正規化窓でpotentialとtensorの規格化を明示した。Zhangの定理文と適用条件は実読済みだが、CY1982 Theorem 4.4の原文・証明は未取得であり、原典確認済みとはしない。正確な書誌・係数点検・確認範囲は `research/source-audit.md`、直接証明は現行本文が正本である。

## 三研究を一体で進める方針

[固定配置補空間・Part I–III](https://github.com/uedakazushi/multiscale-kaehler-einstein)、本repoの退化族局所解析・Part IVと条件付き距離論・Part V、[曲面のactual KE Lagrangian構成と大域GH実現](https://github.com/uedakazushi/surface-lagrangian-torus-fibration)を共同で編集・監査する。各repoと主論文の正本はこの責任分担で維持する。証明を重複収録せず、仮定・定理ラベル・尺度・確認版を揃える。固定空間の漸近と退化族の一様性、Part IIのcomplex periodsとsymplectic actions、曲面の直接評価と本稿のCP/PBE/TCを区別する。詳しい方針は[現行研究方針](00_research_plan.md)、共有局所入力は[研究ノートの依存表](research/notes.md)を参照する。

Part I v1.10（研究一式v1.19）は、連結なsmooth projective pairのreduced SNC境界とK+D ampleを仮定する。n=1を含み、空境界はcompactな一点錐の場合として扱う。固定空間のexact collar/tensor入力からproperな1-Lipschitz全射と有界加法誤差Kを与え、固定基点のblow-downは一意に定まる。固定した写像について、全中心・全半径のambient閉球のGH誤差は3K/(2R)以下である。LDPのambient-open下界に加え、非空境界のexact tail・joint law・distance Laplace transformも通常の全face volume-IRFAで扱い、指数的volume remainderを追加仮定しない。Kは固定空間の定数であり、退化parameterに一様な評価を意味しない。曲面の `ke:intermediate-moving-classification` は、P0の同じ全射のdistortionを吸収する中間尺度で、任意の移動基点のpointed GH極限を成分錐、分岐する半平面の積模型、全角3π/2の錐、平面の四型に分類する。これは既存の全域歪みと有限targetの計量幾何の帰結であり、Part IV/Vの新しいtensor入力ではない。利用条件・監査範囲・正本のラベルは研究ノートに集約する。

同じ固定空間の移動基点極限は、有界基点のcone、またはEuclidean因子とincidence link coneの積に分類され、任意の拡大列に対して全て実現する。正の面座標を保つstarとm>2Aのambient閉球同定を用いる。復元対象はmetric linkの等長型であり、元の標識・cell分割・depth重みは別のデータである。標準cone幾何やLeuzingerのlocally symmetric spaceでの先行結果との関係は、研究ノートとPart I Introductionに記す。

固定空間の測度付き平行移動は、全normal中心の最小値が無限大へ進む任意の列について、通常のvolume-IRFAからstrip上の全変動収束を、metric-IRFAと収束する基点offset・残余点も用いて全半径のambient閉球上の測度付き積極限を与える。Smooth volume-IRFAは不要である。Face massの交点数公式は非正規化KE体積に対するもので、確率正規化では全体積で割る。Ordinary volume-IRFAによるAbel極限と、有理型延長に必要な追加条件を区別する。標識と向きを伴うPart II v2.1のsecondary periodsも、裸の距離極限やsymplectic actionsとは異なる。直接Stokes・Mellin・Chambert–Loir–Tschinkelとの一次比較を含む仮定依存と確認範囲は、研究ノートと正本Introductionを参照する。

## 現行の解析結果

正確な三重点座標をζ0ζ1ζ2=t、ell_i=−log|ζ_i|²、L=−log|t|²、R=log Lとする。以下のactual結果は任意の固定次数d≥5について全phase・全三重点に一様であり、定数は固定次数と族に依存してよい。次数一様性は主張しない。

- **全深部三重点のtensor比較。** Complete simplex KE模型g_L^sfに対して、min ell_i≥mで全固定階の誤差O(1/m)。大域capped volume下界、内外simplex barriers、Yau Schwarz、Savin小摂動定理を用いる。全固定次数のweighted cap minorsとresidue規格化によるdensity下界を含めて証明し、三重点内には(TC)/(PBE)を仮定しない。正本は[full triple節](papers/sections/full_triple_comparison.tex)の `coarse:thm:full-triple-tensor`。
- **全閉cornerのGH収縮。** 三枚のunit squaresからなるC_Jに、その内部の経路で定める距離d_Jを入れる。全phaseを含むsoftmax hexagonの内在距離と、外側保護領域{min ell_i>R/2}内の全経路を許すprotected-ambient距離の双方で、R^−2 g_tのprojection distortionはO(log R/R)。Seamsと共通頂点も含む。正本は[closed corner節](papers/sections/closed_triple_metric.tex)の `simplex:thm:closed-corner-model` / `simplex:cor:actual-closed-corner-metric`。
- **境界の鋭い積漸近。** δ=(a+b)/Lなら二重cusp productへのmodel誤差はO(δ²)、actual誤差はO(1/min ell_i+δ²)。0<η<1/2の開正方形a,b∈[L^η/2,2L^(1−η)]ではO(L^−η)。Facetではb=ell_0、a=ell_1、d_*=min(a,L−a)としてcusp×finite-annulusへのmodel誤差O((b/d_*)^(2/3))、actualにはO(1/b)を加える。すべて全固定階・全角度の評価である。正本は[simplex境界節](papers/sections/simplex_boundary_geometry.tex)の `simplex:prop:dominant-product` / `simplex:cor:actual-dominant-product` / `simplex:prop:facet-product`。
- **正確な係数1とactive co-Gram。** 各iについて |d log ell_i|_{g_L^sf}≤1。ell_i≤Le^−Aのactive indicesが一つまたは二つならco-GramはId+O(e^(−A/2))、二つならO(e^−2A)。ActualにはO(1/min ell_i)を加える。正本は同節の `simplex:lem:rank-one-schwarz` / `simplex:cor:active-cogram`。

**Volume比較の入力。** `coarse:lem:complete-volume-upper` はcomplete負KE背景hに対し、u=log(ω²/h²)の上有界性を明示的に仮定し、Laplacian型Omori–Yauと算術幾何平均で上比較を得る。本稿のfinite windowsでは、固定tの有限angular quotient上でactual densityが人工境界まで有限に延長し、complete model densityが全人工境界で発散するため、この仮定を確認できる。完備性だけからuの上有界性を推論しない。Full tripleの下比較は固定face上の全phase・t一様なdensity下界で足りる（`coarse:rem:full-triple-face-input`）。Interiorの下界はmaximum principleで得られ、actual tensor比較やactual距離の境界逃避は前提としない。小potentialはRicci恒等式によるlog-volume ratio自身である。

関連[Lagrangian主稿](https://github.com/uedakazushi/surface-lagrangian-torus-fibration/blob/main/papers/surface-lagrangian-torus-fibration.tex)の `ke:closed-corner-gh` / `ke:closed-corner-protected-gh` により、**同じactual Lagrangian torus bundleの同じ射影**が上記二つの距離についてGH近似となる。全fiberの非正規化intrinsic/ambient diameterはO(1/R)、正規化後はO(1/R²)、raw cubical mapとの誤差はO(log R/R)。継目でもfibersはregular T²である。開正方形の固定長方形Kη=[η,1−η]²でも、actual Lagrangian fibrationによる平坦長方形への内在GH収束とprojection distortion O(L^−η)を得ている。

## Source-free neckで得た接続の入力

[束座標とnormal moment](papers/sections/source_free_neck_coordinates.tex)では、固定compact base上の射影的法線束からexact uv=tと共通の正則S¹を構成する。単一のcanonical primitiveにより円平均η_tのmomentを規格化し、`pair:prop:fixed-end-transfer` が、固定end collarsのlog-densityのC¹収束と極限成分のradial derivative評価からperiod 1の主項±4π/(−log r²)と共通moment intervalを与える。Songの固定gauge収束とRochon–ZhangのSNC定理がこの二条件を検証する。Hermitian normと局所frameの半径差によるO(s_r^−2)を含め、rを先に固定してから全複素t→0とする。全neckのMoser flow bufferは別の入力である。

`pair:rem:normal-frame-winding` は、全orbitを含むpatch上でΩをbΩへ変更するとmomentが−2π wind(b)だけ変わることを示す。Base-onlyでないunitでもnormal windingが零なら同じmomentを保つが、primitiveの残余閉periodまで消えるとは限らない。

関連Lagrangian稿の[二段階平均](https://github.com/uedakazushi/surface-lagrangian-torus-fibration/blob/main/papers/sections/paper/ke_staged_neck_averaging.tex)は、normal circleを先に平均して、同じactual circleと全marked cycleの作用周期を保つ。指定primitive subgroupに適合するclosed-corner bundleにも同じO(log R/R)のGH評価を与え、一段階bundleとはHamiltonian mapで比較する。

Sourceを含む固定基底のendとshellは、同じ曲面稿の `ke:source-inclusive-fixed-shell` が証明の正本である。一つのΩ_tを固定したままsourceへ非零正則に延ばし、全phaseでの±4π/s_rと、rを先に固定したshellの正の横断費用を示す。Source-freeなPart IVの定理を無条件に拡張した扱いにはしない。異なる体積frameのprimitiveの閉形式差とresidual periodsも保持する。

[Neckの解析比較](papers/sections/source_free_neck_comparison.tex)では、無条件のbounded volume envelope、固定residual境界の非消失誤差、mixed termsを許すrank-one下界によるnormal circle長の評価を整理した。Actual bufferからrank-one下界を得る場合、そのbufferを別に証明する。Small log-densityを用いる比較背景はcoupled KE metricでもよく、source-freeという条件だけでproduct asymptoticsを結論しない。

## 残る核心と次の着手

本repoの公表準備では、固定faceの局所安定性と固定end移送の最小入力を基準に、未確認の一次資料・定量的新規性と実際の利用箇所を絞って確認する。既存のcapped-volume、full-triple、固定endの指定証明鎖を一律に反復しない。曲面の同じ射影によるatlas/GH実現と確率測度極限の適用範囲を整え、六次の先指定追加保持集合への拡張、CP/PBE/TCと高次元化は別の完成条件で進める。

曲面repoの `ke:global-metric-realization` には、各固定d≥5・既存の一般性条件の族について、actual全域Lagrangian fibrationと同じ f_t=p_Tπ_t の全曲面ambient距離のGH実現を示す証明がある。Normal Moser buffer、全交わりのmatching、core filling、sourceの全moment退出O(1)、global scalar下界とportal上界はそこで別に構成する。本repoの局所closed-corner評価だけからこれらが従うという意味ではない。

本repoのSourceを含むexterior全体の(TC)_5と、全域の(CP)_d+(PBE)_dは未検証のまま保持する。曲面稿の直接証明はこのpackage自体の検証を与えない。保護領域内の距離と全曲面ambient距離を区別し、targetの三枚のcorner距離が全C_dの距離の制限と一致することは曲面稿の `topo:coordinate-retraction` に委ねる。

共有局所入力とK5の指定鎖の監査を保持し、曲面改訂38では固定領域を保つcritical-area調整を実構成へ進めた。`ng8:componentwise-critical-area` は、各自由成分の面積を保存する正の有限配分行列の存在と、指定relative orbit内の面積実現を同値にする。`ng8:strict-area-cuts` はその可否を成分ごとの総量一致とstrictな有限cut条件で判定する。Sourceを通るregular葉の飽和annuliを保持するactual P0では、固定t・小さいmoment区間で総和零の十分小さい滑らかな面積増分を実現できる（`ng8:p0-small-area-flexibility`）。Source内の面積がμ=0で滑らかであることや、退化parameterに一様な余裕は要求しない。

固定tのfree compact bandでは、同じ曲面稿の `ng8:fixed-fiber-relative-dh` がinvariant primitiveとaffineなtoric boundary actionsからStokesによりreduced areaのaffine性を与える。t=0への全空間延長は不要だが、source固定点を横切る標準模型の面積π(c−|μ|)は折れを持つ（`ng8:source-dh-wall`）。またraw momentのo(1)誤差だけではGHのlongitude誤差は消えない（`ke:raw-moment-error-insufficient`）。これらの適用条件と証明の正本は曲面稿であり、本repoには接続条件だけを記す。

Core側の `ke:actual-anchor-fan-criterion` は、同じLiouville primitiveでのactual anchor periodsと保持overlapのcycle markingが所定値を満たせば、既存domain・skeleton・corner葉を保つK4／Petersen作用chartを構成する。五次では、anchor上の保持集合を標準K2 end collarsだけに選ぶ局所適用を `ke:k4-actual-end-anchor`（曲面改訂39に統合済み）として得る。正のresiduesを固定し、stage→component cut→小さいtの順に選ぶと、全保持境界のperiodはQ_ab=ν_b−ρ_b<−ρ_b/2となる。同じtransported meridiansのclutchingも確認でき、任意の有向四角形のK4 anchor targetsを実現できる。Sourceの全compact pinched fibersの飽和近傍は、各固定tで|μ|<δ/2に選び、anchor bandから離して保持する。

五次では `ke:k4-actual-neck-periods` が共通primitiveの実切片とsource shearを有限式へ帰着し、`ng8:quintic-full-moment` がcompatible dataの全intervalを実現する。Source-free部分の自由作用仮定をsource-inclusive neckへ移さず、全sourceのwallを差し引いた滑らかな自由需要に面積Moserを適用する。解析領域・cuts・小さいtを選んだ後、source同定S_tとK2補正Dを変えずにthin葉を取り、固定end massを除く全tailの追加質量をDiniで小さくする。葉の微分評価やthin幅選択後の追加t閾値は不要である。有限source pointsと局所葉を固定し、全開overlapの作用と全葉を一致させ、実数平行移動まで含むatlasに `ke:relative-replacement-gh` を接続する。

**Atlas側では五次と六次標準Petersenの同時実現を公表範囲に含め、任意に追加した保持annuli・大きいsource tailsに対する相対可解性を別課題とする。** 五次の存在証明は初期葉を選ぶ自由を使い、その後に全nodal neighborhoodsを固定する。既固定の任意P0の変更やt方向のsmooth familyを主張しない。Part IV/Vの新tensor入力、CP/PBE/TC又はH_loc/H_ancの検証にも読み替えない。

## 論文と再現資産

2026-08-31五篇連作の退化二部作を元の全文TeXから移行し、有効な内容を現行稿に保持している。

- [Part IV：局所安定性と閉cornerの収縮](papers/kaehler-einstein-degeneration.tex)：主たる公表用原稿。現行v1.14は124頁、変更箇所を含む9頁の表示を確認済み。Complete simplexの最小存在入力と一意性・完備性・規格化の直接証明を統合した。全深部三重点・閉cornerの無条件結果と、sourceを含むquintic exteriorの(TC)_5付き結果を分ける。全域のsharp co-Gramは粗い比較と(PBE)_d付き。
- [Part V：cubical GH](papers/cubical-gh-limit.tex)：現行v1.10、37頁。一般次数のcubical複体の位相・整数ホモロジー、abstract pruning–transport、diam(C_5)=sqrt(13)を含む。全曲面のactual GH適用は(CP)_d+(PBE)_d付き。
- [Punctured-neck技術稿](papers/punctured-neck-scattering.tex)：旧81頁の証明全文をLuaLaTeXへ移植した稿（回収時92頁）。条件付きの解析入力を冒頭に明記。
- [Source-free比較の研究ノート](papers/source-free-comparison.tex)：source-free領域の補助原稿。
- [補助検算](scripts/)：2026-11-20に統合稿5本と旧v0.12の16本を再実行し、全件成功。現行の研究資料v1.27では再実行していない。旧16本は配布時のSHA-256と一致。有限計算・式の診断であり解析証明の代用ではない。

関連Lagrangian研究の人工PL基底計量では、分岐基底からC_dへのdistortionはd=5でΘ(ε²)、d≥6でΘ(ε)。これはactual KE計量の収束とは別の結果である。大域的な適用にはno-shortcut、square lifts、fiber/portal connectorsの定量条件を揃える必要があり、最初の二条件だけから第三は従わない。

固定補空間側は[Part I v1.10・総説v1.14・研究資料v1.19](https://github.com/uedakazushi/multiscale-kaehler-einstein/tree/2926300c2425c7e68550ac08ee81a2afa639a0c6)を確認版とする。尖点付き有限面積双曲曲線Sと境界のないコンパクト連結Riemann因子Yの積で、距離Laplace変換をRe s<3の切断半平面上でW/(1−s)−H(s)Log(1−s)+G(s)と表示する。Hはentire、GはRe s<3で正則であり、WとmonodromyからYの正規化基点距離分布を回収する。通常volume-IRFA一般への解析接続・等長型・族一様性は主張しない。総説はこの積の結果、Part IV v1.12の固定end/winding、曲面改訂44の同じ射影による確率体積極限を統合する。これらは固定補空間側の成果・共同編集であり、Part IV/Vへの新しい解析仮定やCP/PBE/TCの検証ではない。 新しい `cor:CW-fixed-cutoff-budget` は固定SNC cutoffの脱落質量とStokes defectをCe^{-A}で抑える。統合担当がこの追加証明を実読し、固定対の予算とtの有効収束率を区別している。

## 保存と検証

Part IV v1.14は124頁に組版し、未定義参照・引用、重複label、欠字、LaTeX error、overfull/underfullの六分類は全て0。1・7–8・49–53・123頁の9頁を150dpiで実表示し、表題、Introduction、simplex模型の全証明とCheng–Yau書誌に欠字・重なり・切断・数式のはみ出しを認めない。全124頁の逐頁表示ではない。内容不変のPart V v1.10は既存37頁・指定5頁表示の記録を保持し、今回は再組版・再表示していない。有限計算証明書も今回再実行していない。各source/PDF hashと実行環境はvalidation.jsonに記す。

Part IV v1.10では新局所定理 `coarse:thm:boundary-to-triple`、モデルとshift比較、小摂動評価、全平面退化への適用を担当と別担当が点検した。Compact phase quotientでの最大値原理、境界上界の各固定tでの有限性、定数依存、normalized coverでの正則性を確認した。全capped determinant・全外部原典・全主稿の包括的再監査、外部査読、形式証明は未実施。有限距離論の計算は今回変更しておらず再実行していない。詳しい状態は[検証状態](research/validation.json)。

研究資料v1.27は、曲面改訂44の等重みPetersen同時実現と測度系の適用範囲を同期する。確認した保存commitは曲面 `d39270ec79ad973551f67c740682dbb06bac48e5`、固定側 `2926300c2425c7e68550ac08ee81a2afa639a0c6`（Part I v1.10・総説v1.14・資料v1.19）である。曲面側の既存の組版・表示記録と、本repoで今回行った確認を区別する。IV/Vの既存の科学引用pin（曲面改訂37・`32c67aefe6beb47c2955923e2b6eb2471d48af31`）は維持し、新しい六次の証明は曲面側を正本とする。保存・hub更新は別に確認する。

再生成はルートで `latexmk`、PDF/SyncTeXの出力先は `build/`。LuaLaTeX、luatexja、Harano Ajiと数学フォントの有効なmapを備えたTeX Liveを用いる。[移行・検証範囲](research/migration.md)と[ソース対応](research/source-manifest.json)を参照する。通常のcommitとmainへのpushで保存し、研究成果の保存とresearch-hubの更新を別々に確認する。
