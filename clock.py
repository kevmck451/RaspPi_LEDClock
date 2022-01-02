import LEDarcade as LED
from rgbmatrix import graphics
from rgbmatrix import RGBMatrix, RGBMatrixOptions
import time
import random

#Variable declaration section
ScrollSleep   = 0.025
HatHeight = 32
HatWidth  = 64

print ("---------------------------------------------------------------")
print ("SHITBOX RULES!!!! ")
print ("")


#LED.DisplayDigitalClock(ClockStyle=2,CenterHoriz=True,v=1, hh=24, ZoomFactor = 1, AnimationDelay=0, RunMinutes = 5 )

#--------------------------------------
#  SHOW TITLE SCREEN                 --
#--------------------------------------

LED.ShowTitleScreen(
    BigText             = "KEV'S",
    BigTextRGB          = LED.HighBlue,
    BigTextShadowRGB    = LED.ShadowBlue,
    LittleText          = 'BADASS CLOCK',
    LittleTextRGB       = LED.HighGreen,
    LittleTextShadowRGB = LED.ShadowGreen,
    ScrollText          = 'FUCK YEAH!!!!!!',
    ScrollTextRGB       = LED.MedYellow,
    ScrollSleep         = ScrollSleep, # time in seconds to control the scrolling (0.005 is fast, 0.1 is kinda slow)
    DisplayTime         = 1,           # time in seconds to wait before exiting 
    ExitEffect          = 0            # 0=Random / 1=shrink / 2=zoom out / 3=bounce / 4=fade /5=fallingsand
    )

#--------------------------------------
#  SHOW CLOCKS                       --
#--------------------------------------

while 1==1:

    LED.DisplayDigitalClock(
      ClockStyle = 1,
      CenterHoriz = True,
      CenterVert=True,
      v   = 1,
      hh  = 12,
      RGB = LED.HighBlue,
      ShadowRGB     = LED.ShadowBlue,
      ZoomFactor    = 4,
      AnimationDelay= 5,
      RunMinutes = 3
    )

    LED.DisplayDigitalClock(
        ClockStyle=2,
        CenterHoriz=True,
        CenterVert=True,
        v=1,
        hh=12,
        ZoomFactor = 5,
        AnimationDelay=10,
        RunMinutes = 3
    )






