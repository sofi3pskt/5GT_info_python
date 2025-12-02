import tm1637
from color_conversion import*
from pyb import Timer, Pin

display = tm1637.TM1637(clk=pyb.Pin('X7'), dio=pyb.Pin('X6'))
pot= pyb.ADC('X19')
rouge = pyb.Pin( 'X1', pyb.Pin.OUT_PP)
vert = pyb.Pin( 'X2', pyb.Pin.OUT_PP)
bleu = pyb.Pin( 'X3', pyb.Pin.OUT_PP)
timer = pyb.Timer(5, freq=500)
channelrouge = timer.channel(3, Timer.PWM, pin=Pin('X1'), pulse_width_percent=100)
channelvert = timer.channel(4, Timer.PWM, pin=Pin('X2'), pulse_width_percent=100)
channelbleu = timer.channel(1, Timer.PWM, pin=Pin('X3'), pulse_width_percent=100)
  
  
  


while True:
    val_pot=pot.read()
    hue= int(val_pot/4095)
    display.number(hue*100)
    rouge, vert, bleu = hsv_to_rgb(hue, 1, 1) 
    channelrouge.pulse_width_percent(int(rouge*100))
    channelvert.pulse_width_percent(int(bleu*100))
    channelbleu.pulse_width_percent(int(vert*100))
    print(rouge, bleu, vert)
    pyb.delay(50)
