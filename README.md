# Kähler–Einstein degeneration

更新：2026-11-22 / v1.13（研究資料。Part IV–V本文はv1.9）

最初に[現行研究方針](00_research_plan.md)、次に[研究ノート](research/notes.md)を読む。固定次数d≥5の一般型曲面の全平面退化について、actual KE計量の径の尺度の極限とLagrangian torus fibrationによる実現を研究する。正本はGitHubのmain、研究全体の入口は[research-hub](https://github.com/uedakazushi/research-hub)。

## 三研究を一体で進める方針

[固定配置補空間・Part I–III](https://github.com/uedakazushi/multiscale-kaehler-einstein)、本repoの退化族局所解析・Part IVと条件付き距離論・Part V、[曲面のactual KE Lagrangian構成と大域GH実現](https://github.com/uedakazushi/surface-lagrangian-torus-fibration)を共同で編集・監査する。各repoと主論文の正本はこの責任分担で維持する。証明を重複収録せず、仮定・定理ラベル・尺度・確認版を揃える。固定空間の漸近と退化族の一様性、Part IIのcomplex periodsとsymplectic actions、曲面の直接評価と本稿のCP/PBE/TCを区別する。詳しい方針は[現行研究方針](00_research_plan.md)、共有局所入力は[研究ノートの依存表](research/notes.md)を参照する。

Part I v1.5（研究一式v1.6）は、固定SNC空間のexact collar/tensor入力からproperな1-Lipschitz全射と有界加法誤差Kを与える。固定した写像について、全中心・全半径のambient閉球のGH誤差は3K/(2R)以下である。LDPのambient-open下界に加え、exact tail・joint law・distance Laplace transformも通常の全face volume-IRFAで扱い、指数的volume remainderを追加仮定しない。Kは固定空間の定数であり、退化parameterに一様な評価を意味しない。曲面改訂33は、P0の同じ全射のdistortionとtarget上の基点変位を吸収する中間尺度で、component coreと変更collarの任意基点から成分錐へのpointed GH収束を与える。利用条件・監査範囲・正本のラベルは研究ノートに集約する。

同じ固定空間の移動基点極限は、有界基点のcone、またはEuclidean因子とincidence link coneの積に分類され、任意の拡大列に対して全て実現する。正の面座標を保つstarとm>2Aのambient閉球同定を用いる。復元対象はmetric linkの等長型であり、元の標識・cell分割・depth重みは別のデータである。標準cone幾何やLeuzingerのlocally symmetric spaceでの先行結果との関係は、研究ノートとPart I Introductionに記す。

固定空間の測度付き平行移動は、全normal中心の最小値が無限大へ進む任意の列について、通常のvolume-IRFAからstrip上の全変動収束を、metric-IRFAも用いて全半径のambient閉球上の測度付き積極限を与える。Smooth volume-IRFAは不要である。滑らかな基準曲率と有界primitiveによる直接Stokes、および全faceのvolume漸近を用いるMellinの一様性とincidenceの確認範囲も、正本への参照とともに研究ノートへ記す。

## 現行の解析結果

正確な三重点座標をζ0ζ1ζ2=t、ell_i=−log|ζ_i|²、L=−log|t|²、R=log Lとする。以下のactual結果は任意の固定次数d≥5について全phase・全三重点に一様であり、定数は固定次数と族に依存してよい。次数一様性は主張しない。

- **全深部三重点のtensor比較。** Complete simplex KE模型g_L^sfに対して、min ell_i≥mで全固定階の誤差O(1/m)。大域capped volume下界、内外simplex barriers、Yau Schwarz、Savin小摂動定理を用いる。全固定次数のweighted cap minorsとresidue規格化によるdensity下界を含めて証明し、三重点内には(TC)/(PBE)を仮定しない。正本は[full triple節](papers/sections/full_triple_comparison.tex)の `coarse:thm:full-triple-tensor`。
- **全閉cornerのGH収縮。** 三枚のunit squaresからなるC_Jに、その内部の経路で定める距離d_Jを入れる。全phaseを含むsoftmax hexagonの内在距離と、外側保護領域{min ell_i>R/2}内の全経路を許すprotected-ambient距離の双方で、R^−2 g_tのprojection distortionはO(log R/R)。Seamsと共通頂点も含む。正本は[closed corner節](papers/sections/closed_triple_metric.tex)の `simplex:thm:closed-corner-model` / `simplex:cor:actual-closed-corner-metric`。
- **境界の鋭い積漸近。** δ=(a+b)/Lなら二重cusp productへのmodel誤差はO(δ²)、actual誤差はO(1/min ell_i+δ²)。0<η<1/2の開正方形a,b∈[L^η/2,2L^(1−η)]ではO(L^−η)。Facetではb=ell_0、a=ell_1、d_*=min(a,L−a)としてcusp×finite-annulusへのmodel誤差O((b/d_*)^(2/3))、actualにはO(1/b)を加える。すべて全固定階・全角度の評価である。正本は[simplex境界節](papers/sections/simplex_boundary_geometry.tex)の `simplex:prop:dominant-product` / `simplex:cor:actual-dominant-product` / `simplex:prop:facet-product`。
- **正確な係数1とactive co-Gram。** 各iについて |d log ell_i|_{g_L^sf}≤1。ell_i≤Le^−Aのactive indicesが一つまたは二つならco-GramはId+O(e^(−A/2))、二つならO(e^−2A)。ActualにはO(1/min ell_i)を加える。正本は同節の `simplex:lem:rank-one-schwarz` / `simplex:cor:active-cogram`。

**Volume比較の入力。** `coarse:lem:complete-volume-upper` はcomplete負KE背景hに対し、u=log(ω²/h²)の上有界性を明示的に仮定し、Laplacian型Omori–Yauと算術幾何平均で上比較を得る。本稿のfinite windowsでは、固定tの有限angular quotient上でactual densityが人工境界まで有限に延長し、complete model densityが全人工境界で発散するため、この仮定を確認できる。完備性だけからuの上有界性を推論しない。Full tripleの下比較は固定face上の全phase・t一様なdensity下界で足りる（`coarse:rem:full-triple-face-input`）。Interiorの下界はmaximum principleで得られ、actual tensor比較やactual距離の境界逃避は前提としない。小potentialはRicci恒等式によるlog-volume ratio自身である。

関連[Lagrangian主稿](https://github.com/uedakazushi/surface-lagrangian-torus-fibration/blob/main/papers/surface-lagrangian-torus-fibration.tex)の `ke:closed-corner-gh` / `ke:closed-corner-protected-gh` により、**同じactual Lagrangian torus bundleの同じ射影**が上記二つの距離についてGH近似となる。全fiberの非正規化intrinsic/ambient diameterはO(1/R)、正規化後はO(1/R²)、raw cubical mapとの誤差はO(log R/R)。継目でもfibersはregular T²である。開正方形の固定長方形Kη=[η,1−η]²でも、actual Lagrangian fibrationによる平坦長方形への内在GH収束とprojection distortion O(L^−η)を得ている。

## Source-free neckで得た接続の入力

[束座標とnormal moment](papers/sections/source_free_neck_coordinates.tex)では、固定compact base上の射影的法線束からexact uv=tと共通の正則S¹を構成した。Canonical primitiveを一つ固定でき、actual KE formの円平均η_tに対するmomentが加法定数なしに大域化する。固定した両endでは、周期1のmomentが±4π/(−log r²)を主項に持つ。Songの固定gauge収束とRochon–ZhangのSNC cusp漸近により、rを固定してからt→0とすればη_tの共通moment intervalを得る。全neckのMoser flow bufferはこの結果に含まれない。

関連Lagrangian稿の[二段階平均](https://github.com/uedakazushi/surface-lagrangian-torus-fibration/blob/main/papers/sections/paper/ke_staged_neck_averaging.tex)は、normal circleを先に平均して、同じactual circleと全marked cycleの作用周期を保つ。指定primitive subgroupに適合するclosed-corner bundleにも同じO(log R/R)のGH評価を与え、一段階bundleとはHamiltonian mapで比較する。

[Neckの解析比較](papers/sections/source_free_neck_comparison.tex)では、無条件のbounded volume envelope、固定residual境界の非消失誤差、mixed termsを許すrank-one下界によるnormal circle長の評価を整理した。後者にはactual bufferが必要。Small log-densityを用いる比較背景はcoupled KE metricでもよく、source-freeという条件だけでproduct asymptoticsを結論しない。

## 残る核心と次の着手

曲面repoの `ke:global-metric-realization` には、各固定d≥5・既存の一般性条件の族について、actual全域Lagrangian fibrationと同じ f_t=p_Tπ_t の全曲面ambient距離のGH実現を示す証明がある。Normal Moser buffer、全交わりのmatching、core filling、sourceの全moment退出O(1)、global scalar下界とportal上界はそこで別に構成する。本repoの局所closed-corner評価だけからこれらが従うという意味ではない。

本repoのSourceを含むexterior全体の(TC)_5と、全域の(CP)_d+(PBE)_dは未検証のまま保持する。曲面稿の直接証明はこのpackage自体の検証を与えない。保護領域内の距離と全曲面ambient距離を区別し、targetの三枚のcorner距離が全C_dの距離の制限と一致することは曲面稿の `topo:coordinate-retraction` に委ねる。

共有局所入力の量化、曲面K2の全交わりの飽和・共通葉、K3のlink→adapted primitive→相対葉族→補間後trim→全域被覆の指定鎖を重点点検した。次は**この確認範囲を起点に、未確認の依存入力と一次文献・主定理のscopeを公表前監査する**。本稿の `pair:lem:diagonal-fixed-end` は選んだ遅いmoving exhaustionへの移行と有限予算の吸収を証明し、任意速度での一様性を主張しない。曲面の一般基点での中間尺度にはdistortionだけでなくtarget変位の予算も要る。CP/PBE/TCの強い解析課題は独立に残し、bounded-densityの反例とsource orientationの障害を研究ノートに保持する。全原稿・全外部入力の包括的再監査、新規性確認、外部査読、形式証明は未実施である。

## 論文と再現資産

2026-08-31五篇連作の退化二部作を元の全文TeXから移行し、有効な内容を現行稿に保持している。

- [Part IV：局所模型](papers/kaehler-einstein-degeneration.tex)：主たる公表用原稿。現行v1.9は117頁。全深部三重点・閉cornerの無条件結果と、sourceを含むquintic exteriorの(TC)_5付き結果を分ける。全域のsharp co-Gramは粗い比較と(PBE)_d付き。
- [Part V：cubical GH](papers/cubical-gh-limit.tex)：現行v1.9は37頁。一般次数のcubical複体の位相・整数ホモロジー、abstract pruning–transport、diam(C_5)=sqrt(13)を含む。全曲面のactual GH適用は(CP)_d+(PBE)_d付き。
- [Punctured-neck技術稿](papers/punctured-neck-scattering.tex)：旧81頁の証明全文をLuaLaTeXへ移植した稿（回収時92頁）。条件付きの解析入力を冒頭に明記。
- [Source-free比較の研究ノート](papers/source-free-comparison.tex)：source-free領域の補助原稿。
- [補助検算](scripts/)：統合稿5本と旧v0.12の16本を再実行し、全件成功。旧16本は配布時のSHA-256と一致。有限計算・式の診断であり解析証明の代用ではない。

関連Lagrangian研究の人工PL基底計量では、分岐基底からC_dへのdistortionはd=5でΘ(ε²)、d≥6でΘ(ε)。これはactual KE計量の収束とは別の結果である。大域的な適用にはno-shortcut、square lifts、fiber/portal connectorsの定量条件を揃える必要があり、最初の二条件だけから第三は従わない。

## 保存と検証

2026-11-22にv1.9のPart IVを117頁、Part Vを37頁へLuaLaTeXで組版した。最終logには未解決参照・引用、重複ラベル、欠字、overfull/underfull boxはない。日本語フォントの代替・featureとPDF bookmark内の数式に関する警告は残る。Part IVの1、6–7、70–71、117頁、Part Vの2、4–5、37頁を画像で確認した。全頁の逐頁点検ではない。環境のformatとfont mapの欠落を既存のTeX Live環境で解消し、PDF/SyncTeXの出力先がbuildであることを確認した。

Part IV–Vの現行v1.9で確認した数学的内容は、共有する局所入力の仮定・量化の重点照合と `pair:lem:diagonal-fixed-end` の証明・別の読み手による独立内部点検である。既存証明全体の再監査、網羅的新規性調査、外部査読、形式証明とは区別する。2026-11-20の有限検算成功記録を保持するが、今回再実行していない。詳しい実行状態は[検証状態](research/validation.json)。

研究資料v1.13はPart I v1.5の移動基点分類とmetric linkの復元範囲を同期した。今回直接点検したのはincidence copies、正のstar、ambient球の2A条件、全極限の分類・実現であり、metric linkとLeuzinger/Bridson–Haefliger比較は共同監査として記録する。Co-Gram→収縮写像→閉球近似と測度付き平行移動の独立点検、Stokes・Mellin等の共同点検も確認範囲に含む。外部稿はPart I v1.5が62頁、総説v1.5が12頁に組版され、共同作業でPart Iの指定19頁と総説全12頁を画像確認した。Part IV–VのTeXは変更しておらず、本文の現行版と組版確認はv1.9のままである。本repoの組版・有限検算は文書同期に伴って再実行していない。

再生成はルートで `latexmk`、PDF/SyncTeXの出力先は `build/`。LuaLaTeX、luatexja、Harano Ajiと数学フォントの有効なmapを備えたTeX Liveを用いる。[移行・検証範囲](research/migration.md)と[ソース対応](research/source-manifest.json)を参照する。通常のcommitとmainへのpushで保存し、研究成果の保存とresearch-hubの更新を別々に確認する。
