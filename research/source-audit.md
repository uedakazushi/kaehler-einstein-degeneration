# 現行原稿の証明状態と監査範囲

2026-11-23 / v1.4。研究資料v1.29、Part IV v1.16・Part V v1.10。

本書は現在有効な主張と、実際に確認した範囲をまとめる。原資料の回収元・版・hashは `source-manifest.json` と `migration.md`、組版・計算・表示の実行記録は `validation.json` が正本である。原稿に証明があること、今回その証明を読んだこと、計算・形式証明による確認を区別する。

## Capped lower の監査と Savin 一次資料

**Capped barrier の前因子は鋭い。** Part IV `coarse:prop:capped-prefactor-sharp` で、同じ α_i と canonical density に対する Ω^(β)=L_t^β∏α_i^(−2)Ω_0 を考えると、h^(β)=dd^c log Ω^(β)=h^low はβに依らず、β≤2では全域 determinant lower が成り立つが、β>2では source中央点で (h^low)^2/Ω^(β)≈L_t^(2−β)→0 のため失敗することを直接証明した。中央rescalingでactive二方向はL_t^(−1)、背景・inactiveはO(|t|)であり、canonical residueは非零である。これはこのcap ansatzの最適性であり、一般の別障壁やactual KE metricそのものに対する最適性を主張しない。Part IVのglobal capped lowerを変更せず、これを利用する曲面稿の仮定も変えない。

命題の代数部分は `research/check_capped_prefactor.py` をSymPyで実行してPASS。ここで実行したのはcap係数・source rescaling・二次minorの恒等式のみであり、各局所型の幾何学的被覆や全曲面のKE方程式を計算で検証したのではない。Six-type determinantの利用は `coarse:lem:weighted-cap-lower` → `coarse:lem:capped-pair` / `coarse:lem:capped-triple` → `coarse:thm:global-determinant` → `coarse:lem:one-sided-volume` → `coarse:cor:degree-d-volume-lower`。対象を限定してこれらの公式と論理順序を確認し、今回の読解範囲内に結論阻害gapは認めなかった。全局所座標の幾何学的被覆と全原稿の形式証明は未実施。

O. Savin, [*Small Perturbation Solutions for Elliptic Equations*](https://www.math.columbia.edu/~savin/Small_pert.pdf), Commun. PDE 32 (2007), 557–578, Theorem 1.3 pp.559–560をPDF画像を含め実読し、必要条件がH1,H2,H4（H3は不要）であることを確認した。現在の `coarse:lem:small-volume-tensor` のoperator `det_+(H+\mathcal H(N))/detH-e^z` はPSD順序でglobal degenerate elliptic、基準行列の近傍でstrictly elliptic、零解の周囲でsmoothという構造を用いる。Savin全原著証明・該当局所入力の全適用鎖を再証明したわけではない。

## 証明の正本と条件

| 正本 | 無条件の中心結果・証明の所在 | 追加条件又は未解決の部分 |
| --- | --- | --- |
| Part IV・本repo | `coarse:cor:degree-d-volume-lower`、`coarse:thm:boundary-to-triple`、`coarse:thm:full-triple-tensor`、閉cornerの内在・protected距離、source-free固定baseの正則normal作用・canonical moment・固定end。局所模型、source packing、固定次数の代数・residue計算も保持。 | Sourceを含むquintic exteriorの一様coarse tensor比較は **(TC)_5付き**。任意のmoving領域のproduct exhaustion・全域sharp co-Gramには(PBE)_d等を要する。Bounded densityだけからtensor比較を推論しない。 |
| Part V・本repo | Abstract pruning–transport、有限cubical target、diam(C_5)=√13。 | 本稿のactual degree-d GHへの適用経路は(CP)_d+(PBE)_d付き。 |
| 曲面repo | 固定d≥5のactual負KE–Lagrangian fibrationと同じ合成写像の全域ambient GH実現、確率体積の等重み原子極限。五次と六次標準等重みPetersenでは同じ射影の作用atlasも実現。 | 任意に先指定した大きいsource近傍、任意weights、t方向の滑らかな射影族、atlasの極限又はHessian性は結論しない。直接scalar/portal証明はCP/PBE/TC自体の検証ではない。 |
| 固定補空間repo・Part I–III | 固定SNCの距離錐と体積漸近、標識付きsecondary periods等。正確な仮定・証明・新規性比較は同repoの現行原稿を参照。 | Part IIの一般secondary WP completionはcontrolled parallel push-off付き、Part IIIのactual localization/global pGHはH_locとH_anc付き。固定空間の結果を退化族へ一様に移さない。 |

曲面の確認保存版は `46e128e47bd536e577afad24641d6461fe6169e8`（改訂46）、固定側は `2926300c2425c7e68550ac08ee81a2afa639a0c6`（Part I v1.10・総説v1.14）である。IV/V本文が既存入力に使う曲面改訂37の科学引用pinは維持する。後続の結果の証明を本repoへ複製しない。

## Complete simplexの現在の確認範囲

**Complete simplex模型の最小入力。** Part IV `coarse:lem:simplex-model` は、Zhang Theorem 2.1に明記されたCheng–Yauの標準実単体上の凸解存在・境界発散・実Hessian完備性を入力とする。一意性は内側homothety比較、tube完備性は有限長曲線の実射影、格子商の完備性は等長作用から直接証明する。w/Lはuniversal cover上の等長写像だが、4πの角度格子を4π/Lへ変える。固定周期商のinjectivity radius下界は結論しない。全深度比の正規化窓でpotentialとtensorの規格化を明示した。Zhangの定理文と適用条件は実読済みだが、CY1982 Theorem 4.4の原文・証明は未取得であり、原典確認済みとはしない。正確な書誌・係数点検・確認範囲は `research/source-audit.md`、直接証明は現行本文が正本である。

- Zhang, arXiv:1505.04728v2, p.4のB_σの定義、p.5 Theorem 2.1と(2.1)、p.6 (2.2)・Proposition 2.2を実読した。σ=R_{≥0}³、u_σ=(1,1,1)でΔ_1そのものであり、多面体境界による適用条件の欠落は認めない。Lの有理性は不要。
- 1982年の原著は著者公式書誌でpp.339–370、公式再録目次で *Selected Works of Shing-Tung Yau*, Part I, Vol.4, Kähler Geometry I (2019), pp.301–332と確認した。Theorem 4.4の原典頁・本文・証明は未確認。この文献確認の状態を、Zhangの明示定理に追加の数学的仮定が必要であることと混同しない。
- 原稿の内側homothetyによる一意性、有限長曲線によるtube完備性、free proper等長格子作用、w/Lと角度period、Ricciとvolumeの係数、normalized potential Φ=φ+log(ab)と固定stripでの正則性の鎖を作成担当と別担当が点検した。実際の模型の高階評価はangular cover上のものである。
- Zhang p.6の4^nという印刷はPDF画像で確認し、w=x+iyから正しい係数4^{−n}を独立に計算した。Ricciには定数なので影響せず、本稿のk²=8e^{2φ}dV_logは正しい。係数を引用から転記せず直接確認する。

原著書誌: https://daweb.qzc.tsinghua.edu.cn/ShingTungYau/en/zdylm/5542/list/index.htm （項目172）。再録目次: https://www.tup.tsinghua.edu.cn/booksCenter/bookcatalog?id=10473901 。実読した定理文: https://arxiv.org/pdf/1505.04728v2 。本文証明と数学的計算の確認を、組版・表示・形式証明・包括的新規性確認と分ける。

## 局所安定性の先行結果との比較

比較対象は、指定したcomplete simplex KE模型への相対小誤差、正規化領域、誤差の率、入力仮定の四点とする。以下の原著の指定定理・対応する証明箇所を実読した。全原著の包括的な証明監査又は本結果の優先権調査を完了した意味ではない。

| 一次資料・確認箇所 | 確認した内容 | 本稿の局所定理との関係 |
| --- | --- | --- |
| Zhang, *Collapsing of negative Kähler–Einstein metrics*, [arXiv:1505.04728v2](https://arxiv.org/pdf/1505.04728v2), Theorem 2.4(ii), p.8; (3.7)–(3.9), Lemma 3.2, p.13; Lemma 3.3, Proposition 3.4, pp.16–17; Lemma 3.5, pp.18–19 | Simple toroidal・Q-factorial全空間・相対canonical ampleの下で、最深stratumのcanonical semi-flat模型へのC∞loc収束。証明の領域はx_i=ell_i/Lの固定K⊂⊂B_Iで、最深stratumの一意性で部分列を除く。 | 指定模型への比較誤差の有効率はこの証明鎖では与えない。固定Kはmin ell_i≥δ_K Lを要求し、min ell_i→∞かつmin ell_i/L→0の点列を含まない。 |
| Ruan I, *Degeneration of Kähler–Einstein manifolds I: the normal crossing case*, [arXiv:math/0303112v2](https://arxiv.org/pdf/math/0303112), Theorems 4.1–4.2, p.9 | 固定exhaustion compactのC^k収束と、全域でC₁g_app,t≤g_KE,t≤C₂g_app,t。 | Moving点・深度比・全phaseを除外していない。比較相手は構成したapproximate metricであり、比較定数が1へ近づく率ではない。 |
| Ruan II, *Degeneration of Kähler–Einstein manifolds II: the toroidal case*, [arXiv:math/0303113v4](https://arxiv.org/pdf/math/0303113), Theorems 5.1–5.2, p.15 | Toroidal canonical degenerationで同種の収束と全域の一様quasi-isometry。 | Ruanの結果全体を固定normalized compact上の定性的収束だけと記述しない。 |
| Ruan, *H-minimal Lagrangian fibrations in Kähler manifolds and minimal Lagrangian vanishing tori in Kähler–Einstein manifolds*, [arXiv:math/0309177v2](https://arxiv.org/pdf/math/0309177), Lemma 3.1, p.6; Proposition 3.1, Corollary 3.1, p.7; Theorem 3.1, p.9 | 一様C∞ quasi-isometryの下で、固定c<1のΔ_(cτ)上のpotentialの角度振動成分に任意多項式率。H-minimal fibrationの変形にはO(1/τ)。 | 比較相手はactual potentialのτ依存のtorus平均。定数C(N,c,I)はcに依存し、指定されたcomplete simplex解との小誤差ではない。c→1への一様性をこの定数だけから推論しない。 |
| Ruan, *Degeneration of Kähler–Einstein hypersurfaces in complex torus to generalized pair of pants decomposition*, [arXiv:math/0311098v2](https://arxiv.org/pdf/math/0311098), Theorems 6.2–6.3, pp.15–16; Lemma 8.1, pp.18–19 | 非compact hypersurfaceのcomplete KE収束と一様C∞ quasi-isometry、固定raw cutoff Δ_(τ−μ)の領域。 | Ruanの議論がmoving領域を扱わないとは述べない。本稿はcanonical simplexへの全深度比一様な消失誤差を比較する。 |

Zhangの(3.9)の角度基本領域は幅2π/|log|t||であり、固定の有界imaginary boxに入る。従って固定K上のcoverの比較はquotientの全phaseを含む。この読み取りから、全phase又は定量評価の存在そのものを本稿の新規性としない。

`coarse:thm:boundary-to-triple` の差分は、fixed-face density下界と各parameterのsmooth compact radial閉包から、既定complete simplexへの相対C^q誤差C_q/min ell_iを全深度比で得る定式化である。Actual buffer、事前のactual/background tensor比較、t一様な境界上界を別入力にしない。Moser flow又は領域外の距離比較に使うactual bufferは別の問題である。ここで挙げた既存の手法を精密化して同様の結論が得られる可能性や、未調査文献を排除したわけではない。

## 局所率の最適性の点検

`simplex:prop:boundary-floor-sharpness` の命題・証明と、pure-model `simplex:prop:dominant-product`、`coarse:thm:boundary-to-triple`、small-volume-tensorの依存を作成担当と別担当が実読した。固定m₀,bの単一KE族、共通density floor、period lattice、logarithmic frame、smooth閉包、balanced点の正確なscalingとcutoff m/2、boundary-escaping例の先頭係数−4b/−2b、点でのoperator normを確認した。Actual安定性を証明へ逆用する循環はない。研究ノートの一般L展開とLだけの率がない帰結は同じ純模型の積比較による。

最適性は固定depth coordinates・固定k_Lに対する局所仮定クラスに限る。Facet shiftを模型へ吸収した後の改善、compact射影的族の誤差下界、幾何学的に不変な最適率は主張しない。数学的手計算と指定本文の内部点検であり、形式証明・数値証明ではない。組版・表示は `validation.json` に別記する。

## 保持するSchwarz半径の点検と精密化

保持する対象は `coarse:lem:localized-chern-lu` と `neck:lem:rank-one-circle` → `neck:cor:buffer-circle` → `neck:cor:shrinking-buffer-circle` に限定した。

- 正則写像FのtargetがKählerでholomorphic sectional curvature≤−κ、sourceがRic(g)=−g、actual球の閉包が定義域にcompactに入るとき、tr_g(F*h)≤C_n κ⁻¹(1+σ⁻²)。恒等写像に限定せず、曲線への射影も含む。
- 距離cutoffの勾配はCσ⁻¹、Laplacian下界は−C(σ⁻²+σ⁻¹)。χ²uの正の最大点で評価し、u=0でlogを取らない。Cut locusは距離の上側supportと非増加cutoffで扱う。Targetの完備性、sourceのinjectivity radius下界、dFの単射性は要らない。
- 複素次元2のrank-one下界p*h_D≤Aωとvolume上界ω²≤Bh²から、mixed coefficientsを許したままnormal tensor≤AB h_Aを得る。平方根と周期1の積分から、m=min(s,M−s)に対しcircle長≤C(1+σ⁻¹)/m。
- 0<σ≤1でmσ→∞なら非正規化circle長が零へ行く。径尺度Rで割る場合はRmσ→∞で足りる。いずれも **actual buffer半径の確保は別入力**。Full tensor比較・Moser flow生存をこの系から結論しない。

作成担当と別の読み手が上記cutoff、rank-one行列式、平方根、period、量化を点検し、修正を要する問題を認めなかった。新規の形式証明・数値証明ではない。古典的Schwarz評価の定量的帰結として記載し、新しいSchwarz lemmaとしての優先権は主張しない。

一次資料としてYau, *A general Schwarz lemma for Kähler manifolds*, Amer. J. Math. 100 (1978), 197–203, §1 (10)–(16)、pp.199–201のChern–Lu公式とTheorem 2を該当する監査で実読した。[原典PDF](https://archive.ymsc.tsinghua.edu.cn/pacm_download/59/11034-Shing-Tung_Yau_30.pdf)。Roydenのholomorphic-sectional版は既存引用を維持し、今回その原典全証明を再監査したとはしない。局所cutoffによる半径依存は本文で証明する。

## 保持する解析監査と適用上の障害

次の対象限定監査は現行証明に有効である。今回のsimplex模型の確認と、これら全体の反復検証を混同しない。

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
