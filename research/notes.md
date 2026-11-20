# 研究ノート：5平面退化と一般型超曲面
2026-11-20 / v1.0

## Candidate cubical complex
(mathcal C_5=\{w\in[0,1]^5:\max_iw_i=1,\ |\operatorname{supp}w|\le3\}\)。既存草稿のcell数は ((f_0,f_1,f_2)=(25,50,30))、位相は (\bigvee^4 S^2)、標準cubical metricではdiameter (\sqrt{13}) と記録。これらは**幾何学的候補・有限計算の状態**であり、actual KE metricの無条件収束証明ではない。

## 観測されたmatching構造
(L_t=-\log|t|^2,\ R_t=\log L_t\)。三重点近傍 (xyz=t\vartheta) で (\ell_x+\ell_y+\ell_z=L_t+O(1))、neck/corner incidenceで (\log\Lambda_{e,\tau}=R_t+\log(1-p_z)+O(L_t^{-1})\)。\(\max_e|\tau_{e,t}|=o(R_t)\) なら、overlap-compatibleなmodel familyのfirst-scale cubical metricには影響しないという条件付き構造。

## 二つのJacobi zero modes
Mandel reduced familyにおいて (u_0=(1+w^2)^{-2}) はscale方向、(u_1=(w+w^3/3)(1+w^2)^{-2}) はend-degree/asymmetry方向に対応する。五点源のrelative degree jump (a_+-a_-=5) はabsolute degreeではない。三つのcuspを含むpair-of-pantsでの (5=(1+1)+(1+1+1)) と整合させる必要がある。

## 主要な解析的障害
root-0 bounded shiftsとroot-1以上のcusp-dependent scale tracesを、一つのnonlinear Lyapunov–Schmidt/scattering matchingに組み込み、実際のKE metricに対してsublinear correctionを得ること。reference softmax cornerの対角translationはactual Calderón responseに直結しない。\(Gamma(2)\) の標準/common channelのfinite-order非退化性から、全尺度のuniform invertibilityは直ちには従わない。

## 移行と再現の状態
元Libraryの `README_v12.md`, `MANIFEST_v12.json` と16 certificate scriptsの記録を参照。コードがGitHubに置かれていても今回実行したかは別途明記する。論文草稿のupLaTeX構成をLuaLaTeXへ移す際は、実際の組版成功と数学検証を区別する。
