+++
title = "Halls of Software Fame and Shame (updated 06/2021)"
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


---

# <a name="fame"></a> The Hall of Fame


### albert
`Added 9/04/2021`

[albert](https://albertlauncher.github.io/) is a launcher for linux distributions. It's pretty and fast and works well for file search, unlike GNOME's launcher.

<img src="/albert.png"></img>

</br>


### vaultwarden (formerly bitwarden_rs)
`Added 6/20/2021`

[vaultwarden](https://github.com/dani-garcia/vaultwarden) is a self-hosted fork of Bitwarden, a password management server, written in rust. It is efficient enough to run on something as small as a raspberry pi. Although it is a bit of a pain to set up correctly, you can run it in docker and back up your credentials as sql files to your hearts content. I love it because I have convenient access to secure passwords and my data is under my control (as opposed to an external service).


<img src="/bwrs.png"></img>

</br>




### bpytop
`Added 6/7/2021`

[bpytop](https://github.com/aristocratos/bpytop) is a stable and generally reliable system monitor tool for Unix systems. I use it across almost every device I have.

<img src="/bpytop.png"></img>

</br>



### OpenAudible
`Added 2/9/2021`


[OpenAudible](https://github.com/openaudible/openaudible) is an open-source shareware ($12, as of 2021) application for converting Audible audiobooks into mp3 files.


<img src="/openaudible.png"></img>
*Image from the OpenAudible github repo: https://github.com/openaudlble*

</br>

 





### inxi
`Added 2/9/2021`

[inxi](https://github.com/smxi/inxi) is an minimal hardware information CLI. It works basically everywhere and tells you most of the things you need to know without too much info-spam (looking at you, `lshw`).

```
$ inxi -Fxz

System:    Kernel: 5.8.0-7625-generic x86_64 bits: 64 compiler: N/A Desktop: Gnome 3.36.4 Distro: Pop!_OS 20.04 LTS 
           base: Ubuntu 20.04 LTS Focal 
Machine:   Type: Laptop System: LENOVO product: 20K4S0EB00 v: ThinkPad X1C 5th W10DG serial: <filter> 
           Mobo: LENOVO model: 20K4S0EB00 v: SDK0J40697 WIN serial: <filter> UEFI: LENOVO v: N1MET49W (1.34 ) date: 07/02/2018 
Battery:   ID-1: BAT0 charge: 40.6 Wh condition: 49.0/57.0 Wh (86%) model: SMP 01AV431 status: Charging 
           Device-1: hid-0003:17EF:60EE.0034-battery model: Lenovo TrackPoint Keyboard II charge: N/A status: N/A 
           Device-2: hidpp_battery_5 model: Logitech Wireless Mouse MX Master 3 charge: 100% (should be ignored) 
           status: Discharging 
CPU:       Topology: Dual Core model: Intel Core i5-6200U bits: 64 type: MT MCP arch: Skylake rev: 3 L2 cache: 3072 KiB 
           flags: avx avx2 lm nx pae sse sse2 sse3 sse4_1 sse4_2 ssse3 vmx bogomips: 19200 
           Speed: 500 MHz min/max: 400/2800 MHz Core speeds (MHz): 1: 500 2: 500 3: 500 4: 500 
Graphics:  Device-1: Intel Skylake GT2 [HD Graphics 520] vendor: Lenovo driver: i915 v: kernel bus ID: 00:02.0 
           Display: x11 server: X.Org 1.20.8 driver: i915 resolution: 3840x2160~30Hz 
           OpenGL: renderer: Mesa Intel HD Graphics 520 (SKL GT2) v: 4.6 Mesa 20.3.2 direct render: Yes 
Audio:     Device-1: Intel Sunrise Point-LP HD Audio vendor: Lenovo driver: snd_hda_intel v: kernel bus ID: 00:1f.3 
           Sound Server: ALSA v: k5.8.0-7625-generic 
Network:   Device-1: Intel Ethernet I219-V vendor: Lenovo driver: e1000e v: 3.2.6-k port: efa0 bus ID: 00:1f.6 
..
```

</br>

### Jellyfin
`Added 2/13/2020`

[Jellyfin](https://github.com/jellyfin/jellyfin) is a lightweight, no-frills, FOSS version of Plex/Kodi. I use it on my Raspberry Pi NAS to stream DLNA to our house's PS4 (when Kodi and Plex wouldn't work) as well as other devices around the house. It has a beautiful interace with very little frills and *just works*.

<img src="/jellyfin.png"></img>

</br>


### BookPlayer (iOS)
`Added 2/13/2020`

[BookPlayer](https://github.com/TortugaPower/BookPlayer) is an [iOS-compatible](https://apps.apple.com/us/app/bookplayer/id1138219998) open source and free (monetarily, not free as in GNU-FOSS) audiobook player. It has a gorgeous, minimal app and adding local files, whether they be a single audiobook mp3 or a hundred m4a's, is a breeze. Highly recommended.

<img src="/bookplayer.PNG" height=500></img>

</br>

### Pi My Life Up
`Added 2/1/2020`

[Pi My Life Up](https://pimylifeup.com/) is a website dedicated to project guides for the Raspberry Pi single board computer (SBC). The span and depth of their content is truly impressive - their site hosts literally _hundreds_ of raspberry pi projects (many of them server/IT based, which I appreciate), and each of their guides is totally comprehensive - unlike most guides you'll find in the top 10 results of a Google search for "raspberry pi [insert thing here] guide". The authors of this site have obviously put a ton of hard work into the site and deserve all the recognition they can get.

P.S.: They also have several Arduino, Linux, electronics, etc. guides, but I think they're mostly known for their Raspberry Pi articles (if the name didn't let that on).

<img src="/pmluy.png"></img>



### Notability
`Added 12/12/2019`

[Notability](https://www.gingerlabs.com/) is the best note taking app (incorporating handwriting) I have ever used. For people who have to write to learn (e.g., me), having a sustainable system for keeping track of notes is crucial. Notability allows me to do that, in addition to incorporating the typical Apple Notes-style notes (typing, checklists, images, etc.). The ability to export and backup automatically is a huge plus as well. Depsite being a commercial project with closed-source code, t's a truly spectacular app and is worth every penny ($9.99 last I checked).
<img src="/notability.png" height=500></img>

### Keepass
`Added 12/12/2019`

[Keepass](https://keepass.info/) is an open-source, locally hosted password management system for those who don't trust online password managers. What you sacrifice in convenience, Keepass makes up for in simplicity. All your passwords are in a single (optional) movable file guarded by a master password - you and you alone are the guardian of your passwords. I recommend it without hesistation to power users.

<img src="/keepass.png">


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


---

# <a name="shame"></a> The Hall of Shame

</br>
### MongoDB Compass
`Added 9/22/2019`

Slow. Slow. So...slow (I'm looking at you, Electron framework). No dark mode. Passwords get voided for no reason if you are adding a connection and click away from the "Add Connection" screen. You have to click at least 3 times to open up another connection (i.e., to look at 2 dbs at one time). In general Compass is a frustrating application, made even more infuriating by the fact there are few competitive free alternatives. Do better, MongoDB. Do better.

<img src="/mongodb_compass.png" width="500"></img>



### Slack
`Added 9/30/2019`

Slack should do essentially what IRC does: store  short text conversations, and then retrieve them quickly when needed (along with the occasional image link). What does Slack *actually* do? Take eons to load **text** conversations, have integrations which are not helpful, implement an obtrusive way to switch between workspaces. Closed source. Admins can read all DMs. There's no dark mode on the app, and the color schemes are disgusting. Search sucks. There are better open source alternatives (Mattermost, Zulip). If you are lucky enough to use anything else, I implore you to do so. Stop using Slack.

<img src="/slack.png" width="500"></img>


### Apple Music App (mobile) 
`Added 10/19/2019`

First off, I want to say my gripes with Apple Music are about the app UI itself, not the music streaming, playlist selection, etc. The most frustrating thing about Apple Music is that Apple had something truly great: the Music app of a few years ago. But Apple being Apple is hellbent on slowly-but-surely making the app more unusable. Let's take a very brief tally on features of the app that were present at some point - but are no longer;

- The ability to filter your library by downloaded songs.
- Sane repeat buttons (now it requires 3 taps in very unintuitive places onscreen)
- A sane bottom row of icons, such as "Playlists", "Artists", "Albums", etc. At the time of this writing, there is "For You", "Browse", and "Radio". Almost no one I know uses any of these on a regular basis, yet they are permanent and prominent icons on the screen.
- A reasonable way to see the album/artist from the currently playing song. Now, this requires two taps (once on the relatively small artist screen, and once on the pop up dialog for artist/album). 
- ...and many other first-world problems

Update Feb 2020: Left AM for Spotify, and never looking back.

<img src="/apple_music.png" height="500"></img>



