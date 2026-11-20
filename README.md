# Kähler–Einstein degeneration

2026-08-31五篇連作の退化二部作を、元の全文TeXから移行した。

- [Part IV：局所模型](papers/kaehler-einstein-degeneration.tex)：66頁。Sharp co-Gramは(PBE)_d付き。
- [Part V：cubical GH](papers/cubical-gh-limit.tex)：34頁。Actual GH適用は(CP)_d+(PBE)_d付き。
- [Punctured-neck技術稿](papers/punctured-neck-scattering.tex)：旧81頁の証明全文をLuaLaTeXへ移植（92頁）。現行の条件付き化を冒頭に明記。
- [Source-free比較の研究ノート](papers/source-free-comparison.tex)（旧v0.21前付け）
- [補助検算](scripts/)：統合稿5本と旧v0.12の16本を再実行し、全件成功。旧16本は配布時のSHA-256と一致。有限計算・式の診断であり解析証明の代用ではない。

**現在の独立検証：** [Part V](papers/cubical-gh-limit.tex) に候補C_dの一般次数のセル数・整数ホモロジーと、Lagrangian分岐基底B_d(T)との位相比較を記載。人工的な区分的長さ計量ではGromov–Hausdorff誤差O(ε)の収縮定理がある（証明はLagrangian repo）。actual KE計量の収束は依然(CP)_d+(PBE)_dの未解決解析入力に依存。

最初に[研究方針](00_research_plan.md)、次に[研究ノート](research/notes.md)。[移行・検証範囲](research/migration.md)と[ソース対応](research/source-manifest.json)を参照する。

ルートで `latexmk`。PDF/SyncTeXはbuild/、正本はmain。[research-hub](https://github.com/uedakazushi/research-hub)。
