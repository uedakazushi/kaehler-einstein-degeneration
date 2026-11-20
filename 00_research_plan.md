# 現行研究方針：一般型超曲面の負Kähler–Einstein退化
更新：2026-11-20 / 原資料全文移行

## 研究固有の目標
一般型超曲面の超平面和への退化とdiameter-scale GH極限を研究する。2026-08-31の五篇連作v1.0（旧三部作と退化二部作の再監査版）のPart IV–Vを回収し、短い再構成稿を全文TeXへ置換した。

## 論文と証明の状態
- `papers/kaehler-einstein-degeneration.tex`：Part IV、66頁。Quintic coarse geometryと局所模型、source packing、固定次数d≥5の代数・残差package。Sharp co-Gramとmoving-window product exhaustionは(PBE)_d付き。
- `papers/cubical-gh-limit.tex`：Part V、34頁。Abstract pruning–transportとdiam(C_5)=sqrt(13)は解析仮定と独立。Actual degree-d GH適用は(CP)_d+(PBE)_d付きであり、無条件のactual GH収束は未証明。
- 高次元ではmixed source–higher-stratum modelsの解析が残るためGH極限は予想。
- Fixed arrangement complement側Part I–IIIの正本は[multiscale-kaehler-einstein](https://github.com/uedakazushi/multiscale-kaehler-einstein)。固定空間の結果から族の一様性を自動的に導かない。

## 候補基底の位相と計量的可能性
Part V主稿には任意のd≥5についてC_dのセル数・Sk_2 Δ^{d-1}との同相・整数ホモロジーの一般次数証明がある。Lagrangianの分岐基底B_d(T)とはcell-like homotopy equivalenceで結ばれる。d≥6では非同相であるが、人工的に定めたpiecewise length metrics d_epsilonについて sup|d_epsilon-d_square∘p_T|≤C epsilon と d_GH≤C epsilon/2 を証明した（厳密な証明はlagrangian-torus-fibrationのbase_topology.tex、ここでは帰結と参照のみを記載）。これらはrealized KE metricのGH収束もLagrangianの作用計量の収束も保証しない。実際の解析課題は依然(CP)_d+(PBE)_dの確立である。独立の有限鎖階数検算はd=5,6,7,8で実施済み。

## 次の課題
1. (PBE)_dのquantitative terminal trivialization、protected rectangular inclusion、uniform comparison、two-metric escapeをactual metricsで証明する。
2. 一般次数の(CP)_dのcoarse realization/connectorsを監査する。
3. 旧v0.12全文は `papers/punctured-neck-scattering.tex` に保持した。元の配布ZIPから旧検算16本を回収し、配布時のSHA-256との一致と再実行を確認した。

## 保存・検証
全文TeXのSHA-256は `research/source-manifest.json`、元監査は `research/source-audit.md`。3原稿のLuaLaTeX組版と、統合稿5 scripts・旧v0.12の16 scriptsの再実行を行った。検査は有限組合せ・式・bookkeepingに限られ、未完成の解析証明を代替しない。詳細は `research/migration.md`。

## 共通研究原則と保存許可（研究固有方針から独立）
数学的重要性・新規性・理解の深化・応用可能性・正確性・実現可能性を総合して方針を更新する。証明済み・仮定付き・未完成・予想・計算観察、既知結果と独自結果、草稿の証明と今回の監査を区別する。重要文献は一次資料の正確な定理と仮定を確認する。日本語LuaLaTeXで公表原稿と十分な証明を保持し、有効なアイデア・反例・計算は現行ノートに統合する。再現コード・証明書・入力を残すが旧版/中間出力は蓄積しない。区切りごと承諾なしに通常コミットで `main` へpush、15–30分を目安に切り良く保存する。force pushとGitHub Actions追加/起動はしない。Library旧資料は削除しないがGitHub移行後は定常二重保存しない。先に対象repoへ保存してからresearch-hubを更新し、数学検証・組版・GitHub・hubを別々に確認する。
