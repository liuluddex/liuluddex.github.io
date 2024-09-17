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

- [Experimental Results](#experimental-results)
  - [Application Validation](#application-validation)
  - [Reachable Sets with Cyberattacks](#reachable-sets-with-cyberattacks)
  - [Tool Error Comparisons](#tool-error-comparisons)
  - [Performance Comparison of Attack Strategy Search Algorithms](#performance-comparison-of-attack-strategy-search-algorithms)

### Experimental Results

#### Application Validation

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
            <th>\(theta_2\)</th>
            <th>\(r_2\)</th>
            <th>\(\delta_2\)</th>
            <th>\(t\)</th>
            <th>\(d_r\)</th>
            <th>\(q\)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan="2">\(S_1\)</td>
            <td rowspan="2">\(q_3\) -> \(q_4\)</td>            
            <td>min</td>
            <td>0.00</td>
            <td>19.09</td>
            <td>0.00</td>
            <td>84.10</td>
            <td>0.00</td>
            <td>0.00</td>
            <td>-1e-19</td>
            <td>0.00</td>
            <td>5.00</td>
            <td>0.00</td>
            <td>98.00</td>
            <td>0.00</td>
            <td>0.00</td>
            <td>-1e-19</td>
            <td>0.00</td>
            <td>13.90</td>
            <td>1</td>
        </tr>
        <tr>
            <td>max</td>
            <td>0.00</td>
            <td>19.10</td>
            <td>0.00</td>
            <td>84.10</td>
            <td>0.00</td>
            <td>0.00</td>
            <td>-1e-19</td>
            <td>0.00</td>
            <td>5.00</td>
            <td>0.00</td>
            <td>98.00</td>
            <td>0.00</td>
            <td>0.00</td>
            <td>1e-19</td>
            <td>0.00</td>
            <td>13.90</td>
            <td>1</td>
        </tr>
    </tbody>  
</table>

#### Reachable Sets with Cyberattacks

#### Tool Error Comparisons

#### Performance Comparison of Attack Strategy Search Algorithms
