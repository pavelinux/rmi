#!/usr/bin/env python
from visual import *
scene.autoscale = 0 
scene.width=800
scene.heigth=600
#opacity=1
t = arange(0, 2 * pi, 0.1)
#curve( x = cos(t), y = sin(t), z = 0.5, red = cos(t), green = 0, blue = 0.5*(1-cos(t)) )
#circulo = curve( x = cos(t), y = sin(t), z = 0.0, color=color.blue)
a = 5
b = 1
h = 0
th = pi/6
#curve(x = cos(t),y = sin(t),z=0.0, pos=[(0,0,0), (1,sqrt(2)/2,sqrt(2)/2)])
dona = ring(pos=(0,0,0), axis=(0,1,0), radius=4, thickness=0.1)
#elipse = curve(x = a * cos(t), y = h * cos(th) - b * sin(t) * sin(th), z = h * sin(th) + b * sin(t) * cos(th) ,color=color.red)
#circulo.rotate(angle=pi/6.0,  axis=axis, origin=pos)

dona.rotate(angle=pi/6,axis=(1,0,0),origin=(0,0,0))

circulo2 = curve(x = 5 * cos(t), y = h * cos(th) - 5 * sin(t) * sin(th), z = h * sin(th) + 5 * sin(t) * cos(th) ,color=color.red)
#myell = ellipsoid(pos=(0,0,0),length=5, height=2, width=1)
#myell.rotate(angle=pi/6, axis=(1,0,0))

