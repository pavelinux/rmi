#!/usr/bin/env python
from visual import *
# parameters
theta = pi/6
w = 2 * pi
B0 = 1.5 
omega = 300
# Masa y Capacidad calorifica humano
t = 760
m = 0.001
Cp = 4190   
# Elipse
a_0 = 0.15 * 10
b_0 = 0.50 * 10

U = (w * (pi* B0 * a_0 * b_0*sin(theta))**2) / (4 * omega) * (2* w * t - sin(2*w*t))
# Mas general
deltaT = (w *(pi * B0 * a_0 * b_0 * sin(theta))**2*2*w*t-sin(2*w*t))/(4*m*Cp*omega)

#print "Aumento de energia: ", U
#print "Incremento de T: ", deltaT
# Espira
scene.autoscale = 0 
scene.width=800
scene.heigth=1024
h = 0
t = arange(0, 2 * pi, 0.1)
elipse = curve(x = a_0 * cos(t), y = h * cos(theta) - b_0 * sin(t) * sin(theta), z = h * sin(theta) + b_0 * sin(t) * cos(theta) ,color=color.white)
rod = cylinder(pos=(0,2,1),axis=(0,0,10), radius=4.5,color=color.white, opacity=0.1)
rod.pos = (0,0,0)
#dona = ring(pos=(0,0,0), axis=(0,1,0), radius=4, thickness=0.1)
#dona.rotate(angle=theta,axis=(1,0,0),origin=(0,0,0))

