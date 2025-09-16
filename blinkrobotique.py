my_pin = pyb.Pin( 'X1', pyb.Pin.OUT_PP)
lo_pin = pyb.Pin( 'X2', pyb.Pin.OUT_PP)

def blink_vert():
   lo_pin.high()
   my_pin.low()
   pyb.delay(1000)
   my_pin.high()
   lo_pin.low()
   pyb.delay(1000)
   

   
while True :
  blink()
