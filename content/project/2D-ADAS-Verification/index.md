---
title: Enhanced Verification and Falsification for ADAS Safety and Security Based on Reachability Analysis and Deep Reinforcement Learning
summary: Enhanced Verification and Falsification for ADAS Safety and Security Based on Reachability Analysis and Deep Reinforcement Learning.
tags:
  - Formal Analysis
  - Reachability Analysis
  - Reinforcement Learning

date: '2024-09-17T00:00:00Z'

# Optional external URL for project (replaces project detail page).
#external_link: 'https://github.com/liuluddex/2D-ADAS-Verification'

#image:
#  caption: Photo by rawpixel on Unsplash
#  focal_point: Smart

links:
#  - icon: twitter
#    icon_pack: fab
#    name: Follow
#    url: https://twitter.com/georgecushen
url_code: 'https://github.com/liuluddex/2D-ADAS-Verification'
#url_pdf: ''
#url_slides: ''
#url_video: ''

# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
#slides: example
---

<style>
  .article-container {
    max-width: 1270px !important;
    padding: 0 20px 0 20px;
    margin: 0 auto 0 auto;
  }
  
  .full_table {
    display: table;
    width: 80%;
  }
  
  .full_table table thead {
    display: table;
    width: 80%;
  }
  
  .full_table table tbody {
    display: table;
    width: 80%;
  }

  table {
    width: 80%;
    border-collapse: collapse;
    text-align: center;
  }

  .featured-image {
      width: 60%;   /* 设置宽度为720px */
      height: auto;   /* 保持图片的纵横比 */
  }

  th {
    background-color: black; /* 将表格头部背景颜色设为黑色 */
    color: white; /* 表头文字设为白色 */
    padding: 10px;
    text-align: center; /* 水平居中 */
    vertical-align: middle; /* 垂直居中 */
  }

  td {
    padding: 10px;
    border: 1px solid #ddd;
    text-align: center; /* 水平居中 */
    vertical-align: middle; /* 垂直居中 */
  }

  /* 确保跨行的单元格居中 */
  td[rowspan] {
    text-align: center;        /* 水平居中 */
    vertical-align: middle;    /* 垂直居中 */
  }
  
  th[rowspan] {
    text-align: center;        /* 水平居中 */
    vertical-align: middle;    /* 垂直居中 */
  }

  figure img {
    width: 80%;
    height: auto;
  }
</style>

- [Hybrid Automaton Modeling](#hybrid-automaton-modeling)
  - [Vehicle Parameters](#vehicle-parameters)
  - [Invariance of Discrete Modes](#invariance-of-discrete-modes)
  - [Transition Relation](#transition-relation)

- [Experimental Results](#experimental-results)
  - [Application Validation](#application-validation)
  - [Reachable Sets with Cyberattacks](#reachable-sets-with-cyberattacks)
  - [Tool Error Comparisons](#tool-error-comparisons)
  - [Performance Comparison of Attack Strategy Search Algorithms](#performance-comparison-of-attack-strategy-search-algorithms)

### Hybrid Automaton Modeling

#### Vehicle Parameters

<table>
    <script type="text/javascript" async
      src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
    </script>
    <caption>Tab. 1. Parameters of Vehicles</caption>
    <thead>
        <tr>
            <th></th>
            <th>Quality</th>
            <th>Cornering Stiffness of Front Tires</th>
            <th>Cornering Stiffness of Rear Tires</th>
            <th>Distance between CG and Front Axle</th>
            <th>Distance between CG and Rear Axle</th>
            <th>Inertia of Z-axle</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Symbol</td>
            <td>m</td>
            <td>\(C_f\)</td>
            <td>\(C_r\)</td>
            <td>\(l_f\)</td>
            <td>\(l_r\)</td>
            <td>\(I_z\)</td>
        </tr>
        <tr>
            <td>Unit</td>
            <td>kg</td>
            <td>N/rad</td>
            <td>N/rad</td>
            <td>m</td>
            <td>m</td>
            <td>-</td>
        </tr>
        <tr>
            <td>Value</td>
            <td>1945</td>
            <td>92064</td>
            <td>92064</td>
            <td>1.265</td>
            <td>1.895</td>
            <td>4095</td>
        </tr>
    </tbody>
</table>


#### Invariance of Discrete Modes

<table>
    <script type="text/javascript" async
      src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
    </script>
    <caption>Tab. 2. Invariance of Discrete Modes</caption>
    <thead>
        <tr>
            <th>Mode</th>
            <th>State</th>
            <th>Invariance</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan="6">\(q_1\) (CC)</td>
            <td>\(S_1\)</td>
            <td>\(d_r \geq 75 \& L_{y_1} \leq d_1 \& L_{y_2} \leq d_1 \& \theta_1 = 0 \& \theta_2 = 0\)</td>
        </tr>
        <tr>
            <td>\(S_2\)</td>
            <td>\(d_r \geq 75 \& L_{y_1} \leq d_1 \& L_{y_2} \geq d_1 \& \theta_1 = 0 \& \theta_2 \leq \frac{\pi}{2}\)</td>
        </tr>
        <tr>
            <td>\(S_3\)</td>
            <td>\(d_r \geq 75 \& L_{y_1} \leq d_1 \& L_{y_2} \geq d_1 \& \theta_1 = 0 \& \theta_2 \geq \frac{\pi}{2}\)</td>
        </tr>
        <tr>
            <td>\(S_4\)</td>
            <td>\(d_r \geq 75 \& L_{y_1} \geq d_1 \& L_{y_2} \geq d_1 \& \theta_1 \leq \frac{\pi}{2} \& \theta_2 \leq \frac{\pi}{2}\)</td>
        </tr>
        <tr>
            <td>\(S_5\)</td>
            <td>\(d_r \geq 75 \& L_{y_1} \geq d_1 \& L_{y_2} \geq d_1 \& \theta_1 \leq \frac{\pi}{2} \& \theta_2 \geq \frac{\pi}{2}\)</td>
        </tr>
        <tr>
            <td>\(S_6\)</td>
            <td>\(d_r \geq 75 \& L_{y_1} \geq d_1 \& L_{y_2} \geq d_1 \& \theta_1 \geq \frac{\pi}{2} \& \theta_2 \geq \frac{\pi}{2}\)</td>
        </tr>
        <tr>
            <td rowspan="6">\(q_2\) (ACC)</td>
            <td>\(S_1\)</td>
            <td>\(vy_2 - vy_1 \leq 0 \& -(d_r - 3) - 1.6 * (vy_2 - vy_1) \leq 0 \& d_r \geq 3 \& d_r \leq d_0 \& Ly_1 \leq d_1 \& Ly_2 \leq d_1 \& \theta_1 = 0 \& \theta_2 = 0\)</td>
        </tr>
        <tr>
            <td>\(S_2\)</td>
            <td>\(vy_2 - vy_1 \leq 0 \& -(d_r - 3) - 1.6 * (vy_2 - vy_1) \leq 0 \& d_r \geq 3 \& d_r \leq d_0 \& Ly_1 \leq d_1 \& Ly_2 \geq d_1 \& \theta_1 = 0 \& \theta_2 \leq \frac{\pi}{2}\)</td>
        </tr>
        <tr>
            <td>\(S_3\)</td>
            <td>\(vy_2 - vy_1 \leq 0 \& -(d_r - 3) - 1.6 * (vy_2 - vy_1) \leq 0 \& d_r \geq 3 \& d_r \leq d_0 \& Ly_1 \leq d_1 \& Ly_2 \geq d_1 \& \theta_1 = 0 \& \theta_2 \geq \frac{\pi}{2}\)</td>
        </tr>
        <tr>
            <td>\(S_4\)</td>
            <td>\(vy_2 - vy_1 \leq 0 \& -(d_r - 3) - 1.6 * (vy_2 - vy_1) \leq 0 \& d_r \geq 3 \& d_r \leq d_0 \& Ly_1 \geq d_1 \& Ly_2 \geq d_1 \& \theta_1 \leq \frac{\pi}{2} \& \theta_2 \leq \frac{\pi}{2}\)</td>
        </tr>
        <tr>
            <td>\(S_5\)</td>
            <td>\(vy_2 - vy_1 \leq 0 \& -(d_r - 3) - 1.6 * (vy_2 - vy_1) \leq 0 \& d_r \geq 3 \& d_r \leq d_0 \& Ly_1 \geq d_1 \& Ly_2 \geq d_1 \& \theta_1 \leq \frac{\pi}{2} \& \theta_2 \geq \frac{\pi}{2}\)</td>
        </tr>
        <tr>
            <td>\(S_6\)</td>
            <td>\(vy_2 - vy_1 \leq 0 \& -(d_r - 3) - 1.6 * (vy_2 - vy_1) \leq 0 \& d_r \geq 3 \& d_r \leq d_0 \& Ly_1 \geq d_1 \& Ly_2 \geq d_1 \& \theta_1 \geq \frac{\pi}{2} \& \theta_2 \geq \frac{\pi}{2}\)</td>
        </tr>
        <tr>
            <td rowspan="6">\(q_3\) (AEB)</td>
            <td>\(S_1\)</td>
            <td>\(vy_2 - vy_1 \leq 0 \& -(d_r - 3) - 1.6 * (vy_2 - vy_1) \geq 0 \& -(d_r - 3) - 0.6 * (vy_2 - vy_1) \leq 0 \& d_r \geq 3 \& d_r \leq d_0 \& Ly_1 \leq d_1 \& Ly_2 \leq d_1 \& \theta_1 = 0 \& \theta_2 = 0\)</td>
        </tr>
        <tr>
            <td>\(S_2\)</td>
            <td>\(vy_2 - vy_1 \leq 0 \& -(d_r - 3) - 1.6 * (vy_2 - vy_1) \geq 0 \& -(d_r - 3) - 0.6 * (vy_2 - vy_1) \leq 0 \& d_r \geq 3 \& d_r \leq d_0 \& Ly_1 \leq d_1 \& Ly_2 \geq d_1 \& \theta_1 = 0 \& \theta_2 \leq \frac{\pi}{2}\)</td>
        </tr>
        <tr>
            <td>\(S_3\)</td>
            <td>\(vy_2 - vy_1 \leq 0 \& -(d_r - 3) - 1.6 * (vy_2 - vy_1) \geq 0 \& -(d_r - 3) - 0.6 * (vy_2 - vy_1) \leq 0 \& d_r \geq 3 \& d_r \leq d_0 \& Ly_1 \leq d_1 \& Ly_2 \geq d_1 \& \theta_1 = 0 \& \theta_2 \geq \frac{\pi}{2}\)</td>
        </tr>
        <tr>
            <td>\(S_4\)</td>
            <td>\(vy_2 - vy_1 \leq 0 \& -(d_r - 3) - 1.6 * (vy_2 - vy_1) \geq 0 \& -(d_r - 3) - 0.6 * (vy_2 - vy_1) \leq 0 \& d_r \geq 3 \& d_r \leq d_0 \& Ly_1 \geq d_1 \& Ly_2 \geq d_1 \& \theta_1 \leq \frac{\pi}{2} \& \theta_2 \leq \frac{\pi}{2}\)</td>
        </tr>
        <tr>
            <td>\(S_5\)</td>
            <td>\(vy_2 - vy_1 \leq 0 \& -(d_r - 3) - 1.6 * (vy_2 - vy_1) \geq 0 \& -(d_r - 3) - 0.6 * (vy_2 - vy_1) \leq 0 \& d_r \geq 3 \& d_r \leq d_0 \& Ly_1 \geq d_1 \& Ly_2 \geq d_1 \& \theta_1 \leq \frac{\pi}{2} \& \theta_2 \geq \frac{\pi}{2}\)</td>
        </tr>
        <tr>
            <td>\(S_6\)</td>
            <td>\(vy_2 - vy_1 \leq 0 \& -(d_r - 3) - 1.6 * (vy_2 - vy_1) \geq 0 \& -(d_r - 3) - 0.6 * (vy_2 - vy_1) \leq 0 \& d_r \geq 3 \& d_r \leq d_0 \& Ly_1 \geq d_1 \& Ly_2 \geq d_1 \& \theta_1 \geq \frac{\pi}{2} \& \theta_2 \geq \frac{\pi}{2}\)</td>
        </tr>
        <tr>
            <td rowspan="6">\(q_4\) (STOP)</td>
            <td>\(S_1\)</td>
            <td>\(vy_1 \geq 1 \& d_r \geq 3 \& Ly_1 \leq d_1 \& Ly_2 \leq d_1 \& \theta_1 = 0 \& \theta_2 = 0\)</td>
        </tr>
        <tr>
            <td>\(S_2\)</td>
            <td>\(vy_1 \geq 1 \& d_r \geq 3 \& Ly_1 \leq d_1 \& Ly_2 \geq d_1 \& \theta_1 = 0 \& \theta_2 \leq \frac{\pi}{2}\)</td>
        </tr>
        <tr>
            <td>\(S_3\)</td>
            <td>\(vy_1 \geq 1 \& d_r \geq 3 \& Ly_1 \leq d_1 \& Ly_2 \geq d_1 \& \theta_1 = 0 \& \theta_2 \geq \frac{\pi}{2}\)</td>
        </tr>
        <tr>
            <td>\(S_4\)</td>
            <td>\(vy_1 \geq 1 \& d_r \geq 3 \& Ly_1 \geq d_1 \& Ly_2 \geq d_1 \& \theta_1 \leq \frac{\pi}{2} \& \theta_2 \leq \frac{\pi}{2}\)</td>
        </tr>
        <tr>
            <td>\(S_5\)</td>
            <td>\(vy_1 \geq 1 \& d_r \geq 3 \& Ly_1 \geq d_1 \& Ly_2 \geq d_1 \& \theta_1 \leq \frac{\pi}{2} \& \theta_2 \geq \frac{\pi}{2}\)</td>
        </tr>
        <tr>
            <td>\(S_6\)</td>
            <td>\(vy_1 \geq 1 \& d_r \geq 3 \& Ly_1 \geq d_1 \& Ly_2 \geq d_1 \& \theta_1 \geq \frac{\pi}{2} \& \theta_2 \geq \frac{\pi}{2}\)</td>
        </tr>
    </tbody>
</table>

#### Transition Relation

<table>
    <script type="text/javascript" async
      src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
    </script>
    <caption>Tab. 3. Transition Relation</caption>
    <thead>
        <tr>
            <th>Source Mode</th>
            <th>Source State</th>
            <th>Target Mode</th>
            <th>Target State</th>
            <th>Condition</th>
            <th>Reset</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>\(q_1\) (CC)</td>
            <td>\(S_1\)</td>
            <td>\(q_1\) (CC)</td>
            <td>\(S_2\)</td>
            <td>\(Ly_1 \leq d_1 \& Ly_2 \geq d_1\)</td>
            <td>\(\delta_2' := 0.5, r_2' := 0\)</td>
        </tr>
        <tr>
            <td>\(q_2\) (ACC)</td>
            <td>\(S_1\)</td>
            <td>\(q_2\) (ACC)</td>
            <td>\(S_2\)</td>
            <td>\(Ly_1 \leq d_1 \& Ly_2 \geq d_1\)</td>
            <td>\(\delta_2' := 0.5, r_2' := 0\)</td>
        </tr>
        <tr>
            <td>\(q_3\) (AEB)</td>
            <td>\(S_1\)</td>
            <td>\(q_3\) (AEB)</td>
            <td>\(S_2\)</td>
            <td>\(Ly_1 \leq d_1 \& Ly_2 \geq d_1\)</td>
            <td>\(\delta_2' := 0.5, r_2' := 0\)</td>
        </tr>
        <tr>
            <td>\(q_4\) (STOP)</td>
            <td>\(S_1\)</td>
            <td>\(q_4\) (STOP)</td>
            <td>\(S_2\)</td>
            <td>\(Ly_1 \leq d_1 \& Ly_2 \geq d_1\)</td>
            <td>\(\delta_2' := 0.5, r_2' := 0\)</td>
        </tr>
        <tr>
            <td>\(q_1\) (CC)</td>
            <td>\(S_2\)</td>
            <td>\(q_1\) (CC)</td>
            <td>\(S_3\)</td>
            <td>\(Ly_1 \leq d_1 \& Ly_2 \geq d_1 \& \theta_2 \geq \frac{\pi}{2}\)</td>
            <td>\(\delta_2' := 0, r_2' := 0\)</td>
        </tr>
        <tr>
            <td>\(q_2\) (ACC)</td>
            <td>\(S_2\)</td>
            <td>\(q_2\) (ACC)</td>
            <td>\(S_3\)</td>
            <td>\(Ly_1 \leq d_1 \& Ly_2 \geq d_1 \& \theta_2 \geq \frac{\pi}{2}\)</td>
            <td>\(\delta_2' := 0, r_2' := 0\)</td>
        </tr>
        <tr>
            <td>\(q_3\) (AEB)</td>
            <td>\(S_2\)</td>
            <td>\(q_3\) (AEB)</td>
            <td>\(S_3\)</td>
            <td>\(Ly_1 \leq d_1 \& Ly_2 \geq d_1 \& \theta_2 \geq \frac{\pi}{2}\)</td>
            <td>\(\delta_2' := 0, r_2' := 0\)</td>
        </tr>
        <tr>
            <td>\(q_4\) (STOP)</td>
            <td>\(S_2\)</td>
            <td>\(q_4\) (STOP)</td>
            <td>\(S_3\)</td>
            <td>\(Ly_1 \leq d_1 \& Ly_2 \geq d_1 \& \theta_2 \geq \frac{\pi}{2}\)</td>
            <td>\(\delta_2' := 0, r_2' := 0\)</td>
        </tr>
        <tr>
            <td>\(q_1\) (CC)</td>
            <td>\(S_2\)</td>
            <td>\(q_1\) (CC)</td>
            <td>\(S_4\)</td>
            <td>\(Ly_1 \geq d_1 \& Ly_2 \geq d_1 \& \theta_1 \leq \frac{\pi}{2} \& \theta_2 \leq \frac{\pi}{2}\)</td>
            <td>\(\delta_1' := 0.5, r_1' := 0\)</td>
        </tr>
        <tr>
            <td>\(q_2\) (ACC)</td>
            <td>\(S_2\)</td>
            <td>\(q_2\) (ACC)</td>
            <td>\(S_4\)</td>
            <td>\(Ly_1 \geq d_1 \& Ly_2 \geq d_1 \& \theta_1 \leq \frac{\pi}{2} \& \theta_2 \leq \frac{\pi}{2}\)</td>
            <td>\(\delta_1' := 0.5, r_1' := 0\)</td>
        </tr>
        <tr>
            <td>\(q_3\) (AEB)</td>
            <td>\(S_2\)</td>
            <td>\(q_3\) (AEB)</td>
            <td>\(S_4\)</td>
            <td>\(Ly_1 \geq d_1 \& Ly_2 \geq d_1 \& \theta_1 \leq \frac{\pi}{2} \& \theta_2 \leq \frac{\pi}{2}\)</td>
            <td>\(\delta_1' := 0.5, r_1' := 0\)</td>
        </tr>
        <tr>
            <td>\(q_4\) (STOP)</td>
            <td>\(S_2\)</td>
            <td>\(q_4\) (STOP)</td>
            <td>\(S_4\)</td>
            <td>\(Ly_1 \geq d_1 \& Ly_2 \geq d_1 \& \theta_1 \leq \frac{\pi}{2} \& \theta_2 \leq \frac{\pi}{2}\)</td>
            <td>\(\delta_1' := 0.5, r_1' := 0\)</td>
        </tr>
        <tr>
            <td>\(q_1\) (CC)</td>
            <td>\(S_3\)</td>
            <td>\(q_1\) (CC)</td>
            <td>\(S_5\)</td>
            <td>\(Ly_1 \geq d_1 \& Ly_2 \geq d_1 \& \theta_1 \leq \frac{\pi}{2} \& \theta_2 \geq \frac{\pi}{2}\)</td>
            <td>\(\delta_1' := 0.5, r_1' := 0\)</td>
        </tr>
        <tr>
            <td>\(q_2\) (ACC)</td>
            <td>\(S_3\)</td>
            <td>\(q_2\) (ACC)</td>
            <td>\(S_5\)</td>
            <td>\(Ly_1 \geq d_1 \& Ly_2 \geq d_1 \& \theta_1 \leq \frac{\pi}{2} \& \theta_2 \geq \frac{\pi}{2}\)</td>
            <td>\(\delta_1' := 0.5, r_1' := 0\)</td>
        </tr>
        <tr>
            <td>\(q_3\) (AEB)</td>
            <td>\(S_3\)</td>
            <td>\(q_3\) (AEB)</td>
            <td>\(S_5\)</td>
            <td>\(Ly_1 \geq d_1 \& Ly_2 \geq d_1 \& \theta_1 \leq \frac{\pi}{2} \& \theta_2 \geq \frac{\pi}{2}\)</td>
            <td>\(\delta_1' := 0.5, r_1' := 0\)</td>
        </tr>
        <tr>
            <td>\(q_4\) (STOP)</td>
            <td>\(S_3\)</td>
            <td>\(q_4\) (STOP)</td>
            <td>\(S_5\)</td>
            <td>\(Ly_1 \geq d_1 \& Ly_2 \geq d_1 \& \theta_1 \leq \frac{\pi}{2} \& \theta_2 \geq \frac{\pi}{2}\)</td>
            <td>\(\delta_1' := 0.5, r_1' := 0\)</td>
        </tr>
        <tr>
            <td>\(q_1\) (CC)</td>
            <td>\(S_4\)</td>
            <td>\(q_1\) (CC)</td>
            <td>\(S_5\)</td>
            <td>\(Ly_1 \geq d_1 \& Ly_2 \geq d_1 \& \theta_1 \leq \frac{\pi}{2} \& \theta_2 \geq \frac{\pi}{2}\)</td>
            <td>\(\delta_2' := 0, r_2' := 0\)</td>
        </tr>
        <tr>
            <td>\(q_2\) (ACC)</td>
            <td>\(S_4\)</td>
            <td>\(q_2\) (ACC)</td>
            <td>\(S_5\)</td>
            <td>\(Ly_1 \geq d_1 \& Ly_2 \geq d_1 \& \theta_1 \leq \frac{\pi}{2} \& \theta_2 \geq \frac{\pi}{2}\)</td>
            <td>\(\delta_2' := 0, r_2' := 0\)</td>
        </tr>
        <tr>
            <td>\(q_3\) (AEB)</td>
            <td>\(S_4\)</td>
            <td>\(q_3\) (AEB)</td>
            <td>\(S_5\)</td>
            <td>\(Ly_1 \geq d_1 \& Ly_2 \geq d_1 \& \theta_1 \leq \frac{\pi}{2} \& \theta_2 \geq \frac{\pi}{2}\)</td>
            <td>\(\delta_2' := 0, r_2' := 0\)</td>
        </tr>
        <tr>
            <td>\(q_4\) (STOP)</td>
            <td>\(S_4\)</td>
            <td>\(q_4\) (STOP)</td>
            <td>\(S_5\)</td>
            <td>\(Ly_1 \geq d_1 \& Ly_2 \geq d_1 \& \theta_1 \leq \frac{\pi}{2} \& \theta_2 \geq \frac{\pi}{2}\)</td>
            <td>\(\delta_2' := 0, r_2' := 0\)</td>
        </tr>
        <tr>
            <td>\(q_1\) (CC)</td>
            <td>\(S_5\)</td>
            <td>\(q_1\) (CC)</td>
            <td>\(S_6\)</td>
            <td>\(Ly_1 \geq d_1 \& Ly_2 \geq d_1 \& \theta_1 \geq \frac{\pi}{2} \& \theta_2 \geq \frac{\pi}{2}\)</td>
            <td>\(\delta_1' := 0, r_1' := 0\)</td>
        </tr>
        <tr>
            <td>\(q_2\) (ACC)</td>
            <td>\(S_5\)</td>
            <td>\(q_2\) (ACC)</td>
            <td>\(S_6\)</td>
            <td>\(Ly_1 \geq d_1 \& Ly_2 \geq d_1 \& \theta_1 \geq \frac{\pi}{2} \& \theta_2 \geq \frac{\pi}{2}\)</td>
            <td>\(\delta_1' := 0, r_1' := 0\)</td>
        </tr>
        <tr>
            <td>\(q_3\) (AEB)</td>
            <td>\(S_5\)</td>
            <td>\(q_3\) (AEB)</td>
            <td>\(S_6\)</td>
            <td>\(Ly_1 \geq d_1 \& Ly_2 \geq d_1 \& \theta_1 \geq \frac{\pi}{2} \& \theta_2 \geq \frac{\pi}{2}\)</td>
            <td>\(\delta_1' := 0, r_1' := 0\)</td>
        </tr>
        <tr>
            <td>\(q_4\) (STOP)</td>
            <td>\(S_5\)</td>
            <td>\(q_4\) (STOP)</td>
            <td>\(S_6\)</td>
            <td>\(Ly_1 \geq d_1 \& Ly_2 \geq d_1 \& \theta_1 \geq \frac{\pi}{2} \& \theta_2 \geq \frac{\pi}{2}\)</td>
            <td>\(\delta_1' := 0, r_1' := 0\)</td>
        </tr>
        <tr>
            <td>\(q_1\) (CC)</td>
            <td>\(S_1\)</td>
            <td>\(q_3\) (AEB)</td>
            <td>\(S_1\)</td>
            <td>\(vy_2 - vy_1 \leq 0 \& -d_r - 1.6 \cdot (vy_2 - vy_1) \geq 0 \& d_r \geq 3 \& d_r \leq d_0\)</td>
            <td>\(q' := 3\)</td>
        </tr>
        <tr>
            <td>\(q_1\) (CC)</td>
            <td>\(S_2\)</td>
            <td>\(q_3\) (AEB)</td>
            <td>\(S_2\)</td>
            <td>\(vy_2 - vy_1 \leq 0 \& -d_r - 1.6 \cdot (vy_2 - vy_1) \geq 0 \& d_r \geq 3 \& d_r \leq d_0\)</td>
            <td>\(q' := 3\)</td>
        </tr>
        <tr>
            <td>\(q_1\) (CC)</td>
            <td>\(S_3\)</td>
            <td>\(q_3\) (AEB)</td>
            <td>\(S_3\)</td>
            <td>\(vy_2 - vy_1 \leq 0 \& -d_r - 1.6 \cdot (vy_2 - vy_1) \geq 0 \& d_r \geq 3 \& d_r \leq d_0\)</td>
            <td>\(q' := 3\)</td>
        </tr>
        <tr>
            <td>\(q_1\) (CC)</td>
            <td>\(S_4\)</td>
            <td>\(q_3\) (AEB)</td>
            <td>\(S_4\)</td>
            <td>\(vy_2 - vy_1 \leq 0 \& -d_r - 1.6 \cdot (vy_2 - vy_1) \geq 0 \& d_r \geq 3 \& d_r \leq d_0\)</td>
            <td>\(q' := 3\)</td>
        </tr>
        <tr>
            <td>\(q_1\) (CC)</td>
            <td>\(S_5\)</td>
            <td>\(q_3\) (AEB)</td>
            <td>\(S_5\)</td>
            <td>\(vy_2 - vy_1 \leq 0 \& -d_r - 1.6 \cdot (vy_2 - vy_1) \geq 0 \& d_r \geq 3 \& d_r \leq d_0\)</td>
            <td>\(q' := 3\)</td>
        </tr>
        <tr>
            <td>\(q_1\) (CC)</td>
            <td>\(S_6\)</td>
            <td>\(q_3\) (AEB)</td>
            <td>\(S_6\)</td>
            <td>\(vy_2 - vy_1 \leq 0 \& -d_r - 1.6 \cdot (vy_2 - vy_1) \geq 0 \& d_r \geq 3 \& d_r \leq d_0\)</td>
            <td>\(q' := 3\)</td>
        </tr>
        <tr>
            <td>\(q_1\) (CC)</td>
            <td>\(S_1\)</td>
            <td>\(q_2\) (ACC)</td>
            <td>\(S_1\)</td>
            <td>\(vy_2 - vy_1 \leq 0 \& -d_r - 1.6 \cdot (vy_2 - vy_1) \leq 0 \& d_r \geq 3 \& d_r \leq d_0\)</td>
            <td>\(q' := 2\)</td>
        </tr>
        <tr>
            <td>\(q_1\) (CC)</td>
            <td>\(S_2\)</td>
            <td>\(q_2\) (ACC)</td>
            <td>\(S_2\)</td>
            <td>\(vy_2 - vy_1 \leq 0 \& -d_r - 1.6 \cdot (vy_2 - vy_1) \leq 0 \& d_r \geq 3 \& d_r \leq d_0\)</td>
            <td>\(q' := 2\)</td>
        </tr>
        <tr>
            <td>\(q_1\) (CC)</td>
            <td>\(S_3\)</td>
            <td>\(q_2\) (ACC)</td>
            <td>\(S_3\)</td>
            <td>\(vy_2 - vy_1 \leq 0 \& -d_r - 1.6 \cdot (vy_2 - vy_1) \leq 0 \& d_r \geq 3 \& d_r \leq d_0\)</td>
            <td>\(q' := 2\)</td>
        </tr>
        <tr>
            <td>\(q_1\) (CC)</td>
            <td>\(S_4\)</td>
            <td>\(q_2\) (ACC)</td>
            <td>\(S_4\)</td>
            <td>\(vy_2 - vy_1 \leq 0 \& -d_r - 1.6 \cdot (vy_2 - vy_1) \leq 0 \& d_r \geq 3 \& d_r \leq d_0\)</td>
            <td>\(q' := 2\)</td>
        </tr>
        <tr>
            <td>\(q_1\) (CC)</td>
            <td>\(S_5\)</td>
            <td>\(q_2\) (ACC)</td>
            <td>\(S_5\)</td>
            <td>\(vy_2 - vy_1 \leq 0 \& -d_r - 1.6 \cdot (vy_2 - vy_1) \leq 0 \& d_r \geq 3 \& d_r \leq d_0\)</td>
            <td>\(q' := 2\)</td>
        </tr>
        <tr>
            <td>\(q_1\) (CC)</td>
            <td>\(S_6\)</td>
            <td>\(q_2\) (ACC)</td>
            <td>\(S_6\)</td>
            <td>\(vy_2 - vy_1 \leq 0 \& -d_r - 1.6 \cdot (vy_2 - vy_1) \leq 0 \& d_r \geq 3 \& d_r \leq d_0\)</td>
            <td>\(q' := 2\)</td>
        </tr>
        <tr>
            <td>\(q_2\) (ACC)</td>
            <td>\(S_1\)</td>
            <td>\(q_3\) (AEB)</td>
            <td>\(S_1\)</td>
            <td>\(vy_2 - vy_1 \leq 0 \& -d_r - 1.6 * (vy_2 - vy_1) \geq 0 \& d_r \geq 3\)</td>
            <td>\(q' := 3\)</td>
        </tr>
        <tr>
            <td>\(q_2\) (ACC)</td>
            <td>\(S_2\)</td>
            <td>\(q_3\) (AEB)</td>
            <td>\(S_2\)</td>
            <td>\(vy_2 - vy_1 \leq 0 \& -d_r - 1.6 * (vy_2 - vy_1) \geq 0 \& d_r \geq 3\)</td>
            <td>\(q' := 3\)</td>
        </tr>
        <tr>
            <td>\(q_2\) (ACC)</td>
            <td>\(S_3\)</td>
            <td>\(q_3\) (AEB)</td>
            <td>\(S_3\)</td>
            <td>\(vy_2 - vy_1 \leq 0 \& -d_r - 1.6 * (vy_2 - vy_1) \geq 0 \& d_r \geq 3\)</td>
            <td>\(q' := 3\)</td>
        </tr>
        <tr>
            <td>\(q_2\) (ACC)</td>
            <td>\(S_4\)</td>
            <td>\(q_3\) (AEB)</td>
            <td>\(S_4\)</td>
            <td>\(vy_2 - vy_1 \leq 0 \& -d_r - 1.6 * (vy_2 - vy_1) \geq 0 \& d_r \geq 3\)</td>
            <td>\(q' := 3\)</td>
        </tr>
        <tr>
            <td>\(q_2\) (ACC)</td>
            <td>\(S_5\)</td>
            <td>\(q_3\) (AEB)</td>
            <td>\(S_5\)</td>
            <td>\(vy_2 - vy_1 \leq 0 \& -d_r - 1.6 * (vy_2 - vy_1) \geq 0 \& d_r \geq 3\)</td>
            <td>\(q' := 3\)</td>
        </tr>
        <tr>
            <td>\(q_2\) (ACC)</td>
            <td>\(S_6\)</td>
            <td>\(q_3\) (AEB)</td>
            <td>\(S_6\)</td>
            <td>\(vy_2 - vy_1 \leq 0 \& -d_r - 1.6 * (vy_2 - vy_1) \geq 0 \& d_r \geq 3\)</td>
            <td>\(q' := 3\)</td>
        </tr>
        <tr>
            <td>\(q_3\) (AEB)</td>
            <td>\(S_1\)</td>
            <td>\(q_2\) (ACC)</td>
            <td>\(S_1\)</td>
            <td>\(vy_2 - vy_1 \leq 0 \& -d_r - 1.6 * (vy_2 - vy_1) \leq 0 \& d_r \geq 3\)</td>
            <td>\(q' := 2\)</td>
        </tr>
        <tr>
            <td>\(q_3\) (AEB)</td>
            <td>\(S_2\)</td>
            <td>\(q_2\) (ACC)</td>
            <td>\(S_2\)</td>
            <td>\(vy_2 - vy_1 \leq 0 \& -d_r - 1.6 * (vy_2 - vy_1) \leq 0 \& d_r \geq 3\)</td>
            <td>\(q' := 2\)</td>
        </tr>
        <tr>
            <td>\(q_3\) (AEB)</td>
            <td>\(S_3\)</td>
            <td>\(q_2\) (ACC)</td>
            <td>\(S_3\)</td>
            <td>\(vy_2 - vy_1 \leq 0 \& -d_r - 1.6 * (vy_2 - vy_1) \leq 0 \& d_r \geq 3\)</td>
            <td>\(q' := 2\)</td>
        </tr>
        <tr>
            <td>\(q_3\) (AEB)</td>
            <td>\(S_4\)</td>
            <td>\(q_2\) (ACC)</td>
            <td>\(S_4\)</td>
            <td>\(vy_2 - vy_1 \leq 0 \& -d_r - 1.6 * (vy_2 - vy_1) \leq 0 \& d_r \geq 3\)</td>
            <td>\(q' := 2\)</td>
        </tr>
        <tr>
            <td>\(q_3\) (AEB)</td>
            <td>\(S_5\)</td>
            <td>\(q_2\) (ACC)</td>
            <td>\(S_5\)</td>
            <td>\(vy_2 - vy_1 \leq 0 \& -d_r - 1.6 * (vy_2 - vy_1) \leq 0 \& d_r \geq 3\)</td>
            <td>\(q' := 2\)</td>
        </tr>
        <tr>
            <td>\(q_3\) (AEB)</td>
            <td>\(S_6\)</td>
            <td>\(q_2\) (ACC)</td>
            <td>\(S_6\)</td>
            <td>\(vy_2 - vy_1 \leq 0 \& -d_r - 1.6 * (vy_2 - vy_1) \leq 0 \& d_r \geq 3\)</td>
            <td>\(q' := 2\)</td>
        </tr>
        <tr>
            <td>\(q_3\) (AEB)</td>
            <td>\(S_1\)</td>
            <td>\(q_4\) (STOP)</td>
            <td>\(S_1\)</td>
            <td>\(vy_1 \geq 0 \& -d_r - 0.6 * (vy_2 - vy_1) \geq 0 \& d_r \geq 3\)</td>
            <td>\(q' := 4\)</td>
        </tr>
        <tr>
            <td>\(q_3\) (AEB)</td>
            <td>\(S_2\)</td>
            <td>\(q_4\) (STOP)</td>
            <td>\(S_2\)</td>
            <td>\(vy_1 \geq 0 \& -d_r - 0.6 * (vy_2 - vy_1) \geq 0 \& d_r \geq 3\)</td>
            <td>\(q' := 4\)</td>
        </tr>
        <tr>
            <td>\(q_3\) (AEB)</td>
            <td>\(S_3\)</td>
            <td>\(q_4\) (STOP)</td>
            <td>\(S_3\)</td>
            <td>\(vy_1 \geq 0 \& -d_r - 0.6 * (vy_2 - vy_1) \geq 0 \& d_r \geq 3\)</td>
            <td>\(q' := 4\)</td>
        </tr>
        <tr>
            <td>\(q_3\) (AEB)</td>
            <td>\(S_4\)</td>
            <td>\(q_4\) (STOP)</td>
            <td>\(S_4\)</td>
            <td>\(vy_1 \geq 0 \& -d_r - 0.6 * (vy_2 - vy_1) \geq 0 \& d_r \geq 3\)</td>
            <td>\(q' := 4\)</td>
        </tr>
        <tr>
            <td>\(q_3\) (AEB)</td>
            <td>\(S_5\)</td>
            <td>\(q_4\) (STOP)</td>
            <td>\(S_5\)</td>
            <td>\(vy_1 \geq 0 \& -d_r - 0.6 * (vy_2 - vy_1) \geq 0 \& d_r \geq 3\)</td>
            <td>\(q' := 4\)</td>
        </tr>
        <tr>
            <td>\(q_3\) (AEB)</td>
            <td>\(S_6\)</td>
            <td>\(q_4\) (STOP)</td>
            <td>\(S_6\)</td>
            <td>\(vy_1 \geq 0 \& -d_r - 0.6 * (vy_2 - vy_1) \geq 0 \& d_r \geq 3\)</td>
            <td>\(q' := 4\)</td>
        </tr>
    </tbody>
</table>

### Experimental Results

#### Application Validation

<table>
    <script type="text/javascript" async
      src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
    </script>
    <caption>Tab. 4. Initial State Sets of Application Validation</caption>
    <thead>
        <tr>
            <th>Set</th>
            <th>Route</th>
            <th>Bound</th>
            <th>\(v_{x_1}\)</th>
            <th>\(v_{y_1}\)</th>
            <th>\(L_{x_1}\)</th>
            <th>\(L_{y_1}\)</th>
            <th>\(\theta_1\)</th>
            <th>\(r_1\)</th>
            <th>\(\delta_1\)</th>
            <th>\(v_{x_2}\)</th>
            <th>\(v_{y_2}\)</th>
            <th>\(L_{x_2}\)</th>
            <th>\(L_{y_2}\)</th>
            <th>\(\theta_2\)</th>
            <th>\(r_2\)</th>
            <th>\(\delta_2\)</th>
            <th>\(t\)</th>
            <th>\(d_r\)</th>
            <th>\(q\)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan="2">\(In_1\)</td>
            <td rowspan="2">\(q_1\)</td>            
            <td>min</td>
            <td>0.00</td>
            <td>17.00</td>
            <td>0.00</td>
            <td>0.00</td>
            <td>0.00</td>
            <td>0.00</td>
            <td>-1e-9</td>
            <td>0.00</td>
            <td>10.00</td>
            <td>0.00</td>
            <td>98.00</td>
            <td>0.00</td>
            <td>0.00</td>
            <td>-1e-9</td>
            <td>0.00</td>
            <td>98.00</td>
            <td>1</td>
        </tr>
        <tr>
            <td>max</td>
            <td>0.00</td>
            <td>17.01</td>
            <td>0.00</td>
            <td>0.00</td>
            <td>0.00</td>
            <td>0.00</td>
            <td>1e-9</td>
            <td>0.00</td>
            <td>10.00</td>
            <td>0.00</td>
            <td>98.00</td>
            <td>0.00</td>
            <td>0.00</td>
            <td>1e-9</td>
            <td>0.00</td>
            <td>98.00</td>
            <td>1</td>
        </tr>
        <tr>
            <td rowspan="2">\(In_2\)</td>
            <td rowspan="2">\(q_2\)</td>            
            <td>min</td>
            <td>0.00</td>
            <td>17.00</td>
            <td>0.00</td>
            <td>48.00</td>
            <td>0.00</td>
            <td>0.00</td>
            <td>-1e-9</td>
            <td>0.00</td>
            <td>10.00</td>
            <td>0.00</td>
            <td>98.00</td>
            <td>0.00</td>
            <td>0.00</td>
            <td>-1e-9</td>
            <td>0.00</td>
            <td>50.00</td>
            <td>1</td>
        </tr>
        <tr>
            <td>max</td>
            <td>0.00</td>
            <td>17.01</td>
            <td>0.00</td>
            <td>48.00</td>
            <td>0.00</td>
            <td>0.00</td>
            <td>1e-9</td>
            <td>0.00</td>
            <td>10.00</td>
            <td>0.00</td>
            <td>98.00</td>
            <td>0.00</td>
            <td>0.00</td>
            <td>1e-9</td>
            <td>0.00</td>
            <td>50.00</td>
            <td>1</td>
        </tr>
        <tr>
            <td rowspan="2">\(In_3\)</td>
            <td rowspan="2">\(q_1\) -> \(q_2\)</td>            
            <td>min</td>
            <td>0.00</td>
            <td>17.00</td>
            <td>0.00</td>
            <td>18.00</td>
            <td>0.00</td>
            <td>0.00</td>
            <td>-1e-9</td>
            <td>0.00</td>
            <td>10.00</td>
            <td>0.00</td>
            <td>98.00</td>
            <td>0.00</td>
            <td>0.00</td>
            <td>-1e-9</td>
            <td>0.00</td>
            <td>80.00</td>
            <td>1</td>
        </tr>
        <tr>
            <td>max</td>
            <td>0.00</td>
            <td>17.01</td>
            <td>0.00</td>
            <td>18.00</td>
            <td>0.00</td>
            <td>0.00</td>
            <td>1e-9</td>
            <td>0.00</td>
            <td>10.00</td>
            <td>0.00</td>
            <td>98.00</td>
            <td>0.00</td>
            <td>0.00</td>
            <td>1e-9</td>
            <td>0.00</td>
            <td>80.00</td>
            <td>1</td>
        </tr>
        <tr>
            <td rowspan="2">\(In_4\)</td>
            <td rowspan="2">\(q_3\) -> \(q_4\)</td>            
            <td>min</td>
            <td>0.00</td>
            <td>19.99</td>
            <td>0.00</td>
            <td>84.10</td>
            <td>0.00</td>
            <td>0.00</td>
            <td>-1e-9</td>
            <td>0.00</td>
            <td>7.00</td>
            <td>0.00</td>
            <td>98.00</td>
            <td>0.00</td>
            <td>0.00</td>
            <td>-1e-9</td>
            <td>0.00</td>
            <td>13.90</td>
            <td>1</td>
        </tr>
        <tr>
            <td>max</td>
            <td>0.00</td>
            <td>20.00</td>
            <td>0.00</td>
            <td>84.10</td>
            <td>0.00</td>
            <td>0.00</td>
            <td>1e-9</td>
            <td>0.00</td>
            <td>7.00</td>
            <td>0.00</td>
            <td>98.00</td>
            <td>0.00</td>
            <td>0.00</td>
            <td>1e-9</td>
            <td>0.00</td>
            <td>13.90</td>
            <td>1</td>
        </tr>
        <tr>
            <td rowspan="2">\(In_5\)</td>
            <td rowspan="2">\(q_3\) -> \(q_2\)</td>            
            <td>min</td>
            <td>0.00</td>
            <td>15.09</td>
            <td>0.00</td>
            <td>84.10</td>
            <td>0.00</td>
            <td>0.00</td>
            <td>-1e-9</td>
            <td>0.00</td>
            <td>7.00</td>
            <td>0.00</td>
            <td>98.00</td>
            <td>0.00</td>
            <td>0.00</td>
            <td>-1e-9</td>
            <td>0.00</td>
            <td>13.90</td>
            <td>1</td>
        </tr>
        <tr>
            <td>max</td>
            <td>0.00</td>
            <td>15.10</td>
            <td>0.00</td>
            <td>84.10</td>
            <td>0.00</td>
            <td>0.00</td>
            <td>1e-9</td>
            <td>0.00</td>
            <td>7.00</td>
            <td>0.00</td>
            <td>98.00</td>
            <td>0.00</td>
            <td>0.00</td>
            <td>1e-9</td>
            <td>0.00</td>
            <td>13.90</td>
            <td>1</td>
        </tr>
        <tr>
            <td rowspan="2">\(In_6\)</td>
            <td>\(q_3\) -> \(q_2\) -> \(q_3\)</td>            
            <td>min</td>
            <td>0.00</td>
            <td>17.00</td>
            <td>0.00</td>
            <td>87.00</td>
            <td>0.00</td>
            <td>0.00</td>
            <td>-1e-9</td>
            <td>0.00</td>
            <td>12.00</td>
            <td>0.00</td>
            <td>98.00</td>
            <td>0.00</td>
            <td>0.00</td>
            <td>-1e-9</td>
            <td>0.00</td>
            <td>11.00</td>
            <td>1</td>
        </tr>
        <tr>
            <td>\(q_3\) -> \(q_2\)</td>
            <td>max</td>
            <td>0.00</td>
            <td>17.01</td>
            <td>0.00</td>
            <td>87.00</td>
            <td>0.00</td>
            <td>0.00</td>
            <td>1e-9</td>
            <td>0.00</td>
            <td>12.00</td>
            <td>0.00</td>
            <td>98.00</td>
            <td>0.00</td>
            <td>0.00</td>
            <td>1e-9</td>
            <td>0.00</td>
            <td>11.00</td>
            <td>1</td>
        </tr>
    </tbody>  
</table>

{{< figure src="images/application_validation.png" title="Fig. 1. Application Validation." >}}

#### Reachable Sets with Cyberattacks

<table>
    <script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    <caption>Tab. 2. Initial State Sets of Reachable Sets</caption>
    <thead>
        <tr>
            <th>Set</th>
            <th>Route</th>
            <th>Bound</th>
            <th>\(v_{x_1}\)</th>
            <th>\(v_{y_1}\)</th>
            <th>\(L_{x_1}\)</th>
            <th>\(L_{y_1}\)</th>
            <th>\(\theta_1\)</th>
            <th>\(r_1\)</th>
            <th>\(\delta_1\)</th>
            <th>\(v_{x_2}\)</th>
            <th>\(v_{y_2}\)</th>
            <th>\(L_{x_2}\)</th>
            <th>\(L_{y_2}\)</th>
            <th>\(\theta_2\)</th>
            <th>\(r_2\)</th>
            <th>\(\delta_2\)</th>
            <th>\(d_r\)</th>
            <th>\(\omega_{d_r}\)</th>
            <th>\(\omega_{v_{y_1}}\)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan="2">\(In_1\)</td>
            <td rowspan="2">\(q_3\) -> \(q_4\)</td>            
            <td>min</td>
            <td>0.00</td>
            <td>19.79</td>
            <td>0.00</td>
            <td>84.10</td>
            <td>0.00</td>
            <td>0.00</td>
            <td>-1e-9</td>
            <td>0.00</td>
            <td>5.00</td>
            <td>0.00</td>
            <td>98.00</td>
            <td>0.00</td>
            <td>0.00</td>
            <td>-1e-9</td>
            <td>13.90</td>
            <td>0.00</td>
            <td>\</td>
        </tr>
        <tr>
            <td>max</td>
            <td>0.00</td>
            <td>19.80</td>
            <td>0.00</td>
            <td>84.10</td>
            <td>0.00</td>
            <td>0.00</td>
            <td>1e-9</td>
            <td>0.00</td>
            <td>5.00</td>
            <td>0.00</td>
            <td>98.00</td>
            <td>0.00</td>
            <td>0.00</td>
            <td>1e-9</td>
            <td>13.90</td>
            <td>2.50</td>
            <td>\</td>
        </tr>
        <tr>
            <td rowspan="2">\(In_2\)</td>
            <td rowspan="2">\(q_3\) -> \(q_4\)</td>            
            <td>min</td>
            <td>-0.01</td>
            <td>10.99</td>
            <td>0.00</td>
            <td>90.99</td>
            <td>-1e-3</td>
            <td>-1e-3</td>
            <td>-1e-9</td>
            <td>-0.01</td>
            <td>3.00</td>
            <td>0.00</td>
            <td>99.00</td>
            <td>-1e-3</td>
            <td>-1e-3</td>
            <td>-1e-9</td>
            <td>8.00</td>
            <td>0.00</td>
            <td>\</td>
        </tr>
        <tr>
            <td>max</td>
            <td>0.01</td>
            <td>11.00</td>
            <td>0.00</td>
            <td>91.00</td>
            <td>1e-3</td>
            <td>1e-3</td>
            <td>1e-9</td>
            <td>0.01</td>
            <td>3.00</td>
            <td>0.00</td>
            <td>99.00</td>
            <td>1e-3</td>
            <td>1e-3</td>
            <td>1e-9</td>
            <td>8.00</td>
            <td>4.00</td>
            <td>\</td>
        </tr>
        <tr>
            <td rowspan="2">\(In_3\)</td>
            <td rowspan="2">\(q_3\) -> \(q_4\)</td>            
            <td>min</td>
            <td>0.00</td>
            <td>16.00</td>
            <td>0.00</td>
            <td>88.10</td>
            <td>0.00</td>
            <td>0.00</td>
            <td>-1e-9</td>
            <td>0.00</td>
            <td>5.00</td>
            <td>0.00</td>
            <td>98.00</td>
            <td>0.00</td>
            <td>0.00</td>
            <td>-1e-9</td>
            <td>9.90</td>
            <td>0.00</td>
            <td>\</td>
        </tr>
        <tr>
            <td>max</td>
            <td>0.00</td>
            <td>16.01</td>
            <td>0.00</td>
            <td>88.10</td>
            <td>0.00</td>
            <td>0.00</td>
            <td>1e-9</td>
            <td>0.00</td>
            <td>5.00</td>
            <td>0.00</td>
            <td>98.00</td>
            <td>0.00</td>
            <td>0.00</td>
            <td>1e-9</td>
            <td>9.90</td>
            <td>2.50</td>
            <td>\</td>
        </tr>
        <tr>
            <td rowspan="2">\(In_4\)</td>
            <td rowspan="2">\(q_3\) -> \(q_4\)</td>            
            <td>min</td>
            <td>0.00</td>
            <td>17.00</td>
            <td>0.00</td>
            <td>87.50</td>
            <td>0.00</td>
            <td>0.00</td>
            <td>-1e-9</td>
            <td>0.00</td>
            <td>5.00</td>
            <td>0.00</td>
            <td>97.90</td>
            <td>0.00</td>
            <td>0.00</td>
            <td>-1e-9</td>
            <td>10.40</td>
            <td>0.00</td>
            <td>\</td>
        </tr>
        <tr>
            <td>max</td>
            <td>0.00</td>
            <td>17.01</td>
            <td>0.00</td>
            <td>87.50</td>
            <td>0.00</td>
            <td>0.00</td>
            <td>1e-9</td>
            <td>0.00</td>
            <td>5.00</td>
            <td>0.00</td>
            <td>97.90</td>
            <td>0.00</td>
            <td>0.00</td>
            <td>1e-9</td>
            <td>10.40</td>
            <td>2.50</td>
            <td>\</td>
        </tr>
    </tbody>
</table>

{{< figure src="images/reachable_sets.png" title="Fig. 2. Reachable Sets." >}}

#### Tool Error Comparisons

<table>
    <script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    <caption>Tab. 3. Initial State Sets of Tool Error Comparisons</caption>
    <thead>
        <tr>
            <th>Set</th>
            <th>Bound</th>
            <th>\(v_{x_1}\)</th>
            <th>\(v_{y_1}\)</th>
            <th>\(L_{x_1}\)</th>
            <th>\(L_{y_1}\)</th>
            <th>\(\theta_1\)</th>
            <th>\(r_1\)</th>
            <th>\(\delta_1\)</th>
            <th>\(v_{x_2}\)</th>
            <th>\(v_{y_2}\)</th>
            <th>\(L_{x_2}\)</th>
            <th>\(L_{y_2}\)</th>
            <th>\(\theta_2\)</th>
            <th>\(r_2\)</th>
            <th>\(\delta_2\)</th>
            <th>\(d_r\)</th>
            <th>RMSE</th>
            <th>MAE</th>
            <th>MAPE</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan="2">\(In_1\)</td> 
            <td>min</td>
            <td>-0.01</td>
            <td>10.57</td>
            <td>0</td>
            <td>81.31</td>
            <td>-1e-3</td>
            <td>-1e-3</td>
            <td>-1e-9</td>
            <td>-0.01</td>
            <td>4.23</td>
            <td>0</td>
            <td>98.76</td>
            <td>-1e-3</td>
            <td>-1e-3</td>
            <td>-1e-9</td>
            <td>17.45</td>
            <td rowspan="2">0.02</td>
            <td rowspan="2">0.02</td>
            <td rowspan="2">0.10</td>
        </tr>
        <tr>
            <td>max</td>
            <td>0.01</td>
            <td>10.58</td>
            <td>0</td>
            <td>81.32</td>
            <td>1e-3</td>
            <td>1e-3</td>
            <td>1e-9</td>
            <td>0.01</td>
            <td>4.23</td>
            <td>0</td>
            <td>98.76</td>
            <td>1e-3</td>
            <td>1e-3</td>
            <td>1e-9</td>
            <td>17.45</td>
        </tr>
        <tr>
            <td rowspan="2">\(In_2\)</td> 
            <td>min</td>
            <td>-0.01</td>
            <td>13.32</td>
            <td>0</td>
            <td>86.12</td>
            <td>-1e-3</td>
            <td>-1e-3</td>
            <td>-1e-9</td>
            <td>-0.01</td>
            <td>10.68</td>
            <td>0</td>
            <td>98.11</td>
            <td>-1e-3</td>
            <td>-1e-3</td>
            <td>-1e-9</td>
            <td>11.99</td>
            <td rowspan="2">0.01</td>
            <td rowspan="2">0.01</td>
            <td rowspan="2">0.10</td>
        </tr>
        <tr>
            <td>max</td>
            <td>0.01</td>
            <td>13.33</td>
            <td>0</td>
            <td>86.13</td>
            <td>1e-3</td>
            <td>1e-3</td>
            <td>1e-9</td>
            <td>0.01</td>
            <td>10.68</td>
            <td>0</td>
            <td>98.11</td>
            <td>1e-3</td>
            <td>1e-3</td>
            <td>1e-9</td>
            <td>11.99</td>
        </tr>
        <tr>
            <td rowspan="2">\(In_3\)</td> 
            <td>min</td>
            <td>-0.01</td>
            <td>14.86</td>
            <td>0</td>
            <td>86.60</td>
            <td>-1e-3</td>
            <td>-1e-3</td>
            <td>-1e-9</td>
            <td>-0.01</td>
            <td>6.79</td>
            <td>0</td>
            <td>98.67</td>
            <td>-1e-3</td>
            <td>-1e-3</td>
            <td>-1e-9</td>
            <td>12.07</td>
            <td rowspan="2">0.13</td>
            <td rowspan="2">0.08</td>
            <td rowspan="2">1.43</td>
        </tr>
        <tr>
            <td>max</td>
            <td>0.01</td>
            <td>14.87</td>
            <td>0</td>
            <td>86.61</td>
            <td>1e-3</td>
            <td>1e-3</td>
            <td>1e-9</td>
            <td>0.01</td>
            <td>6.79</td>
            <td>0</td>
            <td>98.67</td>
            <td>1e-3</td>
            <td>1e-3</td>
            <td>1e-9</td>
            <td>12.07</td>
        </tr>
        <tr>
            <td rowspan="2">\(In_4\)</td>
            <td>min</td>
            <td>-0.01</td>
            <td>16.41</td>
            <td>0</td>
            <td>88.05</td>
            <td>-1e-3</td>
            <td>-1e-3</td>
            <td>-1e-9</td>
            <td>-0.01</td>
            <td>9.56</td>
            <td>0</td>
            <td>98.83</td>
            <td>-1e-3</td>
            <td>-1e-3</td>
            <td>-1e-9</td>
            <td>10.78</td>
            <td rowspan="2">0.05</td>
            <td rowspan="2">0.04</td>
            <td rowspan="2">0.46</td>
        </tr>
        <tr>
            <td>max</td>
            <td>0.01</td>
            <td>16.42</td>
            <td>0</td>
            <td>88.06</td>
            <td>1e-3</td>
            <td>1e-3</td>
            <td>1e-9</td>
            <td>0.01</td>
            <td>9.56</td>
            <td>0</td>
            <td>98.83</td>
            <td>1e-3</td>
            <td>1e-3</td>
            <td>1e-9</td>
            <td>10.78</td>
        </tr>
        <tr>
            <td rowspan="2">\(In_5\)</td>
            <td>min</td>
            <td>-0.01</td>
            <td>16.72</td>
            <td>0</td>
            <td>88.59</td>
            <td>-1e-3</td>
            <td>-1e-3</td>
            <td>-1e-9</td>
            <td>-0.01</td>
            <td>6.77</td>
            <td>0</td>
            <td>98.86</td>
            <td>-1e-3</td>
            <td>-1e-3</td>
            <td>-1e-9</td>
            <td>10.27</td>
            <td rowspan="2">0.03</td>
            <td rowspan="2">0.02</td>
            <td rowspan="2">0.29</td>
        </tr>
        <tr>
            <td>max</td>
            <td>0.01</td>
            <td>16.73</td>
            <td>0</td>
            <td>88.60</td>
            <td>1e-3</td>
            <td>1e-3</td>
            <td>1e-9</td>
            <td>0.01</td>
            <td>6.77</td>
            <td>0</td>
            <td>98.86</td>
            <td>1e-3</td>
            <td>1e-3</td>
            <td>1e-9</td>
            <td>10.27</td>
        </tr>
        <tr>
            <td rowspan="2">\(In_6\)</td>
            <td>min</td>
            <td>-0.01</td>
            <td>15.47</td>
            <td>0</td>
            <td>82.58</td>
            <td>-1e-3</td>
            <td>-1e-3</td>
            <td>-1e-9</td>
            <td>-0.01</td>
            <td>12.58</td>
            <td>0</td>
            <td>98.32</td>
            <td>-1e-3</td>
            <td>-1e-3</td>
            <td>-1e-9</td>
            <td>15.74</td>
            <td rowspan="2">0.02</td>
            <td rowspan="2">0.02</td>
            <td rowspan="2">0.10</td>
        </tr>
        <tr>
            <td>max</td>
            <td>0.01</td>
            <td>15.48</td>
            <td>0</td>
            <td>82.59</td>
            <td>1e-3</td>
            <td>1e-3</td>
            <td>1e-9</td>
            <td>0.01</td>
            <td>12.58</td>
            <td>0</td>
            <td>98.32</td>
            <td>1e-3</td>
            <td>1e-3</td>
            <td>1e-9</td>
            <td>15.74</td>
        </tr>
        <tr>
            <td rowspan="2">\(In_7\)</td>
            <td>min</td>
            <td>-0.01</td>
            <td>14.37</td>
            <td>0</td>
            <td>83.49</td>
            <td>-1e-3</td>
            <td>-1e-3</td>
            <td>-1e-9</td>
            <td>-0.01</td>
            <td>9.91</td>
            <td>0</td>
            <td>98.72</td>
            <td>-1e-3</td>
            <td>-1e-3</td>
            <td>-1e-9</td>
            <td>15.23</td>
            <td rowspan="2">0.01</td>
            <td rowspan="2">0.01</td>
            <td rowspan="2">0.06</td>
        </tr>
        <tr>
            <td>max</td>
            <td>0.01</td>
            <td>14.38</td>
            <td>0</td>
            <td>83.5</td>
            <td>1e-3</td>
            <td>1e-3</td>
            <td>1e-9</td>
            <td>0.01</td>
            <td>9.91</td>
            <td>0</td>
            <td>98.72</td>
            <td>1e-3</td>
            <td>1e-3</td>
            <td>1e-9</td>
            <td>15.23</td>
        </tr>
        <tr>
            <td rowspan="2">\(In_8\)</td>
            <td>min</td>
            <td>-0.01</td>
            <td>17.5</td>
            <td>0</td>
            <td>84.72</td>
            <td>-1e-3</td>
            <td>-1e-3</td>
            <td>-1e-9</td>
            <td>-0.01</td>
            <td>3.52</td>
            <td>0</td>
            <td>98.03</td>
            <td>-1e-3</td>
            <td>-1e-3</td>
            <td>-1e-9</td>
            <td>13.31</td>
            <td rowspan="2">0.05</td>
            <td rowspan="2">0.04</td>
            <td rowspan="2">0.61</td>
        </tr>
        <tr>
            <td>max</td>
            <td>0.01</td>
            <td>17.51</td>
            <td>0</td>
            <td>84.73</td>
            <td>1e-3</td>
            <td>1e-3</td>
            <td>1e-9</td>
            <td>0.01</td>
            <td>3.52</td>
            <td>0</td>
            <td>98.03</td>
            <td>1e-3</td>
            <td>1e-3</td>
            <td>1e-9</td>
            <td>13.31</td>
        </tr>
        <tr>
            <td rowspan="2">\(In_9\)</td>
            <td>min</td>
            <td>-0.01</td>
            <td>15.77</td>
            <td>0</td>
            <td>80.76</td>
            <td>-1e-3</td>
            <td>-1e-3</td>
            <td>-1e-9</td>
            <td>-0.01</td>
            <td>5.31</td>
            <td>0</td>
            <td>98.94</td>
            <td>-1e-3</td>
            <td>-1e-3</td>
            <td>-1e-9</td>
            <td>18.18</td>
            <td rowspan="2">0.28</td>
            <td rowspan="2">0.19</td>
            <td rowspan="2">1.93</td>
        </tr>
        <tr>
            <td>max</td>
            <td>0.01</td>
            <td>15.78</td>
            <td>0</td>
            <td>80.77</td>
            <td>1e-3</td>
            <td>1e-3</td>
            <td>1e-9</td>
            <td>0.01</td>
            <td>5.31</td>
            <td>0</td>
            <td>98.94</td>
            <td>1e-3</td>
            <td>1e-3</td>
            <td>1e-9</td>
            <td>18.18</td>
        </tr>
        <tr>
            <td rowspan="2">\(In_{10}\)</td>
            <td>min</td>
            <td>-0.01</td>
            <td>13.21</td>
            <td>0</td>
            <td>81.04</td>
            <td>-1e-3</td>
            <td>-1e-3</td>
            <td>-1e-9</td>
            <td>-0.01</td>
            <td>10.69</td>
            <td>0</td>
            <td>98.58</td>
            <td>-1e-3</td>
            <td>-1e-3</td>
            <td>-1e-9</td>
            <td>17.54</td>
            <td rowspan="2">0.02</td>
            <td rowspan="2">0.02</td>
            <td rowspan="2">0.11</td>
        </tr>
        <tr>
            <td>max</td>
            <td>0.01</td>
            <td>13.22</td>
            <td>0</td>
            <td>81.05</td>
            <td>1e-3</td>
            <td>1e-3</td>
            <td>1e-9</td>
            <td>0.01</td>
            <td>10.69</td>
            <td>0</td>
            <td>98.58</td>
            <td>1e-3</td>
            <td>1e-3</td>
            <td>1e-9</td>
            <td>17.54</td>
        </tr>
        <tr>
            <td rowspan="2">\(In_{11}\)</td>
            <td>min</td>
            <td>-0.01</td>
            <td>19.29</td>
            <td>0</td>
            <td>81.36</td>
            <td>-1e-3</td>
            <td>-1e-3</td>
            <td>-1e-9</td>
            <td>-0.01</td>
            <td>4.25</td>
            <td>0</td>
            <td>98.9</td>
            <td>-1e-3</td>
            <td>-1e-3</td>
            <td>-1e-9</td>
            <td>17.54</td>
            <td rowspan="2">0.04</td>
            <td rowspan="2">0.03</td>
            <td rowspan="2">0.32</td>
        </tr>
        <tr>
            <td>max</td>
            <td>0.01</td>
            <td>19.3</td>
            <td>0</td>
            <td>81.37</td>
            <td>1e-3</td>
            <td>1e-3</td>
            <td>1e-9</td>
            <td>0.01</td>
            <td>4.25</td>
            <td>0</td>
            <td>98.9</td>
            <td>1e-3</td>
            <td>1e-3</td>
            <td>1e-9</td>
            <td>17.54</td>
        </tr>
        <tr>
            <td rowspan="2">\(In_{12}\)</td>
            <td>min</td>
            <td>-0.01</td>
            <td>12.87</td>
            <td>0</td>
            <td>80.53</td>
            <td>-1e-3</td>
            <td>-1e-3</td>
            <td>-1e-9</td>
            <td>-0.01</td>
            <td>4.85</td>
            <td>0</td>
            <td>98.47</td>
            <td>-1e-3</td>
            <td>-1e-3</td>
            <td>-1e-9</td>
            <td>17.94</td>
            <td rowspan="2">0.02</td>
            <td rowspan="2">0.02</td>
            <td rowspan="2">0.11</td>
        </tr>
        <tr>
            <td>max</td>
            <td>0.01</td>
            <td>12.88</td>
            <td>0</td>
            <td>80.54</td>
            <td>1e-3</td>
            <td>1e-3</td>
            <td>1e-9</td>
            <td>0.01</td>
            <td>4.85</td>
            <td>0</td>
            <td>98.47</td>
            <td>1e-3</td>
            <td>1e-3</td>
            <td>1e-9</td>
            <td>17.94</td>
        </tr>
        <tr>
            <td rowspan="2">\(In_{13}\)</td>
            <td>min</td>
            <td>-0.01</td>
            <td>18.23</td>
            <td>0</td>
            <td>79.73</td>
            <td>-1e-3</td>
            <td>-1e-3</td>
            <td>-1e-9</td>
            <td>-0.01</td>
            <td>9.76</td>
            <td>0</td>
            <td>98.48</td>
            <td>-1e-3</td>
            <td>-1e-3</td>
            <td>-1e-9</td>
            <td>18.75</td>
            <td rowspan="2">0.02</td>
            <td rowspan="2">0.02</td>
            <td rowspan="2">0.11</td>
        </tr>
        <tr>
            <td>max</td>
            <td>0.01</td>
            <td>18.24</td>
            <td>0</td>
            <td>79.74</td>
            <td>1e-3</td>
            <td>1e-3</td>
            <td>1e-9</td>
            <td>0.01</td>
            <td>9.76</td>
            <td>0</td>
            <td>98.48</td>
            <td>1e-3</td>
            <td>1e-3</td>
            <td>1e-9</td>
            <td>18.75</td>
        </tr>
        <tr>
            <td rowspan="2">\(In_{14}\)</td>
            <td>min</td>
            <td>-0.01</td>
            <td>18.14</td>
            <td>0</td>
            <td>83.6</td>
            <td>-1e-3</td>
            <td>-1e-3</td>
            <td>-1e-9</td>
            <td>-0.01</td>
            <td>10.1</td>
            <td>0</td>
            <td>98.72</td>
            <td>-1e-3</td>
            <td>-1e-3</td>
            <td>-1e-9</td>
            <td>15.12</td>
            <td rowspan="2">0.04</td>
            <td rowspan="2">0.03</td>
            <td rowspan="2">0.27</td>
        </tr>
        <tr>
            <td>max</td>
            <td>0.01</td>
            <td>18.15</td>
            <td>0</td>
            <td>83.61</td>
            <td>1e-3</td>
            <td>1e-3</td>
            <td>1e-9</td>
            <td>0.01</td>
            <td>10.1</td>
            <td>0</td>
            <td>98.72</td>
            <td>1e-3</td>
            <td>1e-3</td>
            <td>1e-9</td>
            <td>15.12</td>
        </tr>
        <tr>
            <td rowspan="2">\(In_{15}\)</td>
            <td>min</td>
            <td>-0.01</td>
            <td>13.24</td>
            <td>0</td>
            <td>84.86</td>
            <td>-1e-3</td>
            <td>-1e-3</td>
            <td>-1e-9</td>
            <td>-0.01</td>
            <td>5.96</td>
            <td>0</td>
            <td>98.5</td>
            <td>-1e-3</td>
            <td>-1e-3</td>
            <td>-1e-9</td>
            <td>13.64</td>
            <td rowspan="2">0.04</td>
            <td rowspan="2">0.03</td>
            <td rowspan="2">0.29</td>
        </tr>
        <tr>
            <td>max</td>
            <td>0.01</td>
            <td>13.25</td>
            <td>0</td>
            <td>84.87</td>
            <td>1e-3</td>
            <td>1e-3</td>
            <td>1e-9</td>
            <td>0.01</td>
            <td>5.96</td>
            <td>0</td>
            <td>98.5</td>
            <td>1e-3</td>
            <td>1e-3</td>
            <td>1e-9</td>
            <td>13.64</td>
        </tr>
        <tr>
            <td rowspan="2">\(In_{16}\)</td>
            <td>min</td>
            <td>-0.01</td>
            <td>12.1</td>
            <td>0</td>
            <td>79.79</td>
            <td>-1e-3</td>
            <td>-1e-3</td>
            <td>-1e-9</td>
            <td>-0.01</td>
            <td>6.5</td>
            <td>0</td>
            <td>98.11</td>
            <td>-1e-3</td>
            <td>-1e-3</td>
            <td>-1e-9</td>
            <td>18.32</td>
            <td rowspan="2">0.01</td>
            <td rowspan="2">0.01</td>
            <td rowspan="2">0.07</td>
        </tr>
        <tr>
            <td>max</td>
            <td>0.01</td>
            <td>12.11</td>
            <td>0</td>
            <td>79.8</td>
            <td>1e-3</td>
            <td>1e-3</td>
            <td>1e-9</td>
            <td>0.01</td>
            <td>6.5</td>
            <td>0</td>
            <td>98.11</td>
            <td>1e-3</td>
            <td>1e-3</td>
            <td>1e-9</td>
            <td>18.32</td>
        </tr>
        <tr>
            <td rowspan="2">\(In_{17}\)</td>
            <td>min</td>
            <td>-0.01</td>
            <td>13.54</td>
            <td>0</td>
            <td>86.98</td>
            <td>-1e-3</td>
            <td>-1e-3</td>
            <td>-1e-9</td>
            <td>-0.01</td>
            <td>6.51</td>
            <td>0</td>
            <td>98.58</td>
            <td>-1e-3</td>
            <td>-1e-3</td>
            <td>-1e-9</td>
            <td>11.6</td>
            <td rowspan="2">0.05</td>
            <td rowspan="2">0.04</td>
            <td rowspan="2">0.46</td>
        </tr>
        <tr>
            <td>max</td>
            <td>0.01</td>
            <td>13.55</td>
            <td>0</td>
            <td>86.99</td>
            <td>1e-3</td>
            <td>1e-3</td>
            <td>1e-9</td>
            <td>0.01</td>
            <td>6.51</td>
            <td>0</td>
            <td>98.58</td>
            <td>1e-3</td>
            <td>1e-3</td>
            <td>1e-9</td>
            <td>11.6</td>
        </tr>
        <tr>
            <td rowspan="2">\(In_{18}\)</td>
            <td>min</td>
            <td>-0.01</td>
            <td>17.84</td>
            <td>0</td>
            <td>79.67</td>
            <td>-1e-3</td>
            <td>-1e-3</td>
            <td>-1e-9</td>
            <td>-0.01</td>
            <td>7.6</td>
            <td>0</td>
            <td>98.81</td>
            <td>-1e-3</td>
            <td>-1e-3</td>
            <td>-1e-9</td>
            <td>19.14</td>
            <td rowspan="2">0.18</td>
            <td rowspan="2">0.12</td>
            <td rowspan="2">0.90</td>
        </tr>
        <tr>
            <td>max</td>
            <td>0.01</td>
            <td>17.85</td>
            <td>0</td>
            <td>79.68</td>
            <td>1e-3</td>
            <td>1e-3</td>
            <td>1e-9</td>
            <td>0.01</td>
            <td>7.6</td>
            <td>0</td>
            <td>98.81</td>
            <td>1e-3</td>
            <td>1e-3</td>
            <td>1e-9</td>
            <td>19.14</td>
        </tr>
        <tr>
            <td rowspan="2">\(In_{19}\)</td>
            <td>min</td>
            <td>-0.01</td>
            <td>19.32</td>
            <td>0</td>
            <td>87.87</td>
            <td>-1e-3</td>
            <td>-1e-3</td>
            <td>-1e-9</td>
            <td>-0.01</td>
            <td>17.08</td>
            <td>0</td>
            <td>98.65</td>
            <td>-1e-3</td>
            <td>-1e-3</td>
            <td>-1e-9</td>
            <td>10.78</td>
            <td rowspan="2">0.02</td>
            <td rowspan="2">0.02</td>
            <td rowspan="2">0.19</td>
        </tr>
        <tr>
            <td>max</td>
            <td>0.01</td>
            <td>19.33</td>
            <td>0</td>
            <td>87.88</td>
            <td>1e-3</td>
            <td>1e-3</td>
            <td>1e-9</td>
            <td>0.01</td>
            <td>17.08</td>
            <td>0</td>
            <td>98.65</td>
            <td>1e-3</td>
            <td>1e-3</td>
            <td>1e-9</td>
            <td>10.78</td>
        </tr>
        <tr>
            <td rowspan="2">\(In_{20}\)</td>
            <td>min</td>
            <td>-0.01</td>
            <td>11.73</td>
            <td>0</td>
            <td>80.27</td>
            <td>-1e-3</td>
            <td>-1e-3</td>
            <td>-1e-9</td>
            <td>-0.01</td>
            <td>3.01</td>
            <td>0</td>
            <td>98.93</td>
            <td>-1e-3</td>
            <td>-1e-3</td>
            <td>-1e-9</td>
            <td>18.66</td>
            <td rowspan="2">0.02</td>
            <td rowspan="2">0.02</td>
            <td rowspan="2">0.12</td>
        </tr>
        <tr>
            <td>max</td>
            <td>0.01</td>
            <td>11.74</td>
            <td>0</td>
            <td>80.28</td>
            <td>1e-3</td>
            <td>1e-3</td>
            <td>1e-9</td>
            <td>0.01</td>
            <td>3.01</td>
            <td>0</td>
            <td>98.93</td>
            <td>1e-3</td>
            <td>1e-3</td>
            <td>1e-9</td>
            <td>18.66</td>
        </tr>
        <tr>
            <td rowspan="2">\(In_{21}\)</td>
            <td>min</td>
            <td>-0.01</td>
            <td>10.69</td>
            <td>0</td>
            <td>78.99</td>
            <td>-1e-3</td>
            <td>-1e-3</td>
            <td>-1e-9</td>
            <td>-0.01</td>
            <td>5.67</td>
            <td>0</td>
            <td>98.84</td>
            <td>-1e-3</td>
            <td>-1e-3</td>
            <td>-1e-9</td>
            <td>19.85</td>
            <td rowspan="2">0.02</td>
            <td rowspan="2">0.01</td>
            <td rowspan="2">0.07</td>
        </tr>
        <tr>
            <td>max</td>
            <td>0.01</td>
            <td>10.7</td>
            <td>0</td>
            <td>79.00</td>
            <td>1e-3</td>
            <td>1e-3</td>
            <td>1e-9</td>
            <td>0.01</td>
            <td>5.67</td>
            <td>0</td>
            <td>98.84</td>
            <td>1e-3</td>
            <td>1e-3</td>
            <td>1e-9</td>
            <td>19.85</td>
        </tr>
        <tr>
            <td rowspan="2">\(In_{22}\)</td>
            <td>min</td>
            <td>-0.01</td>
            <td>11.98</td>
            <td>0</td>
            <td>79.04</td>
            <td>-1e-3</td>
            <td>-1e-3</td>
            <td>-1e-9</td>
            <td>-0.01</td>
            <td>6.11</td>
            <td>0</td>
            <td>98.62</td>
            <td>-1e-3</td>
            <td>-1e-3</td>
            <td>-1e-9</td>
            <td>19.58</td>
            <td rowspan="2">0.02</td>
            <td rowspan="2">0.02</td>
            <td rowspan="2">0.10</td>
        </tr>
        <tr>
            <td>max</td>
            <td>0.01</td>
            <td>11.99</td>
            <td>0</td>
            <td>79.05</td>
            <td>1e-3</td>
            <td>1e-3</td>
            <td>1e-9</td>
            <td>0.01</td>
            <td>6.11</td>
            <td>0</td>
            <td>98.62</td>
            <td>1e-3</td>
            <td>1e-3</td>
            <td>1e-9</td>
            <td>19.58</td>
        </tr>
        <tr>
            <td rowspan="2">\(In_{23}\)</td>
            <td>min</td>
            <td>-0.01</td>
            <td>14.4</td>
            <td>0</td>
            <td>80.56</td>
            <td>-1e-3</td>
            <td>-1e-3</td>
            <td>-1e-9</td>
            <td>-0.01</td>
            <td>7.37</td>
            <td>0</td>
            <td>98.6</td>
            <td>-1e-3</td>
            <td>-1e-3</td>
            <td>-1e-9</td>
            <td>18.04</td>
            <td rowspan="2">0.03</td>
            <td rowspan="2">0.03</td>
            <td rowspan="2">0.18</td>
        </tr>
        <tr>
            <td>max</td>
            <td>0.01</td>
            <td>14.41</td>
            <td>0</td>
            <td>80.57</td>
            <td>1e-3</td>
            <td>1e-3</td>
            <td>1e-9</td>
            <td>0.01</td>
            <td>7.37</td>
            <td>0</td>
            <td>98.6</td>
            <td>1e-3</td>
            <td>1e-3</td>
            <td>1e-9</td>
            <td>18.04</td>
        </tr>
        <tr>
            <td rowspan="2">\(In_{24}\)</td>
            <td>min</td>
            <td>-0.01</td>
            <td>15.59</td>
            <td>0</td>
            <td>79.4</td>
            <td>-1e-3</td>
            <td>-1e-3</td>
            <td>-1e-9</td>
            <td>-0.01</td>
            <td>4.45</td>
            <td>0</td>
            <td>98.79</td>
            <td>-1e-3</td>
            <td>-1e-3</td>
            <td>-1e-9</td>
            <td>19.39</td>
            <td rowspan="2">0.23</td>
            <td rowspan="2">0.16</td>
            <td rowspan="2">1.48</td>
        </tr>
        <tr>
            <td>max</td>
            <td>0.01</td>
            <td>15.6</td>
            <td>0</td>
            <td>79.41</td>
            <td>1e-3</td>
            <td>1e-3</td>
            <td>1e-9</td>
            <td>0.01</td>
            <td>4.45</td>
            <td>0</td>
            <td>98.79</td>
            <td>1e-3</td>
            <td>1e-3</td>
            <td>1e-9</td>
            <td>19.39</td>
        </tr>
        <tr>
            <td rowspan="2">\(In_{25}\)</td>
            <td>min</td>
            <td>-0.01</td>
            <td>11.42</td>
            <td>0</td>
            <td>78.22</td>
            <td>-1e-3</td>
            <td>-1e-3</td>
            <td>-1e-9</td>
            <td>-0.01</td>
            <td>3.99</td>
            <td>0</td>
            <td>98.11</td>
            <td>-1e-3</td>
            <td>-1e-3</td>
            <td>-1e-9</td>
            <td>19.89</td>
            <td rowspan="2">0.02</td>
            <td rowspan="2">0.02</td>
            <td rowspan="2">0.09</td>
        </tr>
        <tr>
            <td>max</td>
            <td>0.01</td>
            <td>11.43</td>
            <td>0</td>
            <td>78.23</td>
            <td>1e-3</td>
            <td>1e-3</td>
            <td>1e-9</td>
            <td>0.01</td>
            <td>3.99</td>
            <td>0</td>
            <td>98.11</td>
            <td>1e-3</td>
            <td>1e-3</td>
            <td>1e-9</td>
            <td>19.89</td>
        </tr>
        <tr>
            <td rowspan="2">\(In_{26}\)</td>
            <td>min</td>
            <td>-0.01</td>
            <td>13.34</td>
            <td>0</td>
            <td>79.99</td>
            <td>-1e-3</td>
            <td>-1e-3</td>
            <td>-1e-9</td>
            <td>-0.01</td>
            <td>8.75</td>
            <td>0</td>
            <td>98.44</td>
            <td>-1e-3</td>
            <td>-1e-3</td>
            <td>-1e-9</td>
            <td>18.45</td>
            <td rowspan="2">0.02</td>
            <td rowspan="2">0.02</td>
            <td rowspan="2">0.09</td>
        </tr>
        <tr>
            <td>max</td>
            <td>0.01</td>
            <td>13.35</td>
            <td>0</td>
            <td>80.0</td>
            <td>1e-3</td>
            <td>1e-3</td>
            <td>1e-9</td>
            <td>0.01</td>
            <td>8.75</td>
            <td>0</td>
            <td>98.44</td>
            <td>1e-3</td>
            <td>1e-3</td>
            <td>1e-9</td>
            <td>18.45</td>
        </tr>
        <tr>
            <td rowspan="2">\(In_{27}\)</td>
            <td>min</td>
            <td>-0.01</td>
            <td>12.19</td>
            <td>0</td>
            <td>80.47</td>
            <td>-1e-3</td>
            <td>-1e-3</td>
            <td>-1e-9</td>
            <td>-0.01</td>
            <td>7.5</td>
            <td>0</td>
            <td>98.42</td>
            <td>-1e-3</td>
            <td>-1e-3</td>
            <td>-1e-9</td>
            <td>17.95</td>
            <td rowspan="2">0.02</td>
            <td rowspan="2">0.01</td>
            <td rowspan="2">0.08</td>
        </tr>
        <tr>
            <td>max</td>
            <td>0.01</td>
            <td>12.2</td>
            <td>0</td>
            <td>80.48</td>
            <td>1e-3</td>
            <td>1e-3</td>
            <td>1e-9</td>
            <td>0.01</td>
            <td>7.5</td>
            <td>0</td>
            <td>98.42</td>
            <td>1e-3</td>
            <td>1e-3</td>
            <td>1e-9</td>
            <td>17.95</td>
        </tr>
    </tbody>
</table>

{{< figure src="images/tool_errors.png" title="Fig. 3. Tool Errors." >}}

Plots of tool error tests.

{{< figure src="images/tool_errors_comparison.png" title="Fig. 4. Tool Error Tests." >}}

#### Performance Comparison of Attack Strategy Search Algorithms
