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
- [Github](https://github.com/hackingmaterials/automatminer/)
- [Docs](http://hackingmaterials.lbl.gov/automatminer/)
- Publication: coming soon

Automatminer is an automatic, general purpose machine learning pipeline for predicting the properties of materials. It works for most materials datasets and includes aspects of AutoML, transfer learning, and reproducible benchmarking (through our benchmark Matbench, analagous to ImageNet for image classification). It is completely automatic and has similar performance to hand-tuned materials ML models. Automatminer is pip installable and can be used by anyone with a Python installation.


---

#### rocketsled 
- [Github](https://github.com/hackingmaterials/rocketsled) 
- [Docs](https://hackingmaterials.lbl.gov/rocketsled/)
- [Publication](https://doi.org/10.1088/2515-7639/ab0c3d)

Rocketsled is a black-box optimization package "on rails" for running expensive, high-throughput computations. For example, if you have 1M configurations of a chemical process you'd like to simulate, an objective metric to optimize (e.g., reaction rate), and an expensive forward simulation (like finite-difference method), *but only the resoures to run 1,000 simulations* - rocketsled will help you find the optimal configuration. It is agnostic to the choice of optimization algorithm, the computer it is run on (from a local laptop to a queued supercomputing center), and the problem it is optimizing (hyperparameter tuning, _ab initio_ calculations, engineering simulations, etc.). The advantage of rocketsled over similar optimization packages is that it is designed with parallel computation in mind, meaning you can run many expensive simulations in parallel. Rocketsled is pip installable and can be used by anyone with a Python installation.

---

#### matscholar-web*
- [Github](https://github.com/materialsintelligence/matscholar-web)
- [Website](https://www.matscholar.com/)
- [Publication](https://doi.org/10.1038/s41586-019-1335-8)

Matscholar-Web is the front-end Plotly dash website for the Matscholar project, an NLP-based search engine of materials. Matscholar-web provides interactive access to more than 3M scientific papers and can search synthesis methods, non-canonical material names, materials descriptors, phases, characterization and modeling methods, applications, properties, and raw text. By searching and summarizing millions of scientific abstracts using algorithms designed specifically for materials data mining, Matscholar-web can be a powerful tool for exploring the published knowledge of materials, and it goes far beyond what Google Scholar's search offers!

*Disclaimer: I currently lead development of the frontend website only; I contribute to the backend, API, and  underlying algorithms but those are led (and were principally developed by) others in the [Materials Intelligence organization](https://github.com/materialsintelligence)!*

</br>

## Personal projects

---

### ucbviz2019

- [Github](https://github.com/calgraddata/ucbviz2019)
- [Website](https://calgraddata.herokuapp.com)

This was the overall winning entry for the (schoolwide) UC Berkeley Graduate Financial Data Visualization Contest (2019). Our entry was an interactive website (written in Plotly Dash) for analyzing trends in the UC Berkeley cost of attendance for graduate and professional programs. You can read more about it in [this post](/posts/ucbviz2019).



---

### mmai (in progress)

- [Github](https://github.com/ardunn/mmai)

mmai (mma-ai) is a project for predicting the outcomes of mixed martial arts bouts using machine learning. It includes code for scraping multiple data sources, processing, and learning trends in MMA data with time series forecasting. This project is in progress at the moment, so if you're eager to use it to make some extra money at the sportsbook, please be patient!
