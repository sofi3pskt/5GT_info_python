from pyb import Timer, Pin

timmer = pyb.Timer(5, freq=500)
channel = timmer.channel(3, Timer.PWM, pin=Pin('X1'), pulse_width_percent=0)

def dimm_up(a):
    print("Dimming up...")
    for i in range(100):
        channel.pulse_width_percent(i)
        pyb.delay(a)
    
def dimm_down(a):
    print("Dimming down...")
    for i in range(100):
        channel.pulse_width_percent(100-i)
        pyb.delay(a)
        
while True:
    dimm_up(50)
    dimm_down(50)
