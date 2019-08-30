+++
title = "Finding Roommates: Data Flows n' Janky Stats"
description = ""
date = "2019-08-08"
heading= true
+++

<script type="text/javascript"
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
  tex2jax: {
    inlineMath: [['$','$'], ['\\(','\\)']],
    displayMath: [['$$','$$'], ['\[','\]']],
    processEscapes: true,
    processEnvironments: true,
    skipTags: ['script', 'noscript', 'style', 'textarea', 'pre'],
    TeX: { equationNumbers: { autoNumber: "AMS" },
         extensions: ["AMSmath.js", "AMSsymbols.js"] }
  }
});
</script>

<script type="text/x-mathjax-config">
  MathJax.Hub.Queue(function() {
    // Fix <code> tags after MathJax finishes running. This is a
    // hack to overcome a shortcoming of Markdown. Discussion at
    // https://github.com/mojombo/jekyll/issues/199
    var all = MathJax.Hub.getAllJax(), i;
    for(i = 0; i < all.length; i += 1) {
        all[i].SourceElement().parentNode.className += ' has-jax';
    }
});
</script>

### Finding new roommates can be a serious pain. 

Both of my housemates moved onto bigger and better things in July, so the unfortunate responsibility to find replacements fell upon me. 99% of the time, I'd call upon a friend to fill a spot, but our house is a bit out in the sticks -- far away from the happening SF Bay tech hubs and city centers, and nobody I knew in the area was looking to change their living arrangement.

So I turned to the trusty backwater of the internet. *Craigslist.*

### The Screening

Craigslist is a reliable tool, insofar that it's guaranteed to give you a large population of replies. But here's a simple fact about Craigslist: it's *filled* with scammers, criminals, and otherwise shady people who you'd rather not live with. So my landlord and I devised a screening procedure to hopefully weed out the slobs, petty criminals, bots, and serial killers of the interweb. 

![screening](/screening_big.png)

First comes a short conversation over email, straight from the ad. Then, a short phone interview. If that all goes well, we invite them over to the house (we'd hope to screen out any sketchy people by this point). If they like the house and we like them, they move onto our landlord's approval process. Then, they're our new roommate!

### Results

Below is a Sankey Diagram (made with [SankeyMatic](http://sankeymatic.com/)) of the whole process over the last two months. In total, almost 100 responses screened! 

<div class="image">
   <img  src="/roommates_sankey.png" alt="Some awesome text"/>
</div>

*Hint: Hover over the picture to zoom!*

In the end, one of our roommates wound up being a craigslister and the other was from a personal connection.

Breaking down the stats, final "acceptance rate" for all candidates is 2/87, or 2.29%. If we limit that to Craigslist inquiries only, it's 1/67, or 1.49% -- even lower! That's [lower](https://www.educationcorner.com/colleges-with-lowest-acceptance-rates.html) than Stanford, Harvard, Yale, MIT, Princeton, and Caltech. So you might say getting into our house is harder than getting into the best universities in the world. :)

If you did say that though, the analyst in me would tell you to hold up! This is a textbook sampling problem, our *n* is <100 in both cases! The college admissions statistics, in contrast, are taken frrom hundreds of thousands of data points. If we had only interviewed half the candidates and accepted none, would our true acceptance rate be 0%? Of course not. We have data on a sample of a population, not comprehensive data of the population itself. So how can we determine whether our screening process is more selective than the world's top universities?

### We need to use some statistics to answer this pressing and important question.


Let's get a measure of probability for whether our house acceptance rate is in fact smaller than say, Stanford's acceptance rate of 5.1% (admission year 2019). **First, we must form a proper null hypothesis.** We will formulate our null hypothesis such that rejecting it indicates our acceptance rate is less than Stanford's. If we fail to reject the null hypothesis, there is insufficient statistical evidence.

Here we'll use the notation `$ p_{\text{Stanford}} $` to represent the Stanford acceptance probability. This number is treated as a population statistic. Our overall acceptance probability is `$ p_{\text{roommate}} $`, and it's point estimate is what we previously calculated from our sample: `$ p_{\text{roommate}} = 0.0229 $`. Stanford's acceptance rate was `$ p_{\text{Stanford}} = 0.051$` in 2019. 

Our hypothesis test is:

<div>$$H_{0}: p_{\text{roommate}} \geq p_{\text{Stanford}} $$</div>
<div>$$H_{a}: p_{\text{roommate}} < p_{\text{Stanford}} $$</div>

We need to determine a the test statistic of some type for `$ p_{\text{roommate}}$`. In our case, we need a statistic for whether the proportion of *one* variable with *two* outcomes is different from the expected proportion; in our case, the outcomes are whether a candidate becomes a roommate or not, and our "expected proportion" is `$ p_{\text{Stanford}} $`. The two usual tests for this scenario are:

</br>

##### Pearson's `$ \chi^{2} $` one-variable test: 
A very popular test based on a `$ \chi^{2} $`-distribution (an approximation of a normal distribution). This test holds as long as the following hold:

1. The sampling is random (i.e., each population individual has an equal chance of being selected for the sample)
2. The observations are independent (e.g., Observation 52 does not depend on Observation 51)
3. The expected frequencies of each outcome are greater than 1 and mostly greater than 5. Expected freqency is just the expected probability multiplied by the sample size. the exact cutoff for "mostly" varies by who you ask, but 80% is commonly used. 

</br>

#####  Binomial test
An exact test, meaning it is not based on approximate distributions or parametric assumptions. This test holds as long as:

1. The sampling is random
2. The observations are independent.

</br>

##### Applying the binomial test

The `$ \chi^{2} $` test will not work here since while 1 and 2 hold, our expected frequency for being a roommate is `$ p_{\text{Stanford}} \cdot n_{\text{candidates}} = 0.102$`, and we need **all** of our expected frequencies to be greater than 1.  We'll use the binomial test statistic based on the probability mass function, defined as:

<div>$$P(X=k) = C(n, k)p^{k}(1-p)^{n-k} $$</div>

Where `$ n $` is the number of samples, `$ k $` is the number of "successes" (actually being a roommate, in our case), `$ C(n, k)$` is the formula for the number of combinations for `$ k$` selections from `$ n$` objects, and `$ p $` is just our population probability, `$ p_{\text{Stanford}} $`. If you're wondering where this equation comes from, I'll refer you to [this excellent derivation](https://newonlinecourses.science.psu.edu/stat414/node/67/) which requires little math background and is written in plain language (for the non-math savvy amongst us).

Let's set some variables from what we know:
* 

### Conclusion (rename this)

Talk about how convincing a case we made, but that it is still not good enough. Since Stanford's applicants are usually driven people with their lives put together and craigslisters are just random people, the pool of people our populations represent are fundamentall different. This is one of the practical challenges with modern data science
