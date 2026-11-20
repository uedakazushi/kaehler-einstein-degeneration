# Kähler–Einstein degeneration

2026-08-31五篇連作の退化二部作を、元の全文TeXから移行した。

- [Part IV：局所模型](papers/kaehler-einstein-degeneration.tex)：66頁（回収時）。五次のcoarse metric packageは(TC)_5付き。Sharp co-Gramは粗い比較に加えて(PBE)_d付き。
- [Part V：cubical GH](papers/cubical-gh-limit.tex)：34頁。Actual GH適用は(CP)_d+(PBE)_d付き。
- [Punctured-neck技術稿](papers/punctured-neck-scattering.tex)：旧81頁の証明全文をLuaLaTeXへ移植（92頁）。現行の条件付き化を冒頭に明記。
- [Source-free比較の研究ノート](papers/source-free-comparison.tex)（旧v0.21前付け）
- [補助検算](scripts/)：統合稿5本と旧v0.12の16本を再実行し、全件成功。旧16本は配布時のSHA-256と一致。有限計算・式の診断であり解析証明の代用ではない。

頁数は回収稿の記録。現行KE比較の改訂は、環境のLuaLaTeX基本資産不足により未組版。

**解析上の訂正と次の入力（2026-11-20 / v1.3）：** [Part IV](papers/kaehler-einstein-degeneration.tex)に、bounded volume densityだけでは滑らかな負KE計量の一様tensor比較が従わない反例と証明を収録した。Exteriorsの比較には独立な(TC)_5を置き、依存するcoarse距離・connectors・source径・CP5も条件付きとした。修復の十分条件はactual metric ballの一様bufferとlocalized Chern–Luであり、対象familyでの検証は未完成。有限cubical計量の結果と、明示的なCP+PBEの下でのPart Vの抽象推論は保持する。

**現行の数学的到達点：** [Part V](papers/cubical-gh-limit.tex)に一般次数のcubical複体の位相・整数ホモロジーを証明。Lagrangian分岐基底からの人工PL計量収縮は次数5で $O(\varepsilon^2)$、次数6以上で $O(\varepsilon)$（厳密な証明の正本はLagrangian repo）。実際のKE計量に応用するには、no-shortcut、各squareのlift、分岐fiber/portal connectorに相当する定量条件が必要。(CP)$_d$+(PBE)$_d$は未証明であり、actual GH収束を確定させたわけではない。

**Lagrangian fibrationとの関係：** 曲面全体の径の尺度のGH収束と、特定のfibrationのfiber収縮による実現は別の主張。[Part V](papers/cubical-gh-limit.tex)に近似写像の適合性条件を追加し、関連Lagrangian原稿へ証明を参照した。標準負KE尺度の非崩壊極限、Zhangの局所collapse定理とsource $xy=tz$ における適用障害は[研究ノート](research/notes.md)に整理。関連Lagrangian主稿の定量的averaging–Moserにより、三重点のfull-orbit moving tensor比較から局所fibrationと小さいambient fibersを構成できる。Actual適合性の大域化も解析仮定も未証明。

最初に[研究方針](00_research_plan.md)、次に[研究ノート](research/notes.md)。[移行・検証範囲](research/migration.md)と[ソース対応](research/source-manifest.json)を参照する。

ルートで `latexmk`。PDF/SyncTeXはbuild/、正本はmain。[research-hub](https://github.com/uedakazushi/research-hub)。
