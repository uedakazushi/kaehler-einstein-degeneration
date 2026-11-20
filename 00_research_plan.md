# 現行研究方針：一般型超曲面の負Kähler–Einstein退化
更新：2026-11-20 / v1.4・現行研究方針

## 研究固有の目標
一般型超曲面の超平面和への退化とdiameter-scale GH極限を研究する。2026-08-31の五篇連作v1.0（旧三部作と退化二部作の再監査版）のPart IV–Vを回収し、短い再構成稿を全文TeXへ置換した。

## 論文と証明の状態
- `papers/kaehler-einstein-degeneration.tex`：Part IV、66頁（回収時）。局所模型、source packing、固定次数d≥5の代数・残差package。Quintic coarse metric geometryは独立な(TC)_5付き。Sharp co-Gramは粗い比較に加えて(PBE)_d付き。Bounded-densityからtensor比較を導く一般的推論は反例により排除した。
- `papers/cubical-gh-limit.tex`：Part V、34頁（回収時）。Abstract pruning–transportとdiam(C_5)=sqrt(13)は解析仮定と独立。Actual degree-d GH適用は(CP)_d+(PBE)_d付きであり、無条件のactual GH収束は未証明。
- 高次元ではmixed source–higher-stratum modelsの解析が残るためGH極限は予想。
- Fixed arrangement complement側Part I–IIIの正本は[multiscale-kaehler-einstein](https://github.com/uedakazushi/multiscale-kaehler-einstein)。固定空間の結果から族の一様性を自動的に導かない。

## 開正方形内部の actual KE 比較と局所collapse
五次族について、主稿 `coarse:thm:moving-triple-tensor` / `coarse:cor:open-square-tensor` に新しい証明を置いた。正確な三重点座標 ζ0ζ1ζ2=t、L=−log|t|²、R=log L、独立深度 a,b とし、0<η<1/2 を固定する。a,b∈[L^η/2,2L^(1−η)] 上で actual g_t は二つの cusp の積 h_prod に全固定階で O(L^(−η/4)) 近づく。全角度について一様であり、(TC)_5、(PBE)_5、actual metric buffer を仮定しない。依存する大域入力は既存の capped volume 下界 `coarse:cor:global-volume-lower` である。

証明は、三重点内の expanding product annuli、shifted-sinh 型の負KE下barrier、finite complete annuli の上barrierから volume ratio→1 を得て、Savin (2007), Theorem 1.3 の small-perturbation regularity を適用する。bounded densityだけの旧推論とは異なり、small C0 potential が入力である。明示式・境界比較・Savinの仮定・Schauderによる誤差率を今回点検した。新規性の網羅的確認は未完了。

関連 Lagrangian 主稿 `ke:open-cell-collapse` により、各開正方形の固定長方形 Kη=[η,1−η]² 上に actual KE–Lagrangian torus fibration を構成できる。Fiberのintrinsic/ambient diameterは O(L^(−η))、raw cubical mapとの値の誤差は O(1/R)。Moser像領域に内在距離を入れれば R^−2 g_t のGH極限は平坦な Kη であり、projection distortion は O(L^(−η/4)+L^(−η)/R)。領域外のshortcutを許すambient距離、大域fibrationとの接着、singular fibersは未解決。

## 局所windowと残るtensor仮定
三つの深度が同程度のとき、一つの独立二座標product windowで任意半径のconstrained-cusp ballを覆うことはできない（`coarse:prop:triple-product-obstruction`）。最大深度を従属座標にする小さい相対箱は有効であり、全deep triple上のvolume上下界とbounded potentialは `coarse:cor:triple-volume-comparison` で証明する。これだけではfull tripleのtensor比較は得られない。

Source gateのfixed model ballはoriented half-armを越える。Full source-coordinate extension上でdensity比較を行い、(TC)_5は**その点で有効なorientation**のmodelに対する下界として定式化する。全ての拡大窓で同じmodelのtensor比較を要求しない。任意半径のexhaustionはcoarse小窓構成の結論に含めず、dominant tripleでの証明と一般の(PBE)_dを分ける。

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
1. 最優先は開正方形で得たbarrier–Savin法をclosed triple cornerへ広げること。三角形tube上のcomplete toric KE metricを背景にし、facetsを内外へ平行移動した領域のKE metricsで挟む方法を検討する。存在・一意性・uniform cusp geometry・facet-shiftの評価をそれぞれ一次資料または直接証明で確定する。
2. 各open-cellの局所fibrationをmultiple-max facesとsupport-drop facesへ延長し、overlapのrelative Moser、source・branch・coreへの接着を進める。全曲面のno-shortcutとconnector径は局所内在GH定理から分離して証明する。
3. (PBE)_dのquantitative terminal trivialization、protected rectangular inclusion、uniform comparison、two-metric escapeをactual metricsで証明し、一般次数の(CP)_dのconnectorsを監査する。

## 保存・検証
全文TeXのSHA-256は `research/source-manifest.json`、元監査は `research/source-audit.md`。3原稿のLuaLaTeX組版と、統合稿5 scripts・旧v0.12の16 scriptsの再実行を行った。検査は有限組合せ・式・bookkeepingに限られ、未完成の解析証明を代替しない。詳細は `research/migration.md`。

現行の解析監査では、expanding product domains、shifted-sinh barriers、Savinの原典のH1/H2/H4とTheorem 1.3、局所MoserのC1評価とGH distortionを点検した。またbounded-density推論のcutoffの欠落、明示的な負KE弱解と滑らかなDirichlet近似による反例、その依存先を点検した。GuanのDirichlet存在定理とBedford–Taylorの比較・pluripolar massの一次資料を確認した。Actual GH収束・fibrationとの一様適合性の解析証明は未完成。現環境では `lualatex.fmt`・LuaTeX-ja等の基本資産がなく、LuaLaTeX組版の試行は本文処理前に停止した。回収時の組版成功と現行改訂の未組版を区別する。

## 共通研究原則と保存許可（研究固有方針から独立）
数学的重要性・新規性・理解の深化・応用可能性・正確性・実現可能性を総合して方針を更新する。証明済み・仮定付き・未完成・予想・計算観察、既知結果と独自結果、草稿の証明と今回の監査を区別する。重要文献は一次資料の正確な定理と仮定を確認する。日本語LuaLaTeXで公表原稿と十分な証明を保持し、有効なアイデア・反例・計算は現行ノートに統合する。再現コード・証明書・入力を残すが旧版/中間出力は蓄積しない。区切りごと承諾なしに通常コミットで `main` へpush、15–30分を目安に切り良く保存する。force pushとGitHub Actions追加/起動はしない。Library旧資料は削除しないがGitHub移行後は定常二重保存しない。先に対象repoへ保存してからresearch-hubを更新し、数学検証・組版・GitHub・hubを別々に確認する。
