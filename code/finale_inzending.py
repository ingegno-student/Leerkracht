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
r = (255, 0, 0)   # rood
l = (30, 30, 255) # lichtblauw
i = (48, 184, 186) # indigo
n = (56, 24, 15)  # bruin

temp_picture1 = [
    b, w, w, w, b, b, b, b,
    b, w, b, w, b, b, b, b,
    b, w, b, w, b, b, b, b,
    b, w, b, w, b, w, w, w,
    b, w, l, w, b, b, w, b,
    b, w, l, w, b, b, w, b,
    b, w, w, w, b, b, w, b,
    b, b, w, b, b, b, b, b
]

temp_picture2 = [
    b, w, w, w, b, b, b, b,
    b, w, b, w, b, b, b, b,
    b, w, b, w, b, b, b, b,
    b, w, i, w, b, w, w, w,
    b, w, l, w, b, b, w, b,
    b, w, l, w, b, b, w, b,
    b, w, w, w, b, b, w, b,
    b, b, w, b, b, b, b, b
]
temp_picture3 = [
    b, w, w, w, b, b, b, b,
    b, w, r, w, b, b, b, b,
    b, w, r, w, b, b, b, b,
    b, w, i, w, b, w, w, w,
    b, w, l, w, b, b, w, b,
    b, w, l, w, b, b, w, b,
    b, w, w, w, b, b, w, b,
    b, b, w, b, b, b, b, b
]

#sense.set_rotation(0)
sense.set_pixels(temp_picture1)
time.sleep(1)
sense.set_pixels(temp_picture2)
time.sleep(1)
sense.set_pixels(temp_picture3)
time.sleep(1)

#sense.show_message("Temp: ", text_colour=(255, 0, 0), back_colour=(0,0,0), scroll_speed=0.1)
sense.show_message(str(round(temp,1)) + " C",
                   text_colour=(255, 0, 0), 
                   back_colour=(0,0,0), 
                   scroll_speed=0.1)


l = (30, 30, 30)

picture_1 = [								
b,	b,	b,	r,	r,	b,	b,	b,	
b,	r,	r,	l,	l,	r,	r,	b,	
b,	r,	l,	l,	l,	l,	r,	b,	
r,	l,	l,	l,	l,	l,	l,	r,	
r,	w,	w,	w,	w,	l,	l,	r,	
b,	r,	n,	n,	n,	n,	r,	b,	
b,	r,	r,	n,	n,	r,	r,	b,	
b,	b,	b,	r,	r,	b,	b,	b,
]

picture_2 = [
b,	b,	b,	r,	r,	b,	b,	b,
b,	r,	r,	l,	l,	r,	r,	b,
b,	r,	w,	l,	l,	l,	r,	b,
r,	l,	l,	w,	l,	l,	l,	r,
r,	l,	l,	l,	w,	l,	l,	r,
b,	r,	n,	n,	n,	n,	r,	b,
b,	r,	r,	n,	n,	r,	r,	b,
b,	b,	b,	r,	r,	b,	b,	b,
]

picture_3 = [
b,	b,	b,	r,	r,	b,	b,	b,
b,	r,	r,	l,	l,	r,	r,	b,
b,	r,	l,	l,	l,	w,	r,	b,
r,	l,	l,	l,	w,	l,	l,	r,
r,	l,	l,	w,	l,	l,	l,	r,
b,	r,	n,	n,	n,	n,	r,	b,
b,	r,	r,	n,	n,	r,	r,	b,
b,	b,	b,	r,	r,	b,	b,	b,
]

picture_4 = [								
b,	b,	b,	r,	r,	b,	b,	b,	
b,	r,	r,	l,	l,	r,	r,	b,	
b,	r,	l,	l,	l,	l,	r,	b,	
r,	l,	l,	l,	l,	l,	l,	r,	
r,	l,	l,	w,	w,	w,	w,	r,	
b,	r,	n,	n,	n,	n,	r,	b,	
b,	r,	r,	n,	n,	r,	r,	b,	
b,	b,	b,	r,	r,	b,	b,	b,
]
snelheid = 0.5
sense.set_pixels(picture_1)
time.sleep(snelheid)
sense.set_pixels(picture_2)
time.sleep(snelheid)
sense.set_pixels(picture_3)
time.sleep(snelheid)
sense.set_pixels(picture_4)
time.sleep(snelheid)
sense.set_pixels(picture_3)
time.sleep(snelheid)
sense.set_pixels(picture_2)
time.sleep(snelheid)
sense.set_pixels(picture_1)
time.sleep(snelheid)
sense.set_pixels(picture_2)
time.sleep(snelheid)
sense.set_pixels(picture_3)
time.sleep(snelheid)

sense.show_message(str(round(pressure,0))[:-2]+ "hPa", 
                   text_colour=(255, 0, 0), 
                   back_colour=(0,0,0), 
                   scroll_speed=0.1)


vocht_pic1 = [
b,	b,	b,	w,	w,	w,	w,	b,
b,	b,	w,	w,	w,	w,	w,	w,
b,	b,	w,	w,	w,	w,	w,	w,
b,	b,	b,	w,	w,	w,	w,	b,
b,	b,	w,	b,	w,	b,	w,	b,
b,	w, 	b,	w,	b,	w,	b,	b,
b,	b,	b,	b,	b,	b,	b,	b,
b,	b,	b,	b,	b,	b,	b,	b,
]
vocht_pic2 = [
b,	b,	b,	w,	w,	w,	w,	b,
b,	b,	w,	w,	w,	w,	w,	w,
b,	b,	w,	w,	w,	w,	w,	w,
b,	b,	b,	w,	w,	w,	w,	b,
b,	b,	b,	b,	b,	b,	b,	b,
b,	w,	b,	w,	b,	w,	b,	b,
w,	b,	w,	b,	w,	b,	b,	b,
b,	b,	b,	b,	b,	b,	b,	b,
]
for i in range(0, 3):
  sense.set_pixels(vocht_pic1)
  time.sleep(0.3)
  sense.set_pixels(vocht_pic2)
  time.sleep(0.3)

sense.show_message(str(round(humidity,0))[:-2] + "%", 
                  text_colour=(255, 0, 0), 
                  back_colour=(0,0,0), 
                  scroll_speed=0.1)


eind_pic = [
w,	b,	b,	w,	b,	b,	w,	b,
w,	b,	b,	w,	b,	w,	b,	w,
w,	w,	w,	w,	b,	w,	w,	w,
w,	b,	b,	w,	b,	w,	b,	w,
w,	b,	b,	w,	b,	b,	b,	b,
b,	b,	w,	b,	b,	b,	w,	b,
b,	b,	w,	b,	w,	b,	w,	b,
b,	b,	b,	w,	b,	w,	b,	b,
]

sense.set_pixels(eind_pic)
