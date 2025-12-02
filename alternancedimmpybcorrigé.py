from pyb import Timer, Pin

pot= pyb.ADC('X19')
led_vert = pyb.Pin( 'X1', pyb.Pin.OUT_PP)
led_jaune = pyb.Pin( 'X2', pyb.Pin.OUT_PP)
timer = pyb.Timer(5, freq=500) 
channel_vert = timer.channel(3, Timer.PWM, pin=Pin('X1'), pulse_width_percent=100)
channel_jaune = timer.channel(4, Timer.PWM, pin=Pin('X2'), pulse_width_percent=100)
val_pot=pot.read()
val_pot=int(val_pot)



def dimm_vert_up():
    val_pot=pot.read()
    print(val_pot)
    intensity_vert=(val_pot/4095)*100
    channel_vert.pulse_width_percent(100-intensity_vert)
    intensity_jaune=(val_pot/4095)*100
    channel_jaune.pulse_width_percent(intensity_jaune)
    pyb.delay(100)
    
    
while True:
    dimm_vert_up()
