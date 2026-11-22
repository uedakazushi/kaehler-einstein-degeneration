# 現行研究方針：一般型超曲面の負Kähler–Einstein退化

更新：2026-11-22 / v1.20・現行研究方針（Part IV–V本文はv1.10）

## 公表に向けた実行計画

数学的重要性、新規性、理解の深化、応用可能性、正確性、読者による検証、実現可能性を総合し、研究全体の価値を最大化する。[三研究の公表計画](https://github.com/uedakazushi/surface-lagrangian-torus-fibration/blob/main/00_research_plan.md)に従い、本repoでは曲面P0を支える無条件の局所解析をPart IVの中心に置く。CP/PBE/TCの解決を局所成果の公表条件にしない。

1. Exact triple領域、各固定parameterの滑らかなradial閉包と全phase quotient、固定faceの一様密度下界を入力とする局所安定性定理 `coarse:thm:boundary-to-triple` を抽出した。境界上界にparameter一様性が不要であることを証明の向きとともに明示し、全平面退化への適用を `coarse:thm:full-triple-tensor` に分けた。証明は一回だけ掲載する。
2. 題名・abstract・主結果を、局所安定性、complete simplexと閉corner、source-free neckと固定end、条件付きexterior/PBEの順に整理した。条件付き結果と必要な証明も保持する。
3. 曲面主稿の実際の引用を逆引きし、capped lowerとoriented upper、full-tripleとsimplex、normal circle、束座標・共通primitive・固定endの最小四入力表を主稿 `tab:surface-minimal-inputs` に置いた。領域、全位相、定数、cutの選択順と曲面側が別に証明する事項を明記する。
4. Part Vの抽象距離論と(CP)+(PBE)付きactual適用、曲面の直接scalar/portal経路の役割を整理した。曲面の数学入力の引用は実読した改訂37・commit `32c67aefe6beb47c2955923e2b6eb2471d48af31` に固定し、局所K4系を統合した研究入口・改訂39と区別する。
5. 変更した局所定理の指定証明鎖を別担当も内部点検し、LuaLaTeX組版・相互参照と指定16頁の表示を確認した。ZhangのQ-factorial/simple toroidalな全空間の結果はsource方程式 \(xy=tz\) へ無条件に適用しない。全原著証明・全主稿の包括監査と定量的新規性の確認は残る。

達成基準は、曲面P0が使う局所解析を最小の正確な入力と一意の証明場所から検証できること。これは全主稿の包括的再監査、外部査読、投稿の完了を意味しない。原稿・ノート・方針・READMEの保存後、利用側の依存表とresearch-hubへ実際の到達点を反映する。共通の一般原則・保存許可は本書後半と `AGENTS.md` に記す。


### 実行状況と次の課題

Part IV v1.10に最小境界入力からの局所安定性定理と全平面退化への適用を分けて統合し、別担当が指定証明鎖を点検した。入口・abstract・主結果と曲面P0の四入力表を整理し、Part Vの条件付き経路との範囲を明示した。次はこの最小入力核から逆向きに未点検の証明・一次資料を確認し、曲面の直接経路との依存関係を保った公表稿を確定する。CP/PBE/TC、同時atlas、高次元化は別の未解決課題である。Part IV v1.10は119頁、Part V v1.10は37頁に組版し、指定16頁の表示確認まで完了した。実施範囲・残るfont/bookmark警告・source/PDFのハッシュはREADMEとvalidationを参照する。

## 研究固有の目標

固定次数d≥5の一般型曲面の全平面退化について、actual KE計量の局所一様解析と、それを大域的な径尺度の極限へ接続するための正確な入力を整える。本稿には全深部三重点のtensor比較、全閉cornerの局所GH収縮、source-freeな固定compact baseの正則normal action・canonical primitive・共通moment intervalの証明がある。全曲面のGH極限とactual Lagrangian射影による実現には曲面repoに別の直接scalar/portal証明があるため、その共有局所入力と量化の接続を最優先で監査する。本repoの(CP)/(PBE)/(TC)という強い解析package自体の検証は残る。高次元のmixed source–higher-stratum modelsは後続課題とする。

## 三研究の共同方針と正本

研究・編集・証明監査は一体で進め、以下の正本分担を保つ。三つの本文を一つに機械的に統合せず、重複する証明は所有repoへ集約して具体的な定理を参照する。

| 正本 | 担当する結果 | 本repoとの接続 |
| --- | --- | --- |
| [multiscale-kaehler-einstein](https://github.com/uedakazushi/multiscale-kaehler-einstein) | 固定配置補空間の空間無限遠・residual complex periods・conifold localization（Part I–III） | 固定成分は P² から d−1 本の直線を除いたもの。固定空間の漸近を退化族のmoving領域へ直接適用しない。 |
| 本repo | 退化族の局所一様解析（Part IV）、条件付きpruning–transportと有限target距離（Part V） | Capped density、full triple、fixed-end momentを曲面側へ供給する。CP/PBE/TCの未検証部分を保持する。 |
| [surface-lagrangian-torus-fibration](https://github.com/uedakazushi/surface-lagrangian-torus-fibration) | Actual KE Lagrangian構成と同じ合成写像の全曲面GH実現 | Source-inclusive fixed-shell、固定段階buffer・同一moment接着・core filling・scalar/portal評価と、その全域歪みからの中間尺度分類を所有する。作用atlasとの同時成立は別問題。 |

共有入力は [研究ノート](research/notes.md) の依存表と曲面側の `research/ke-dependencies.md` で、定理・仮定・尺度・固定/可動領域・確認版を照合する。Part IIのsecondary complex periodsと第二symplectic actionは同一視しない。Part IIIの(H_loc)/(H_anc)も別模型の仮定として残す。方針・本文・ノートを先に保存し、その結果をhubの短い要約へ反映する。

固定補空間側のPart I v1.7（研究一式v1.12）は、連結smooth projective・reduced SNC・K+D ampleの範囲で、n=1と空境界のcompact caseを含む。Hermitian depthsを保つ可換collars・全残余一様なRZ延長比較・一面tensor評価からmetric-IRFAを検証し、properな1-Lipschitz全射Sと有界加法誤差Kを構成する。固定基点からのblow-downは一意である。固定したSについて、中心oと半径Aに一様に、ambient閉球のGH誤差は3K/(2R)以下で、比較先の中心はS(o)/Rである。指定compact集合をSで零へ送る選択もでき、その場合Kはその集合に依存してよい。LDPと、非空境界のexact tail・joint law・distance Laplace transformは通常の全face volume-IRFAで成立し、指数的volume remainderを追加仮定しない。正本・ラベル・独立点検と共同監査の範囲は研究ノートに記す。

同じ固定空間のmoving-basepoint blow-downは、cone内の有界基点極限、または面αに沿うEuclidean因子とincidence link coneの積に分類され、任意に指定した拡大列に対して全て実現する。正のα座標を持つstarと、最小weighted座標m>2Aでのambient閉A球の厳密な積同定を用いる。Closed star全体のambient積表示は一般に成り立たない。距離だけから復元するのはmetric linkの等長型であり、標識付きcell分割・depth重み・geodesic-ray boundaryの復元は含めない。Leuzingerのlocally symmetric cone比較・radial公式、Bridson–Haefligerの標準cone幾何との重なりを正本Introductionに明記する。

同稿の面ごとの測度付き平行移動は、任意のnormal中心vectorでmin T_i→∞なら、通常volume-IRFAから全残余strip上の全変動収束を得る。Metric-IRFAと収束するnormal offset・残余基点も仮定すると、固定gのscale-one積極限と全半径のambient閉球測度の全変動収束が成立する。Smooth volume-IRFAを必要としない。滑らかな基準曲率からの有界primitiveを用いる直接Stokes・face mass規格化、および全faceのvolume漸近に基づくMellinの一様momentとincidenceは共同点検として同期する。交点数公式のface massは非正規化KE体積に対応し、確率版では全体積で割る。通常volume-IRFAからのAbel極限は有理型延長を意味せず、1/t誤差による反例と追加のjoint polyhomogeneity条件を区別する。これらの証明は固定空間のものであり、退化族の一様bufferやCP/PBE/TCへ移さない。

公表範囲の依存表では、距離に必要なmetric-IRFA、測度に必要なordinary volume-IRFA、交点数のbounded primitive、複素有理型延長の追加条件を分ける。Part II v2.1のsecondary periodはcomponent-labelled collarとdeeper-face labelsを伴う収束から得る標識付き残余曲線であり、複素periodにはKähler orientationも保持する。向きだけを忘れる場合にもfactor/cusp labelsは保持し、一般secondary WP completionのcontrolled parallel push-off仮定は残す。Chambert–Loir–Tschinkelのresidue measures・Igusa積分の先行結果と本稿のordinary L1/一側Abel条件の比較は、正本Introductionと一次資料監査に委ねる。

曲面改訂38の `topo:cubical-local-models` / `topo:cubical-moving-blowups` と `ke:intermediate-moving-classification` は、同じP0のdistortion ε_tに対しa_t→∞、a_t/R_t→0、R_t ε_t/a_t→0の尺度で、任意の移動基点の全pointed GH極限を、成分錐C_{2,d−1}、R×Y_{d−2}、全角3π/2のEuclidean錐、R²の四型に分類する。Y_mは原点を共有するm本の半直線であり、各型の有限基点を指定した尺度・退化列で実現できる。`ke:intermediate-component-cone` の成分頂点を基点とする結論にはtarget変位も吸収し、component coreと変更collarの任意基点へ適用する。証明は曲面稿の既存全域歪みと有限targetの局所計量幾何による。固定Part Iの定理の退化族への直接適用や、Part IV/Vの新しいtensor入力ではなく、CP/PBE/TCの未検証状態を変えない。

## 論文と証明の状態

- `papers/kaehler-einstein-degeneration.tex`：Part IV、現行v1.10は119頁。局所模型、source packing、固定次数d≥5の代数・残差packageに、全深部三重点のactual tensor比較、simplex境界の積漸近、全閉cornerのGH定理を統合。Sourceを含むquintic exteriorのcoarse metric geometryは独立な(TC)_5付き。全域のsharp co-Gramは粗い比較に加えて(PBE)_d付きであり、証明済みの三重点内のactive co-Gramと区別する。Bounded-densityからtensor比較を導く一般的推論は反例により排除した。
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

固定toric模型の存在・完備性にはZhang (2015), §2.1, Theorem 2.1 / Proposition 2.2を用いる（退化族のTheorem 2.4とQ-factorial仮定は使わない）。ψ_L=log L−Σlog ell_iに対してψ_L−(log3)/2≤φ_L≤ψ_L、V_L/3≤k_L²≤V_Lを内外にずらした障壁で証明する。Complete模型から三つの半平面へのYau Schwarz lemma、determinant比較、内部正則性により一様cusp geometryを得る。凸性からfacet shiftのlog-density差をO(1/min ell)とし、actual計量を内外のsimplex KE metricsでvolume比較する。Savinの小摂動定理でtensor・全高階誤差へ移る。Actual metric bufferや(TC)/(PBE)を前提としない。

Actual側の大域入力は `coarse:cor:degree-d-volume-lower`。Adjunction residueでcanonical densityを固定し、backgroundによるHermitian frame errorの吸収と各正のcap方向のminorから六型のdeterminant下界を証明する。Sourceでは元のplane coordinatesを保つexact xy=tzとrescalingにより二つのcap係数≥c_d/Lを使う。Compact minimum原理からactual volume下界を得る。

Full tripleの証明に必要なのは、この大域入力が供給する固定face ∂D_{t,m0}上の全phase・t一様なdensity下界だけである（`coarse:rem:full-triple-face-input`）。各固定tのradial closure×phase quotientがchartにcompactに含まれ、actual metricが近傍で滑らかなら、内外simplexのmaximum principleからinteriorのvolume sandwichを得る。Interiorのdensity下界、t一様な境界上界、actual tensor比較、actual距離の境界逃避を別に仮定しない。Shift評価で小さくなるv=log(ω_t²/k_L²)自身が、Ricci恒等式dd^cv=ω_t−k_Lによって小さい相対potentialとなる。全深部三重点の独立監査では大域capped densityを前段入力として分離し、それから先の領域・境界・全深度比・Savin/Schauderの連鎖を確認した。

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

### K5の相対接着と同じ射影でのatlasへの経路

曲面改訂38の `ke:moment-relative-replacement` / `ke:relative-replacement-gh` は条件付きの安定性を与える。同じ保持cornerと全K2 end collars、sourceのcompact nodal neighborhoods、向き・加法定数を含むcanonical momentとanchor cuts、coreと変更collarを保ち、実際のmarked product/cone商と全overlapのwhole-fiber一致が得られれば、同じcubical targetへの値の差はCη、η=A(1+log(N+1))/R以下に取れる。変更する葉の座標やdiffeomorphismの微分の小ささは要求しない。この条件付き評価を主担当の証明・別担当の独立点検から同期する。五次の標準K2 end collarsだけを保持する局所anchor問題は下記の新系で解決したが、追加の保持annuli・六次の面積条件、両端の切片・framingと全neck intervalの整合はなお未解決である。

既存の直接監査は、固定coupling chartsのregular-leaf periodsとbasic＋exact cutoff、固定graph gaugeのexact Moser、actual作用によるprimitive平均とnontrapping、全end collarsに相対的な葉族補間を対象とした。固定stage・残余compact・cuts・有限bufferの後にt閾値を取る順序を確認した。曲面稿 `ng8:fixed-fiber-relative-dh` は各固定tのfree bandで、全空間のt=0延長なしにStokesによるreduced areaのaffine性を与えるが、positive target areas・総量一致・全protected collarsの余裕・端germs・marked identificationsは別に要る。Sourceのμ=0を横切る標準模型の面積π(c−|μ|)と、raw moment o(1)だけではlongitude誤差が消えない例を有効な障害として保持する。いずれも既存P0の訂正やPart IV/Vの新tensor入力、CP/PBE/TCの検証ではない。

## Source-free neckの座標・作用周期・解析条件

正本は主稿の `papers/sections/source_free_neck_coordinates.tex` と `papers/sections/source_free_neck_comparison.tex`。二重線のsourceと三重点を避ける固定compact baseに対して次を証明した。Moving baseやmoving endの一様性は別問題である。

- `pair:prop:bundle-conic`：射影的法線束の表示を先に固定し、h=−F_d/∏_{k≠i,j}L_k、h0=h|Dとしてx_i'=x_i h0/h、x_j'=x_jでexact uv=tを得る。Base、labelled axes、normal first jetを保ち、固定compact上で一様な正則逆を持つ。局所conic overlapをcomplete C*の自己同型と扱う旧証明をこの明示構成で置き換えた。
- `pair:cor:normal-circle` / `pair:prop:canonical-normal-moment`：同じ正則normal S¹と、η_t=Aω_tに対するcanonical μ_tを構成。ι_Vη_t=−dμ_t、dμ_t(−JV)=η_t(V,JV)>0。周期は1で、patchごとの加法定数はない。
- `pair:cor:global-primitive`：open base上の非消滅正則1-form τを選び、Ω=dlog v∧τ、λ_t=d^c log(ω_t²/|Ω|²)を一つの大域primitiveとする。τの変更ではnormal momentは不変だが、residual periodsのためにprimitiveの選択は保持する。
- `pair:thm:fixed-end-moment` / `pair:cor:actual-common-moment`：s_r=−log r²として両固定endのmomentは±4π/s_r+O(s_r^(−1−δ))+o_t(1)。rを小さく固定した後でt→0とする。Song, arXiv:1706.01518, Definition 2.3 / Lemmas 4.4–4.5とRochon–Zhang, arXiv:1106.0873, (5.5)–(5.6) / Theorem 5.1を用い、η_tのreductionsに共通のintervalを得る。
- `neck:prop:volume-envelope`：固定residual compact上でc h_t²≤ω_t²≤h_t²。ただし誤差はO(1)である。`neck:prop:residual-boundary-obstruction`はexact negative KE productでも固定residual境界の影響が消えないことを示す。Actual compact familyへの反例ではない。
- `neck:lem:rank-one-circle`：p*h_D≤Aωかつω²≤B(h_A+h_D)²ならnormal real vectorsについてg_ω≤AB g_A。Mixed termsを許す。Actual metric ballの一様bufferを別途仮定すればnormal circleの長さはO(1/min(s,M−s))となる。この補題自体はbufferを証明しない。必要な固定段階bufferは曲面稿K1–K2の別結果である。
- `neck:prop:small-density-coupled`：一般のsmooth negative KE背景h_tに対しsmall log-volume errorから同率のtensor誤差を得る。積分離は要求しない。Complete strip×curve上への延長・完備性・global bounded log-ratioがあればproductを同定できるが、そのglobal仮定は未検証である。

関連Lagrangian主稿 `ke:staged-neck-averaging` は、一つのnormal circleを先に平均し、endで残る円を平均することで、同じactual normal actionと全marked action periodsを保つ。共通のdomain/image bufferの下で一段階構成や整数基底変更とHamiltonian比較できる。`ke:staged-closed-corner-gh` は指定primitive subgroupに適合するactual triple bundleにも同じGH誤差O(log R/R)を与える。旧bundleと同一のfiber分割は主張しない。固定base上のprimitiveとmoment intervalだけからは、neck全体のflow生存、tripleとの同一作用、reduced foliationの同時整合は従わない。曲面稿のK1–K2がこれらを固定段階で別に構成する。本稿の `pair:lem:diagonal-fixed-end` は、固定K・固定endの結果を選んだ遅い対角列に適用する量化と有限予算の吸収だけを定式化し、bufferそのものは供給しない。

Sourceを含む固定baseでは、曲面稿の `ke:source-inclusive-fixed-shell` を正本とする。Source-inclusive正規形x′y′=t h_t(p)と同じΩ_t=dlog x′∧dpを用い、固定rのend/shellが中央成分のsmooth locusのcompactへ収束することを確認する。Ω_tはsourceでdx′∧dy′/(t h′_t(p))と非零正則に延び、period 1のend値±4π/s_rとrに共通の正のshell横断費用を得る。全複素tの閾値は固定rに依存し、異なる正規形のprimitiveやresidual periodsを無条件に同一視しない。この証明は曲面原稿にだけ置き、Part IVのsource-free定理の範囲は保持する。

## 曲面側の相対面積実現とcoreの条件

曲面稿 `ng8:componentwise-critical-area` は、保持領域Kの補集合成分U_αごとの面積保存と、各critical region D_hへの正の配分を同時に課す。自由cell D_h∩U_αにだけ正のx_hαを置き、row sumをtargetからK内の固定質量を引いた値、column sumをU_αの実面積とする有限条件が、同じrelative Diff0 orbit内の面積実現と同値である。`ng8:strict-area-cuts` は成分ごとの総量一致とstrict Hall cutに帰着させる。全総量と各regionのmarginだけでは足りない。全可動面積と要求量がaffineなら両端の確認で十分だが、一般のsmooth familyだけから端点判定の十分性は従わない。

`ng8:p0-source-protected-reduction` / `ng8:p0-small-area-flexibility` はactual P0のsourceを通るregular閉葉の飽和annuliを保持する。固定t・小さいcompact moment区間では自由部分がμ=0を跨いで滑らかで、incidence graphは連結となる。Spanning-treeの線形右逆とcell内部のbump densityから、総和零で十分小さい滑らかな面積増分を、normal moment・source全近傍・end germs・whole-fiber接着を保って実現する。Sourceを含む絶対面積やprotected massの滑らかさは不要であり、t一様な面積余裕や所定の大きいtargetの実現は結論しない。

Core側は `ke:anchor-liouville-actions`、`ke:anchor-stokes-budget` と `ke:actual-anchor-fan-criterion` を使う。同じprimitiveと周期1のcycleで、M=δ−ρ<0、anchor period Aを固定すればLiouville fillingのcritical actionは A(q−ρ)/(δ−ρ) である。Neckの直線c+pqとの一致にはA=p(δ−ρ)、c=−pρが必要で、primitiveが異なる場合は残余period差と整数framingも式に残す。実際のanchor葉が所定のK4／Petersen period値を持ち、保持overlapの標識と符号が一致する場合には同じdomain・skeleton上に作用chartを得る。Stokesが与える総量一致は有限配分の全cutや反対側のopen germsを代替しない。この条件付き構成と微小面積実現を、同じ射影のatlas/GH完成又はPart IV/Vの新解析入力とはしない。

五次の限定actual適用は曲面稿 `ke:k4-actual-end-anchor`（改訂39に統合済み）に置く。正のresiduesを固定し、十分大きいstage j、その後N、最後にt閾値を選ぶ。Anchor q_a=δ=4π/Nでは、標準K2 end collarsの最内境界をsource label B=5.45b_jに取れる。これはprimitive切替え終了5.4と全actual交わりの下限5.5の間にあり、min ell>3b_jの広いconstruction domainと5b_j<B<9b_jの共通葉族を使う。深度比に一様な二作用評価からQ_ab=ν_b−ρ_b<−ρ_b/2を全境界で得る。同じ正meridiansのclutchingは直線のnormal bundle O(1)とP0のisotopiesで確認できるので、任意の有向四角形のK4 targetsを実現する。Sourceの全compact pinched fibersの飽和近傍は各固定tで|μ|<δ/2に選び、anchor上には追加保持annuliを置かない。この量化では局所core chartを得るが、既指定の大きいsource近傍、一般の追加保持annuli、全neck interval・反対側germsの整合は結論しない。今回の独立点検はこの指定経路の範囲に限る。

## 次の課題

1. 公表の中心となる最小局所入力核から逆向きに、未点検の前段証明・一次資料と定量的新規性を確認する。今回確認した局所定理の証明を一律に再監査せず、capped density、source-free neck、固定成分収束のうち実際の利用に必要で未確認の箇所を特定して進める。曲面の直接scalar/portal経路との依存関係を保ち、正確な仮定と一意の証明場所を備えた公表稿を確定する。
2. Atlas側では、五次の標準K2 end collarsに対する局所K4 anchor実現を出発点とし、追加の保持annuliを指定する場合と六次Petersenの有限面積条件を調べる。全neck intervalの所定targetsについては実際のsource保護領域と全parameterのstrict cutsを検証し、反対側neckの切片、同じprimitiveの残余periodと整数framing、全open overlapのwhole-fiber一致を確かめる。局所coreの達成を全intervalの実現へ読み替えない。条件が揃った相対構成には `ke:moment-relative-replacement` のGH比較を適用する。既存の共有解析・K2/K3/K5監査は保持し、全外部入力の再監査済みとはしない。
3. 曲面改訂38の四型分類は既存P0と有限targetの帰結として保持し、適用する中間尺度でR_t ε_t/a_t→0を確認する。成分錐の頂点を指定する場合はtarget変位も尺度予算へ入れる。Part Iの固定空間の全中心一様性、raw/probability face mass、metric linkと標識付きincidence、Abel極限と有理型延長の入力を使い分け、未確認の退化族への適用は具体的な定理と量化へ戻って点検する。
4. 独立の解析課題としてsourceを含むexteriorの(TC)_5、(PBE)_dのquantitative terminal trivialization・protected rectangular inclusion・uniform comparison・two-metric escape、および(CP)_dのconnectorsを検証する。固定baseの定理を任意速度のmoving領域へ拡張せず、bounded densityをtensor比較へ読み替えない。これらの強いpackageの解決を曲面global結果の完成条件へ戻さない。
5. 高次元mixed source modelsと一般のsecondary completionは、現在の固定次数曲面の公表準備と別の優先順位で扱う。

## 保存・検証

回収元TeXのSHA-256は `research/source-manifest.json`、元監査は `research/source-audit.md`、現行source/PDFのSHA-256と実行状態は `research/validation.json` に置く。回収時に3原稿のLuaLaTeX組版と、統合稿5 scripts・旧v0.12の16 scriptsの再実行を行った。検査は有限組合せ・式・bookkeepingに限られ、未完成の解析証明を代替しない。詳細は `research/migration.md`。

現行資料にはexplicit bundle coordinates、canonical moment、fixed-end漸近、weighted cap determinant、source residue、全三重点比較、simplex境界漸近、閉corner評価を保持する。現行v1.10では局所安定性定理 `coarse:thm:boundary-to-triple` とその適用を分離し、別担当がモデル・shift比較・小摂動評価・全平面族への適用を内部点検した。SavinのH1/H2/H4・Theorem 1.3もその担当が一次資料で再確認した。Capped density→full-triple固定face→fixed-end/canonical moment→遅い対角列という既存の共有入力監査は保持し、今回全てを反復したとはしない。Yau Theorems 1–2、Zhang Theorem 2.1・Proposition 2.2等の既存一次照合の範囲は研究ノートに記す。Cheng–Yau 1982原典全証明、全主稿の包括監査、外部査読、形式証明、新規性の包括的確認は未了である。

2026-11-22にPart IV v1.10を119頁、Part V v1.10を37頁にLuaLaTeX/latexmkで組版した。最終logの未定義参照・引用、重複ラベル、欠字、LaTeX error、overfull/underfull boxは全て0。Font feature・斜体・微小math fontの代替とPDF bookmark数式の警告は残る。IVの1、2、6、9–11、51–54、119頁（11頁）とVの1–3、5、37頁（5頁）を150 dpiで単頁PNGへrenderして実表示し、題名・abstract・入力表・局所定理と証明・適用・引用に見切れ、重なり、欠落、数式のはみ出しを認めなかった。全頁の表示確認と有限検算の再実行は行っていない。LuaTeX-ja、Harano Aji、CM/AMS/RSFS vector fontsを備えた環境を用い、通常のlatexmk/SyncTeX設定とbuild出力を保持する。

研究資料v1.20は、曲面改訂39に統合済みの限定actual K4系とPart I v1.7の公表準備を参照する。局所K4の指定証明鎖に対する独立点検をノート・検証JSONに記した。Part IV–V本文の曲面引用は実読した改訂37・commit `32c67aefe6beb47c2955923e2b6eb2471d48af31` に固定している。旧確認版の証明・表示記録を新しい現行版の実施結果へ読み替えない。固定Part Iの新しい四項目に対する限定した独立点検と、各repo担当の組版・表示確認も区別し、詳細と保存commitは研究ノート・検証JSONへ集約する。本repo担当による外部稿の再組版・再表示はない。証明記載、内部点検、計算、組版、GitHub反映、hub更新を別々の状態として扱う。

## 共通研究原則と保存許可（研究固有方針から独立）

数学的重要性・新規性・理解の深化・応用可能性・正確性・実現可能性を総合して方針を更新する。証明済み・仮定付き・未完成・予想・計算観察、既知結果と独自結果、草稿の証明と今回の監査を区別する。重要文献は一次資料の正確な定理と仮定を確認する。日本語LuaLaTeXで公表原稿と十分な証明を保持し、有効なアイデア・反例・計算は現行ノートに統合する。再現コード・証明書・入力を残すが旧版/中間出力は蓄積しない。区切りごと承諾なしに通常コミットで `main` へpush、15–30分を目安に切り良く保存する。force pushとGitHub Actions追加/起動はしない。Library旧資料は削除しないがGitHub移行後は定常二重保存しない。先に対象repoへ保存してからresearch-hubを更新し、数学検証・組版・GitHub・hubを別々に確認する。
