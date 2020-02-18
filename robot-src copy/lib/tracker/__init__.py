from machine import Pin
from machine import PWM
import time

class Tracker:
    millis = 0
    dist = 0
    dist_state = 'no_dist'
    en1 = Pin(0, Pin.OUT)
    a1 = Pin(0, Pin.OUT)
    b1 = Pin(0, Pin.OUT)
    
    en2 = Pin(0, Pin.OUT)
    a2 = Pin(0, Pin.OUT)
    b2 = Pin(0, Pin.OUT)
    m = Pin(0,Pin.OUT)
    
    def __init__(self, en1, a1, b1, en2, a2, b2, m):
        self.en1 = Pin(en1, Pin.OUT)
        self.en1 = PWM(self.en1)
        self.a1 = Pin(a1, Pin.OUT)
        self.b1 = Pin(b1, Pin.OUT)
        
        self.en2 = Pin(en2, Pin.OUT)
        self.en2 = PWM(self.en2)
        self.a2 = Pin(a2, Pin.OUT)
        self.b2 = Pin(b2, Pin.OUT)
        self.m = Pin(m,Pin.OUT)
     
    def setup(self):
        self.en1.duty(500)
        self.en2.duty(500)
        
        self.en1.freq(10)
        self.en2.freq(10)
     
    def forward(self):
        self.a1.on()
        self.b1.off()
        
        self.a2.on()
        self.b2.off()
        self.dist_state = "dist"
        self.millis = int(round(time.time() * 1000))
        
    def backward(self):
        print("backward")
        self.a1.off()
        self.b1.on()
        
        self.a2.off()
        self.b2.on()
        self.dist_state = "dist"
        self.millis = int(round(time.time() * 1000))
        
    def left(self):
        self.a1.off()
        self.b1.on()
        
        self.a2.on()
        self.b2.off()
        self.dist_state = "no_dist"
        self.millis = int(round(time.time() * 1000))
        
    def right(self):
        self.a1.on()
        self.b1.off()
        
        self.a2.off()
        self.b2.on()
        self.dist_state = "no_dist"
        
    def stop(self):
        self.a1.off()
        self.b1.off()
        
        self.a2.off()
        self.b2.off()
        self.dist_state = "no_dist"
    
    def setSpeed(self, duty):
        #self.en1.freq(freq)
        speed = duty * 10
        print(speed)
        
        self.en1.duty(speed)
        
        #self.en2.freq(freq)
        self.en2.duty(speed)
    
    def blade_toggle(self, curr_mstate):
        if(curr_mstate=="Off"):
            self.m.on()
            curr_mstate="On"
        elif(curr_mstate=="On"):
            self.m.off()
            curr_mstate="Off"
        else:
            print(curr_mstate)
        return curr_mstate
    
    def get_dist(self):
        if
    
    def millis_handler(self):
        if self.dist_state == "dist":
            self.millis = int(round(time.time() * 1000))
            
