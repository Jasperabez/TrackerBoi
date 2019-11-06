---
layout: post
title: Esp32 and MicroPython
---

"Flashing MicroPython to the Esp32 for Windows"

```bash
pip install esptool
```

Connect your Esp32 to your computer and find its port number.
For Windows, use device manager (either ask Cortana for it or for hotkeys user: Win_btn + X)

under "Ports (COM & LPT)"

![Device Manager > Ports (COM & LPT)](../images/comPortFinding.jpg)

as you can see, mine is on COM8

run the following in terminal, replacing "COM8" with whatever port yours is connected to

```bash
esptool.py --chip esp32 --port COM8 erase_flash
```

Now, get the new firmware flash here: [MicroPython for Esp32](https://micropython.org/download#esp32)
I've downloaded the very first "Generic" one but you can choose whichever that fits your requirement.

> Note: Some of the firwares only have WiFi support or only Bluetooth support, so take note

After downloading the file, navigate your terminal to the location of the downloaded file and run the following

```bash
esptool.py --chip esp32 --port COM8 --baud 460800 write_flash -z 0x1000 esp32-idf3-20191105-v1.11-558-gd209f9ebe.bin
```

Similarly, change "COM8" to your own port number and "esp32-idf3-20191105-v1.11-558-gd209f9ebe.bin" to the firmware you download.

Now for testing!

on windows terminal install rshell

```bash
pip install rshell
```

then run repl in rshell

```bash
rshell
connect serial COM8
repl
```

again, change COM8 to your port number.
If everything works, the MicroPython interpreter will show up! Congratz!
