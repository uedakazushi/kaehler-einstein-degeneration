# 現行原稿の証明状態と監査範囲

2026-11-23 / v1.1。研究資料v1.26、Part IV v1.13・Part V v1.10。

本書は現在有効な主張と、実際に確認した範囲をまとめる。原資料の回収元・版・hashは `source-manifest.json` と `migration.md`、組版・計算・表示の実行記録は `validation.json` が正本である。原稿に証明があること、今回その証明を読んだこと、計算・形式証明による確認を区別する。

## 証明の正本と条件

| 正本 | 無条件の中心結果・証明の所在 | 追加条件又は未解決の部分 |
| --- | --- | --- |
| Part IV・本repo | `coarse:cor:degree-d-volume-lower`、`coarse:thm:boundary-to-triple`、`coarse:thm:full-triple-tensor`、閉cornerの内在・protected距離、source-free固定baseの正則normal作用・canonical moment・固定end。局所模型、source packing、固定次数の代数・residue計算も保持。 | Sourceを含むquintic exteriorの一様coarse tensor比較は **(TC)_5付き**。任意のmoving領域のproduct exhaustion・全域sharp co-Gramには(PBE)_d等を要する。Bounded densityだけからtensor比較を推論しない。 |
| Part V・本repo | Abstract pruning–transport、有限cubical target、diam(C_5)=√13。 | 本稿のactual degree-d GHへの適用経路は(CP)_d+(PBE)_d付き。 |
| 曲面repo | 固定d≥5のactual負KE–Lagrangian fibrationと同じ合成写像の全域ambient GH実現、確率体積の等重み原子極限。五次と六次標準等重みPetersenでは同じ射影の作用atlasも実現。 | 任意に先指定した大きいsource近傍、任意weights、t方向の滑らかな射影族、atlasの極限又はHessian性は結論しない。直接scalar/portal証明はCP/PBE/TC自体の検証ではない。 |
| 固定補空間repo・Part I–III | 固定SNCの距離錐と体積漸近、標識付きsecondary periods等。正確な仮定・証明・新規性比較は同repoの現行原稿を参照。 | Part IIの一般secondary WP completionはcontrolled parallel push-off付き、Part IIIのactual localization/global pGHはH_locとH_anc付き。固定空間の結果を退化族へ一様に移さない。 |

曲面の確認保存版は `1088f86cf8f0c70c74a1e4caa3b90393ff627067`（改訂44）、固定側は `2926300c2425c7e68550ac08ee81a2afa639a0c6`（Part I v1.10・総説v1.14）である。IV/V本文が既存入力に使う曲面改訂37の科学引用pinは維持する。後続の結果の証明を本repoへ複製しない。

## 今回の局所解析の点検と精密化

対象は `coarse:lem:localized-chern-lu` と `neck:lem:rank-one-circle` → `neck:cor:buffer-circle` → `neck:cor:shrinking-buffer-circle` に限定した。

- 正則写像FのtargetがKählerでholomorphic sectional curvature≤−κ、sourceがRic(g)=−g、actual球の閉包が定義域にcompactに入るとき、tr_g(F*h)≤C_n κ⁻¹(1+σ⁻²)。恒等写像に限定せず、曲線への射影も含む。
- 距離cutoffの勾配はCσ⁻¹、Laplacian下界は−C(σ⁻²+σ⁻¹)。χ²uの正の最大点で評価し、u=0でlogを取らない。Cut locusは距離の上側supportと非増加cutoffで扱う。Targetの完備性、sourceのinjectivity radius下界、dFの単射性は要らない。
- 複素次元2のrank-one下界p*h_D≤Aωとvolume上界ω²≤Bh²から、mixed coefficientsを許したままnormal tensor≤AB h_Aを得る。平方根と周期1の積分から、m=min(s,M−s)に対しcircle長≤C(1+σ⁻¹)/m。
- 0<σ≤1でmσ→∞なら非正規化circle長が零へ行く。径尺度Rで割る場合はRmσ→∞で足りる。いずれも **actual buffer半径の確保は別入力**。Full tensor比較・Moser flow生存をこの系から結論しない。

作成担当と別の読み手が上記cutoff、rank-one行列式、平方根、period、量化を点検し、修正を要する問題を認めなかった。新規の形式証明・数値証明ではない。古典的Schwarz評価の定量的帰結として記載し、新しいSchwarz lemmaとしての優先権は主張しない。

一次資料としてYau, *A general Schwarz lemma for Kähler manifolds*, Amer. J. Math. 100 (1978), 197–203, §1 (10)–(16)、pp.199–201のChern–Lu公式とTheorem 2を今回実読した。[原典PDF](https://archive.ymsc.tsinghua.edu.cn/pacm_download/59/11034-Shing-Tung_Yau_30.pdf)。Roydenのholomorphic-sectional版は既存引用を維持し、今回その原典全証明を再監査したとはしない。局所cutoffによる半径依存は本文で証明する。

## 保持する解析監査と適用上の障害

次の対象限定監査は現行証明に有効である。今回のSchwarz鎖の確認と、これら全体の反復検証を混同しない。

- Capped positivity、零点を含むChern恒等式、weighted minor、pair/tripleと六型cover、adjunction residue、compact最小値原理、固定次数の大域volume下界。
- 固定faceの一様density下界から、translated complete simplexの上下barrier、small Ricci potential、SavinのH1/H2/H4とSchauderによるfull-triple tensor。境界上界のt一様性やactual距離bufferを追加仮定しない。
- Fixed-end transferのlog-densityの固定collar収束、Rochon–Zhangのradial remainder、period 1の係数4π、Hermitian深度差O(1)、normal frame windingと残余closed periods。
- 固定stageの後にt閾値を取る遅い対角選択。固定stageで未証明のbuffer、matching、費用の有効成長率を対角操作で補わない。

ZhangのQ-factorial/simple toroidalな退化定理をsource方程式xy=tzへ直接適用しない。Complete envelopeの上比較ではlog-volume ratioの上有界性を別に検証する。Fixed residual discのvolume boundだけでは指定productへの収束を導けず、fixed tame gaugeだけではgrowing chart chainsのproduct exhaustionを構成できない。詳細と反例は `research/notes.md` と現行本文に置く。

## 六次の現行到達点の同期

曲面稿の `ke:petersen-full-moment`、`ke:sextic-simultaneous-realization` の仮定・結論と接続を確認した。標準Petersen系、等重み2/5、配分(1,1,1,1;2)、初期source葉の選択の下で、全momentと両anchorの全open germsを実現する。内部source blockは幅だけでなく累積位置が条件であり、正cut margin後に中央helperをfreezeし、その後でfull annuliを固定する。同じprimitive/domainを使い、anchor葉は全moment構成後に選ぶ。曲面側の独立内部点検の記録を同期するが、本repoで全六次証明を今回再監査したとはしない。

## 規格化と固定次数の代数

`X_t={∏L_i+tF_d=0}⊂P³`、固定d≥5、Ric(ω_t)=−ω_tに対し、現行本文の規約は次である。

| 量 | 値 |
| --- | --- |
| Maximal squares | d binom(d−1,2) |
| Double-line sources | d binom(d,2) |
| Residual curve | (d−2)-punctured sphere |
| Relative section | O(d)⊗O(−(d−2))=O(2) |
| Canonical class | K_X=O(d−4) |
| K_X² | d(d−4)² |
| KE volume | 2π²d(d−4)² |
| Leading co-Gram coefficient | 1 |

定数は固定dと固定族に依存してよい。Primitive normalizationでは距離は1/√(d−4)倍、co-Gramは(d−4)Iとなる。次数に一様な評価は主張しない。

高次元degree-d hypersurface X⊂P^NではK_X=O(d−N−1)、体積は(2π)^(N−1)d(d−N−1)^(N−1)/(N−1)!。候補C_(d,N)={max w_i=1, |supp w|≤N}はsk_(N−1)Δ^(d−1)と同相である。一方N≥4ではsource locusが正次元で高階strataと交わり、mixed modelsの解析が残るためactual GH極限は予想の段階である。

## 未了の公表前確認

全原稿・全一次資料の包括監査、外部査読、形式証明、定量的新規性の網羅的確認は未了。先に局所成果と曲面の直接GH証明を公表可能な範囲にまとめ、CP/PBE/TC、高次元化、先指定追加保持集合の相対可解性は独立の課題とする。組版・表示・計算の実施範囲と保存状態は `validation.json` を参照する。
