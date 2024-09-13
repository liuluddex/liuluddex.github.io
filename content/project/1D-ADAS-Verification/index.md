---
title: Enhanced Verification and Falsification of Safety and Cybersecurity for ADAS Based on Reachability Analysis and Dynamic Programming
summary: Enhanced Verification and Falsification of Safety and Cybersecurity for ADAS Based on Reachability Analysis and Dynamic Programming.
tags:
  - Formal Analysis
  - Reachability Analysis

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

[//]: # (## Content)

[//]: # (- [Content]&#40;#content&#41;)

[//]: # (  - [Abstract]&#40;#abstract&#41;)

[//]: # (  - [Introduction]&#40;#introduction&#41;)

[//]: # (  - [Related Work]&#40;#related-work&#41;)

[//]: # (  - [System Assumptions and Problem Statements]&#40;#problems&#41;)

[//]: # (  - [Methods for Enhanced Verification and Falsification of ADAS Safety with Security]&#40;#methods&#41;)

[//]: # (  - [Experiments and Results]&#40;#experiments&#41;)

[//]: # (  - [Conclusion]&#40;#conclusion&#41;)

[//]: # ()
[//]: # (### Abstract)

[//]: # (Ensuring safety of advanced driver assistance systems &#40;ADASs&#41; is crucial to the reliability and automation of autonomous vehicles. ADASs are featured in intra-vehicle as well as inter-vehicle communications, which brings about cybersecurity threats that may eventually lead to safety violations or even collisions. Moreover, cyberattacks introduce complex yet unpredictable uncertainties to the closed-loop systems composed of ADASs and the vehicle dynamics, and this makes safety verification extremely conservative or even inconclusive. This paper is devoted to tackling this challenge and proposes an enhanced approach of verification and falsification for ADASs under cyberattacks. We first use hybrid automata to model the vehicle dynamics with ADASs in the loop, and verify their dynamic behaviors through reachability analysis. In cases that no conclusion can be drawn, a falsification process based on dynamic programming is designed for searching cyberattack strategies that may lead to safety violations. Finally, experimental results show that by minimizing the cost of cyberattacks, the proposed approach can effectively find safety violations caused by cyberattacks, thereby enhancing verification performances on safety and cybersecurity guarantees. )

[//]: # ()
[//]: # (### Introduction)

[//]: # (#### Background)

[//]: # (With the development of autonomous driving technology, advanced driver assistance systems &#40;ADAS&#41; play an increasingly important role in intra-vehicle and inter-vehicle communications. However, this connectivity also brings serious cybersecurity threats, which may lead to safety violations and even traffic accidents. Therefore, it is crucial to ensure the safety and reliability of ADAS, especially in the face of potential cyberattacks.)

[//]: # ()
[//]: # (#### Challenge )

[//]: # (Cyberattacks introduce complex and unpredictable uncertainties, especially in the closed-loop system composed of ADAS and vehicle dynamics. This makes traditional safety verification methods too conservative or difficult to draw clear conclusions, resulting in insufficient guarantee of system safety.)

[//]: # ()
[//]: # (#### Project Goals )

[//]: # (This project is dedicated to solving the problem of security verification of ADAS under cyber attacks. It proposes a new method that combines verification and falsification to help detect cyberattack strategies that may lead to security violations, thereby enhancing the safety and cyber security of ADAS.)

[//]: # ()
[//]: # (#### Solution)

[//]: # (  * System Modeling)

[//]: # (  We first model the dynamics of a vehicle containing ADAS using hybrid automata to evaluate its dynamic behavior.)

[//]: # ()
[//]: # (  * Verification Process)

[//]: # (  Through reachability analysis, we can verify the system's security under normal conditions.)

[//]: # ()
[//]: # (  * Falsification Process)

[//]: # (  Without a clear conclusion, we designed a dynamic programming-based falsification process to explore cyberattack strategies that could lead to security violations.)

[//]: # ()
[//]: # (#### Experimental Results)

[//]: # (Experiments show that this method can effectively find security violations caused by cyberattacks. While reducing the cost of cyberattacks, it significantly improves the verification performance of the system, providing stronger protection for the safety and cyber security of ADAS.)

[//]: # ()
[//]: # (### Related Work)

[//]: # ()
[//]: # (### System Assumptions and Problem Statements)

[//]: # ()
[//]: # (### Methods for Enhanced Verification and Falsification of ADAS Safety with Security)

[//]: # ()
[//]: # (### Experiments and Results)

[//]: # ()
[//]: # (### Conclusion)

- [Experimental Results](#experimental_results)
  - [Application Validation](#application_validation)
  - [Reachable Sets with Cyberattacks](#reachable_sets)
  - [Tool Error Comparisons](#tool_error_comparison)
  - [Performance Comparison of Attack Strategy Search Algorithms](#performance_comparison)

### Experimental Results

#### Application Validation
In this section, we present the functional test results of the Flow* model in more detail. First, we give 20 initial state sets, as shown in Table 1.

[![Motion Simulation.](https://cichengzi.github.io/uploads/projects/1D-ADAS-Verification/motion_simulation.gif)(https://liuluddex.github.io/project/1d-adas-verification)]

#### Reachable Sets with Cyberattacks

#### Tool Error Comparisons

#### Performance Comparison of Attack Strategy Search Algorithms
