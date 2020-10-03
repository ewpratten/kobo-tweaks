# Kobo Tweaks
A collection of tools and software modifications for the [Kobo e-reader](https://ca.kobobooks.com/collections/ereaders?utm_source=Kobo&utm_medium=eReadersApps&utm_campaign=eReadersApps)

## Some background

A little-known fact about the entire fleet of Kobo e-readers is that they are simple busybox-based Linux devices. By flashing custom firmware to the devices via their USB update functionality, root access can be exposed.

This repo contains both the tools required to generate these firmware updates, and some tools and scripts I use on my Kobo Aura (they should work on any kobo though).


## What is provided

This project currently provides:
 - A Telnet server that runs on boot
 - An FTP server that runs on boot

I am working to add:
 - A Python3 interpreter
 - A `kobo_ctl` tool for interacting with the kobo system

## Acknowledgements

This project piggybacks off the works of:
  - [Lee Yingtong Li](https://yingtongli.me/blog/2018/07/30/kobo-telnet.html)
  - [Patrick Gaskin](https://github.com/pgaskin/NickelMenu)