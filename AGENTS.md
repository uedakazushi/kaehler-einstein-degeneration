# kaehler-einstein-degeneration — 研究・保存指示
2026-11-23 / v1.11（研究資料v1.30、Part IV v1.17・Part V v1.10）

## 公表計画の実行

- 最上位の目的は数学的価値の最大化。現在の公表計画と担当作業は `00_research_plan.md` 冒頭に置く。中心結果の正確性・新規性・読者の検証可能性を優先し、既存の論文順や任意保持集合へのatlas拡張・条件付き解析packageの完成を他の成果の公表条件にしない。
- 計画をmainへ保存した後、証明・先行研究比較・原稿整理を実行し、実際の点検範囲と残る課題を現行資料へ反映する。計画を書いただけで研究完了とはしない。

## 入口と正本
- 研究全体の入口は https://github.com/uedakazushi/research-hub 。再開時はhubの該当項目を確認し、最初にこのrepoの `00_research_plan.md`、次に本書、`research/notes.md` と必要な原稿を読む。
- 本研究の現行資料の正本はGitHub `main`。主たる公表用原稿は `papers/kaehler-einstein-degeneration.tex`（本文のある主原稿）であり、節分割可。独立論文は記述的な別名を付け、READMEと研究方針に役割を明記する。
- 一般原則と研究固有の目標を区別する。研究で使う文献、証明、再現入力の正本は当該repoに置く。

## 研究の方針と確実性
1. 数学的重要性・新規性・理解の深化・応用可能性・正確性・実現可能性を総合し、目的と方針を柔軟に修正する。履歴を積み増す代わりに現行資料を整理する。
2. 証明済み・追加仮定付き・証明未完成・予想・計算観察を区別し、仮定・証明の所在・依存関係・未解決箇所を記録する。原稿に証明が存在することは、その証明を今回独立に監査したことと異なる。
3. 先行研究の一次資料を確認し、適用範囲と本研究の貢献をIntroductionに明示する。文献と新規性の未確認事項は憶測で埋めない。他repoの結果を使うときは具体的な定理と仮定を記す。
4. 論文は原則日本語のLuaLaTeX。https://github.com/uedakazushi/research-hub の `papers/paper-template.tex`, `papers/README.md`, `.latexmkrc`, `.vscode/` を参考にする。主原稿を改名するときはinput、分割原稿のTeX root、文献、README、設定も更新する。
5. 研究ノートは現行の着想・例・補題・計算・障害・文献比較を保持する。論文中の十分な証明は複製せず参照する。過去の会話や更新日誌・旧版ZIPを蓄積しない。
6. 誤りの判明時は依存する主張を含めて修正し、ノート・方針・公表原稿・hubの記述を一致させる。

## 保存と検証
- 現行資料だけで再開できるよう、ソース、必要な文献情報、再現コード、入力、証明書を保持する。軽量化を理由に価値ある証明を削らない。古い資料の有効部分を統合するまでは消去しない。
- 研究の区切りでは追加の承諾なしに通常コミットで `main` へpush。長時間作業時は15〜30分で区切り保存する。他の作業者の変更を保護し、force push・GitHub Actionsの追加/起動は行わない。
- `latexmk` と VS Code LaTeX Workshopで組版し、SyncTeXとPDFを `build/` に整合させる。PDF・中間生成物は通常Git追跡しない。実行した数学的点検、計算、組版、pushは別々に報告する。
- GitHub管理後はLibraryへの定常的二重保存/ZIP作成をしない。push不能時は緊急保存する。既存Libraryファイルは明示指示なしに削除しない。

## KE三研究の共同編集
- `multiscale-kaehler-einstein`（固定配置補空間・Part I–III）、本repo（退化族の局所一様解析・Part IVと条件付き距離論・Part V）、`surface-lagrangian-torus-fibration`（actual KE Lagrangian構成と同じ射影の全域GH実現）を一つの研究計画の下で編集・検証する。リポジトリと本文の正本はこの分担で維持し、同一証明を複製しない。論文の統合・分割は中心結果と論理的まとまりに基づいて判断する。
- 外部結果を使う箇所には定理ラベル、仮定、次数と族の固定、計量と距離の規格化、固定領域とmoving領域の区別、確認した版を記す。共同作業の現在の依存表は本repoの `research/notes.md` と曲面repoの `research/ke-dependencies.md`、全体の短い分担はhubを正本とする。
- 曲面repoの直接scalar/portal証明を、本repoの(CP)/(PBE)/(TC)又はPart IIIの(H_loc)/(H_anc)自体の検証と読み替えない。局所結果が与えないglobal入力と、別稿で証明を持つglobal結果を区別する。固定配置の空間無限遠から退化族の一様性を推論せず、固定段階の証明と遅い対角選択の順を守る。
- 曲面稿の `ng8:quintic-full-moment` と `ke:quintic-simultaneous-realization` は、初期のmarked source allocationと全保持近傍を選べる五次で、同じactual射影による作用atlasとGH実現を与える。旧neck補題のsource-free仮定と、全source-wallを差し引く自由需要を区別する。解析領域・cuts・小さいtを選んだ後にthin葉を取り、既存の解析閾値を葉の微分に依存させない。全開collarの葉と作用を一致させ、実数平行移動を含めてatlasを接続する。結論は各tでの同時実現であり、atlasのt方向の収束、極限距離のHessian性、任意に既固定の大きいsource tailsの保存又はt方向に滑らかなfibration族を含めない。正本は曲面repoに置き、Part IV/V本文の改訂37の入力確認pinと、曲面稿で新たに確認した結果の現行版・保存状態を区別する。
- 六次では曲面稿 `ke:petersen-full-moment` と `ke:sextic-simultaneous-realization` が、等重み2/5・source配分(1,1,1,1;2)・初期source葉選択の下で同じ射影のatlas/GH/測度を実現する。内部二端cutの累積位置、正margin後の中央freeze、full annuli固定とanchor後選択を保つ。任意先指定保持集合と非等重みへの拡張は別課題である。
- Complete simplexの外部入力は実単体の凸解存在・Hessian完備性として引用する。Zhangの明示定理文の確認とCY1982原典本文の確認状態を区別する。一意性・tube完備・格子商・係数は本稿の直接証明を使い、w/Lのcover等長性を固定periodのquotient等長性やinjectivity radius下界へ読み替えない。
- `coarse:prop:capped-prefactor-sharp` は固定capとadjunction canonical densityのL_t^β前因子について、h=dd^c log Ωの全域 determinant lower を維持できる指数がβ≤2であることを示す。単純source中央でh²/Ω^(β)∼L_t^(2−β)となる。曲面repo `ke:source-capped-actual-prefactor-sharp` は既存中央sourceのactual体積二側比較も入力として、実際のω_t²の同じ前因子最適性を証明する。指定cap以外の障壁や全域GHの収束率の最適性を結論しない。
- `simplex:prop:boundary-floor-sharpness` は固定したexact深度座標と既定のcomplete simplex模型k_Lに対するO(1/m)の最適性である。固定facet shiftを模型へ吸収した後の改善、座標不変の最適性、compact射影的退化族での下限を結論しない。Balancedの正確例と正規化単体の境界へ向かう例を区別する。Zhangの固定normalized compact集合での全phase比較、Ruanの全域coarse比較とtorus-averageへの定量比較を既存成果として認め、canonical simplexへの全深度比一様小誤差・局所境界入力と比較する。
- Localized Chern–Luの `coarse:eq:localized-chern-lu-radius` と `neck:cor:shrinking-buffer-circle` を用いる際は、actual計量の球半径σを別に確保する。長さ評価C(1+σ⁻¹)/mから、mσ→∞又はRで正規化したRmσ→∞を検査する。この条件付き系をbuffer存在、full tensor比較、flow生存へ格上げしない。
- 固定endの最小解析入力は `pair:prop:fixed-end-transfer` の固定collarのlog-density収束と極限成分のradial derivativeに分ける。Volume frame変更時には `pair:rem:normal-frame-winding` のnormal windingと残余閉periodを確認する。これらや遅い対角選択をmoving neckのtensor比較・bufferの存在証明と読み替えない。曲面側の `ke:global-volume-measure` を引用するときは確率体積、同じ射影、成分頂点の等重み原子測度と全cubical計量空間を区別し、確認した版・保存commitを明記する。
- 優先順は、共有する局所入力の仮定・量化の照合、曲面の大域証明の利用箇所の監査、シリーズ総説とIntroductionの同期、公表前の一次文献比較。実質的な訂正は利用側にも反映してからhubを更新し、三次元研究は独立した未完成の課題として保持する。

## research-hub 更新義務
1. まず本repoの方針・原稿・ノート・READMEを最新の内容へ整理し、`main`へ保存する。
2. hubの最新READMEとAGENTS.mdを読んで、主要到達点・主張の状態・未解決の核心・次の一手・依存関係・正本・再開先・資料を実際に確認した日を更新する。
3. 詳細todo/証明/履歴はhubに転載しない。実質変更がないときは無用に更新しない。他項目と並行変更を保つ。
4. hubも通常コミットで`main`へ反映し、研究repo保存とhub更新の成否を独立に確認する。失敗した場合は対象と理由を報告する。公開範囲を勝手に変更しない。

## 回収した原資料の扱い
`research/source-manifest.json`と`research/migration.md`で全文・要約・未回収を区別する。移行完了の判定に短い要約を使わない。取得した最新版の訂正・追加仮定を旧稿の強い記述より優先する。保存済みの証明書と今回の再実行を混同しない。
