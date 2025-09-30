from pyb import Timer, Pin

pot= pyb.ADC('X19')
my_pin = pyb.Pin( 'X1', pyb.Pin.OUT_PP)
timmer = pyb.Timer(5, freq=500) #horloge obligatoire pour programme PWM
channel = timmer.channel(3, Timer.PWM, pin=Pin('X1'), pulse_width_percent=100)
  
  


def dimm():
   val_pot=pot.read()
   print(val_pot)
   intensity=(val_pot/4095)*100
   channel.pulse_width_percent(intensity)
   pyb.delay(100)
  
  
while True:
    dimm()
