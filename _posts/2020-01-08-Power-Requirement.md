---
layout: post
title: Power Requirements 
---

Track Vehicle - 
by Team TrackerBoi 

Component Diagram:


Input Power: 6000mAh x 7.4V = 44.4Wh (Based on 2 x 18650 LiON 3.7V 3000 mAh)


Provided Components:

MB102 Breadboard Power Supply Module


Specification
Locking ON / OFF Switch
LED Power Indicator
Input Voltage: 6.5 V to 12 V (DC)
Output Voltage: 3.3 V / 5 V
Maximum Output Current: 700 mA
Power Rails 0 V, 3.3 V, 5 V on Breadboard
Two Groups of Header Pins
Size: 5.3 cm × 3.5 cm
Power: 700mA x 3.3V = 2.31W
	 700mA x 5v = 3.5W

Link: http://www.handsontec.com/dataspecs/mb102-ps.pdf

ESP32: Requires 3.3V


Specification
On-chip sensor: Hall sensor
Integrated crystal: 40 MHz crystal
Integrated SPI flash: 1 4 MB
Operating voltage/Power supply: 3.0 V ~ 3.6 V
Operating current Average: 80 mA
Minimum current delivered by power supply:500 mA
Power: 500mA x 3.3V = 1.65W

Link: https://www.espressif.com/sites/default/files/documentation/esp32-wroom-32d_esp32-wroom-32u_datasheet_en.pdf

DC Gear Motor X2: 12V, 100mA (no load) 



Specification
Voltage: 12V DC    
RPM: 320RPM    
Current: 0.1A    
Diameter: 33mm    
Height (excl. shaft): 39mm    
Shaft length: 9mm    
Shaft diameter: 5mm    
Weight: 100g     
Torque:2.5kg.cm  (ESTIMATED)  
Power: 0.1A x 12V = 1.2W X 2 Motors = 2.4W

Link: https://www.aliexpress.com/item/32352827888.html







L298N Motor Driver

Specification
Input Voltage: 3.2V~40Vdc.
Brief Data:
Driver: L298N Dual H Bridge DC Motor Driver
Power Supply: DC 5 V - 35 V
Peak current: 2 Amp
Operating current range: 0 ~ 36mA
Control signal input voltage range :
Low: -0.3V ≤ Vin ≤ 1.5V.
High: 2.3V ≤ Vin ≤ Vss.
Enable signal input voltage range :
Low: -0.3 ≤ Vin ≤ 1.5V (control signal is invalid).
High: 2.3V ≤ Vin ≤ Vss (control signal active).
Power: 36mA x 5V = 0.18W

Link: http://www.handsontec.com/dataspecs/L298N%20Motor%20Driver.pdf

Total theoretical power required: 2.31 + 3.5 + 0.075 + 1.65 + 13.2 + 0.18 = 20.915W

Run time: 44.4Wh / 20.915W = 2.12h




Additional Components:

3S Series Lithium Battery Capacity Indicator Display Electric Vehicle Battery Power Tester Li-po Li-ion Module


Specification
Operating current: 2.3mA

https://www.aliexpress.com/item/4000300676403.html?spm

DC-DC Step Up Power Module Boost Volt Converter 3.3V-35V To 12V

	
	Specification
Rectification method:Non-synchonous rectfication
Input voltage:3V-35V
Output voltage:5V-40V(notes can not step down voltage)
Input current:3A(maximum 5A)

https://www.aliexpress.com/item/32983378035.html?spm=a2g0o.productlist.0.0.17202192WjIYju&algo_pvid=b58fdefe-53d1-4497-81f3-b8be43926616&algo_expid=b58fdefe-53d1-4497-81f3-b8be43926616-5&btsid=dcb47fa5-37a9-4131-9ff9-f135a000983e&ws_ab_test=searchweb0_0,searchweb201602_1,searchweb201603_53

HC-SR04 Ultrasonic sensor 
	
	Specification
Working Voltage: DC 5V
Working Current: 15mA
Working Frequency: 40Hz
Max Range: 4m
Min Range: 2cm
MeasuringAngle: 15 degree
Trigger Input Signal: 10uS TTL pulse
Echo Output Signal: Input TTL lever signal and the range in
proportion
Dimension 45*20*15mm 
Power: 15mA x 5V = 0.075W

Specification Link:
https://cdn.sparkfun.com/datasheets/Sensors/Proximity/HCSR04.pdf

Link: https://www.aliexpress.com/item/32786781050.html?spm=a2g0o.productlist.0.0.4ea31de2vVTS84&algo_pvid=f674f341-3269-4253-9bbe-dc4f7dfafc70&algo_expid=f674f341-3269-4253-9bbe-dc4f7dfafc70-0&btsid=d7e1a990-aed8-4088-85d6-95fdd8c8a9f0&ws_ab_test=searchweb0_0,searchweb201602_1,searchweb201603_53

Tilt Sensor Module 

Specification
Input voltage:3.3V - 5V

https://www.aliexpress.com/item/4000051420436.html?spm=a2g0o.productlist.0.0.c0637034VqoJe0&algo_pvid=38940cd2-bcd4-4b67-8da6-dafbdc8855c2&algo_expid=38940cd2-bcd4-4b67-8da6-dafbdc8855c2-45&btsid=1f396284-2a6e-4016-8d01-01e5fdcd7736&ws_ab_test=searchweb0_0,searchweb201602_1,searchweb201603_53


DC Motor, 12V, Model RK-370CA-15370 (For Cutter)


Specification
https://product.mabuchi-motor.com/detail.html?id=88 (Specification Sheet)
Voltage: 12V DC    
RPM: 5500RPM    
Current: 0.032A    
Motor Diameter: 24.2mm    
Motor Height (excl. shaft): 30.8mm    
Shaft Length: 10.5mm   
Shaft Diameter: 2mm    
Weight: 50g
Torque: 27.7gcm
Power: 0.032A x 12V = 0.384W X 1 Motor = 0.384W

https://www.aliexpress.com/item/33010469151.html

