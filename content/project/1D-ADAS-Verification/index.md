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

## Content
- [Content](#content)
  - [Abstract](#abstract)
  - [Introduction](#introduction)
  - [Related Work](#related-work)
  - [System Assumptions and Problem Statements](#problems)
  - [Methods for Enhanced Verification and Falsification of ADAS Safety with Security](#methods)
  - [Experiments and Results](#experiments)
  - [Conclusion](#conclusion)

### Abstract
Ensuring safety of advanced driver assistance systems (ADASs) is crucial to the reliability and automation of autonomous vehicles. ADASs are featured in intra-vehicle as well as inter-vehicle communications, which brings about cybersecurity threats that may eventually lead to safety violations or even collisions. Moreover, cyberattacks introduce complex yet unpredictable uncertainties to the closed-loop systems composed of ADASs and the vehicle dynamics, and this makes safety verification extremely conservative or even inconclusive. This paper is devoted to tackling this challenge and proposes an enhanced approach of verification and falsification for ADASs under cyberattacks. We first use hybrid automata to model the vehicle dynamics with ADASs in the loop, and verify their dynamic behaviors through reachability analysis. In cases that no conclusion can be drawn, a falsification process based on dynamic programming is designed for searching cyberattack strategies that may lead to safety violations. Finally, experimental results show that by minimizing the cost of cyberattacks, the proposed approach can effectively find safety violations caused by cyberattacks, thereby enhancing verification performances on safety and cybersecurity guarantees. 
