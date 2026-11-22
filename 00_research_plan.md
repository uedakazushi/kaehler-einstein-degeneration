# 現行研究方針：一般型超曲面の負Kähler–Einstein退化

更新：2026-11-23 / v1.29・現行研究方針（Part IV v1.16、Part V v1.10）

## 公表に向けた実行計画

数学的重要性、新規性、理解の深化、応用可能性、正確性、読者による検証、実現可能性を総合し、研究全体の価値を最大化する。[三研究の公表計画](https://github.com/uedakazushi/surface-lagrangian-torus-fibration/blob/main/00_research_plan.md)に従い、本repoでは曲面P0を支える無条件の局所解析をPart IVの中心に置く。CP/PBE/TCの解決を局所成果の公表条件にしない。

1. Exact triple領域、各固定parameterの滑らかなradial閉包と全phase quotient、固定faceの一様密度下界を入力とする局所安定性定理 `coarse:thm:boundary-to-triple` を抽出した。境界上界にparameter一様性が不要であることを証明の向きとともに明示し、全平面退化への適用を `coarse:thm:full-triple-tensor` に分けた。証明は一回だけ掲載する。
2. 題名・abstract・主結果を、局所安定性、complete simplexと閉corner、source-free neckと固定end、条件付きexterior/PBEの順に整理した。条件付き結果と必要な証明も保持する。
3. 曲面主稿の実際の引用を逆引きし、capped lowerとoriented upper、full-tripleとsimplex、normal circle、束座標・共通primitive・固定endの最小四入力表を主稿 `tab:surface-minimal-inputs` に置いた。領域、全位相、定数、cutの選択順と曲面側が別に証明する事項を明記する。固定endには `pair:prop:fixed-end-transfer` の最小log-density入力を置き、normal windingによる加法定数と残余periodを分離する。
4. Part Vの(CP)+(PBE)付きactual適用と曲面の直接scalar/portal経路を区別する。Part IV/V本文の曲面入力引用は実読した改訂37・commit `32c67aefe6beb47c2955923e2b6eb2471d48af31` に保持する。曲面稿は五次の全moment・同時atlas/GH実現と `ke:global-volume-measure` の証明を所有し、現在確認した数学保存版は `46e128e47bd536e577afad24641d6461fe6169e8`（改訂46）である。
5. 局所安定性とcapped-volumeの指定証明鎖、固定end移送とframe windingの追加式を作成担当と別担当が内部点検した。組版・表示は各版の実施範囲を別に記す。ZhangのQ-factorial/simple toroidalな全空間の結果はsource方程式 \(xy=tz\) へ無条件に適用しない。全原著証明・全主稿の包括監査と定量的新規性の確認は残る。

達成基準は、曲面P0が使う局所解析を最小の正確な入力と一意の証明場所から検証できること。これは全主稿の包括的再監査、外部査読、投稿の完了を意味しない。原稿・ノート・方針・READMEの保存後、利用側の依存表とresearch-hubへ実際の到達点を反映する。共通の一般原則・保存許可は本書後半と `AGENTS.md` に記す。


**Capped barrier の前因子は鋭い。** Part IV `coarse:prop:capped-prefactor-sharp` で、同じ α_i と canonical density に対する Ω^(β)=L_t^β∏α_i^(−2)Ω_0 を考えると、h^(β)=dd^c log Ω^(β)=h^low はβに依らず、β≤2では全域 determinant lower が成り立つが、β>2では source中央点で (h^low)^2/Ω^(β)≈L_t^(2−β)→0 のため失敗することを直接証明した。中央rescalingでactive二方向はL_t^(−1)、背景・inactiveはO(|t|)であり、canonical residueは非零である。これはこのcap ansatzの最適性であり、一般の別障壁やactual KE metricそのものに対する最適性を主張しない。Part IVのglobal capped lowerを変更せず、これを利用する曲面稿の仮定も変えない。

### 実行状況と次の課題

Part IV v1.15は、complete simplexの最小存在入力と直接証明を保持し、`simplex:prop:boundary-floor-sharpness` により固定深度座標でのO(1/m)の最適性を示す。同じ境界floorを持つ平行移動模型では、balanced点で計量比と体積対数比が正確に求まり、L=m²の正規化境界へ向かう点列でも−2b/m、−4b/mの一次項が残る。固定facet shiftを模型へ吸収した後の改善や、compact射影的退化族の最適率は結論しない。後続の精度問題としてfixed-end情報から有界facet shiftを選ぶ追加条件と、補正模型への剰余を検討する。補正模型による率の改善は、現在の局所安定性と最適性の公表条件にしない。公表準備は指定一次比較・主張範囲の整理を優先する。

先行比較ではZhangの固定normalized compact集合上のcanonical semi-flat収束、Ruanの全域coarse比較とtorus-averageへの定量比較を認める。本稿の比較点は、既定complete simplexへの最小深度に関する小誤差、全深度比での一様性、局所境界入力である。全phaseや定量評価の存在そのものを差分としない。指定原著箇所を照合したが、Cheng–Yau 1982 Theorem 4.4原文の取得、全原著・全主稿の包括監査、新規性の包括確認は未了である。CP/PBE/TC、任意保持集合、高次元化は別課題とし、組版・表示は検証JSONに独立に記す。

固定補空間側は[Part I v1.10・総説v1.14・研究資料v1.19](https://github.com/uedakazushi/multiscale-kaehler-einstein/tree/2926300c2425c7e68550ac08ee81a2afa639a0c6)を確認版とする。尖点付き有限面積双曲曲線Sと境界のないコンパクト連結Riemann因子Yの積で、距離Laplace変換をRe s<3の切断半平面上でW/(1−s)−H(s)Log(1−s)+G(s)と表示する。Hはentire、GはRe s<3で正則であり、WとmonodromyからYの正規化基点距離分布を回収する。通常volume-IRFA一般への解析接続・等長型・族一様性は主張しない。総説はこの積の結果、Part IV v1.12の固定end/winding、曲面改訂44の同じ射影による確率体積極限を統合する。これらは固定補空間側の成果・共同編集であり、Part IV/Vへの新しい解析仮定やCP/PBE/TCの検証ではない。 新しい `cor:CW-fixed-cutoff-budget` は固定SNC cutoffの脱落質量とStokes defectをCe^{-A}で抑える。統合担当がこの追加証明を実読し、固定対の予算とtの有効収束率を区別している。

**Actual bufferの半径と円周収縮。** `coarse:lem:localized-chern-lu` は、actual球の半径σとtargetの負曲率κに対して tr_g(F*h)≤C_n κ⁻¹(1+σ⁻²)を与える。正則写像のrank低下、潰れたinjectivity radius、targetの非完備性を許す。`neck:cor:shrinking-buffer-circle` はrank-one下界と体積上界を組み合わせ、normal深度m=min(s,M−s)に対しlength≤C(1+σ⁻¹)/mを得る。0<σ≤1ならmσ→∞が非正規化の収縮、Rmσ→∞がRで割った収縮の十分条件となる。半径は別の幾何的議論で確保する入力であり、bufferの存在、全tensor比較、Moser flow生存、CP/PBE/TCは証明しない。証明は距離cutoffの勾配・Laplacian bounds、正の最大点、mixed coefficientsを含むdeterminant比較を明記する。これは古典的なSchwarz評価の定量的帰結であり、新しいSchwarz lemmaとしての優先権は主張しない。

## 研究固有の目標

固定次数d≥5の一般型曲面の全平面退化について、actual KE計量の局所一様解析と、それを大域的な径尺度の極限へ接続するための正確な入力を整える。本稿には全深部三重点のtensor比較、全閉cornerの局所GH収縮、source-freeな固定compact baseの正則normal action・canonical primitive・共通moment intervalの証明がある。全曲面のGH極限とactual Lagrangian射影による実現には曲面repoに別の直接scalar/portal証明があるため、その共有局所入力と量化の接続を最優先で監査する。五次ではさらに `ke:quintic-simultaneous-realization` が、初期marked source葉と全保持近傍を選ぶ範囲で、一つのactual射影に作用atlasとGH実現を同時に与える。六次では別の `ke:sextic-simultaneous-realization` が標準等重みについて同じ三結論を与える。本repoの(CP)/(PBE)/(TC)という強い解析package、Part IIIの(H_loc)/(H_anc)は未解決のまま残る。高次元のmixed source–higher-stratum modelsは後続課題とする。

曲面側 `ke:global-volume-measure` は、確率体積を同じGH近似写像およびLagrangian射影で押し出したとき、各成分頂点に重み1/dを置く弱極限を与える。固定成分体積の交点数、固定compact収束と既存全域値比較を用い、moving neckの体積漸近を追加仮定しない。極限測度の台は成分頂点である一方、計量極限は辺とsquareを含む全cubical空間である。証明正本の確認保存版（改訂46）は曲面repoの `46e128e47bd536e577afad24641d6461fe6169e8` である。

## 三研究の共同方針と正本

研究・編集・証明監査は一体で進め、以下の正本分担を保つ。三つの本文を一つに機械的に統合せず、重複する証明は所有repoへ集約して具体的な定理を参照する。

| 正本 | 担当する結果 | 本repoとの接続 |
| --- | --- | --- |
| [multiscale-kaehler-einstein](https://github.com/uedakazushi/multiscale-kaehler-einstein) | 固定配置補空間の空間無限遠・residual complex periods・conifold localization（Part I–III） | 固定成分は P² から d−1 本の直線を除いたもの。固定空間の漸近を退化族のmoving領域へ直接適用しない。 |
| 本repo | 退化族の局所一様解析（Part IV）、条件付きpruning–transportと有限target距離（Part V） | Capped density、full triple、fixed-end momentを曲面側へ供給する。CP/PBE/TCの未検証部分を保持する。 |
| [surface-lagrangian-torus-fibration](https://github.com/uedakazushi/surface-lagrangian-torus-fibration) | Actual KE Lagrangian構成と同じ合成写像の全曲面GH実現 | Source-inclusive fixed-shell、固定段階buffer・同一moment接着・core filling・scalar/portal評価と、その全域歪みからの中間尺度分類を所有する。五次および六次の標準等重みについて、同じ射影の作用atlas/GH/測度の同時実現も所有する。 |

共有入力は [研究ノート](research/notes.md) の依存表と曲面側の `research/ke-dependencies.md` で、定理・仮定・尺度・固定/可動領域・確認版を照合する。Part IIのsecondary complex periodsと第二symplectic actionは同一視しない。Part IIIの(H_loc)/(H_anc)も別模型の仮定として残す。方針・本文・ノートを先に保存し、その結果をhubの短い要約へ反映する。

固定補空間側のPart I v1.10（研究一式v1.19）は、連結smooth projective・reduced SNC・K+D ampleの範囲で、n=1と空境界のcompact caseを含む。Hermitian depthsを保つ可換collars・全残余一様なRZ延長比較・一面tensor評価からmetric-IRFAを検証し、properな1-Lipschitz全射Sと有界加法誤差Kを構成する。固定基点からのblow-downは一意である。固定したSについて、中心oと半径Aに一様に、ambient閉球のGH誤差は3K/(2R)以下で、比較先の中心はS(o)/Rである。指定compact集合をSで零へ送る選択もでき、その場合Kはその集合に依存してよい。LDPと、非空境界のexact tail・joint law・distance Laplace transformは通常の全face volume-IRFAで成立し、指数的volume remainderを追加仮定しない。正本・ラベル・独立点検と共同監査の範囲は研究ノートに記す。

同じ固定空間のmoving-basepoint blow-downは、cone内の有界基点極限、または面αに沿うEuclidean因子とincidence link coneの積に分類され、任意に指定した拡大列に対して全て実現する。正のα座標を持つstarと、最小weighted座標m>2Aでのambient閉A球の厳密な積同定を用いる。Closed star全体のambient積表示は一般に成り立たない。距離だけから復元するのはmetric linkの等長型であり、標識付きcell分割・depth重み・geodesic-ray boundaryの復元は含めない。Leuzingerのlocally symmetric cone比較・radial公式、Bridson–Haefligerの標準cone幾何との重なりを正本Introductionに明記する。

同稿の面ごとの測度付き平行移動は、任意のnormal中心vectorでmin T_i→∞なら、通常volume-IRFAから全残余strip上の全変動収束を得る。Metric-IRFAと収束するnormal offset・残余基点も仮定すると、固定gのscale-one積極限と全半径のambient閉球測度の全変動収束が成立する。Smooth volume-IRFAを必要としない。滑らかな基準曲率からの有界primitiveを用いる直接Stokes・face mass規格化、および全faceのvolume漸近に基づくMellinの一様momentとincidenceは共同点検として同期する。交点数公式のface massは非正規化KE体積に対応し、確率版では全体積で割る。通常volume-IRFAからのAbel極限は有理型延長を意味せず、1/t誤差による反例と追加のjoint polyhomogeneity条件を区別する。これらの証明は固定空間のものであり、退化族の一様bufferやCP/PBE/TCへ移さない。

公表範囲の依存表では、距離に必要なmetric-IRFA、測度に必要なordinary volume-IRFA、交点数のbounded primitive、複素有理型延長の追加条件を分ける。Part II v2.1のsecondary periodはcomponent-labelled collarとdeeper-face labelsを伴う収束から得る標識付き残余曲線であり、複素periodにはKähler orientationも保持する。向きだけを忘れる場合にもfactor/cusp labelsは保持し、一般secondary WP completionのcontrolled parallel push-off仮定は残す。Chambert–Loir–Tschinkelのresidue measures・Igusa積分の先行結果と本稿のordinary L1/一側Abel条件の比較は、正本Introductionと一次資料監査に委ねる。

曲面改訂38の `topo:cubical-local-models` / `topo:cubical-moving-blowups` と `ke:intermediate-moving-classification` は、同じP0のdistortion ε_tに対しa_t→∞、a_t/R_t→0、R_t ε_t/a_t→0の尺度で、任意の移動基点の全pointed GH極限を、成分錐C_{2,d−1}、R×Y_{d−2}、全角3π/2のEuclidean錐、R²の四型に分類する。Y_mは原点を共有するm本の半直線であり、各型の有限基点を指定した尺度・退化列で実現できる。`ke:intermediate-component-cone` の成分頂点を基点とする結論にはtarget変位も吸収し、component coreと変更collarの任意基点へ適用する。証明は曲面稿の既存全域歪みと有限targetの局所計量幾何による。固定Part Iの定理の退化族への直接適用や、Part IV/Vの新しいtensor入力ではなく、CP/PBE/TCの未検証状態を変えない。

## 論文と証明の状態

- `papers/kaehler-einstein-degeneration.tex`：Part IV、現行v1.15は、complete simplexの最小存在入力と直接証明を保持し、固定深度座標での局所安定性率の最適性と指定先行結果との比較を統合した。126頁に組版し、変更箇所を含む9頁を150dpiで実表示した。主要log六分類は0で、詳細は検証JSONを参照する。局所模型、source packing、固定次数d≥5の代数・残差packageに、全深部三重点のactual tensor比較、simplex境界の積漸近、全閉cornerのGH定理を統合。Sourceを含むquintic exteriorのcoarse metric geometryは独立な(TC)_5付き。全域のsharp co-Gramは粗い比較に加えて(PBE)_d付きであり、証明済みの三重点内のactive co-Gramと区別する。Bounded-densityからtensor比較を導く一般的推論は反例により排除した。
- `papers/cubical-gh-limit.tex`：Part V、現行v1.10は37頁。Abstract pruning–transportとdiam(C_5)=sqrt(13)は解析仮定と独立。本稿の全曲面actual degree-d GHへの適用経路は(CP)_d+(PBE)_d付きであり、このpackageの検証は未完。関連する[曲面fibration研究](https://github.com/uedakazushi/surface-lagrangian-torus-fibration)の `ke:global-metric-realization` は別の直接scalar/portal評価で同じ族の大域GH実現を与えるが、このpackage自体の検証を結論しない。
- 高次元ではmixed source–higher-stratum modelsの解析が残るためGH極限は予想。
- Fixed arrangement complement側Part I–IIIの正本は[multiscale-kaehler-einstein](https://github.com/uedakazushi/multiscale-kaehler-einstein)。固定空間の結果から族の一様性を自動的に導かない。

## 全深部三重点の actual semi-flat 比較

任意の固定次数 d≥5 の一般位置全平面退化で、三重点の全深度比・全角度に一様な actual KE 比較を証明した。正確な座標 ζ0ζ1ζ2=t、ell_i=−log|ζ_i|²、L=−log|t|²、R=log L とし、k_Lをlogarithmic simplex上のcomplete toric KE form、その実計量をg_L^sfとする。十分大きい固定m1と各qのCqについて、m≥m1、min ell_i≥mで
\[
\left|\log\frac{\omega_t^2}{k_L^2}\right|\le C/m,\qquad
\|g_t-g_L^{sf}\|_{C^q}\le C_q/m.
\]
定数は固定dと族に依存してよい。次数一様性は主張しない。証明の正本はKE主稿 `coarse:thm:full-triple-tensor`。

**Complete simplex模型の最小入力。** Part IV `coarse:lem:simplex-model` は、Zhang Theorem 2.1に明記されたCheng–Yauの標準実単体上の凸解存在・境界発散・実Hessian完備性を入力とする。一意性は内側homothety比較、tube完備性は有限長曲線の実射影、格子商の完備性は等長作用から直接証明する。w/Lはuniversal cover上の等長写像だが、4πの角度格子を4π/Lへ変える。固定周期商のinjectivity radius下界は結論しない。全深度比の正規化窓でpotentialとtensorの規格化を明示した。Zhangの定理文と適用条件は実読済みだが、CY1982 Theorem 4.4の原文・証明は未取得であり、原典確認済みとはしない。正確な書誌・係数点検・確認範囲は `research/source-audit.md`、直接証明は現行本文が正本である。 ψ_L=log L−Σlog ell_iに対する内外障壁、complete模型へのYau Schwarz、determinant比較、内部正則性、facet shiftとSavin小摂動による全深部O(1/m)比較の証明は保持する。Actual familyのQ-factorial性、actual距離buffer、TC/PBEを模型の存在入力に追加しない。

Actual側の大域入力は `coarse:cor:degree-d-volume-lower`。Adjunction residueでcanonical densityを固定し、backgroundによるHermitian frame errorの吸収と各正のcap方向のminorから六型のdeterminant下界を証明する。Sourceでは元のplane coordinatesを保つexact xy=tzとrescalingにより二つのcap係数≥c_d/Lを使う。Compact minimum原理からactual volume下界を得る。

**Capped-volume入力の確認：** Part IV v1.11では、正値性からweighted cap minors、pair/triple、六つの局所型、compact最小値原理、固定次数の大域下界までの指定証明鎖を実読した。結論を妨げる誤りは見つからず、零点を含むChern微分の正確なcap恒等式、曲率・frame誤差の明示的吸収条件、固定adjunction residue、有限coverから最後に小さい複素parameterを取る順序を補った。追加式と定数依存は別担当も独立点検した。全原著・全主稿の包括的検証とは区別する。

Full tripleの証明に必要なのは、この大域入力が供給する固定face ∂D_{t,m0}上の全phase・t一様なdensity下界だけである（`coarse:rem:full-triple-face-input`）。各固定tのradial closure×phase quotientがchartにcompactに含まれ、actual metricが近傍で滑らかなら、内外simplexのmaximum principleからinteriorのvolume sandwichを得る。Interiorのdensity下界、t一様な境界上界、actual tensor比較、actual距離の境界逃避を別に仮定しない。Shift評価で小さくなるv=log(ω_t²/k_L²)自身が、Ricci恒等式dd^cv=ω_t−k_Lによって小さい相対potentialとなる。全深部三重点の独立監査では大域capped densityを前段入力として分離し、それから先の領域・境界・全深度比・Savin/Schauderの連鎖を確認した。

**局所仮定クラスでの率の最適性。** `simplex:prop:boundary-floor-sharpness` のω_b,L=F_b* k_(L+3b)、F_b(w)=w+b·1は、全Lでc_*=(1/3)(m₀/(m₀+b))⁶という同じ境界floorを持つ。L=3mのbalanced点では相対実計量(m/(m+b))² Idと体積対数比−4log(1+b/m)が正確に成立する。L=m²、ell=(m²−2m,m,m)では−2b/m Idと−4b/mの一次項、O_b(m⁻²)の剰余を得る。これにより固定深度座標と既定k_Lへの比較を一般にo(1/m)へ改善できない。模型をfacet shiftで補正した後やcompact射影族の最適性は別課題である。後者の点列はnormalized simplexの境界へ近づく。本文は模型scalingとpure-model dominant-productだけを用い、actual定理を逆用しない。一般L展開とLだけの一律率がないことは研究ノートに置く。

## 全閉cornerの距離と同じLagrangian bundleによるGH収縮

三つのlabelsからなるJについて、C_J={w∈[0,1]^J:max w_i=1}を三枚のunit squaresからなる閉cornerとし、d_JはC_J自身の内在距離とする。Softmax hexagonの全phase preimage H_{t,R}にR^−2 g_tを入れると、projectionのdistortionはO(log R/R)である。H_{t,R}内の曲線だけを用いる内在距離と、外側保護領域{min ell_i>R/2}内の全曲線を許すprotected-ambient距離の双方で成立する。正本は `simplex:thm:closed-corner-model` / `simplex:cor:actual-closed-corner-metric`。

関連Lagrangian主稿 `ke:closed-corner-gh` / `ke:closed-corner-protected-gh` は、`ke:actual-closed-corner` と同じactual Lagrangian torus bundleと同じ射影に、このO(log R/R)のGH近似を与える。全fiberの非正規化intrinsic/ambient diameterはO(1/R)、正規化後はO(1/R²)、raw cubical mapとの誤差はO(log R/R)。Squareの継目・共通頂点でもfiberはregular T²である。模型のLie derivativeを評価したMoser pullback比較を使うため、粗い比較だけからGH距離を推論していない。

距離下界は両端をclippingしたdepth写像をcomplete simplex全体で定義し、active coordinateが一つなら係数1のSchwarz評価、二つならdominant product漸近を用いて全経路を制御する。上界は高々三枚のsquaresを通るgeodesicを内部へずらし、固定位相で持ち上げる。Seam collarが狭いという事実だけに依存しない。

C_Jには三枚自身の内在距離を用い、protected-ambient距離は全曲面X_tの距離とは区別する。曲面稿の `topo:coordinate-retraction` はtarget側の距離が全C_dの距離の制限と一致することを示すが、source側の保護領域外のshortcutを排除する定理ではない。全曲面のshortcutとsource・branch・coreを含む相対接着は曲面稿の直接評価で別に扱われ、本局所定理単独の帰結ではない。新規性の包括的確認と外部査読・形式証明は未実施。

## Simplex境界の鋭い積漸近とactive co-Gram

主稿 `papers/sections/simplex_boundary_geometry.tex` に次を証明する。全固定階のnormはangular universal coverの正規化された正則座標、または同値な模型covariant normで取り、全phaseに一様である。

- `simplex:lem:rank-one-schwarz`：各iについて |d log ell_i|_{g_L^sf}≤1。半平面へのrank-one Schwarz計算で正確な係数1を得る。
- `simplex:prop:dominant-product`：独立深度a,b、δ=(a+b)/L→0なら、二重cusp productに対してmodel誤差O(δ²)。Expanded quadrantとinner rectangleにより1≤k_L²/ω_prod²≤(πδ/sin πδ)^4を得て、Savinと線形化後のSchauder評価を用いる。Pure modelには深度の絶対的下限を置かない。
- `simplex:cor:actual-dominant-product`：actual誤差はO(1/min ell_i+δ²)。特に0<η<1/2、a,b∈[L^η/2,2L^(1−η)]の開正方形領域ではO(L^−η)。関連Lagrangian主稿 `ke:open-cell-collapse` は固定長方形Kη=[η,1−η]²への内在GH収束とprojection distortion O(L^−η)、fiber径O(L^−η)、raw誤差O(1/R)を与える。
- `simplex:prop:facet-product`：b=ell_0、a=ell_1、d_*=min(a,L−a)、b/d_*→0なら、cusp(b)×finite-annulus(a,width L)へのmodel誤差O((b/d_*)^(2/3))。Actual側にはO(1/b)を加える。比較rectangleの幅β=(b²d_*)^(1/3)で二つの誤差を釣り合わせる。
- `simplex:cor:active-cogram`：ell_i≤Le^−Aのactive indicesが一つまたは二つなら、d log ell_iのco-GramはId+O(e^(−A/2))。二つならO(e^−2A)へ改善し、actualにはO(1/min ell_i)を加える。

Actual chart内でexpanding product annuliとshifted-sinh下barrierを直接使う別の比較法も、`coarse:thm:moving-triple-tensor` / `coarse:cor:open-square-tensor` に保持する。いずれも有界densityだけでなく、小さいC0 potentialをSavinへ入力する。三重点内のこれらの結論には(TC)/(PBE)を仮定しない。

## 局所windowと残るtensor仮定

三つの深度が同程度のとき、一つの独立二座標product windowで任意半径のconstrained-cusp ballを覆うことはできない（`coarse:prop:triple-product-obstruction`）。最大深度を従属座標にする小さい相対箱は有効であり、全deep triple上のvolume上下界とbounded potentialは `coarse:cor:triple-volume-comparison` で証明する。このvolume比較単独ではtensor比較は得られず、上記のcomplete simplex barriersとSavinを組み合わせてfull tripleの比較を証明する。

Source gateのfixed model ballはoriented half-armを越える。Full source-coordinate extension上でdensity比較を行い、(TC)_5は**その点で有効なorientation**のmodelに対する下界として定式化する。全ての拡大窓で同じmodelのtensor比較を要求しない。任意半径のexhaustionはcoarse小窓構成の結論に含めず、dominant tripleでの証明と一般の(PBE)_dを分ける。

## 体積密度とtensor比較：現行の解析条件

`coarse:lem:complete-volume-upper` は、complete負KE背景hに対するu=log(ω²/h²)が上に有界という仮定の下で、Ricci下界に対するLaplacian型Omori–Yauとtr_hω=2+Δ_hu、算術幾何平均からω²≤h²を得る。Hessian型最大値原理は用いない。本稿のfinite ball、annulus–disc、product-annulus windowsでは、各固定tの有限angular quotient上でactual densityが人工境界を越えて有限に延長し、explicit complete modelのdensityが全人工境界で発散するのでu→−∞となる。周期的coverにはその上界を引き戻し、residual universal coverでは内部のfinite disc windowを使う。完備性だけから上有界性は導かず、非周期な無限coverへの適用には別の確認を要する。

主稿 `coarse:prop:density-counterexample` は、固定ball上で滑らかな負KE計量列の体積密度が正に一様有界でも、内側ballでtensorが一様有界とは限らないことを証明する。したがってvolume lower/upper estimatesだけを用いた局所tensor比較は使えない。

五次のexterior comparisonには独立な仮定 $(\mathrm{TC})_5$（`coarse:hyp:TC5`）を置く。これに依存するraw submetry、actual connectors、source diameter、粗い距離二側比較、$(\mathrm{CP})_5$ の検証も条件付きである。Raw coordinatesの代数的構成、閉セルの実現、determinant/volume評価、actual metric ballsを用いたsource inradius/escapeの議論、抽象有限距離論は、このtensor比較の推論から分離する。旧来の全証明を今回独立監査したことにはしない。

修復の具体的な十分条件は、各点にactual metric ballが入る一様bufferと、そこから負のholomorphic sectional curvatureを持つcomplete productへの正則写像である。`coarse:lem:actual-buffer-comparison` によりlocalized Chern–Luから一方向の比較を得て、volume upper boundと合わせる。Model metricでのbufferだけではactual bufferを証明したことにならず、欲しいcoarse distanceを先に使う循環を避ける。

## 位相・人工計量とactual metricの区別

候補\(\mathcal C_d\)の一般次数のセル数・\(\operatorname{Sk}_2\Delta^{d-1}\)との同相・整数ホモロジーはPart Vに証明がある。Lagrangian分岐基底\(B_d(T)\)からのcell-like写像は\(d\ge6\)では同相でないが、人工PL長さ距離によるdistortionは\(d=5\)で\(\Theta(\varepsilon^2)\)、\(d\ge6\)で\(\Theta(\varepsilon)\)であり、GH距離には各々対応する上界がある。証明の正本はLagrangian repoの`topo:metric-collapse-sharp`。
Actual計量への大域適用には(N) global no-shortcut、(S) square path lifts、(F) small fiber/portal connectorsが一つの十分条件であり、(F)は前二条件からは従わない（同repoの`topo:portal-counterexample`）。曲面稿の現行証明は、厳密な(S)の代わりに共通momentのendpoint portal比較を使う。閉corner定理単独は他の領域との大域的接続を含まない。Part IV–Vの\((CP)_d+(PBE)_d\)自体は依然未証明。六次Petersen木系は6点の\(S_6\)軌道をなすが、これはrealized KE計量の対称性を決めない。

## Lagrangian fibrationとの接続

標準負KE尺度での四実次元非崩壊極限と、$R_t^{-2}g_t$ のcubical候補を区別する。Zhang (MRL, 2015)の局所torus collapse定理はQ-factorialなtoroidal全空間を仮定するため、我々のsource $xy=tz$ へ直接適用しない。主稿序論に先行比較を統合した。閉corner内では同じactual Lagrangian fibrationの射影がGH近似となることを証明した。一方、Part Vの大域GH近似を既存大域fibrationのfiber収縮と同定するには、$\sup_x d_\square(\Phi_t(x),p_T\pi_t(x))\to0$ を全X_tで検証する必要がある。関連Lagrangian主原稿の `topo:ke-map-compatibility` がその十分性を示す。本稿Part Vの特定の写像Φ_tとの一様近接性を別途証明したとはしない。一方、曲面稿は `ke:global-metric-realization` において同じ f_t=p_Tπ_t 自体のdistortionを直接評価し、この比較条件を経由せずに大域実現する。

### K5の相対接着と五次の同時atlas/GH実現

曲面改訂38の `ke:moment-relative-replacement` / `ke:relative-replacement-gh` は条件付きの安定性を与える。同じ保持cornerと全K2 end collars、sourceのcompact nodal neighborhoods、向き・加法定数を含むcanonical momentとanchor cuts、coreと変更collarを保ち、実際のmarked product/cone商と全overlapのwhole-fiber一致が得られれば、同じcubical targetへの値の差はCη、η=A(1+log(N+1))/R以下に取れる。変更する葉の座標やdiffeomorphismの微分の小ささは要求しない。この条件付き評価を主担当の証明・別担当の独立点検から同期する。五次のcompatible dataについては `ng8:quintic-full-moment` が両端の切片・framing、全neck intervalのstrict cutsと全開overlapを実現し、`ke:quintic-simultaneous-realization` がこの相対評価を同じ射影へ適用する。任意に既固定の追加annuli・大きいsource tailsを保持する相対存在は結論しない。六次は標準等重みPetersenの場合に別の全moment定理で実現する。

既存の直接監査は、固定coupling chartsのregular-leaf periodsとbasic＋exact cutoff、固定graph gaugeのexact Moser、actual作用によるprimitive平均とnontrapping、全end collarsに相対的な葉族補間を対象とした。固定stage・残余compact・cuts・有限bufferの後にt閾値を取る順序を確認した。曲面稿 `ng8:fixed-fiber-relative-dh` は各固定tのfree bandで、全空間のt=0延長なしにStokesによるreduced areaのaffine性を与えるが、positive target areas・総量一致・全protected collarsの余裕・端germs・marked identificationsは別に要る。Sourceのμ=0を横切る標準模型の面積π(c−|μ|)と、raw moment o(1)だけではlongitude誤差が消えない例を有効な障害として保持する。いずれも既存P0の訂正やPart IV/Vの新tensor入力、CP/PBE/TCの検証ではない。

## Source-free neckの座標・作用周期・解析条件

正本は主稿の `papers/sections/source_free_neck_coordinates.tex` と `papers/sections/source_free_neck_comparison.tex`。二重線のsourceと三重点を避ける固定compact baseに対して次を証明した。Moving baseやmoving endの一様性は別問題である。

- `pair:prop:bundle-conic`：射影的法線束の表示を先に固定し、h=−F_d/∏_{k≠i,j}L_k、h0=h|Dとしてx_i'=x_i h0/h、x_j'=x_jでexact uv=tを得る。Base、labelled axes、normal first jetを保ち、固定compact上で一様な正則逆を持つ。局所conic overlapをcomplete C*の自己同型と扱う旧証明をこの明示構成で置き換えた。
- `pair:cor:normal-circle` / `pair:prop:canonical-normal-moment`：同じ正則normal S¹と、η_t=Aω_tに対するcanonical μ_tを構成。ι_Vη_t=−dμ_t、dμ_t(−JV)=η_t(V,JV)>0。周期は1で、patchごとの加法定数はない。
- `pair:cor:global-primitive`：open base上の非消滅正則1-form τを選び、Ω=dlog v∧τ、λ_t=d^c log(ω_t²/|Ω|²)を一つの大域primitiveとする。τの変更ではnormal momentは不変だが、residual periodsのためにprimitiveの選択は保持する。
- `pair:prop:fixed-end-transfer`：固定end collarsのlog-densityのC¹収束と極限成分のradial 4/s評価から同じcanonical momentの両端漸近を得る。全複素t・全phaseとr先行の量化を保ち、Hermitian normによる深度差O(1)が生むO(s_r^−2)を吸収する。
- `pair:rem:normal-frame-winding`：全orbit上のholomorphic frame変更Ω↦bΩはmomentを−2π wind(b)だけ移す。Zero windingならnonbasic unitでもnormal momentを保つが、primitiveの残余閉periodは別に保持する。
- `pair:thm:fixed-end-moment` / `pair:cor:actual-common-moment`：s_r=−log r²として両固定endのmomentは±4π/s_r+O(s_r^(−1−δ))+o_t(1)。rを小さく固定した後でt→0とする。Song, arXiv:1706.01518, Definition 2.3 / Lemmas 4.4–4.5とRochon–Zhang, arXiv:1106.0873, (5.5)–(5.6) / Theorem 5.1を用い、η_tのreductionsに共通のintervalを得る。
- `neck:prop:volume-envelope`：固定residual compact上でc h_t²≤ω_t²≤h_t²。ただし誤差はO(1)である。`neck:prop:residual-boundary-obstruction`はexact negative KE productでも固定residual境界の影響が消えないことを示す。Actual compact familyへの反例ではない。
- `neck:lem:rank-one-circle`：p*h_D≤Aωかつω²≤B(h_A+h_D)²ならnormal real vectorsについてg_ω≤AB g_A。Mixed termsを許す。Actual metric ballの一様bufferを別途仮定すればnormal circleの長さはO(1/min(s,M−s))となる。この補題自体はbufferを証明しない。必要な固定段階bufferは曲面稿K1–K2の別結果である。
- `neck:prop:small-density-coupled`：一般のsmooth negative KE背景h_tに対しsmall log-volume errorから同率のtensor誤差を得る。積分離は要求しない。Complete strip×curve上への延長・完備性・global bounded log-ratioがあればproductを同定できるが、そのglobal仮定は未検証である。

関連Lagrangian主稿 `ke:staged-neck-averaging` は、一つのnormal circleを先に平均し、endで残る円を平均することで、同じactual normal actionと全marked action periodsを保つ。共通のdomain/image bufferの下で一段階構成や整数基底変更とHamiltonian比較できる。`ke:staged-closed-corner-gh` は指定primitive subgroupに適合するactual triple bundleにも同じGH誤差O(log R/R)を与える。旧bundleと同一のfiber分割は主張しない。固定base上のprimitiveとmoment intervalだけからは、neck全体のflow生存、tripleとの同一作用、reduced foliationの同時整合は従わない。曲面稿のK1–K2がこれらを固定段階で別に構成する。本稿の `pair:lem:diagonal-fixed-end` は、固定K・固定endの結果を選んだ遅い対角列に適用する量化と有限予算の吸収だけを定式化し、bufferそのものは供給しない。

Sourceを含む固定baseでは、曲面稿の `ke:source-inclusive-fixed-shell` を正本とする。Source-inclusive正規形x′y′=t h_t(p)と同じΩ_t=dlog x′∧dpを用い、固定rのend/shellが中央成分のsmooth locusのcompactへ収束することを確認する。Ω_tはsourceでdx′∧dy′/(t h′_t(p))と非零正則に延び、period 1のend値±4π/s_rとrに共通の正のshell横断費用を得る。全複素tの閾値は固定rに依存し、異なる正規形のprimitiveやresidual periodsを無条件に同一視しない。この証明は曲面原稿にだけ置き、Part IVのsource-free定理の範囲は保持する。

## 曲面側の相対面積実現とcoreの条件

曲面稿 `ng8:componentwise-critical-area` は、保持領域Kの補集合成分U_αごとの面積保存と、各critical region D_hへの正の配分を同時に課す。自由cell D_h∩U_αにだけ正のx_hαを置き、row sumをtargetからK内の固定質量を引いた値、column sumをU_αの実面積とする有限条件が、同じrelative Diff0 orbit内の面積実現と同値である。`ng8:strict-area-cuts` は成分ごとの総量一致とstrict Hall cutに帰着させる。全総量と各regionのmarginだけでは足りない。全可動面積と要求量がaffineなら両端の確認で十分だが、一般のsmooth familyだけから端点判定の十分性は従わない。

`ng8:p0-source-protected-reduction` / `ng8:p0-small-area-flexibility` はactual P0のsourceを通るregular閉葉の飽和annuliを保持する。固定t・小さいcompact moment区間では自由部分がμ=0を跨いで滑らかで、incidence graphは連結となる。Spanning-treeの線形右逆とcell内部のbump densityから、総和零で十分小さい滑らかな面積増分を、normal moment・source全近傍・end germs・whole-fiber接着を保って実現する。Sourceを含む絶対面積やprotected massの滑らかさは不要であり、t一様な面積余裕や所定の大きいtargetの実現は結論しない。

Core側は `ke:anchor-liouville-actions`、`ke:anchor-stokes-budget` と `ke:actual-anchor-fan-criterion` を使う。同じprimitiveと周期1のcycleで、M=δ−ρ<0、anchor period Aを固定すればLiouville fillingのcritical actionは A(q−ρ)/(δ−ρ) である。Neckの直線c+pqとの一致にはA=p(δ−ρ)、c=−pρが必要で、primitiveが異なる場合は残余period差と整数framingも式に残す。実際のanchor葉が所定のK4／Petersen period値を持ち、保持overlapの標識と符号が一致する場合には同じdomain・skeleton上に作用chartを得る。Stokesが与える総量一致は有限配分の全cutや反対側のopen germsを代替しない。この条件付き構成と微小面積実現だけから同時atlas/GHを推論しない。五次の同時実現には、次の有限両端条件と全moment構成を用いる。Part IV/Vの新解析入力ではない。

五次の限定actual適用は曲面稿 `ke:k4-actual-end-anchor`（改訂39に統合済み）に置く。正のresiduesを固定し、十分大きいstage j、その後N、最後にt閾値を選ぶ。Anchor q_a=δ=4π/Nでは、標準K2 end collarsの最内境界をsource label B=5.45b_jに取れる。これはprimitive切替え終了5.4と全actual交わりの下限5.5の間にあり、min ell>3b_jの広いconstruction domainと5b_j<B<9b_jの共通葉族を使う。深度比に一様な二作用評価からQ_ab=ν_b−ρ_b<−ρ_b/2を全境界で得る。同じ正meridiansのclutchingは直線のnormal bundle O(1)とP0のisotopiesで確認できるので、任意の有向四角形のK4 targetsを実現する。Sourceの全compact pinched fibersの飽和近傍は各固定tで|μ|<δ/2に選び、anchor上には追加保持annuliを置かない。この局所系単独は、既指定の大きいsource近傍、一般の追加保持annuli、全neck interval・反対側germsの整合を結論しない。局所系の独立点検と、以下の新しい全moment証明の点検を分ける。

五次の全moment構成の正本は曲面稿の `neck_action_matching.tex`、両端periodと全域接続の正本は `global_action_atlas.tex` である。前半の `ng8:relative-dh`・`ng8:straight-neck`・`ng8:central-criterion` は全moment bandでcircle作用が自由なsource-free neckに限る。Actual source-inclusive neckには固定tでもμ=0の固定点があり、全sourceを数える `ng8:actual-source-area-wall` と `ng8:source-corrected-area-demand` を用いる。Targetと保護質量の同じwallを差し引いた自由需要が全intervalで滑らかとなり、商全体の滑らかなbundle性や面積自体のaffine性を仮定しない。

`ke:k4-actual-neck-periods` は共通primitiveの残余定数を同定し、source数・整数勾配・正residueの切片に関する有限二式を与える。`ng8:uniform-k2-end-periods` はfull-triple primitiveから全momentでO(1/b_r)のend period上界を得る。`ng8:thin-source-tail-choice` は固定end massを除いた初期rooted-tree近傍の追加質量にDiniを適用する。解析領域・cutsと小さいtを先に選び、source同定S_tとK2 radial補正Dを変えずに同じmarked class内でthin葉を取る。Sourceとsaddleの点近傍では局所葉をμに依存させない。同じ初期葉から通常P0と作用指定版をそれぞれ作るため、葉の微分一様性やthin幅の選択後の追加t閾値は不要である。`ng8:quintic-full-moment` は成分別面積Moserと有限source sectionsのfirst-jet補正を用い、両coreの全開collarで作用と全葉を一致させる。

`ke:quintic-simultaneous-realization` はこれを全十neck・五coreへ適用し、実数平行移動を含む全三面共通の整数affine transitionを明示して、同じactual Lagrangian射影にdenominator 1の作用適合matroidal atlasと全域GH実現を与える。Focus valuesには穿孔focus affine structureを用いる。等重みと対称六系の配分(3,1,1)は有限条件の明示解であり、五次の存在に追加の未検証解析仮定はない。結論は各tでの同時実現であって、atlas自体のt方向の極限や極限距離のHessian性を含まない。各固定stageとtで初期葉・全nodal neighborhoodsを選ぶ存在であり、任意の既指定大近傍の保存、t方向に滑らかなfibration族は主張しない。六次の標準等重み同時実現は別定理である。CP/PBE/TCとH_loc/H_ancも未検証のままである。指定証明鎖の内部点検と、外部査読・形式証明・新規性の包括確認は区別する。

一次比較では、Fernández de Bobadilla–Pełka Remark 5.9の正則部分のaction-affine構造とTheorem 6.14の構成された補助計量によるproperな全fiberのGH結果、Evans–Mauri Remarks 2.11–2.12のcontact/Liouville作用座標を認めた上で、actual負KE形式・branch/coreを含むatlas・同じ射影の全域GH実現という接続を比較する。正確な参照先と範囲は研究ノートに置く。

**六次の標準Petersen同時実現。** 曲面現行保存版（改訂46）の `ke:petersen-full-moment` と `ke:sextic-simultaneous-realization` は、六つの標準Petersen系の一つ、等重みw_i,j=2/5、各二重線のsource配分(1,1,1,1;2)を固定し、初期source葉を構成中に選ぶ範囲で、同じactual射影に作用atlas・全域GH実現・確率体積極限を与える。内部二端cutの累積位置はbalanced separatorとthin blockで調整し、正marginの後に中央parameterをfreezeしてからfull source annuliを固定する。Core domain・primitiveは先に固定し、anchor葉は全moment構成後に選ぶ。現在の同期では定理の仮定・結論、全開接着・相対GHへの接続を実読し、曲面側の指定独立点検の記録を確認した。全六次証明の新たな包括監査ではない。任意の非等重み、先指定された大きいsource近傍、t方向に滑らかなfibration族、atlasのparameter極限とHessian性は含まない。

## 次の課題

1. 現在の局所安定性と最適性の公表へ向け、指定一次比較と主張範囲を整理する。固定深度座標でのO(1/m)の最適性を踏まえたfacet shiftの選択条件と補正済み模型への剰余の改善は、独立の後続課題とし、公表条件にしない。一般の境界入力が三つの定数shiftだけで記述できるとは仮定しない。Zhangの固定normalized compact集合、Ruanの全域coarse・torus-average比較との違いを保ち、CY1982原文取得と先行比較を続ける。既存のcapped-volume/full-triple/fixed-end監査を一律に反復せず、曲面の固定stage bufferと全域scalar/portal経路の依存を保持する。
2. 五次の全moment・同時実現を公表範囲に組み込み、有限両端条件、source wallと全tail、初期選択からの二構成、全開overlapの依存を保つ。六次の標準等重みPetersen targetsは曲面現行保存版（改訂46）で全moment・両anchor・全open接着まで証明されている。その仮定と依存の公表上の明確化を優先する。任意に追加した保持annuli・大きいsource tailsの相対可解性も別に検査する。五次の初期葉を選ぶ存在を任意既固定P0への変更へ広げない。既存の共有解析・K2/K3/K5監査を全外部入力の包括的再監査と扱わない。
3. 曲面改訂38の四型分類は既存P0と有限targetの帰結として保持し、適用する中間尺度でR_t ε_t/a_t→0を確認する。成分錐の頂点を指定する場合はtarget変位も尺度予算へ入れる。Part Iの固定空間の全中心一様性、raw/probability face mass、metric linkと標識付きincidence、Abel極限と有理型延長の入力を使い分け、未確認の退化族への適用は具体的な定理と量化へ戻って点検する。
4. 独立の解析課題としてsourceを含むexteriorの(TC)_5、(PBE)_dのquantitative terminal trivialization・protected rectangular inclusion・uniform comparison・two-metric escape、および(CP)_dのconnectorsを検証する。固定baseの定理を任意速度のmoving領域へ拡張せず、bounded densityをtensor比較へ読み替えない。これらの強いpackageの解決を曲面global結果の完成条件へ戻さない。
5. 高次元mixed source modelsと一般のsecondary completionは、現在の固定次数曲面の公表準備と別の優先順位で扱う。

## 保存・検証

回収元TeXのSHA-256は `research/source-manifest.json`、現行の主張・監査範囲は `research/source-audit.md`、現行source/PDFのSHA-256と実行状態は `research/validation.json` に置く。回収時に3原稿のLuaLaTeX組版と、統合稿5 scripts・旧v0.12の16 scriptsの再実行を行った。検査は有限組合せ・式・bookkeepingに限られ、未完成の解析証明を代替しない。詳細は `research/migration.md`。

現行資料にはexplicit bundle coordinates、canonical moment、fixed-end漸近、weighted cap determinant、source residue、全三重点比較、simplex境界漸近、閉corner評価を保持する。局所安定性定理 `coarse:thm:boundary-to-triple` とその適用を分離し、別担当がモデル・shift比較・小摂動評価・全平面族への適用を内部点検した。SavinのH1/H2/H4・Theorem 1.3もその担当が一次資料で再確認した。Capped density→full-triple固定face→fixed-end/canonical moment→遅い対角列という既存の共有入力監査は保持し、今回全てを反復したとはしない。Yau Theorems 1–2、Zhang Theorem 2.1・Proposition 2.2等の既存一次照合の範囲は研究ノートに記す。Cheng–Yau 1982原典全証明、全主稿の包括監査、外部査読、形式証明、新規性の包括的確認は未了である。

Part IV v1.15は126頁に組版し、未定義参照・引用、重複label、欠字、LaTeX error、overfull/underfullの六分類は全て0。1–2・7–9・60–62・125頁の9頁を150dpiで個別に実表示し、和英要約、Introductionと先行比較、最適性命題11.4の二例と全証明、追加Ruan書誌に欠字・重なり・切断・数式やURLのはみ出しを認めない。全126頁の逐頁表示ではない。内容不変のPart V v1.10は既存37頁・指定5頁表示の記録を保持し、今回は再組版・再表示していない。有限計算証明書も今回再実行していない。各source/PDF hashと実行環境はvalidation.jsonに記す。

研究資料v1.28は、固定深度座標での局所安定性率の最適性とZhang/Ruanとの指定比較を統合し、曲面現行保存版（改訂46）の等重みPetersen同時実現と測度系の適用範囲を同期する。確認した保存commitは曲面 `46e128e47bd536e577afad24641d6461fe6169e8`、固定側 `2926300c2425c7e68550ac08ee81a2afa639a0c6`（Part I v1.10・総説v1.14・資料v1.19）である。曲面側の既存の組版・表示記録と、本repoで今回行った確認を区別する。IV/Vの既存の科学引用pin（曲面改訂37・`32c67aefe6beb47c2955923e2b6eb2471d48af31`）は維持し、新しい六次の証明は曲面側を正本とする。保存・hub更新は別に確認する。

## 共通研究原則と保存許可（研究固有方針から独立）

数学的重要性・新規性・理解の深化・応用可能性・正確性・実現可能性を総合して方針を更新する。証明済み・仮定付き・未完成・予想・計算観察、既知結果と独自結果、草稿の証明と今回の監査を区別する。重要文献は一次資料の正確な定理と仮定を確認する。日本語LuaLaTeXで公表原稿と十分な証明を保持し、有効なアイデア・反例・計算は現行ノートに統合する。再現コード・証明書・入力を残すが旧版/中間出力は蓄積しない。区切りごと承諾なしに通常コミットで `main` へpush、15–30分を目安に切り良く保存する。force pushとGitHub Actions追加/起動はしない。Library旧資料は削除しないがGitHub移行後は定常二重保存しない。先に対象repoへ保存してからresearch-hubを更新し、数学検証・組版・GitHub・hubを別々に確認する。
