---
title: Enhanced Verification and Falsification of Safety and Cybersecurity for ADAS Based on Reachability Analysis and Dynamic Programming
summary: Enhanced Verification and Falsification of Safety and Cybersecurity for ADAS Based on Reachability Analysis and Dynamic Programming.
tags:
  - Formal Analysis
  - Reachability Analysis
featured: false

date: '2024-08-25T00:00:00Z'

# Optional external URL for project (replaces project detail page).
#external_link: 'https://github.com/liuluddex/1D-ADAS-Verification'

#image:
#  caption: Photo by rawpixel on Unsplash
#  focal_point: Smart

links:
#  - icon: twitter
#    icon_pack: fab
#    name: Follow
#    url: https://twitter.com/georgecushen
url_code: 'https://github.com/liuluddex/1D-ADAS-Verification'
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

<br><br><br><br><br><br><br>
- [Experimental Results](#experimental-results)
  - [Application Validation](#application-validation)
  - [Reachable Sets with Cyberattacks](#reachable-sets-with-cyberattacks)
  - [Tool Error Comparisons](#tool-error-comparisons)
  - [Performance Comparison of Attack Strategy Search Algorithms](#performance-comparison-of-attack-strategy-search-algorithms)

### Experimental Results

#### Application Validation
In this section, we present the application validation results of the Flow* model in more detail. First, we give six initial state sets, as shown in Tab. 1.

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

<table>
    <script type="text/javascript" async
      src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
    </script>
    <caption>Tab. 1. Initial State Sets of Application Validation</caption>
    <thead>
        <tr>
            <th>Set</th>
            <th>Route</th>
            <th>Bound</th>
            <th>\(v_1\)</th>
            <th>\(v_2\)</th>
            <th>\(d_1\)</th>
            <th>\(d_2\)</th>
            <th>\(t\)</th>
            <th>\(d_r\)</th>
            <th>\(q\)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan="2">\(S_1\)</td>
            <td rowspan="2">\(q_1\)</td>            
            <td>min</td>
            <td>17.0</td>
            <td>15.0</td>
            <td>0.0</td>
            <td>120.0</td>
            <td>0.0</td>
            <td>120.0</td>
            <td>1</td>
        </tr>
        <tr>
            <td>max</td>
            <td>17.01</td>
            <td>15.0</td>
            <td>0.0</td>
            <td>120.0</td>
            <td>0.0</td>
            <td>120.0</td>
            <td>1</td>
        </tr>
        <tr>
            <td rowspan="2">\(S_2\)</td>
            <td rowspan="2">\(q_2\)</td>            
            <td>min</td>
            <td>17.0</td>
            <td>10.0</td>
            <td>0.0</td>
            <td>50.0</td>
            <td>0.0</td>
            <td>50.0</td>
            <td>1</td>
        </tr>
        <tr>
            <td>max</td>
            <td>17.01</td>
            <td>10.0</td>
            <td>0.0</td>
            <td>50.0</td>
            <td>0.0</td>
            <td>50.0</td>
            <td>1</td>
        </tr>
        <tr>
            <td rowspan="2">\(S_3\)</td>
            <td rowspan="2">\(q_1\) -> \(q_2\)</td>
            <td>min</td>
            <td>17.0</td>
            <td>5.0</td>
            <td>0.0</td>
            <td>80.0</td>
            <td>0.0</td>
            <td>80.0</td>
            <td>1</td>
        </tr>
        <tr>
            <td>max</td>
            <td>17.01</td>
            <td>5.0</td>
            <td>0.0</td>
            <td>80.0</td>
            <td>0.0</td>
            <td>80.0</td>
            <td>1</td>
        </tr>
        <tr>
            <td rowspan="2">\(S_4\)</td>
            <td rowspan="2">\(q_3\) -> \(q_4\)</td>
            <td>min</td>
            <td>17.0</td>
            <td>5.0</td>
            <td>0.0</td>
            <td>15.0</td>
            <td>0.0</td>
            <td>15.0</td>
            <td>1</td>
        </tr>
        <tr>
            <td>max</td>
            <td>17.01</td>
            <td>5.0</td>
            <td>0.0</td>
            <td>15.0</td>
            <td>0.0</td>
            <td>15.0</td>
            <td>1</td>
        </tr>
        <tr>
            <td rowspan="2">\(S_5\)</td>
            <td rowspan="2">\(q_3\) -> \(q_2\)</td>
            <td>min</td>
            <td>17.0</td>
            <td>6.8</td>
            <td>0.0</td>
            <td>19.0</td>
            <td>0.0</td>
            <td>19.0</td>
            <td>1</td>
        </tr>
        <tr>
            <td>max</td>
            <td>17.01</td>
            <td>6.8</td>
            <td>0.0</td>
            <td>19.0</td>
            <td>0.0</td>
            <td>19.0</td>
            <td>1</td>
        </tr>
        <tr>
            <td rowspan="2">\(S_6\)</td>
            <td rowspan="2">\(q_2\) -> \(q_3\)</td>
            <td>min</td>
            <td>17.0</td>
            <td>12.0</td>
            <td>0.0</td>
            <td>11.0</td>
            <td>0.0</td>
            <td>11.0</td>
            <td>1</td>
        </tr>
        <tr>
            <td>max</td>
            <td>17.01</td>
            <td>12.0</td>
            <td>0.0</td>
            <td>11.0</td>
            <td>0.0</td>
            <td>11.0</td>
            <td>1</td>
        </tr>
    </tbody>
</table>

Furthermore, based on the constructed Flow* model [normal.model](https://liuluddex.github.io/uploads/1D-ADAS-Verification/normal.model), the reachable sets under given initial state sets are solved, as shown in Fig. 1.

{{< figure src="images/application_validation.png" title="Fig. 1. Application Validation." >}}



#### Reachable Sets with Cyberattacks

In this section, we will show more reachable sets corresponding to the initial state sets in Tab. 2, as shown in Fig. 2. 

<table>
    <script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    <caption>Tab. 2. Initial State Sets of Reachable Sets</caption>
    <thead>
        <tr>
            <th>Set</th>
            <th>Route</th>
            <th>Bound</th>
            <th>\(v_1\)</th>
            <th>\(v_2\)</th>
            <th>\(d_1\)</th>
            <th>\(d_2\)</th>
            <th>\(t\)</th>
            <th>\(d_r\)</th>
            <th>\(\omega_{d_r}\)</th>
            <th>\(\omega_{v_1}\)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan="2">\(S_1\)</td>
            <td rowspan="2">\(q_3\) -> \(q_4\)</td>            
            <td>min</td>
            <td>17.0</td>
            <td>5.0</td>
            <td>0.0</td>
            <td>15.9</td>
            <td>0.0</td>
            <td>15.9</td>
            <td>0.0</td>
            <td>-4.0</td>
        </tr>
        <tr>
            <td>max</td>
            <td>18.5</td>
            <td>5.0</td>
            <td>0.0</td>
            <td>15.9</td>
            <td>0.0</td>
            <td>15.9</td>
            <td>4.0</td>
            <td>0.0</td>
        </tr>
        <tr>
            <td rowspan="2">\(S_2\)</td>
            <td rowspan="2">\(q_3\) -> \(q_4\)</td>            
            <td>min</td>
            <td>9.5</td>
            <td>3.0</td>
            <td>0.0</td>
            <td>8.0</td>
            <td>0.0</td>
            <td>8.0</td>
            <td>0.0</td>
            <td>-4.0</td>
        </tr>
        <tr>
            <td>max</td>
            <td>11.0</td>
            <td>3.0</td>
            <td>0.0</td>
            <td>8.0</td>
            <td>0.0</td>
            <td>8.0</td>
            <td>4.0</td>
            <td>0.0</td>
        </tr>
        <tr>
            <td rowspan="2">\(S_3\)</td>
            <td rowspan="2">\(q_3\) -> \(q_4\)</td>            
            <td>min</td>
            <td>17.0</td>
            <td>5.0</td>
            <td>0.0</td>
            <td>30.0</td>
            <td>0.0</td>
            <td>30.0</td>
            <td>0.0</td>
            <td>/</td>
        </tr>
        <tr>
            <td>max</td>
            <td>18.5</td>
            <td>5.0</td>
            <td>0.0</td>
            <td>30.0</td>
            <td>0.0</td>
            <td>30.0</td>
            <td>4.0</td>
            <td>/</td>
        </tr>
        <tr>
            <td rowspan="2">\(S_4\)</td>
            <td rowspan="2">\(q_3\) -> \(q_4\)</td>            
            <td>min</td>
            <td>9.5</td>
            <td>3.0</td>
            <td>0.0</td>
            <td>16.0</td>
            <td>0.0</td>
            <td>16.0</td>
            <td>0.0</td>
            <td>/</td>
        </tr>
        <tr>
            <td>max</td>
            <td>11.0</td>
            <td>3.0</td>
            <td>0.0</td>
            <td>16.0</td>
            <td>0.0</td>
            <td>16.0</td>
            <td>4.0</td>
            <td>/</td>
        </tr>
    </tbody>
</table>

We simulated cyberattacks on perceptions of relative distance $d_r$ and ego vehicle speed $v_1$, respectively, with Flow* models [abnormal_dr.model](https://liuluddex.github.io/uploads/1D-ADAS-Verification/abnormal_dr.model) and [abnormal_v1.model](https://liuluddex.github.io/uploads/1D-ADAS-Verification/abnormal_v1.model).

{{< figure src="images/reachable_sets.png" title="Fig. 2. Reachable Sets." >}}

#### Tool Error Comparisons

We used gymnasium's environment as a template to build a similar ADAS env, and its core code is [here](https://liuluddex.github.io/uploads/1D-ADAS-Verification/adas_env.py).

{{< figure src="images/tool_errors.png" title="Fig. 3. Tool Error Comparisons." >}}

#### Performance Comparison of Attack Strategy Search Algorithms

We compared the performance of multiple search algorithms for searching feasible attack strategies, including Random Uniform ([RAND](https://liuluddex.github.io/uploads/1D-ADAS-Verification/random_uniform.py)), Cross Entropy (CE), Simulated Annealing (SA), and Dynamic Programming ([DP](https://liuluddex.github.io/uploads/1D-ADAS-Verification/dynamic_programming.py)). The results are shown in Tab. 4.

<table>
    <script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    <caption>Tab. 4. Performance Comparison of Attack Strategy Search Algorithms</caption>
    <thead>
        <tr>
            <th rowspan="2">Algorithm</th>
            <th colspan="4">Average Cost</th>
            <th colspan="4">Minimum Cost</th>
            <th colspan="4">Time Cost</th>
        </tr>
        <tr>
            <th>\(S_1\) - \(d_r\)</th>
            <th>\(S_1\) - \(v_1\)</th>
            <th>\(S_2\) - \(d_r\)</th>
            <th>\(S_2\) - \(v_1\)</th>
            <th>\(S_1\) - \(d_r\)</th>
            <th>\(S_1\) - \(v_1\)</th>
            <th>\(S_2\) - \(d_r\)</th>
            <th>\(S_2\) - \(v_1\)</th>
            <th>\(S_1\) - \(d_r\)</th>
            <th>\(S_1\) - \(v_1\)</th>
            <th>\(S_2\) - \(d_r\)</th>
            <th>\(S_2\) - \(v_1\)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>RAND</td>
            <td>2.257</td>
            <td>2.975</td>
            <td>1.893</td>
            <td>/</td>
            <td>1.984</td>
            <td>2.916</td>
            <td>1.496</td>
            <td>/</td>
            <td>387.918</td>
            <td>375.986</td>
            <td>385.402</td>
            <td>/</td>
        </tr>
        <tr>
            <td>CE</td>
            <td>1.995</td>
            <td>3.267</td>
            <td>0.533</td>
            <td>3.255</td>
            <td>1.740</td>
            <td>2.904</td>
            <td>0.480</td>
            <td>3.236</td>
            <td>533.561</td>
            <td>538.393</td>
            <td>596.698</td>
            <td>513.465</td>
        </tr>
        <tr>
            <td>SA</td>
            <td>1.938</td>
            <td>2.959</td>
            <td>1.284</td>
            <td>3.312</td>
            <td>1.744</td>
            <td>2.910</td>
            <td>0.556</td>
            <td>3.013</td>
            <td>374.980</td>
            <td>369.274</td>
            <td>384.005</td>
            <td>361.785</td>
        </tr>
        <tr>
            <td>DP</td>
            <td>2.125</td>
            <td>3.455</td>
            <td>1.347</td>
            <td>3.238</td>
            <td>1.740</td>
            <td>2.896</td>
            <td>0.480</td>
            <td>2.572</td>
            <td>2497.692</td>
            <td>4196.656</td>
            <td>1775.631</td>
            <td>3641.464</td>
        </tr>
    </tbody>
</table>

Fig. 4 shows a scenario where an unsafe state is entered when the perception of relative distance is incorrect.

{{< figure src="images/1D-ADAS-Verification-motion_simulation.gif" title="Fig. 4. Motion Simulation." >}}
