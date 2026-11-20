# 原資料の移行と検証

2026-11-20。Libraryの `Multiscale_KE_Geometry_I-V_ja_v1_source_and_pdfs.zip`（2026-08-31）を取得した。これは旧配置補空間三部作と旧退化二部作を再監査・統合した五篇連作である。元資料のREADME・数学的監査と本文の仮定を照合し、短い再構成稿を全文のTeXへ置換した。旧稿への誤り訂正・条件付き化を引き継ぐ。元Libraryファイルは削除していない。

ソースの対応、バイト数、SHA-256は `source-manifest.json`。五篇統合稿のTeX本文は元ファイルからバイト単位で保持し、ファイル名のみ変更した。旧v0.12全文も回収し、元manifestとSHA-256が一致することを確認。upLaTeX固有のclass・font・hyperref設定をLuaLaTeXへ変更し、現行の条件付き化を冒頭に明記した。全数学本文は保持する（papers/punctured-neck-scattering.tex、今回92頁）。Part I–IIIと総説の正本はmultiscale-kaehler-einstein、Part IV–Vと五つの補助スクリプトの正本はkaehler-einstein-degeneration。元の統合PDFと旧版ZIPはGitへ重複保存しない。新しい定理の証明や文献の再監査を今回実施したことを意味しない。

## 組版

リポジトリルートから `latexmk`。LuaLaTeX、PDF/SyncTeXはbuild/に出力する。今回TeX Live 2026で実行。フォントキャッシュが書込不可の環境では、書込可能なTEXMFCACHE・TEXMFVARを指定する。最終頁数・参照と引用・警告の確認結果は検証結果に記す。VS Code UIの検証は実施していない。

## 完全移行の範囲

本記録は取得できた統合版の全文移行を示す。Libraryの全履歴・全旧稿だけに残る内容の網羅的照合は未了。旧v0.12の16 scripts中11本を回収した。9本は元manifestのSHA-256と一致し、cusp_indicial_parametrix_certificate.pyとsemistable_resolution_certificate.pyは異なる取得版である。元と同一版とは報告しない。統合版の五つの検査で旧16本全てを代替したとは扱わない。Post-trilogy noteの正本は配置補空間repo。旧資料の独自内容を回収する作業と、現行稿の数学的な未解決問題は別である。

## 計算の再実行

`scripts/run_checks.py`が元scriptsをbuild/certificate-runs/へコピーして実行する。Pythonのsympy、mpmath、scipyが必要。統合稿5本・旧neck関連11本は全てexit 0、出力にFAIL・AssertionErrorはなし。有限gallery、25,000点のcomplete-window診断、20,000点のframe-shear診断等と、解析証明を区別する。詳細はresearch/validation.json。今回の再実行結果と、原bundleに付属したcertificates/の記録は異なる。

## 残る旧資産

未回収：cubical_diameter_orbit_certificate.py、node_weight_identity_certificate.py、ordered_resolution_chamber_certificate.py、punctured_neck_charge_certificate.py、vertical_twist_tradeoff_certificate.py。Source-manifestに全リストと既知の元hashを記録する。Library検索は一部読み込み失敗を報告し、chargeの再試行も同じ状態だったため、ファイル不存在とは断定しない。旧mesh-orbit検査をexact gallery検査の代わりに実行したとは扱わない。

今回の全主原稿の最終logに未解決参照・引用とoverfull/underfull boxはなし。各原稿の冒頭・中間・末尾を描画して確認した。全頁の目視監査は未実施。フォント置換・scale・PDF bookmarkの数式警告は残る。VS Codeは主原稿だけをroot候補とする設定を検査したがUI操作は未検証。
