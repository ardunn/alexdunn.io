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

Here we'll use the notation `$ p_{\text{Stanford}} $` to represent the Stanford acceptance probability. This number is treated as a population statistic. Our overall acceptance probability is `$ p_{\text{roommate}} $`, and it's point estimate is what we previously calculated from our sample: `$ p_{\text{roommate}} = 0.0229 $`.

Our hypothesis test is:

<div>$$H_{0}: p_{\text{roommate}} \geq p_{\text{Stanford}} $$</div>
<div>$$H_{a}: p_{\text{roommate}} < p_{\text{Stanford}} $$</div>


Work in progress, rest coming soon!



