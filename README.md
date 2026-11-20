# Kähler–Einstein degeneration

2026-08-31五篇連作の退化二部作を、元の全文TeXから移行した。

- [Part IV：局所模型](papers/kaehler-einstein-degeneration.tex)：66頁（回収時）。五次のcoarse metric packageは(TC)_5付き。Sharp co-Gramは粗い比較に加えて(PBE)_d付き。
- [Part V：cubical GH](papers/cubical-gh-limit.tex)：34頁。Actual GH適用は(CP)_d+(PBE)_d付き。
- [Punctured-neck技術稿](papers/punctured-neck-scattering.tex)：旧81頁の証明全文をLuaLaTeXへ移植（92頁）。現行の条件付き化を冒頭に明記。
- [Source-free比較の研究ノート](papers/source-free-comparison.tex)（旧v0.21前付け）
- [補助検算](scripts/)：統合稿5本と旧v0.12の16本を再実行し、全件成功。旧16本は配布時のSHA-256と一致。有限計算・式の診断であり解析証明の代用ではない。

頁数は回収稿の記録。現行KE比較の改訂は、環境のLuaLaTeX基本資産不足により未組版。

**actual KEについての新しい局所結果（2026-11-20 / v1.4）：** [Part IV](papers/kaehler-einstein-degeneration.tex)の `coarse:cor:open-square-tensor` は、開正方形の固定compact部分でproduct-cusp漸近を全位相・全固定階で証明する。Shifted-sinh/complete-annulusのvolume barriersとSavinの定理を用い、(TC)_5や(PBE)_5を仮定しない。関連Lagrangian主稿 `ke:open-cell-collapse` により、この領域でactual KE–Lagrangian fibersと、内在距離での平坦長方形へのGH collapseを得た。

**残る解析条件：** 全閉triple領域・sourceを含むcoarse metric packageの(TC)_5と、大域のCP+PBEは未検証。Bounded densityだけではtensor比較が従わない反例を保持する。三重点の任意半径product窓の誤りは小さい相対窓へ修正し、sourceのtensor仮定は点で有効なorientationへ限定した。領域外のshortcutとsingular fibersの接着は局所GH結果から独立。

**現行の数学的到達点：** [Part V](papers/cubical-gh-limit.tex)に一般次数のcubical複体の位相・整数ホモロジーを証明。Lagrangian分岐基底からの人工PL計量収縮は次数5で $O(\varepsilon^2)$、次数6以上で $O(\varepsilon)$（厳密な証明の正本はLagrangian repo）。実際のKE計量に応用するには、no-shortcut、各squareのlift、分岐fiber/portal connectorに相当する定量条件が必要。(CP)$_d$+(PBE)$_d$は未証明であり、actual GH収束を確定させたわけではない。

**Lagrangian fibrationとの関係：** 曲面全体の径の尺度のGH収束と、特定のfibrationのfiber収縮による実現は別の主張。[Part V](papers/cubical-gh-limit.tex)に近似写像の適合性条件を追加し、関連Lagrangian原稿へ証明を参照した。標準負KE尺度の非崩壊極限、Zhangの局所collapse定理とsource $xy=tz$ における適用障害は[研究ノート](research/notes.md)に整理。関連Lagrangian主稿の定量的averaging–Moserにより、三重点のfull-orbit moving tensor比較から局所fibrationと小さいambient fibersを構成できる。開正方形では解析比較を証明済みだが、全閉cornerへの延長とactual適合性の大域化は未証明。

最初に[研究方針](00_research_plan.md)、次に[研究ノート](research/notes.md)。[移行・検証範囲](research/migration.md)と[ソース対応](research/source-manifest.json)を参照する。

ルートで `latexmk`。PDF/SyncTeXはbuild/、正本はmain。[research-hub](https://github.com/uedakazushi/research-hub)。
