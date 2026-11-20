# 現行研究方針：一般型超曲面の負KE退化
2026-11-20 / v1.0

## 研究固有の目標
(X_t=\{\prod_{i=0}^{d-1}L_i+tF_d=0\}\) のような超平面和への退化で、KE距離をdiameterで正規化した**大域Gromov–Hausdorff極限と極限計量**を同定する。特に5平面へ退化する5次曲面のexplicit metric complexを最初の主例とする。既知の局所pointed collapseと大域diameter-scale theoremを混同しない。

## 既存原稿と状態
2026-08-21 v0.12、81頁の日本語論文草稿 `quintic_five_planes_KE_GH_paper_draft_ja_v12.tex` を核とする。候補のcubical complex
(mathcal C_5=\{w\in[0,1]^5:\max_iw_i=1,\ |\mathrm{supp}(w)|\le3\}\)
は25頂点、50辺、30枚のsquareという計算、および (mathrm{diam}(\mathcal C_5)=\sqrt{13}) の記録がある。モデル幾何の証明・有限次元certificateと、actual KE metricの一様gluing解析を区別する。

## 大域的主予想と必要な仮定
標準cubical length metricの (\mathcal C_5) へdiameter-rescaled GH収束するという主張は**現在も予想**である。主な欠落はglobal matching、neck/corner間の定量的なKE比較、nonlinear scale-channel correctionの (o(R_t)) 制御。古い論文草稿に強い表現があっても、条件付き結果を無条件の定理に格上げしない。

## 確認できる中間材料（草稿・計算に記録）
- triple intersectionの (ell_x+ell_y+ell_z=L_t+O(1)) とleading synchronization。
- neck sourceの (a_+-a_-=5) およびflux identity (5=2+3)。この5はcusp trivializationに相対的。
- Mandel reduced familyのlongitudinal zero modesはscale/asymmetry Jacobi方向。
- finite incidence network、twisted orientation local system、Calderón/scatteringの有限次元モデル。
- 剛性のあるtopological/cubical計算と、actual nonlinear KE estimateは区別する。

## 最優先課題
1. source scriptsを再実行し、証明に使うcertificate/入力のみ保持する。
2. actual neck-to-corner uniform parametrix とroot-0/root-1 filtered scale modulationの (o(R_t)) 評価を示す。
3. \(n,d\) 一般の超平面和退化へ一般化する前に、5次曲面でmetric glueの論理鎖を閉じる。
4. 外部文献 Zhang、Song–Sturm–Wang等の適用条件と論文の新規部分を一次資料で照合する。

## 正本と依存
- 主原稿：`papers/kaehler-einstein-degeneration.tex`。
- ノート：`research/notes.md`。
- 固定配置補空間のKE幾何は [multiscale-kaehler-einstein](https://github.com/uedakazushi/multiscale-kaehler-einstein) を参照するが、そこでのfixed-space estimatesから退化族の一様性を仮定しない。

## 共通研究原則・保存許可（研究固有の方針ではない）
数学的重要性・新規性・理解の深化・応用可能性・正確性・実現可能性を総合して研究方針を更新する。証明済み・追加仮定付き・未完成・予想・計算観察を区別する。先行研究は一次資料を確認し、重要な定理の仮定と寄与を明示する。日本語LuaLaTeXの主論文と現行ノートに有効な成果・十分な証明を残す。再現入力・コード・証明書を保持し、旧ZIP/ログ/中間生成物は正本にしない。研究の区切りで承諾不要の通常コミットを `main` にpushし、長時間では15〜30分を目安に保存する。force pushとActionsの追加/起動は禁止、並行変更・指定公開範囲を守る。Libraryの既存資料は削除せず、GitHub移行後の定常二重保存はしない。本repo保存後にresearch-hubの主要到達点・障害・次の一手・依存・再開先・実確認日を更新する。数学検証・組版・保存を別々に記録する。
