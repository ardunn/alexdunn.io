+++
title = "My (Running) Halls of Software Fame and Shame"
description = ""
date = "2019-09-22"
heading= true
+++

## TOC:

* What is this?
* [The Hall of Fame](#fame)
* [The Hall of Shame](#shame)


## What is this?

Much as great literature, high art, or great music deserves praise, so does software. And I mean software in all of its forms - from robust bash scripts which hide in the internet's shadows, to the expansive open-source projects known the world over, to weirdly helpful websites which refuse to run ads, and even to a select few high-gloss corporate products. 


#### The Hall of Fame
<img src="/hof.png" width="150"></img>

The **Hall of Fame** is a running compendium of my favorite codes, tools, and websites to which I owe a great deal of saved time and praise. While it doesn't include *all* the software I've ever found useful (e.g., things I use every day but have their problems), it does contain some which:

* have *huge* pros with respect to their cons,
* are elegantly written,
* aren't all that well known (yet)
* are doing good in the world, thanks to the kind hearts of their developers, or
* simply work better than anything else!

Hopefully you, dear reader, find some of them useful too.

</br>
#### Hall of Shame
Then there is the HOF's antithesis, the **Hall of Shame**: a list full of buggy, intrusive, resource-heavy, or otherwise appalling software which should simply be `rm -rf`'d off the face of the planet.

<img src="/hos.png" width="175"></img>

</br>
#### A quick disclaimer
If you find your favorite website/program/code in the Hall of Shame or the bane of your cyber-existence in the Hall of Fame, fret not. These are not expert reviews, just my opinions as a humble user and enthusiast. 

And with that out of the way, enjoy!

</br>

# <a name="fame"></a> The Hall of Fame

### Polybar
`Added 9/22/2019`

[Polybar](https://polybar.github.io/) is an open source status bar for linux. Works well, easy to configure. Utilitarian. Looks good if you want it to. The three area of my polybar look like:

<img src="/polybar_1.png"></img>
<img src="/polybar_2.png"></img>
<img src="/polybar_3.png"></img>

So at all times I have a view of the CPU usage, temp, memory usage, disk usage, network usage and signal, my current workspace, power consumption, etc (and it matches with my desktop theme!). You can do much better though if you put some time into it. Copy my config: [link](https://github.com/ardunn/scraps/blob/master/polybar_config.txt)

</br>
### Julia
`Added 9/22/2019`

[Julia](https://github.com/JuliaLang/julia) is an open soure programming language for scientific computing. You write it like MATLAB (i.e., it's interpreted) and it can be as fast as C or Fortran. It's easy to learn, has a lot of packages, and is *very* fast. I used it to run a Monte Carlo simulation when Python was orders of magnitude too slow. I'd wager Julia will play a growing role in scientific computing in the near future (watch out, R).

```
   _       _ _(_)_     |  Documentation: https://docs.julialang.org
  (_)     | (_) (_)    |
   _ _   _| |_  __ _   |  Type "?" for help, "]?" for Pkg help.
  | | | | | | |/ _` |  |
  | | |_| | | | (_| |  |  Version 1.0.4 (2019-05-16)
 _/ |\__'_|_|_|\__'_|  |  Official https://julialang.org/ release
|__/                   |

```

</br>
### Universal media server
`Added 9/22/2019`

[Universal media server](https://github.com/UniversalMediaServer/UniversalMediaServer/) is the lightweight, no-frills version of Plex/Kodi. I use it on my Raspberry Pi NAS to stream DLNA to our house's PS4 (when Kodi and Plex wouldn't work). They also have a very helpful forum to help you debug, if you need to.

<img src="/ums.png"></img>

</br>
### dmenu-extended
`Added 9/22/2019`

[dmenu-extended](https://github.com/MarkHedleyJones/dmenu-extended) is an open source dmenu ... well, extension - for linux. Press alt + space and you have a nice bar to find files, executables, and more. I use it a hundred times a day on my linux machine. If you're a Mac user, this basically has the same functionality as Spotlight, but is faster and more customizable. It has one job and does it well!

<img src="/dmenu-extended.png"></img>

</br>
### Notion
`Added 9/22/2019`

[Notion](https://notion.so) is a workspace company (app and website) - think of a mix between Trello and a markdown editor, if you're familiar with those. I was torn on actually putting Notion on this list because there are some major cons to using it - it's closed source, pay-to-use (past a certain amount of data), and has some clunky bugs. Despite all these software transgressions I've found it **so useful** that it gets my props nonetheless. I use it to track my work and personal projects, keep track of the books I'm reading, and help organize my day. It also has capabilities far beyond what I use it for, such as collaborative online workflows, wikis, etc. It's tremendously useful and I'd wager you could replace your favorite management tool with Notion (and no, this isn't a paid promotion).

<img src="/notion.png"></img>

</br>

### Draw.io
`Added 9/22/2019`

[Draw.io](https://draw.io) is a website (and now desktop app!) for making flowcharts and custom graphics. It's extremely easy to use and suprisingly versatile (once you get the hang of it). I use it for everything from making figures for papers to writing notes for classes. Here's a figure I made for one of our research group's projects using Draw.io:

<img src="/drawio.png" width="500"></img>

It supports Latex math typesetting and is resource-light even when manipulating *huge* diagrams. It just works(TM). In a direct comparison to something like Adobe Illustrator, it comes up short; but for a **free** application, it's quite amazing.

</br>

### Dark Reader
`Adde 9/22/2019`

[Dark reader](https://github.com/darkreader/darkreader) is a browser plugin for Chromium-based browsers that transforms regular webpages into dark mode webpages. What sets this plugin apart from the competitors is how *easy* on the eyes the colors are; other dark mode plugins display ultra-high contrast ratios (e.g., `#FFFFFF` on `#000000`) which are the reading equivalent of a staring contest with the sun, whereas Dark reader's color inversions feel like reading e-ink. Also it is easily toggle-able via `alt+shift+d`!

<img src="/darkreader.png" width="300"></img>

</br>
</br>
# <a name="shame"></a> The Hall of Shame

### MongoDB Compass
`Added 9/22/2019`

Slow. Slow. So...slow (I'm looking at you, Electron framework). No dark mode. Passwords get voided for no reason if you are adding a connection and click away from the "Add Connection" screen. You have to click at least 3 times to open up another connection (i.e., to look at 2 dbs at one time). In general Compass is a frustrating application, made even more infuriating by the fact there are few competitive free alternatives. Do better, MongoDB. Do better.

<img src="/mongodb_compass.png" width="500"></img>
