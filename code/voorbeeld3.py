from sense_hat import SenseHat

import time
import random
sense = SenseHat()
sense.set_rotation(270)

#sense.show_message("hello", text_colour=(0, 250, 0), back_colour=(255, 165, 0)) 

for i in range(100):
  xpos = random.randint(0,7)
  ypos = random.randint(0,7)
 
  color =  random. randint(1, 3)
  if color == 1:
    sense.set_pixel(xpos, ypos, (0, random.randint(100, 255), random.randint(100,255)))
  elif color == 2:
    sense.set_pixel(xpos, ypos, (random. randint(100, 255), 0, random.randint(100,255)))
  else:
    sense.set_pixel(xpos, ypos, (random.randint(100, 255), random.randint(100,255), 0))
  time.sleep(0.02)
  
temp = sense.get_temperature()
pressure = sense.get_pressure()
humidity = sense.get_humidity()

w = (255, 255, 255)
b = (0, 0, 0)

picture = [
    b, b, w, w, w, w, b, b,
    b, w, b, b, b, b, w, b,
    b, w, b, w, w, b, w, b,
    b, w, b, b, b, b, w, b,
    b, b, w, w, w, w, b, b,
    b, b, w, w, w, w, b, b,
    b, w, w, w, w, w, w, b,
    b, w, w, w, w, w, w, b
]

sense.set_rotation(0)
sense.set_pixels(picture)
time.sleep(2)

sense.show_message("Temp: ", text_colour=(255, 0, 0), back_colour=(0,0,0), scroll_speed=0.1)
sense.show_message(str(round(temp,1)),
                   text_colour=(255, 0, 0), 
                   back_colour=(0,0,0), 
                   scroll_speed=0.1)

sense.show_message(str(round(pressure,0))[:-2], 
                   text_colour=(255, 0, 0), 
                   back_colour=(0,0,0), 
                   scroll_speed=0.1)
                   
sense.show_message(str(round(humidity,0))[:-2], 
                  text_colour=(255, 0, 0), 
                  back_colour=(0,0,0), 
                  scroll_speed=0.1)

