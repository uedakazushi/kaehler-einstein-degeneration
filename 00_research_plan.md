# 現行研究方針：一般型超曲面の負Kähler–Einstein退化
更新：2026-11-20 / 原資料全文移行

## 研究固有の目標
一般型超曲面の超平面和への退化とdiameter-scale GH極限を研究する。2026-08-31の五篇連作v1.0（旧三部作と退化二部作の再監査版）のPart IV–Vを回収し、短い再構成稿を全文TeXへ置換した。

## 論文と証明の状態
- `papers/kaehler-einstein-degeneration.tex`：Part IV、66頁（回収時）。Quintic coarse geometryと局所模型、source packing、固定次数d≥5の代数・残差package。Sharp co-Gramとmoving-window product exhaustionは(PBE)_d付き。
- `papers/cubical-gh-limit.tex`：Part V、34頁（回収時）。Abstract pruning–transportとdiam(C_5)=sqrt(13)は解析仮定と独立。Actual degree-d GH適用は(CP)_d+(PBE)_d付きであり、無条件のactual GH収束は未証明。
- 高次元ではmixed source–higher-stratum modelsの解析が残るためGH極限は予想。
- Fixed arrangement complement側Part I–IIIの正本は[multiscale-kaehler-einstein](https://github.com/uedakazushi/multiscale-kaehler-einstein)。固定空間の結果から族の一様性を自動的に導かない。

## 位相・人工計量とactual metricの区別
候補\(\mathcal C_d\)の一般次数のセル数・\(\operatorname{Sk}_2\Delta^{d-1}\)との同相・整数ホモロジーはPart Vに証明がある。Lagrangian分岐基底\(B_d(T)\)からのcell-like写像は\(d\ge6\)では同相でないが、人工PL長さ距離によるdistortionは\(d=5\)で\(\Theta(\varepsilon^2)\)、\(d\ge6\)で\(\Theta(\varepsilon)\)であり、GH距離には各々対応する上界がある。証明の正本はLagrangian repoの`topo:metric-collapse-sharp`。
Actual計量へ適用するには(N) global no-shortcut、(S) local square path lifts、(F) small fiber/portal connectorsを証明する必要があり、(F)は前二条件からは従わない（同repoの`topo:portal-counterexample`）。Part IV–Vの\((CP)_d+(PBE)_d\)は依然未証明。六次Petersen木系は6点の\(S_6\)軌道をなすが、これはrealized KE計量の対称性を決めない。

## Lagrangian fibrationとの接続
標準負KE尺度での四実次元非崩壊極限と、$R_t^{-2}g_t$ のcubical候補を区別する。Zhang (MRL, 2015)の局所torus collapse定理はQ-factorialなtoroidal全空間を仮定するため、我々のsource $xy=tz$ へ直接適用しない。主稿序論に先行比較を統合した。Part VのGH近似を我々のLagrangian fibrationのfiber収縮と同定するには、$\sup_x d_\square(\Phi_t(x),p_T\pi_t(x))\to0$ という追加の適合性が必要。関連Lagrangian主原稿の `topo:ke-map-compatibility` がその十分性を示すが、actual適合性は未証明である。

## 次の課題
1. (PBE)_dのquantitative terminal trivialization、protected rectangular inclusion、uniform comparison、two-metric escapeをactual metricsで証明する。
2. 一般次数の(CP)_dのcoarse realization/connectorsを監査する。
3. 旧v0.12全文は `papers/punctured-neck-scattering.tex` に保持した。元の配布ZIPから旧検算16本を回収し、配布時のSHA-256との一致と再実行を確認した。

## 保存・検証
全文TeXのSHA-256は `research/source-manifest.json`、元監査は `research/source-audit.md`。3原稿のLuaLaTeX組版と、統合稿5 scripts・旧v0.12の16 scriptsの再実行を行った。検査は有限組合せ・式・bookkeepingに限られ、未完成の解析証明を代替しない。詳細は `research/migration.md`。

現行のKE比較部分では、一次文献の仮定、写像比較命題の三角不等式による証明、追加引用と参照先を点検した。Actual GH収束・fibrationとの一様適合性の解析証明は未完成。現環境では `lualatex.fmt`・LuaTeX-ja等の基本資産がなく、LuaLaTeX組版の試行は本文処理前に停止した。回収時の組版成功と現行改訂の未組版を区別する。

## 共通研究原則と保存許可（研究固有方針から独立）
数学的重要性・新規性・理解の深化・応用可能性・正確性・実現可能性を総合して方針を更新する。証明済み・仮定付き・未完成・予想・計算観察、既知結果と独自結果、草稿の証明と今回の監査を区別する。重要文献は一次資料の正確な定理と仮定を確認する。日本語LuaLaTeXで公表原稿と十分な証明を保持し、有効なアイデア・反例・計算は現行ノートに統合する。再現コード・証明書・入力を残すが旧版/中間出力は蓄積しない。区切りごと承諾なしに通常コミットで `main` へpush、15–30分を目安に切り良く保存する。force pushとGitHub Actions追加/起動はしない。Library旧資料は削除しないがGitHub移行後は定常二重保存しない。先に対象repoへ保存してからresearch-hubを更新し、数学検証・組版・GitHub・hubを別々に確認する。
