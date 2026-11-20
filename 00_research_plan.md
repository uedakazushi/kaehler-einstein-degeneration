# 現行研究方針：一般型超曲面の負Kähler–Einstein退化
更新：2026-11-20 / v1.1

## 研究固有の目標
超平面和に退化する一般型超曲面の負KE計量について、diameter正規化した大域GH極限と極限計量を求める。最初の実験場は \(X_t=\{L_0L_1L_2L_3L_4+tF_5=0\}\subset\mathbf P^3\) である。ZhangやSongの局所・非正規化極限と、求めるdiameter-scale global limitを区別する。

## 現時点の主要資料と状態
- Libraryの2026-08-21 v0.12、81頁TeX草稿 `quintic_five_planes_KE_GH_paper_draft_ja_v12.tex` には数多くの補題と計算がある。現在GitHubに作成した `papers/kaehler-einstein-degeneration.tex` は再構成草稿であり、全81頁の完全移行ではない。
- Candidate cubical complex \(\mathcal C_5=\{w\in[0,1]^5:\max_i w_i=1,\ |\operatorname{supp}w|\le3\}\) は25頂点・50辺・30 squares、\(\bigvee^4S^2\) と同じホモトピー型。これはGitHub主稿に直接の組合せ証明がある。
- 原資料の計算では標準cubical metricの直径は \(\sqrt{13}\)。今回は当該距離最大化計算の再実行は行っていない。
- Actual負KE計量がこのcubical complexへGH収束するという主張は**予想**。局所同期・finite scattering certificatesはその証明の一部でしかない。

## 最優先課題
1. 元草稿の全証明・必要なsource scriptsとcertificateを移行・再実行する。
2. Actual neck/cornerのuniform metric comparison、root-0/root-1 filtered scale modulationを \(o(R_t)\) で評価する。
3. Reference softmax/Calderón modelsからactual nonlinear KE gluingへの推論の不足を明確にする。
4. 一般 \(n,d\) への拡張と先行研究の一次資料比較を進める。

## 正本と依存
主原稿は `papers/kaehler-einstein-degeneration.tex`、研究ノートは `research/notes.md`。Fixed arrangement complementの結果は [multiscale-kaehler-einstein](https://github.com/uedakazushi/multiscale-kaehler-einstein) を参照するが、その局所入力から退化族のuniformityを自動的に導かない。

## 共通研究原則と保存許可（研究固有方針から独立）
数学的重要性・新規性・理解の深化・応用可能性・正確性・実現可能性を総合して方針を更新する。証明済み・仮定付き・未完成・予想・計算観察、既知結果と独自結果、草稿の証明と今回の監査を区別する。重要文献は一次資料の正確な定理と仮定を確認する。日本語LuaLaTeXで公表原稿と十分な証明を保持し、有効なアイデア・反例・計算は現行ノートに統合する。再現コード・証明書・入力を残すが旧版/中間出力は蓄積しない。区切りごと承諾なしに通常コミットで `main` へpush、15–30分を目安に切り良く保存する。force pushとGitHub Actions追加/起動はしない。Library旧資料は削除しないがGitHub移行後は定常二重保存しない。先に対象repoへ保存してからresearch-hubを更新し、数学検証・組版・GitHub・hubを別々に確認する。
