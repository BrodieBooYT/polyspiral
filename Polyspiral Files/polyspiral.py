import turtle as pen
import fileinput
import time
import math
while 1:
  pen.colormode(255)
  pen.hideturtle()
  pen.speed(100)
  pen.goto(0, 0)
  pen.down()
  rotset = float(input("[Polyspiral v1.4] Enter Rotation Offset: "))
  n = float(input("[Polyspiral v1.4] Enter Side Count: "))
  increment = float(input("[Polyspiral v1.4] Enter Length Increment: "))
  incrementstart = float(input("[Polyspiral v1.4] Enter Start Length: "))
  redchannel = int(input("[Polyspiral v1.4] Enter Pen Red Channel: "))
  greenchannel = int(input("[Polyspiral v1.4] Enter Pen Green Channel: "))
  bluechannel = int(input("[Polyspiral v1.4] Enter Pen Blue Channel: "))
  steps = int(input("[Polyspiral v1.4] Enter Steps in Recursive Spiral: "))
  print("Formulas: \"default\", \"increment+1\", \"rotate+1\", \"rotate+x\", \"edge+x\", \"multix\", \"sqrtx\", \"tan\"")
  optionalformula = input("[Polyspiral v1.4] Enter Name Of Desired Formula: ")
  if optionalformula == "rotate+x":
      paramvalue1 = float(input("[Polyspiral v1.4] Enter Parameter Value 1: "))
  if optionalformula == "edge+x":
      paramvalue1 = float(input("[Polyspiral v1.4] Enter Parameter Value 1: "))
  if optionalformula == "multix":
      paramvalue1 = float(input("[Polyspiral v1.4] Enter Parameter Value 1: "))
  if optionalformula == "sqrtx":
      paramvalue1 = float(input("[Polyspiral v1.4] Enter Parameter Value 1: "))
  if int(input("[Polyspiral v1.4] New Screen? 0/1: ")) == 1:
    zoom = int(input("[Polyspiral v1.4] Set Window Zoom: "))
    pen.setworldcoordinates(-zoom, -zoom, zoom, zoom)
    pen.colormode(255)
    pen.hideturtle()
    pen.speed(100)
    pen.goto(0, 0)
    pen.down()
    redbackchannel = int(input("[Polyspiral v1.4] Enter Pen Red Background Channel: "))
    greenbackchannel = int(input("[Polyspiral v1.4] Enter Pen Green Background Channel: "))
    bluebackchannel = int(input("[Polyspiral v1.4] Enter Pen Blue Background Channel: "))
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
    if optionalformula == "tan":
      incrementstart = incrementstart + increment
      incrementstart = (math.tan(incrementstart))
    log = open('log.txt', 'a')
    log.write("[Polyspiral v1.4 Debug] [" + str(time.ctime(time.time()) + "] " + str(pen.pos()) + "\n"))
    log.close()
  print("[Polyspiral v1.4] Generation Complete.")
  pen.up()
