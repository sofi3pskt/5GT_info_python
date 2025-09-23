from pyb import Timer, Pin

timmer = pyb.Timer(5, freq=500)
channel = timmer.channel(3, Timer.PWM, pin=Pin('X1'), pulse_width_percent=0)

def dimm_up(duration):
    """Pour dimmer la led vers le haut, prend une durée (int)"""
    print("Dimming up...")
    for i in range(100):
        channel.pulse_width_percent(i)
        pyb.delay(int((duration/100)*1000))#durée totale divisée en 100 étapes *1000 pour convert en millisec
    
def dimm_down(duration):
    """Pour dimmer la led vers le bas, prend une durée (int)"""
    print("Dimming down...")
    for i in range(100):
        channel.pulse_width_percent(100-i)
        pyb.delay(int((duration/100)*1000))
        
while True:
    dimm_up(15)
    dimm_down(20)
