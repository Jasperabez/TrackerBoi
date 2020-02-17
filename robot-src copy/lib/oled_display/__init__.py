from machine import Pin, I2C
import ssd1306

class Oled_display:
    state = "STOP"
    batt_lvl=99
    dist_covered=100
    speed = 50
    # ESP32 Pin assignment 
    i2c = I2C(-1, scl=Pin(22), sda=Pin(21))
    oled_width = 128
    oled_height = 32
    oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

    def __init__(self,state,speed,batt_lvl,dist_covered):
        self.state = state
        self.speed = speed
        self.batt_lvl= batt_lvl
        self.dist_covered= dist_covered
        self.oled.text('Welcome!', 0, 0)
        self.oled.text('Press ON,', 0, 10)
        self.oled.text('To start!', 0, 20)
        self.oled.show()
    def display(self,state=None,speed=None,batt_lvl=None,dist_covered=None):
        if state:
            self.state = state
        if speed:
            self.speed = speed
        if batt_lvl:
            self.batt_lvl = batt_lvl
        if dist_covered:
            self.dist_covered = dist_covered
        self.oled.fill(0)
        self.oled.text("{} {}".format(self.state,self.speed), 0, 0)
        self.oled.text('Batt Lvl:%d' % (self.batt_lvl), 0, 10)
        self.oled.text('Distance:%d m' % (self.dist_covered), 0, 20)
        self.oled.show()