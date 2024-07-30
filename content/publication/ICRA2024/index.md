---
title: 'Enhanced Verification and Falsification of ADAS Under Cyber Attacks Using Hybrid Automaton Reachability and Heuristic Search'

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here
# and it will be replaced with their full name and linked to their profile.
authors:
  - admin
  - Qi Sun
  - Liren Yang
  - Chunjie Zhou

# Author notes (optional)
author_notes:
#  - 'Equal contribution'
#  - 'Equal contribution'

date: '2024-04-06T00:00:00Z'
doi: ''

# Schedule page publish date (NOT publication's date).
publishDate: '2024-04-06T00:00:00Z'

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ['paper-conference']

# Publication name and optional abbreviated publication name.
publication: In *2025 IEEE International Conference on Robotics and Automation (ICRA)*
publication_short: In *Atlant, USA*

abstract: Advanced driver assistance systems (ADAS) are driving increased levels of vehicle automation, and it is critical to ensure their functional safety. The networking of autonomous vehicles presents a significant cybersecurity risk, which may affect functional safety. However, traditional techniques for system verification do not account for the presence of cyber attacks, rendering them inapplicable to ADAS. To address this issue, attack-guided falsification of ADAS is introduced. First, hybrid automata are used to model the different functions of ADAS to systematically analyze their dynamic behaviors and interactions. Then, Flow* is applied to compute reachable sets given an initial set of states. These reachable sets are compared with reachable sets obtained by cyber attacks, revealing difference sets generated due to cyber attacks. These difference sets are then intersected with the unsafe sets defined by the safety specifications, resulting in the unsafe sets caused by cyber attacks. Finally, three different algorithms for cyber attack path search are used to demonstrate that generating the unsafe set is not an overestimation, thereby falsifying the safety of ADAS under cyber attacks. Experimental results demonstrate that attack-guided falsification can effectively and intuitively falsify the safety of ADAS under cyber attacks.

# Summary. An optional shortened abstract.
#summary: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis posuere tellus ac convallis placerat. Proin tincidunt magna sed ex sollicitudin condimentum.

tags: []

# Display this page in the Featured widget?
featured: true

# Custom links (uncomment lines below)
# links:
# - name: Custom Link
#   url: http://example.org

#url_pdf: 'https://cichengzi.github.io/publication/CCC2024-RCA/conference-paper.pdf'
#url_code: 'https://github.com/HugoBlox/hugo-blox-builder'
#url_dataset: 'https://github.com/HugoBlox/hugo-blox-builder'
#url_poster: ''
#url_project: ''
#url_slides: ''
#url_source: 'https://github.com/HugoBlox/hugo-blox-builder'
#url_video: 'https://youtube.com'

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/pLCdAaMFLTE)'
  focal_point: ''
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects:
#  - example

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
#slides: example
---

This is a paper about enhanced verification and falsification of ADAS under cyber attacks using hybrid automaton reachability and heuristic search.
