# 原資料の移行と検証

2026-11-20。Libraryの `Multiscale_KE_Geometry_I-V_ja_v1_source_and_pdfs.zip`（2026-08-31）を取得した。これは旧配置補空間三部作と旧退化二部作を再監査・統合した五篇連作である。元資料のREADME・数学的監査と本文の仮定を照合し、短い再構成稿を全文のTeXへ置換した。旧稿への誤り訂正・条件付き化を引き継ぐ。元Libraryファイルは削除していない。

ソースの対応、バイト数、SHA-256は `source-manifest.json`。五篇統合稿のTeX本文は移行時に元ファイルとのバイト一致を確認した。その後の一般次数の位相命題追加やビルド設定の修正を施した現行ファイルでは、`source-manifest.json` の `source_sha256` が元資料、`sha256`・`bytes`・`current_blob_sha` が記載した確認日の本文を表す。2026-11-23に現行destinationの値を更新し、元の `source_sha256` は保持した。分割TeXと組版PDFの現行hashは `validation.json` に置く。旧v0.12全文も回収し、元manifestとSHA-256が一致することを確認。upLaTeX固有のclass・font・hyperref設定をLuaLaTeXへ変更し、現行の条件付き化を冒頭に明記した。全数学本文は保持する（papers/punctured-neck-scattering.tex、今回92頁）。Part I–IIIと総説の正本はmultiscale-kaehler-einstein、Part IV–Vと五つの補助スクリプトの正本はkaehler-einstein-degeneration。元の統合PDFと旧版ZIPはGitへ重複保存しない。新しい定理の証明や文献の再監査を今回実施したことを意味しない。

## 組版

リポジトリルートから `latexmk`。LuaLaTeX、PDF/SyncTeXはbuild/に出力する。今回TeX Live 2026で実行。フォントキャッシュが書込不可の環境では、書込可能なTEXMFCACHE・TEXMFVARを指定する。最終頁数・参照と引用・警告の確認結果は検証結果に記す。VS Code UIの検証は実施していない。

## 完全移行の範囲

統合版全文と旧v0.12本文・検算16本を移行した。Libraryの全履歴と旧版固有内容の網羅的照合は未了。Post-trilogy noteの正本は配置補空間repo。

## 計算の再実行

`scripts/run_checks.py`が元scriptsをbuild/certificate-runs/へコピーして実行する。PythonのNumPy、SymPy、mpmath、SciPyが必要。統合稿5本・旧v0.12の16本は全てexit 0、出力にFAIL・AssertionErrorはなし。有限gallery、25,000点のcomplete-window診断、20,000点のframe-shear診断等と、解析証明を区別する。詳細はresearch/validation.json。今回の再実行結果と、原bundleに付属したcertificates/の記録は異なる。

## v0.12配布ZIPとの照合

元チャット「5平面への退化1」の `quintic_five_planes_KE_note_v12_bundle.zip` を取得した。ZIP内の元一覧と別途取得済みの一覧にある16本のSHA-256が一致し、コード本体もすべて一致した。未回収だった5本を追加し、cusp-indicialとsemistable-resolutionを配布時の版に差し替えた。原版コードはバイト単位で保持した。mesh-orbit検査は既定の分母12で実行した。

今回の全主原稿の最終logに未解決参照・引用とoverfull/underfull boxはなし。各原稿の冒頭・中間・末尾を描画して確認した。全頁の目視監査は未実施。フォント置換・scale・PDF bookmarkの数式警告は残る。VS Codeは主原稿だけをroot候補とする設定を検査したがUI操作は未検証。

## 旧v0.21との照合

配布ZIPの前付けには、強いdepth-map予想と、SFEC・LRP・sharp neck packageによる還元経路の整理がある。第IV・V篇の(CP)・(PBE)による定式化や、旧v0.12のpunctured-neck計算とは別の研究素材として、`papers/source-free-comparison.tex` に収録した。旧稿の含意には現行稿に対する追加の証明保証を与えない。LuaLaTeXで11頁を生成し、未解決の参照・引用とoverfull boxがないことを確認した。このZIPのv0.19詳細本文はPDF収録で、対応する元TeXと現行稿の補題単位の照合は残る。
