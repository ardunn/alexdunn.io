+++
title = "Tech macguyvering a raspberry pi home cloud"
description = ""
date = "2018-06-01"
+++


# Tech Macguyvering a Raspberry Pi Home Cloud

For $35, the Raspberry Pi is an incredible single board computer. You can connect to the internet, run Linux, automate your home,  or make a robot - the list goes on and on. And regardless of your choice of project, the Raspberry Pi community will almost always be there for you if (read: when) you need help.

![rpi](/rpi.png)

## But what good is a RPi if you don't have a good project?

This is the question I was faced with, after giddily buying one in 2017. I played around with it ... but honestly? I never really had a need for it, nor could I think of any projects that (1) were cool or interesting, (2) I'd actually use on a frequent basis, and (3) didn't require buying $100+ in gadgets I wouldn't otherwise use. So, my RPi 3b was delegated to a lonely drawer, where it sat for over a year.


## An Actual Use

This year, my personal archive, holding all my family's beloved family pictures since 1997, my financial documents, my photography, nearly 100,000 songs, and 200+ legally *cough* acquired movies, spilled over the 1TB mark. My poor old laptop's HDD could no longer hold it all. Plus, my HDD was the only current and full copy of my data I had. If it got lost, corrupted, or destroyed somehow, my entire digital life was as good as gone! Backing up to external HDDs via wires was annoying, cloud services for backup cost money (+ I don't trust them), and premanufactured network attached storage (NAS) systems can cost hundreds of dollars. I needed a better solution, using tech I already had. Hence, my Raspberry Pi "Home Cloud" was born.


## Making the Home Cloud 

### Disclaimer: This NAS setup is very hacky but works

When setting up this cloud, my only requirements were:

* it be fast enough that I could stream HD movies off of it to the local network without buffering
* it make at least one redundant backup
* it be resistant to my own stupidity (*e.g.*, an accidental `rm -rf * && shred *` won't nuke all my data)

The guide is written such that these requirements are satisfied while not requiring an exorbitant amount of debugging or headaches (i.e., no reformatting to set up RAID with delayed parity). Hey, this is tech maguyver after all, not "how to do things the most perfect, right, and clean way humanly possible".


### What does it do, in layman's terms?

Access all documents/photos/movies on my data archive from my laptop or phone wirelessly, whether on the local network or outside the local network. Keep two separate disks, in case of a random failure. Automatically back up the main disk to the backup disk every 24 hours. I no longer have to keep my archive on my laptop, but can still access it whenever I want.

### What does it do, specifically?

Samba and SFTP servers on the local network; SFTP server outside the local network accessible made possible via port forwarding. Uses rsync to sync disks on a regular basis with crontab.

### What you need:

**A main computer (or a phone)**

![computer](/laptop.jpg)

This is what you will use to SSH into your RPi, and transfer/view media. Or just use your phone with an SSH and Samba/FTP client.

**A raspberry pi with an OS installed** - This will control your network attached storage. I used a Raspberry Pi 3b+.

**One (or some) external HDDs and USB SATA connectors**

<img src="/4tb.jpg" width="100" align="left"/> <img src="/8tb.jpg" width="100" align="left"/> <br/>


These will be your storage disks. I used some garbage 2TB Seagate Backup Slim I had lying around, and a 8TB Seagate Backup Plus I got as a christmas present.

**Access to a wifi network and router, + an ethernet cable**




