# Kähler–Einstein degeneration

更新：2026-11-20 / v1.6

最初に[現行研究方針](00_research_plan.md)、次に[研究ノート](research/notes.md)を読む。固定次数d≥5の一般型曲面の全平面退化について、actual KE計量の径の尺度の極限とLagrangian torus fibrationによる実現を研究する。正本はGitHubのmain、研究全体の入口は[research-hub](https://github.com/uedakazushi/research-hub)。

## 現行の解析結果

正確な三重点座標をζ0ζ1ζ2=t、ell_i=−log|ζ_i|²、L=−log|t|²、R=log Lとする。以下のactual結果は任意の固定次数d≥5について全phase・全三重点に一様であり、定数は固定次数と族に依存してよい。次数一様性は主張しない。

- **全深部三重点のtensor比較。** Complete simplex KE模型g_L^sfに対して、min ell_i≥mで全固定階の誤差O(1/m)。大域capped volume下界、内外simplex barriers、Yau Schwarz、Savin小摂動定理を用いる。全固定次数のweighted cap minorsとresidue規格化によるdensity下界を含めて証明し、三重点内には(TC)/(PBE)を仮定しない。正本は[full triple節](papers/sections/full_triple_comparison.tex)の `coarse:thm:full-triple-tensor`。
- **全閉cornerのGH収縮。** 三枚のunit squaresからなるC_Jに、その内部の経路で定める距離d_Jを入れる。全phaseを含むsoftmax hexagonの内在距離と、外側保護領域{min ell_i>R/2}内の全経路を許すprotected-ambient距離の双方で、R^−2 g_tのprojection distortionはO(log R/R)。Seamsと共通頂点も含む。正本は[closed corner節](papers/sections/closed_triple_metric.tex)の `simplex:thm:closed-corner-model` / `simplex:cor:actual-closed-corner-metric`。
- **境界の鋭い積漸近。** δ=(a+b)/Lなら二重cusp productへのmodel誤差はO(δ²)、actual誤差はO(1/min ell_i+δ²)。0<η<1/2の開正方形a,b∈[L^η/2,2L^(1−η)]ではO(L^−η)。Facetではb=ell_0、a=ell_1、d_*=min(a,L−a)としてcusp×finite-annulusへのmodel誤差O((b/d_*)^(2/3))、actualにはO(1/b)を加える。すべて全固定階・全角度の評価である。正本は[simplex境界節](papers/sections/simplex_boundary_geometry.tex)の `simplex:prop:dominant-product` / `simplex:cor:actual-dominant-product` / `simplex:prop:facet-product`。
- **正確な係数1とactive co-Gram。** 各iについて |d log ell_i|_{g_L^sf}≤1。ell_i≤Le^−Aのactive indicesが一つまたは二つならco-GramはId+O(e^(−A/2))、二つならO(e^−2A)。ActualにはO(1/min ell_i)を加える。正本は同節の `simplex:lem:rank-one-schwarz` / `simplex:cor:active-cogram`。

関連[Lagrangian主稿](https://github.com/uedakazushi/lagrangian-torus-fibration/blob/main/papers/lagrangian-torus-fibration.tex)の `ke:closed-corner-gh` / `ke:closed-corner-protected-gh` により、**同じactual Lagrangian torus bundleの同じ射影**が上記二つの距離についてGH近似となる。全fiberの非正規化intrinsic/ambient diameterはO(1/R)、正規化後はO(1/R²)、raw cubical mapとの誤差はO(log R/R)。継目でもfibersはregular T²である。開正方形の固定長方形Kη=[η,1−η]²でも、actual Lagrangian fibrationによる平坦長方形への内在GH収束とprojection distortion O(L^−η)を得ている。

## 残る核心と次の着手

閉cornerのd_JはC_J自身の距離であり、full complex C_dの他のcellsを経由する距離ではない。Protected-ambient距離も全曲面X_tの距離とは異なる。全X_tのshortcut、異なるtriple chartsとneckの接着、source・branch・coreを含む既存大域fibrationとの同定は未解決である。

次は**neck collarのorbit partition matching**を行う。Lagrangian側の `ke:relative-fiber-preserving` / `ke:relative-neck-matching` は、既にLagrangianで同じorbit partitionを持つcollarを集合として保つ。Actual overlapでこの分割、action periods、quantitative bufferを合わせる必要があり、非定数holomorphic unitを含む座標変更では分割が変わり得る。その後、sourceの正しいorientationでtensor・connector評価を進め、global no-shortcutとportal費用を検証する。

Sourceを含むexterior全体の(TC)_5と、大域の(CP)_d+(PBE)_dは未検証のまま保持する。Bounded densityだけからtensor比較が従わない反例、任意半径product窓の障害、source orientationの区別は[研究ノート](research/notes.md)に残す。新結果の新規性の包括的確認、外部査読、形式証明は未実施。

## 論文と再現資産

2026-08-31五篇連作の退化二部作を元の全文TeXから移行し、有効な内容を現行稿に保持している。

- [Part IV：局所模型](papers/kaehler-einstein-degeneration.tex)：主たる公表用原稿。66頁は回収時の記録。全深部三重点・閉cornerの無条件結果と、sourceを含むquintic exteriorの(TC)_5付き結果を分ける。全域のsharp co-Gramは粗い比較と(PBE)_d付き。
- [Part V：cubical GH](papers/cubical-gh-limit.tex)：34頁は回収時の記録。一般次数のcubical複体の位相・整数ホモロジー、abstract pruning–transport、diam(C_5)=sqrt(13)を含む。全曲面のactual GH適用は(CP)_d+(PBE)_d付き。
- [Punctured-neck技術稿](papers/punctured-neck-scattering.tex)：旧81頁の証明全文をLuaLaTeXへ移植した稿（回収時92頁）。条件付きの解析入力を冒頭に明記。
- [Source-free比較の研究ノート](papers/source-free-comparison.tex)：source-free領域の補助原稿。
- [補助検算](scripts/)：統合稿5本と旧v0.12の16本を再実行し、全件成功。旧16本は配布時のSHA-256と一致。有限計算・式の診断であり解析証明の代用ではない。

関連Lagrangian研究の人工PL基底計量では、分岐基底からC_dへのdistortionはd=5でΘ(ε²)、d≥6でΘ(ε)。これはactual KE計量の収束とは別の結果である。大域的な適用にはno-shortcut、square lifts、fiber/portal connectorsの定量条件を揃える必要があり、最初の二条件だけから第三は従わない。

## 保存と検証

新節の証明を独立に再読し、参照・labels・環境対応を静的確認した。回収稿の組版成功とは別に、**現行改訂はLuaLaTeX基本資産不足により未組版**である。`lualatex.fmt`・LuaTeX-ja等がなく、組版の試行は本文処理前に停止した。

再生成はルートで `latexmk`、PDF/SyncTeXの出力先は `build/`。[移行・検証範囲](research/migration.md)と[ソース対応](research/source-manifest.json)を参照する。通常のcommitとmainへのpushで保存し、研究成果の保存とresearch-hubの更新を別々に確認する。
