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
  .page-body {
    width: 100%;
    align-items: center;
    align-content: center;
  }

  .article-project, .article-container {
    width: 90%;
    max-width: 1700px;
    padding: 0 20px 0 20px;
    margin: 0 auto 0 auto;
  }
  
  .full_table {
    display: table;
    width: 90%;
  }
  
  .full_table table thead {
    display: table;
    width: 90%;
  }
  
  .full_table table tbody {
    display: table;
    width: 90%;
  }

  table {
    width: 90%;
    border-collapse: collapse;
    margin: 20px 0;
    text-align: center;
    font-family: Arial, sans-serif;
    border-radius: 8px;
    overflow: hidden;
  }

  .featured-image {
      width: 60%;   /* 设置宽度为720px */
      height: auto;   /* 保持图片的纵横比 */
  }

  th {
    background-color: #6C7AE0; /* 将表格头部背景颜色设为 */
    color: #ffffff; /* 表头文字设为白色 */
    padding: 12px;
    text-align: center; /* 水平居中 */
    vertical-align: middle; /* 垂直居中 */
    font-weight: bold;
    font-size: 0.875rem;
  }

  td {
    padding: 10px;
    border: 1px solid #e0e0e0;
    color: #333333;
    background-color: #f7f7fb;
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

  tbody tr:hover {
    background-color: #eaf0ff;
  }

  figure img {
    width: 90%;
    height: auto;
  }
</style>

- [Verification with Hybrid Automaton Reachability](#verification)
  - [Vehicle Parameters](#vehicle-parameters)
  - [Invariance of Discrete Modes](#invariance-of-discrete-modes)
  - [Transition Relation](#transition-relation)
  - [Application Validation](#application-validation)
  - [Reachable Sets with Cyberattacks](#reachable-sets-with-cyberattacks)
- [Falsification with Deep Reinforcement Learning](#falsification)
  - [Tool Error Comparisons](#tool-error-comparisons)
  - [Performance Comparison of Attack Strategy Search Algorithms](#performance-comparison-of-attack-strategy-search-algorithms)
  - [Training of Deep Reinforcement Learning Models](#training-of-deep-reinforcement-learning-models)
  - [Analysis of Energy Consumption](#analysis-of-energy-consumption)

<script type="text/javascript" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

### Verification with Hybrid Automaton Reachability

#### Vehicle Parameters

We use the Audi A8 as the subject of our study, with its key vehicle parameters listed in Tab. 1. For example, its weight is 1945 kg. These parameters are related to the motion of the vehicle and will be used in the ordinary differential equations (ODEs) that describe the vehicle's motion. For example, when a vehicle is turning, both longitudinal and lateral accelerations are related to the vehicle mass. In addition, the other five parameters are also related to the vehicle's steering movement and vary from vehicle to vehicle.

<table>
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

To explain in more detail, we show the ODEs of vehicle motion as follows.

$$
	\dot{L_x}= v_{y}\sin\theta + v_{x}\cos\theta \\ 
	\dot{L_y}= v_{y}\cos\theta + v_{x}\sin\theta  \\ 
	\dot{v_x}=-\frac{C_{f}+C_{r}}{m v_{y}} v_{x} + \left(\frac{C_{r}l_{r}-C_{f}l_{f}}{m v_{y}}-v_{y}\right) r +\frac{C_{f}}{m}\delta \\ 
	\dot{v_y}= v_{x} r + \frac{F_y}{m} \\ 
	\dot{\theta}=r \\ 
	\dot{r}= \frac{C_{r}l_{r}-C_{f}l_{f}}{I_{Z} v_{y}} v_{x}- \frac{l_{r}^2 C_{r}+l_{f}^2 C_{f}}{I_{Z} v_{y}} r + \frac{C_{f} l_{f}}{I_{Z}} \delta
$$

#### Invariance of Discrete Modes

We study the relative motion between two vehicles and model it using a hybrid automaton. The hybrid automaton contains a total of 4 discrete modes, namely $q_1$(CC), $q_2$(ACC), $q_3$(AEB), and $q_4$(STOP). Each discrete mode has 6 clones $S_1$-$S_6$, corresponding to different states of the two cars turning. Tab. 2 shows the invariance of the discrete modes of the hybrid automaton.

<table>
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

Tab. 3 shows the transition relation between different discrete modes of the hybrid automaton. Some are mode switches, others are state switches, and their corresponding conditions and resets are shown.

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
            <td>\(\delta_2' := 0.07, r_2' := 0\)</td>
        </tr>
        <tr>
            <td>\(q_2\) (ACC)</td>
            <td>\(S_1\)</td>
            <td>\(q_2\) (ACC)</td>
            <td>\(S_2\)</td>
            <td>\(Ly_1 \leq d_1 \& Ly_2 \geq d_1\)</td>
            <td>\(\delta_2' := 0.07, r_2' := 0\)</td>
        </tr>
        <tr>
            <td>\(q_3\) (AEB)</td>
            <td>\(S_1\)</td>
            <td>\(q_3\) (AEB)</td>
            <td>\(S_2\)</td>
            <td>\(Ly_1 \leq d_1 \& Ly_2 \geq d_1\)</td>
            <td>\(\delta_2' := 0.07, r_2' := 0\)</td>
        </tr>
        <tr>
            <td>\(q_4\) (STOP)</td>
            <td>\(S_1\)</td>
            <td>\(q_4\) (STOP)</td>
            <td>\(S_2\)</td>
            <td>\(Ly_1 \leq d_1 \& Ly_2 \geq d_1\)</td>
            <td>\(\delta_2' := 0.07, r_2' := 0\)</td>
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
            <td>\(\delta_1' := 0.07, r_1' := 0\)</td>
        </tr>
        <tr>
            <td>\(q_2\) (ACC)</td>
            <td>\(S_2\)</td>
            <td>\(q_2\) (ACC)</td>
            <td>\(S_4\)</td>
            <td>\(Ly_1 \geq d_1 \& Ly_2 \geq d_1 \& \theta_1 \leq \frac{\pi}{2} \& \theta_2 \leq \frac{\pi}{2}\)</td>
            <td>\(\delta_1' := 0.07, r_1' := 0\)</td>
        </tr>
        <tr>
            <td>\(q_3\) (AEB)</td>
            <td>\(S_2\)</td>
            <td>\(q_3\) (AEB)</td>
            <td>\(S_4\)</td>
            <td>\(Ly_1 \geq d_1 \& Ly_2 \geq d_1 \& \theta_1 \leq \frac{\pi}{2} \& \theta_2 \leq \frac{\pi}{2}\)</td>
            <td>\(\delta_1' := 0.07, r_1' := 0\)</td>
        </tr>
        <tr>
            <td>\(q_4\) (STOP)</td>
            <td>\(S_2\)</td>
            <td>\(q_4\) (STOP)</td>
            <td>\(S_4\)</td>
            <td>\(Ly_1 \geq d_1 \& Ly_2 \geq d_1 \& \theta_1 \leq \frac{\pi}{2} \& \theta_2 \leq \frac{\pi}{2}\)</td>
            <td>\(\delta_1' := 0.07, r_1' := 0\)</td>
        </tr>
        <tr>
            <td>\(q_1\) (CC)</td>
            <td>\(S_3\)</td>
            <td>\(q_1\) (CC)</td>
            <td>\(S_5\)</td>
            <td>\(Ly_1 \geq d_1 \& Ly_2 \geq d_1 \& \theta_1 \leq \frac{\pi}{2} \& \theta_2 \geq \frac{\pi}{2}\)</td>
            <td>\(\delta_1' := 0.07, r_1' := 0\)</td>
        </tr>
        <tr>
            <td>\(q_2\) (ACC)</td>
            <td>\(S_3\)</td>
            <td>\(q_2\) (ACC)</td>
            <td>\(S_5\)</td>
            <td>\(Ly_1 \geq d_1 \& Ly_2 \geq d_1 \& \theta_1 \leq \frac{\pi}{2} \& \theta_2 \geq \frac{\pi}{2}\)</td>
            <td>\(\delta_1' := 0.07, r_1' := 0\)</td>
        </tr>
        <tr>
            <td>\(q_3\) (AEB)</td>
            <td>\(S_3\)</td>
            <td>\(q_3\) (AEB)</td>
            <td>\(S_5\)</td>
            <td>\(Ly_1 \geq d_1 \& Ly_2 \geq d_1 \& \theta_1 \leq \frac{\pi}{2} \& \theta_2 \geq \frac{\pi}{2}\)</td>
            <td>\(\delta_1' := 0.07, r_1' := 0\)</td>
        </tr>
        <tr>
            <td>\(q_4\) (STOP)</td>
            <td>\(S_3\)</td>
            <td>\(q_4\) (STOP)</td>
            <td>\(S_5\)</td>
            <td>\(Ly_1 \geq d_1 \& Ly_2 \geq d_1 \& \theta_1 \leq \frac{\pi}{2} \& \theta_2 \geq \frac{\pi}{2}\)</td>
            <td>\(\delta_1' := 0.07, r_1' := 0\)</td>
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

#### Application Validation

Tab. 4 shows the six initial state sets used for application validation. These six initial state sets contain six different state transition routes. The corresponding reachable sets are shown in Fig. 1.

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

Fig. 1 shows the reachable sets under six different state transition routes. As can be seen from the figure, the functions of the four discrete modes are all normal. The ego vehicle can maintain a safe relative distance from the front vehicle and no collision will occur. In addition, the nonlinearity of the system can be observed, which illustrates the complexity of the system. It can also be found that there is an over-estimation problem in the reachable sets, and some areas suddenly expand. This also reflects the necessity of the subsequent falsification process.

{{< figure src="images/application_validation.svg" title="Fig. 1. Application Validation." >}}


#### Reachable Sets with Cyberattacks

Tab. 5 shows four different initial state sets and the range of attack intensity per unit time under the two attack strategies.

<table>
    <script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    <caption>Tab. 5. Initial State Sets of Reachable Sets</caption>
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
            <td>19.50</td>
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
            <td>13.90</td>
            <td>0.00</td>
            <td>-2.40</td>
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
            <td>13.90</td>
            <td>1.80</td>
            <td>0.00</td>
        </tr>
        <tr>
            <td rowspan="2">\(In_2\)</td>
            <td rowspan="2">\(q_3\) -> \(q_4\)</td>            
            <td>min</td>
            <td>-0.01</td>
            <td>17.50</td>
            <td>0.00</td>
            <td>85.10</td>
            <td>0.00</td>
            <td>0.00</td>
            <td>-1e-9</td>
            <td>0.00</td>
            <td>5.00</td>
            <td>0.00</td>
            <td>99.00</td>
            <td>0.00</td>
            <td>0.00</td>
            <td>-1e-9</td>
            <td>13.90</td>
            <td>0.00</td>
            <td>-2.40</td>
        </tr>
        <tr>
            <td>max</td>
            <td>0.01</td>
            <td>18.00</td>
            <td>0.00</td>
            <td>85.10</td>
            <td>0.00</td>
            <td>0.00</td>
            <td>1e-9</td>
            <td>0.00</td>
            <td>5.00</td>
            <td>0.00</td>
            <td>99.00</td>
            <td>0.00</td>
            <td>0.00</td>
            <td>1e-9</td>
            <td>13.90</td>
            <td>1.80</td>
            <td>0.00</td>
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
            <td>-1.00</td>
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
            <td>1.00</td>
            <td>0.00</td>
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
            <td>-1.00</td>
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
            <td>1.00</td>
            <td>0.00</td>
        </tr>
    </tbody>
</table>

Fig. 2 shows the reachable sets of four different initial state sets under two attack strategies. It can be seen that when there is no cyberattack, the reachable sets do not intersect with the unsafe set. However, when the state quantity is disturbed by the cyberattack, the reachable sets intersect with the unsafe set. However, it is still unknown whether this is due to conservative estimates in reachability analysis. Therefore, further falsification is needed.

{{< figure src="images/reachable_sets.svg" title="Fig. 2. Reachable Sets." >}}


### Falsification with Deep Reinforcement Learning

#### Tool Error Comparisons

Due to the falsification part, we use Python to implement a method based on deep reinforcement learning to solve feasible attack strategies, so we need to compare the error between the Python code implementation and flow*. We compared the errors between the two code solutions under 27 different initial state sets, including root mean squared error (RMSE), mean absolute error (MAE), mean absolute percentage error (MAPE), and mean square error (MSE). Tab. 3 shows 27 initial state sets and the corresponding errors between tools.

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

Fig. 3 shows the errors under 27 initial state sets more intuitively. It can be seen that the two tools have a high degree of similarity and the errors are in a small range.

{{< figure src="images/tool_errors.svg" title="Fig. 3. Tool Errors." >}}

In more detail, Fig. 4 shows the variation of relative distance over time for 27 initial state sets. It can be seen that the results obtained by the two tools are highly consistent.

{{< figure src="images/tool_errors_comparison.svg" title="Fig. 4. Tool Error Tests." >}}

#### Performance Comparison of Attack Strategy Search Algorithms

<table>
    <script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    <caption>Tab. 4. Performance Comparison of Attack Strategy Search Algorithms</caption>
    <thead>
        <tr>
            <th rowspan="2">Algorithm</th>
            <th colspan="4">Minimum Cost</th>
            <th colspan="4">Successful Rate</th>
            <th colspan="4">Time Cost</th>
        </tr>
        <tr>
            <th>\(In_1\) - \(d_r\)</th>
            <th>\(In_1\) - \(v_1\)</th>
            <th>\(In_2\) - \(d_r\)</th>
            <th>\(In_2\) - \(v_1\)</th>
            <th>\(In_1\) - \(d_r\)</th>
            <th>\(In_1\) - \(v_1\)</th>
            <th>\(In_2\) - \(d_r\)</th>
            <th>\(In_2\) - \(v_1\)</th>
            <th>\(In_1\) - \(d_r\)</th>
            <th>\(In_1\) - \(v_1\)</th>
            <th>\(In_2\) - \(d_r\)</th>
            <th>\(In_2\) - \(v_1\)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>CE</td>
            <td>0.409</td>
            <td>0.682</td>
            <td>0.408</td>
            <td>0.680</td>
            <td>66.172%</td>
            <td>71.860%</td>
            <td>70.540%</td>
            <td>65.882%</td>
            <td>530.298</td>
            <td>530.367</td>
            <td>530.781</td>
            <td>543.308</td>
        </tr>
        <tr>
            <td>SA</td>
            <td>0.412</td>
            <td>0.680</td>
            <td>0.410</td>
            <td>0.676</td>
            <td>89.649%</td>
            <td>87.963%</td>
            <td>89.769%</td>
            <td>89.192%</td>
            <td>116.361</td>
            <td>116.419</td>
            <td>115.903</td>
            <td>115.419</td>
        </tr>
        <tr>
            <td>WC</td>
            <td>0.402</td>
            <td>0.675</td>
            <td>0.402</td>
            <td>0.666</td>
            <td>4.512%</td>
            <td>1.216%</td>
            <td>4.182%</td>
            <td>1.623%</td>
            <td>4573.060</td>
            <td>4499.111</td>
            <td>4675.637</td>
            <td>4628.965</td>
        </tr>
        <tr>
            <td>DP</td>
            <td>0.400</td>
            <td>0.667</td>
            <td>0.400</td>
            <td>0.665</td>
            <td>13.947%</td>
            <td>14.194%</td>
            <td>12.938%</td>
            <td>14.762%</td>
            <td>11748.529</td>
            <td>9949.106</td>
            <td>12013.184</td>
            <td>10234.273</td>
        </tr>
        <tr>
            <td>A2C</td>
            <td>0.408</td>
            <td>0.678</td>
            <td>0.405</td>
            <td>0.682</td>
            <td>1.456%</td>
            <td>1.456%</td>
            <td>2.427%</td>
            <td>1.456%</td>
            <td>179.092</td>
            <td>175.254</td>
            <td>174.752</td>
            <td>185.398</td>
        </tr>
        <tr>
            <td>DQN</td>
            <td>0.406</td>
            <td>0.674</td>
            <td>0.404</td>
            <td>0.670</td>
            <td>40.673%</td>
            <td>6.216%</td>
            <td>32.662%</td>
            <td>7.294%</td>
            <td>494.224</td>
            <td>484.012</td>
            <td>643.709</td>
            <td>513.895</td>
        </tr>
        <tr>
            <td>PPO</td>
            <td>0.403</td>
            <td>0.671</td>
            <td>0.402</td>
            <td>0.669</td>
            <td>11.111%</td>
            <td>15.375%</td>
            <td>36.190%</td>
            <td>24.671%</td>
            <td>386.462</td>
            <td>389.381</td>
            <td>387.235</td>
            <td>385.952</td>
        </tr>
        <tr>
            <td>A2C_Veri</td>
            <td>0.406</td>
            <td>0.678</td>
            <td>0.407</td>
            <td>0.675</td>
            <td>13.967%</td>
            <td>14.843%</td>
            <td>18.932%</td>
            <td>16.536%</td>
            <td>412.093</td>
            <td>392.047</td>
            <td>397.103</td>
            <td>403.572</td>
        </tr>
        <tr>
            <td>DQN_Veri</td>
            <td>0.402</td>
            <td>0.672</td>
            <td>0.400</td>
            <td>0.671</td>
            <td>27.311%</td>
            <td>6.454%</td>
            <td>28.444%</td>
            <td>5.546%</td>
            <td>469.901</td>
            <td>488.809</td>
            <td>556.677</td>
            <td>558.064</td>
        </tr>
        <tr>
            <td>PPO_Veri</td>
            <td>0.400</td>
            <td>0.668</td>
            <td>0.401</td>
            <td>0.665</td>
            <td>25.163%</td>
            <td>23.197%</td>
            <td>21.075%</td>
            <td>27.693%</td>
            <td>371.192</td>
            <td>381.942</td>
            <td>375.038</td>
            <td>369.173</td>
        </tr>
    </tbody>
</table>

#### Training of Deep Reinforcement Learning Models

We recorded all the deep reinforcement learning training processes, as shown in Fig. 5.

{{< figure src="images/drl_model_training.svg" title="Fig. 5. DRL Models Training Comparison." >}}

#### Analysis of Energy Consumption

We compare the energy consumption of different algorithms, including running time, memory usage and CPU usage, as shown in Fig. 6. It can be found that deep reinforcement learning, especially PPO, has the highest efficiency and can quickly find low-cost feasible attack strategies. In addition, its memory and CPU usage are relatively low, showing the advantages of falsification based on deep reinforcement learning.

{{< figure src="images/energy_consumption.svg" title="Fig. 6. Energy Consumption Comparison." >}}

