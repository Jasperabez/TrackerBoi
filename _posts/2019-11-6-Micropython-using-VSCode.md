---
layout: post
title: Micropython using VSCode
---

VSCode is a powerful text editor which capabilities can be enhance through various extensions. With the Micropython IDE extension installed it is a viable alternative to Thonny and MuEditor. In this guide I am using the Esp32 and running <b>Linux (Manjaro)</b> as my OS, differences in steps might be expected if your configuration is different.

## 1. Install Visual Studio Code
## 2. Install Micropython IDE extension
search for it at the extension page
![Micropython IDE page]({{site.baseurl}}/images/Micropython_IDE_page.png)
## 3. Install the neccessary requirements
listed at the extension installation page.
python, pip, Ampy, rshell
## 4. Download and flash firmware for first setup
Select "Micropython: Getting Started" from the command palette the options are there.
Port number on windows will be "COMX" and on Linux "dev/ttyUSBX" X is any integer
## 5. Edit your Script
## 6. Run Script
Select "Micropython: Run.." from the command palette and run it. <b>Press the reset button on the board</b> after a successful build to ensure the program is loaded.


That's all and enjoy using VSCode!!