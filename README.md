# Engineering Realisation - TrackerBot

**Demo Video:**

[![alt text](http://img.youtube.com/vi/un4iWNQuDIo/0.jpg)](http://www.youtube.com/watch?v=un4iWNQuDIo "title")

**Final Realisation**

TrackerBot : The ultimate rechargeable weeding robot for all applications

Gardening | Farming | Maintenance

With TrackerBot, gardeners can now perform weeding without the monotony and frustration of weeding while environmentalists can breathe easily with a chemical-free solution to weeding.

1) IMPROVE WORKING CONDITIONS - TrackerBot allows remote weeding to reduce workload and danger

2) LOWER COSTS - TrackerBot is reduced pesticide and maintenance costs as it weeds mechanically

3) FEWER MAINTENANCE WORRIES - The robot is entirely electric, so you no longer need to spend time on the maintaining tools

Our Team: Jabez Tho, Hans Delano, Ahmad Rifaaie, Lee Wei Juin

Mentors: Mr. Rodney Dorville and Mr. Tune Chien Jung

# Timeline

**Week 1**

* Module Intro
* Github Set-up
* Introduction to Markdown

**Week 2**

Micropython
Micro-controllers: esp32, microbit.

Types of Micropython IDE: https://thonny.org/, https://codewith.mu/

What?:

* Intepreted programming language created by Guido van Rossum
* First released in 1991
* Available in all platforms

Why?:

* code readability with its notable use of significant whitespace
* object-oriented approach
* aims to help programmers write code clear, logical code for small and large scale Project

Homework Assignment: https://github.com/weijuinlee/EA_Projects

**Week 3**

Continuous Track Vehicles:

 * Drive Wheel Motor Torque Calculations
 * Environmental assumptions

**T100**

![](images/dimensions.jpg)

Main Parameters:

 * Material: Aluminum Alloy

 * Surface treatment: sandblasting oxidation

 * Color: Black

 * Track: Engineering plastic

 * Size: About 185*200*60mm(Length*width*Height)

 * Weight: 0.65kg

 * Design load: 5kg

Motor parameters(25mm 9V 150rpm DC Motor, has hall sensor):

 * Output speed: 150±10%rpm

 * No_load Current: 200mA (Max)

 * Stall current: 4500mA(max)

 * Stall torque: 9.5kgNaN

 * Rated speed: 100±10%rpm

 * Rated torque: 3000gNaN

 * Rated Current: 1200mA (Max)

 * Noise: 56dB

 * Working voltage: 9V

 * Outside Shaft Length: 14.5mm

 * Shaft End Play: 0.05-0.50mm

 * Screw Size: M3.0

 * Dia. Of Shaft phi4mm, D3.5

 * encoder: 2 pulses/circle


Equipment List:

  1. 1 x Chassis bracket

  2. 1 x Track (pair)

  3. 2 x Driving wheels

  4. 4 x Wheel drive

  5. 1 x Motor (pair) (with encoder)

**Assembly of T100:**

  1. <br/>

  ![](images/wheels.jpg)

  2. <br/>

  ![](images/bolts.jpg)

  3. <br/>

  ![](images/frames.jpg)

  4. <br/>

  ![](images/assem1.jpg)

  5. <br/>

  ![](images/rif.jpg)

  6. <br/>

  ![](images/t100.jpg)

**Week 4**

Flashing of micropython on ESP32 and controlled LED: https://learn.adafruit.com/micropython-basics-blink-a-led/blink-led

![](images/esp32blink.png)

<img src="images/blink.gif" width="100%">

**Week 5**

ESP 32 documentation brief.

**Week 6**

Tutorial on mechanical drawing on Fusion 360.

**Week 7**

Class on Power Management.

**P = IV(W)**

**How do we measure?**

* Voltmeter in Parallel

* Current in series

* Power Meter

**Non- Evasive methods**

* Clamp Meters

* Shunts

**Rectification**

**AC-to-DC Conversion**

* 230V AC to 3.3 ~ 24 DC

  **Linear Rectification**

  * Simple, cheap

  * Losses

  * Weight

    

**Switch Mode Power Supplies**

Main Input -> Input rectifier -> Inverter "Chopper" -> Output Transformer -> Output rectifier and filter -> DC Output / Chopper Controller -> Inverter "Chopper"

#EEVblog90

**Linear Power Supply**

* Simplicity
* Quiet Operation and load-handling capacity
* Low cost
* Range of application
* Number of Outputs
* Average Efficiency

**Switch Mode Power Supply**

* High Efficiency
* Low  cost and size
* Complicated design
* Cost compared with Linear Rectification

**Typical DC Power Supply**

* Large mains transformer provides isolation
* Rectifier converts AC to DC using diodes
* Filter circuits (using capacitors) remove variations/ ripple in the signal producing a smooth DC
* Regulators maintain a constant voltage level

**Series Transistor Regulator Circuit**

* Uses transistor and DC biasing to set output voltage
* Emitter Follower circuit has unity voltage gain, hence with suitable biasing a stable output voltage can be obtained
* Input voltage must be sufficiently high enough to get the desired output voltage (approx. 0.7V is dropped across base and emitter terminals)
* Problems
  * Heat from power dissipation(I*V)
  * Only applicable in low power output applications
  * Weight of isolation transformer

Examples: Travel adapters

**Switch Mode Power Supplies**

* SMPS becoming the more common ac-to-dc supply
* Use a semiconductor switching technique
* Consists of a power switching stage and a control circuit with output filtration
* Advantages:
  * Higher efficiency with low power dissipation
  * Can offer step-up or step-down and negation of input voltage

**Buck Switch Mode Power Supply**

* Efficiently reduce DC voltage from a higher voltage to a lower one
* Does not change the polarity
* A DC-to-DC converter and a switching regulator
* Boost converter needed to boost voltage higher

**Application of SMPS**

* Buck Converters
  * Efficient method to convert High DC to Low DC voltages
  * Cost effective

* Boost Converters
  * Converts Low DC to High DC voltages
  * Most commonly used in Li-ion battery banks (3.74V to 5V)




