from sense_hat import SenseHat

from time import sleep as sl
from random import randint as ra
s = SenseHat()
s.set_rotation(270)
f = s.set_pixel
fs = s.set_pixels

for i in range(100):
  xpos = ra(0,7)
  ypos = ra(0,7)
 
  color = ra(1, 3)
  if color == 1:
    f(xpos, ypos, (0, ra(100, 255), ra(100,255)))
  elif color == 2:
    f(xpos, ypos, (ra(100, 255), 0, ra(100,255)))
  else:
    f(xpos, ypos, (ra(100, 255), ra(100,255), 0))
  sl(0.02)
  
t = s.get_temperature()
p = s.get_pressure()
h = s.get_humidity()

w = (255, 255, 255)
b = (0, 0, 0)
r = (255, 0, 0)
l = (30, 30, 255)
i = (48, 184, 186)
n = (56, 24, 15)

p1 = [
    b, w, w, w, b, b, b, b, # 0
    b, w, b, w, b, b, b, b, # 8
    b, w, b, w, b, b, b, b, #16
    b, w, b, w, b, w, w, w, #24
    b, w, l, w, b, b, w, b, #32
    b, w, l, w, b, b, w, b, #40
    b, w, w, w, b, b, w, b, #48
    b, b, w, b, b, b, b, b  #56
]

p2 = p1[:]
p2[26] = i
p3 = p2[:]
p3[10] = r
p3[18] = r

fs(p1)
sl(1)
fs(p2)
sl(1)
fs(p3)
sl(1)

s.show_message(str(round(t,1)) + " C",
                   text_colour=(255, 0, 0), 
                   back_colour=(0,0,0), 
                   scroll_speed=0.1)


l = (30, 30, 30)

p1 = [								
b,	b,	b,	r,	r,	b,	b,	b,	
b,	r,	r,	l,	l,	r,	r,	b,	
b,	r,	l,	l,	l,	l,	r,	b,	
r,	l,	l,	l,	l,	l,	l,	r,	
r,	w,	w,	w,	w,	l,	l,	r,	
b,	r,	n,	n,	n,	n,	r,	b,	
b,	r,	r,	n,	n,	r,	r,	b,	
b,	b,	b,	r,	r,	b,	b,	b,
]
p2 = p1[:]
p2[18] = w
p2[27] = w
p2[33:36] = [l]*3

p3 = [
b,	b,	b,	r,	r,	b,	b,	b,
b,	r,	r,	l,	l,	r,	r,	b,
b,	r,	l,	l,	l,	w,	r,	b,
r,	l,	l,	l,	w,	l,	l,	r,
r,	l,	l,	w,	l,	l,	l,	r,
b,	r,	n,	n,	n,	n,	r,	b,
b,	r,	r,	n,	n,	r,	r,	b,
b,	b,	b,	r,	r,	b,	b,	b,
]

p4 = [								
b,	b,	b,	r,	r,	b,	b,	b,	
b,	r,	r,	l,	l,	r,	r,	b,	
b,	r,	l,	l,	l,	l,	r,	b,	
r,	l,	l,	l,	l,	l,	l,	r,	
r,	l,	l,	w,	w,	w,	w,	r,	
b,	r,	n,	n,	n,	n,	r,	b,	
b,	r,	r,	n,	n,	r,	r,	b,	
b,	b,	b,	r,	r,	b,	b,	b,
]

fs(p1)
sl(0.5)
fs(p2)
sl(0.5)
fs(p3)
sl(0.5)
fs(p4)
sl(0.5)
fs(p3)
sl(0.5)
fs(p2)
sl(0.5)
fs(p1)
sl(0.5)
fs(p2)
sl(0.5)
fs(p3)
sl(0.5)

s.show_message(str(round(p,0))[:-2]+ "hPa", 
                   text_colour=(255, 0, 0), 
                   back_colour=(0,0,0), 
                   scroll_speed=0.1)


p1 = [
b,	b,	b,	w,	w,	w,	w,	b,
b,	b,	w,	w,	w,	w,	w,	w,
b,	b,	w,	w,	w,	w,	w,	w,
b,	b,	b,	w,	w,	w,	w,	b,
b,	b,	w,	b,	w,	b,	w,	b,
b,	w, 	b,	w,	b,	w,	b,	b,
b,	b,	b,	b,	b,	b,	b,	b,
b,	b,	b,	b,	b,	b,	b,	b,
]
p2 = p1[:]
p2[32:40] = [b]*8
p2[48:53:2] = [w]*3

for i in [0, 1, 2]:
  fs(p1)
  sl(0.3)
  fs(p2)
  sl(0.3)

s.show_message(str(round(h,0))[:-2] + "%", 
                  text_colour=(255, 0, 0), 
                  back_colour=(0,0,0), 
                  scroll_speed=0.1)


p = [
w,	b,	b,	w,	b,	b,	w,	b,
w,	b,	b,	w,	b,	w,	b,	w,
w,	w,	w,	w,	b,	w,	w,	w,
w,	b,	b,	w,	b,	w,	b,	w,
w,	b,	w,	w,	b,	b,	w,	b,
b,	b,	w,	b,	b,	b,	w,	b,
b,	b,	w,	b,	w,	b,	w,	b,
b,	b,	b,	w,	b,	w,	b,	b,
]

fs(p)
