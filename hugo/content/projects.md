---
title: "Projects"
date: false
draft: false
heading: true
---

Here's a short list of recent - and relatively self-contained - software projects I've created, led, or principally developed.

</br>

## Work projects

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



---

#### matscholar-web*

<center>
<a href="https://github.com/materialsintelligence/matscholar-web" target="_blank">
    <img src="/matscholar.png" width="300" ></img>
</a>
</center>

Matscholar-Web is the front-end Plotly dash website for the Matscholar project, an NLP-based search engine of materials. Matscholar-web provides interactive access to more than 3M scientific papers and can search synthesis methods, non-canonical material names, materials descriptors, phases, characterization and modeling methods, applications, properties, and raw text. By searching and summarizing millions of scientific abstracts using algorithms designed specifically for materials data mining, Matscholar-web can be a powerful tool for exploring the published knowledge of materials, and it goes far beyond what Google Scholar's search offers!

*Disclaimer: I currently lead development of the frontend website only; I contribute to the backend, API, and  underlying algorithms but those are led (and were principally developed by) others in the [Materials Intelligence organization](https://github.com/materialsintelligence)!*

- [Github](https://github.com/materialsintelligence/matscholar-web)
- [Website](https://www.matscholar.com/)
- [Publication](https://doi.org/10.1038/s41586-019-1335-8)




</br>

## Personal projects

---

### ucbviz2019

<center>
<a href="https://calgraddata.herokuapp.com" target="_blank">
    <img src="/ucbviz2019_still.png" width="500"></img>
</a>
</center>


This was the overall winning entry for the (schoolwide) UC Berkeley Graduate Financial Data Visualization Contest (2019). Our entry was an interactive website (written in Plotly Dash) for analyzing trends in the UC Berkeley cost of attendance for graduate and professional programs. We incorporated predictive modelling for future program years as well. You can read more about it in [this post](/posts/ucbviz2019).

- [Github](https://github.com/calgraddata/ucbviz2019)
- [Website](https://calgraddata.herokuapp.com)



---

### dion

<center>
<a href="https://calgraddata.herokuapp.com" target="_blank">
    <img src="/example_tasks_by_project.png" width="600" ></img>
</a>
</center>

dion (Dionysus) is an opinionated and ultra-minimal productivity tool operated from the command line. It intelligently tells you what to work on based on task prorities and status (done, doing, on hold, etc.) and keeps all your tasks as local markdown files in a very simple format.

- [Github](https://github.com/ardunn/dion)


---

### mmai (in progress)

mmai (mma-ai) is a project for predicting the outcomes of mixed martial arts bouts using machine learning. It includes code for scraping multiple data sources, processing, and learning trends in MMA data with time series forecasting. This project is in progress at the moment, so if you're eager to use it to make some extra money at the sportsbook, please be patient!

- [Github](https://github.com/ardunn/mmai)



---

### nikobellicbot

<center>
<img src="/nbbot.png" ></img>
</center>

NikoBellicBot is a heuristic-based Reddit comment and voice-quip bot which quotes Niko Bellic, the protagonist of Rockstar Games' 2008 title *GTAIV*. It's currently running 24/7 on an old Android phone (via Termux) sitting in a drawer. **Fair warning: the bot is quite vulgar**; all of its dialogue is taken directly from the game. It's quite basic right now, but if NBB gets enough attention, it may be worth adding in NLP to make the bot seem more... "sentient".

- [Github](https://github.com/ardunn/nikobellicbot)
- [Website](https://www.reddit.com/u/nikobellicbot)
