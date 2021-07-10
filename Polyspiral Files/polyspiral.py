#Polyspiral v1.6
#Made by BrodieBooYT
import turtle as pen
import fileinput
import time
import math
import colorsys
hue = 0
def hsv2rgb(h, s, v):  #Thanks to Cory Kramer for the Stack Overflow Answer! https://stackoverflow.com/questions/24852345/hsv-to-rgb-color-conversion
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h,s,v))
while 1:
  pen.colormode(255)
  pen.hideturtle()
  pen.speed(100)
  pen.goto(0, 0)
  pen.down()
  rotset = float(input("[Polyspiral v1.6] Enter Rotation Offset: "))
  n = float(input("[Polyspiral v1.6] Enter Side Count: "))
  increment = float(input("[Polyspiral v1.6] Enter Length Increment: "))
  incrementstart = float(input("[Polyspiral v1.6] Enter Start Length: "))
  redchannel = int(input("[Polyspiral v1.6] Enter Pen Red Channel: "))
  greenchannel = int(input("[Polyspiral v1.6] Enter Pen Green Channel: "))
  bluechannel = int(input("[Polyspiral v1.6] Enter Pen Blue Channel: "))
  steps = int(input("[Polyspiral v1.6] Enter Steps in Recursive Spiral: "))
  print("Formulas: \"default\", \"increment+1\", \"rotate+1\", \"rotate+x\", \"edge+x\", \"multix\", \"sqrtx\", \"divx\", \"rainbow\"")
  optionalformula = input("[Polyspiral v1.6] Enter Name Of Desired Formula: ")
  if optionalformula == "rotate+x":
      paramvalue1 = float(input("[Polyspiral v1.6] Enter Parameter Value 1: "))
  if optionalformula == "edge+x":
      paramvalue1 = float(input("[Polyspiral v1.6] Enter Parameter Value 1: "))
  if optionalformula == "multix":
      paramvalue1 = float(input("[Polyspiral v1.6] Enter Parameter Value 1: "))
  if optionalformula == "sqrtx":
      paramvalue1 = float(input("[Polyspiral v1.6] Enter Parameter Value 1: "))
  if optionalformula == "divx":
      paramvalue1 = float(input("[Polyspiral v1.6] Enter Parameter Value 1: "))
  if optionalformula == "rainbow":
      paramvalue1 = float(input("[Polyspiral v1.6] Enter Pallate Squeeze: "))
      paramvalue2 = float(input("[Polyspiral v1.6] Enter Minimum Threshold 0 - 1: "))
      hue = paramvalue2
      paramvalue3 = float(input("[Polyspiral v1.6] Enter Maximum Threshold 0 - 1: "))
      paramvalue4 = float(input("[Polyspiral v1.6] Enter Brightness 0 - 1: "))
      paramvalue5 = float(input("[Polyspiral v1.6] Enter Saturation 0 - 1: "))
  if int(input("[Polyspiral v1.6] New Screen? 0/1: ")) == 1:
    zoom = int(input("[Polyspiral v1.6] Set Window Zoom: "))
    pen.setworldcoordinates(-zoom, -zoom, zoom, zoom)
    pen.colormode(255)
    pen.hideturtle()
    pen.speed(100)
    pen.goto(0, 0)
    pen.down()
    redbackchannel = int(input("[Polyspiral v1.6] Enter Pen Red Background Channel: "))
    greenbackchannel = int(input("[Polyspiral v1.6] Enter Pen Green Background Channel: "))
    bluebackchannel = int(input("[Polyspiral v1.6] Enter Pen Blue Background Channel: "))
    penbackground = (redbackchannel, greenbackchannel, bluebackchannel)
    pen.color(penbackground)
    pen.dot(16000)
  pencolorpoly = (redchannel, greenchannel, bluechannel)
  pen.color(pencolorpoly)
  for i in range(steps):
    pen.forward(incrementstart)
    pen.right(rotset + (360 / n))
    if optionalformula == "default":
      incrementstart = incrementstart + increment
    if optionalformula == "rainbow":
      incrementstart = incrementstart + increment
      hue = hue + 1 / (360 / paramvalue1)
      pen.color(hsv2rgb(hue, paramvalue5, paramvalue4))
      if hue >= paramvalue3:
        hue = paramvalue2
    if optionalformula == "increment+1":
      incrementstart = incrementstart + increment
      increment = increment + 1
    if optionalformula == "rotate+1":
      incrementstart = incrementstart + increment
      rotset = rotset + 1
    if optionalformula == "rotate+x":
      incrementstart = incrementstart + increment
      rotset = rotset + paramvalue1
    if optionalformula == "edge+x":
      incrementstart = incrementstart + increment
      n = n + paramvalue1
    if optionalformula == "multix":
      incrementstart = incrementstart * paramvalue1
    if optionalformula == "sqrtx":
      incrementstart = (math.sqrt(incrementstart + paramvalue1))
    if optionalformula == "divx":
      incrementstart = (incrementstart / paramvalue1) * increment
      
    log = open('log.txt', 'a')
    log.write("[Polyspiral v1.6 Debug] [" + str(time.ctime(time.time()) + "] " + str(pen.pos()) + "\n"))
    log.close()
  print("[Polyspiral v1.6] Generation Complete.")
  pen.up()
