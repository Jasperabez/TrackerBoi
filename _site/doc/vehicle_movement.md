# Vehicle movement documentation

Import libraries for micropython

```python
from machine import Pin
```

Setup pin for input or output

```python
pin3 = Pin(3, Pin.OUT) #set pin 3 as output
pin5 = Pin(5, Pin.IN) #set pin 5 as input
```

Digital control for pins

```python
pin3.on()
pin3.off()
```

get input values for pins

```python
digitalInForPin5 = pin5.value()
```
