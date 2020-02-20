As physics is something that exist and influence us all, it is required for us to do some mechanical calculations for our Tracker Bot too! These are some calculations we have to do.

*Maximum velocity*
```
Vmax(m/s) = radius x revolutions per minute x 0.10472
= 0.03 x 320 x 0.10472
= 1.00m/s
```

*Maximum acceleration*
```
= Vmax / s
= 1.005312 / 5
= 0.20 m/s^2
```

*Grand Total Weight*
```
1381g = 
1.381kg * 9.81 = 
13.55 N
```

*Rolling Resistance*
```
= Gross Weight of Vehicle(Gw)[N] x Surface Friction Coeff(SFc)
= 8.64261N * 0.015 (Fair Concrete Contact Surface)
= 0.20 N
```

*Grade Resistance*
```
= Gross Weight of Vehicle(WGV) [N] x sin(θ)(degrees)
= 8.64261N * sin(26.565 °)
= 6.05 N
```

*Acceleration Force*
```
Fa [N] = WGV [N] * Vmax [m/s] / (32.2 [ft/s^2 ] * ta [s]) 
= ( 8.64261N * 1.005312m/s ) / 
( 9.81m/s^2 * 5s )
= 0.28 N
```

*Total Tractive Effort*
```
TTE [N] = 
RR [N] + GR [N] + FA [N]
                  = 
0.12963915N + 6.650930825 N + 0.3048105984N
= 6.54 N
```

*Torque Wheel*
```
Tw [Nm] = TTE [N] * Rw [m] * RF [-] 
= 
6.539545882 * 
0.03m * 
1.1
= 0.22Nm
```

*Assuming 100% efficiency*, the torque required,0.216Nm, successfully meets the motor specs (just nicely, which the maximum torque can provide is, 
```
2500gcm*10^-3*10^-2*9.81 
= 
0.25 Nm
```

Here comes the important cutting grass! Because that's basically what our bot is all about.

Since average rpm of a grass cutter motor is about *2700 rpm*

Our motor has a speed that can reach *4360 rpm* at max efficiency.
Hence, assuming it is at 100% efficiency, it is able to cut weeds with *very little to no resistance.*

With these calculations you could churn out your own weed destructo!!




