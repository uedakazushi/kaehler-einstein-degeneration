# Kähler–Einstein degeneration

更新：2026-11-20 / v1.7

最初に[現行研究方針](00_research_plan.md)、次に[研究ノート](research/notes.md)を読む。固定次数d≥5の一般型曲面の全平面退化について、actual KE計量の径の尺度の極限とLagrangian torus fibrationによる実現を研究する。正本はGitHubのmain、研究全体の入口は[research-hub](https://github.com/uedakazushi/research-hub)。

## 現行の解析結果

正確な三重点座標をζ0ζ1ζ2=t、ell_i=−log|ζ_i|²、L=−log|t|²、R=log Lとする。以下のactual結果は任意の固定次数d≥5について全phase・全三重点に一様であり、定数は固定次数と族に依存してよい。次数一様性は主張しない。

- **全深部三重点のtensor比較。** Complete simplex KE模型g_L^sfに対して、min ell_i≥mで全固定階の誤差O(1/m)。大域capped volume下界、内外simplex barriers、Yau Schwarz、Savin小摂動定理を用いる。全固定次数のweighted cap minorsとresidue規格化によるdensity下界を含めて証明し、三重点内には(TC)/(PBE)を仮定しない。正本は[full triple節](papers/sections/full_triple_comparison.tex)の `coarse:thm:full-triple-tensor`。
- **全閉cornerのGH収縮。** 三枚のunit squaresからなるC_Jに、その内部の経路で定める距離d_Jを入れる。全phaseを含むsoftmax hexagonの内在距離と、外側保護領域{min ell_i>R/2}内の全経路を許すprotected-ambient距離の双方で、R^−2 g_tのprojection distortionはO(log R/R)。Seamsと共通頂点も含む。正本は[closed corner節](papers/sections/closed_triple_metric.tex)の `simplex:thm:closed-corner-model` / `simplex:cor:actual-closed-corner-metric`。
- **境界の鋭い積漸近。** δ=(a+b)/Lなら二重cusp productへのmodel誤差はO(δ²)、actual誤差はO(1/min ell_i+δ²)。0<η<1/2の開正方形a,b∈[L^η/2,2L^(1−η)]ではO(L^−η)。Facetではb=ell_0、a=ell_1、d_*=min(a,L−a)としてcusp×finite-annulusへのmodel誤差O((b/d_*)^(2/3))、actualにはO(1/b)を加える。すべて全固定階・全角度の評価である。正本は[simplex境界節](papers/sections/simplex_boundary_geometry.tex)の `simplex:prop:dominant-product` / `simplex:cor:actual-dominant-product` / `simplex:prop:facet-product`。
- **正確な係数1とactive co-Gram。** 各iについて |d log ell_i|_{g_L^sf}≤1。ell_i≤Le^−Aのactive indicesが一つまたは二つならco-GramはId+O(e^(−A/2))、二つならO(e^−2A)。ActualにはO(1/min ell_i)を加える。正本は同節の `simplex:lem:rank-one-schwarz` / `simplex:cor:active-cogram`。

関連[Lagrangian主稿](https://github.com/uedakazushi/lagrangian-torus-fibration/blob/main/papers/lagrangian-torus-fibration.tex)の `ke:closed-corner-gh` / `ke:closed-corner-protected-gh` により、**同じactual Lagrangian torus bundleの同じ射影**が上記二つの距離についてGH近似となる。全fiberの非正規化intrinsic/ambient diameterはO(1/R)、正規化後はO(1/R²)、raw cubical mapとの誤差はO(log R/R)。継目でもfibersはregular T²である。開正方形の固定長方形Kη=[η,1−η]²でも、actual Lagrangian fibrationによる平坦長方形への内在GH収束とprojection distortion O(L^−η)を得ている。

## Source-free neckで得た接続の入力

[束座標とnormal moment](papers/sections/source_free_neck_coordinates.tex)では、固定compact base上の射影的法線束からexact uv=tと共通の正則S¹を構成した。Canonical primitiveを一つ固定でき、actual KE formの円平均η_tに対するmomentが加法定数なしに大域化する。固定した両endでは、周期1のmomentが±4π/(−log r²)を主項に持つ。Songの固定gauge収束とRochon–ZhangのSNC cusp漸近により、rを固定してからt→0とすればη_tの共通moment intervalを得る。全neckのMoser flow bufferはこの結果に含まれない。

関連Lagrangian稿の[二段階平均](https://github.com/uedakazushi/lagrangian-torus-fibration/blob/main/papers/sections/paper/ke_staged_neck_averaging.tex)は、normal circleを先に平均して、同じactual circleと全marked cycleの作用周期を保つ。指定primitive subgroupに適合するclosed-corner bundleにも同じO(log R/R)のGH評価を与え、一段階bundleとはHamiltonian mapで比較する。

[Neckの解析比較](papers/sections/source_free_neck_comparison.tex)では、無条件のbounded volume envelope、固定residual境界の非消失誤差、mixed termsを許すrank-one下界によるnormal circle長の評価を整理した。後者にはactual bufferが必要。Small log-densityを用いる比較背景はcoupled KE metricでもよく、source-freeという条件だけでproduct asymptoticsを結論しない。

## 残る核心と次の着手

閉cornerのd_JはC_J自身の距離であり、full complex C_dの他のcellsを経由する距離ではない。Protected-ambient距離も全曲面X_tの距離とは異なる。全X_tのshortcut、異なるtriple chartsとneckの接着、source・branch・coreを含む既存大域fibrationとの同定は未解決である。

次は**neck全体のnormal Moser flowの一様bufferと、複数のtriple endsの整合**を扱う。固定baseでの正則作用・primitive・moment intervalは得たので、residual方向のrank-one下界とactual bufferを独立に調べる。Triple overlapでは同じnormal actionとreduced foliationを合わせ、非定数holomorphic unitによるfull orbit partitionの変化を確認する。その後、sourceの正しいorientationでtensor・connector評価を進め、global no-shortcutとportal費用を検証する。

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

局所conic overlapの旧論証を明示的なprojective bundle変換で修復した。Source-free neckの座標・canonical moment・fixed-end評価と、二段階平均のexact periods・Hamiltonian比較の証明を独立に再読し、参照・labels・環境対応を静的確認した。回収稿の組版成功とは別に、**現行改訂はLuaLaTeX基本資産不足により未組版**である。`lualatex.fmt`・LuaTeX-ja等がなく、組版の試行は本文処理前に停止した。

再生成はルートで `latexmk`、PDF/SyncTeXの出力先は `build/`。[移行・検証範囲](research/migration.md)と[ソース対応](research/source-manifest.json)を参照する。通常のcommitとmainへのpushで保存し、研究成果の保存とresearch-hubの更新を別々に確認する。
