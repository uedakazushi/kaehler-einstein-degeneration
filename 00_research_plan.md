# 現行研究方針：一般型超曲面の負Kähler–Einstein退化
更新：2026-11-20 / v1.3・現行研究方針

## 研究固有の目標
一般型超曲面の超平面和への退化とdiameter-scale GH極限を研究する。2026-08-31の五篇連作v1.0（旧三部作と退化二部作の再監査版）のPart IV–Vを回収し、短い再構成稿を全文TeXへ置換した。

## 論文と証明の状態
- `papers/kaehler-einstein-degeneration.tex`：Part IV、66頁（回収時）。局所模型、source packing、固定次数d≥5の代数・残差package。Quintic coarse metric geometryは独立な(TC)_5付き。Sharp co-Gramは粗い比較に加えて(PBE)_d付き。Bounded-densityからtensor比較を導く一般的推論は反例により排除した。
- `papers/cubical-gh-limit.tex`：Part V、34頁（回収時）。Abstract pruning–transportとdiam(C_5)=sqrt(13)は解析仮定と独立。Actual degree-d GH適用は(CP)_d+(PBE)_d付きであり、無条件のactual GH収束は未証明。
- 高次元ではmixed source–higher-stratum modelsの解析が残るためGH極限は予想。
- Fixed arrangement complement側Part I–IIIの正本は[multiscale-kaehler-einstein](https://github.com/uedakazushi/multiscale-kaehler-einstein)。固定空間の結果から族の一様性を自動的に導かない。

## 体積密度とtensor比較：現行の解析条件
主稿 `coarse:prop:density-counterexample` は、固定ball上で滑らかな負KE計量列の体積密度が正に一様有界でも、内側ballでtensorが一様有界とは限らないことを証明する。したがってvolume lower/upper estimatesだけを用いた局所tensor比較は使えない。

五次のexterior comparisonには独立な仮定 $(\mathrm{TC})_5$（`coarse:hyp:TC5`）を置く。これに依存するraw submetry、actual connectors、source diameter、粗い距離二側比較、$(\mathrm{CP})_5$ の検証も条件付きである。Raw coordinatesの代数的構成、閉セルの実現、determinant/volume評価、actual metric ballsを用いたsource inradius/escapeの議論、抽象有限距離論は、このtensor比較の推論から分離する。旧来の全証明を今回独立監査したことにはしない。

修復の具体的な十分条件は、各点にactual metric ballが入る一様bufferと、そこから負のholomorphic sectional curvatureを持つcomplete productへの正則写像である。`coarse:lem:actual-buffer-comparison` によりlocalized Chern–Luから一方向の比較を得て、volume upper boundと合わせる。Model metricでのbufferだけではactual bufferを証明したことにならず、欲しいcoarse distanceを先に使う循環を避ける。

## 位相・人工計量とactual metricの区別
候補\(\mathcal C_d\)の一般次数のセル数・\(\operatorname{Sk}_2\Delta^{d-1}\)との同相・整数ホモロジーはPart Vに証明がある。Lagrangian分岐基底\(B_d(T)\)からのcell-like写像は\(d\ge6\)では同相でないが、人工PL長さ距離によるdistortionは\(d=5\)で\(\Theta(\varepsilon^2)\)、\(d\ge6\)で\(\Theta(\varepsilon)\)であり、GH距離には各々対応する上界がある。証明の正本はLagrangian repoの`topo:metric-collapse-sharp`。
Actual計量へ適用するには(N) global no-shortcut、(S) local square path lifts、(F) small fiber/portal connectorsを証明する必要があり、(F)は前二条件からは従わない（同repoの`topo:portal-counterexample`）。Part IV–Vの\((CP)_d+(PBE)_d\)は依然未証明。六次Petersen木系は6点の\(S_6\)軌道をなすが、これはrealized KE計量の対称性を決めない。

## Lagrangian fibrationとの接続
標準負KE尺度での四実次元非崩壊極限と、$R_t^{-2}g_t$ のcubical候補を区別する。Zhang (MRL, 2015)の局所torus collapse定理はQ-factorialなtoroidal全空間を仮定するため、我々のsource $xy=tz$ へ直接適用しない。主稿序論に先行比較を統合した。Part VのGH近似を我々のLagrangian fibrationのfiber収縮と同定するには、$\sup_x d_\square(\Phi_t(x),p_T\pi_t(x))\to0$ という追加の適合性が必要。関連Lagrangian主原稿の `topo:ke-map-compatibility` がその十分性を示すが、actual適合性は未証明である。

## 次の課題
1. 最優先は(TC)_5の非循環な検証。Complete productへの写像が定義される外側windowに、半径が一様に正のactual metric ballが含まれることを示し、localized Chern–Luとvolume upper boundを適用する。Densityの上下界だけで置き換えない。
2. 三重点の全phaseを含むmoving領域で同様のtensor比較を得て、関連Lagrangian主稿 `ke:triple-moving-fibration` の局所fibrationへ適用する。固定simplex compactaの局所収束はcubical vertexしか見ないため、境界へ動く領域の制御を別に行う。
3. (PBE)_dのquantitative terminal trivialization、protected rectangular inclusion、uniform comparison、two-metric escapeをactual metricsで証明し、一般次数の(CP)_dのconnectorsを監査する。

## 保存・検証
全文TeXのSHA-256は `research/source-manifest.json`、元監査は `research/source-audit.md`。3原稿のLuaLaTeX組版と、統合稿5 scripts・旧v0.12の16 scriptsの再実行を行った。検査は有限組合せ・式・bookkeepingに限られ、未完成の解析証明を代替しない。詳細は `research/migration.md`。

現行の解析監査では、bounded-density推論のcutoffの欠落、明示的な負KE弱解と滑らかなDirichlet近似による反例、その依存先を点検した。GuanのDirichlet存在定理とBedford–Taylorの比較・pluripolar massの一次資料を確認した。Actual GH収束・fibrationとの一様適合性の解析証明は未完成。現環境では `lualatex.fmt`・LuaTeX-ja等の基本資産がなく、LuaLaTeX組版の試行は本文処理前に停止した。回収時の組版成功と現行改訂の未組版を区別する。

## 共通研究原則と保存許可（研究固有方針から独立）
数学的重要性・新規性・理解の深化・応用可能性・正確性・実現可能性を総合して方針を更新する。証明済み・仮定付き・未完成・予想・計算観察、既知結果と独自結果、草稿の証明と今回の監査を区別する。重要文献は一次資料の正確な定理と仮定を確認する。日本語LuaLaTeXで公表原稿と十分な証明を保持し、有効なアイデア・反例・計算は現行ノートに統合する。再現コード・証明書・入力を残すが旧版/中間出力は蓄積しない。区切りごと承諾なしに通常コミットで `main` へpush、15–30分を目安に切り良く保存する。force pushとGitHub Actions追加/起動はしない。Library旧資料は削除しないがGitHub移行後は定常二重保存しない。先に対象repoへ保存してからresearch-hubを更新し、数学検証・組版・GitHub・hubを別々に確認する。
