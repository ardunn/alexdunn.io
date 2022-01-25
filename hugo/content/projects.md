---
title: "Projects"
date: false
draft: false
heading: false
---

Here's a short list of recent - and relatively self-contained - open-source software projects I've created, led, or principally developed. 
If you are interested in larger scale projects that I helped develop, but did not lead (e.g., matminer), see my [Github profile](https://github.com/ardunn). If you are interested in non-open source projects I've lead , please contact me via email.

</br>

## Data Mining

---

#### automatminer

<center>
<a href="https://github.com/hackingmaterials/automatminer" target="_blank">
    <img src="/automatminer.png" width="300" ></img>
</a>
</center>

Automatminer is an automatic, general purpose machine learning pipeline for predicting the properties of materials. It works for most materials datasets and includes aspects of AutoML, transfer learning, and reproducible benchmarking (through our benchmark Matbench, analagous to ImageNet for image classification). It is completely automatic and has similar performance to hand-tuned materials ML models. Automatminer is pip installable and can be used by anyone with a Python installation.


- [Github](https://github.com/hackingmaterials/automatminer/)
- [Docs](http://hackingmaterials.lbl.gov/automatminer/)
- [Publication](https://doi.org/10.1038/s41524-020-00406-3)


---


#### matbench

<center>
<a href="https://github.com/hackingmaterials/matbench" target="_blank">
    <img src="/matbench.png" width="200" ></img>
</a>
</center>

Matbench is a online dynamic leaderboard (similar to online leaderboards for ImageNet) and Python package for benchmarking ML property prediction algorithms in materials science. The leaderboard is 
updated via pull request, is extensible to many types of materials data and benchmark versions, and contains comprehensive data about every algorithm on every ML task in every benchmark.
The leaderboard also contains task-specific leaderboards and high-level leaderboard overviews for making broad conclusions from diverse and complex materials-ML predictions. The python
package contains code for
 
- obtaining standardized  benchmarking data for solid-state chemistry and materials science in common formats (such as dataframes)
- recording algorithm results in self-contained and validatable intermediate formats for persistence, distribution, and reproduction
- automatically computing comprehensive error metrics for 10+ datasets spanning multiple domains of solid state materials science


Matbench is pip installable and can be used by anyone with a Python installation.

- [Github](https://github.com/materialsproject/matbench)
- [Docs](http://matbench.materialsproject.org)
- [Publication](https://doi.org/10.1038/s41524-020-00406-3)



</br>

## High throughput computing

---

#### rocketsled

<center>
<a href="https://github.com/hackingmaterials/rocketsled" target="_blank">
    <img src="/rocketsled.png" width="300" ></img>
</a>
</center>

Rocketsled is a black-box optimization package "on rails" for running expensive, high-throughput computations. For example, if you have 1M configurations of a chemical process you'd like to simulate, an objective metric to optimize (e.g., reaction rate), and an expensive forward simulation (like finite-difference method), *but only the resoures to run 1,000 simulations* - rocketsled will help you find the optimal configuration. It is agnostic to the choice of optimization algorithm, the computer it is run on (from a local laptop to a queued supercomputing center), and the problem it is optimizing (hyperparameter tuning, _ab initio_ calculations, engineering simulations, etc.). The advantage of rocketsled over similar optimization packages is that it is designed with parallel computation in mind, meaning you can run many expensive simulations in parallel. Rocketsled is pip installable and can be used by anyone with a Python installation.

- [Github](https://github.com/hackingmaterials/rocketsled)
- [Docs](https://hackingmaterials.lbl.gov/rocketsled/)
- [Publication](https://doi.org/10.1088/2515-7639/ab0c3d)


</br> 

## Natural Language Processing

---

#### lbnlp

<center>
<a href="https://github.com/lbnlp/lbnlp" target="_blank">
    <img src="/lbnlp1.png" width="300" ></img>
</a>
</center>

LBNLP (LBNL + NLP) is a collection of Natural Language Processing tools jointly developed by the Persson, Ceder, and HackingMaterials groups at Lawrence Berkeley National Laboratory. It includes methods for common NLP pre- and post-processing tasks as well as one-line commands to load models (such as named entity recognition, relevance classification, Word2Vec, BERT, and more)  we have trained and validated on millions of materials science texts.

- [Github](https://github.com/lbnlp/lbnlp)
- [Docs](http://lbnlp.github.io/lbnlp)


</br>


## Assorted Personal projects

---

### dsmt


<center>
   <img src="/dsmt.png" width="500"></img>
</center>


Dumb simple monitoring tool (DSMT) is a server process monitor Web UI meant to monitor the status of a single server's docker containers, systemd services, and arbitrary linux processes. I made it when other tools like Grafana, Prometheus, and LibreRMS were difficult to set up for simple process monitoring.

- [Github](https://github.com/ardunn/dsmt)


---

### dex

<center>
<a href="https://github.com/ardunn/dex" target="_blank">
    <img src="/example_tasks_by_project.png" width="600" ></img>
</a>
</center>

dex (Day-executor) is an opinionated and ultra-minimal productivity tool operated from the command line. It intelligently tells you what to work on based on task prorities and status (done, doing, on hold, etc.) and keeps all your tasks as local markdown files in a very simple format compatible with most markdown note-taking apps and version control systems. 

- [Github](https://github.com/ardunn/dex)



</br>
 
## Defunct (no longer maintained) personal projects

---

### ucbviz2019


<center>
<a href="https://calgraddata.herokuapp.com" target="_blank">
    <img src="/ucbviz2019_still.png" width="500"></img>
</a>
</center>


This was the overall winning entry for the schoolwide UC Berkeley Graduate Financial Data Visualization Contest (2019). Our entry was an interactive website (written in Plotly Dash) for analyzing trends in the UC Berkeley cost of attendance for graduate and professional programs. We incorporated predictive modelling for future program years as well. You can read more about it in [this post](/posts/ucbviz2019).

- [Github](https://github.com/calgraddata/ucbviz2019)
- [Website](https://calgraddata.herokuapp.com)

---

### wdash

<center>
<img src="/wdashv1_1.png" ></img>
</center>


wdash is a self-hosted weather dashboard that pulls data from OpenWeatherMaps API and Windy. The data you collect is yours forever and stays locally on a MongoDB. You can read more about it in [this post](/posts/wdashv1).

- [Github](https://github.com/ardunn/wdash)

---
 
### nikobellicbot

<center>
<img src="/nbbot.png" ></img>
</center>

NikoBellicBot is a heuristic-based Reddit comment and voice-quip bot which quotes Niko Bellic, the protagonist of Rockstar Games' 2008 title *GTAIV*. It's currently running 24/7 on an old Android phone (via Termux) sitting in a drawer. **Fair warning: the bot is quite vulgar**; all of its dialogue is taken directly from the game. It's quite basic right now, but if NBB gets enough attention, it may be worth adding in NLP to make the bot seem more... "sentient".

- [Github](https://github.com/ardunn/nikobellicbot)
- [Website](https://www.reddit.com/u/nikobellicbot)
