---
layout: post
title: Esp32 Micropython With DHT11 Temperature Sensor
---

GO TO <a href="https://github.com/weijuinlee/esp32micropythondht11">https://github.com/weijuinlee/esp32micropythondht11</a>

Here’s a list of parts you need to build the circuit:
 1. DHT11 or DHT22 temperature and humidity sensor
 2. 10k Ohm resistor
 3. Breadboard
 4. Jumper wires

**Code:**

```python
from machine import Pin
from time import sleep
import dht 
sensor = dht.DHT22(Pin(14))
#sensor = dht.DHT11(Pin(14))
while True:
  try:
    sleep(2)
    sensor.measure()
    temp = sensor.temperature()-590
    hum = sensor.humidity() - 1600
    print('Temperature: %f C' %temp)
    print('Humidity: %3.1f %%' %hum)
  except OSError as e:
    print('Failed to read sensor.')

```