import numpy as np
from visual import *

scene.autoscale = 0
scene.width = 800
scene.heigth = 600

t = arange(0.0, 2 * np.pi, 0.1)

#Parametros elipse
a = 5
b = 1
r 
#Angulo inicial
theta = np.pi/6
#Espira param
espira = curve()
#Dona
dona = ring(pos=(0,0,0), axis=(0,1,0), radius=4, thicknes=0.1)
dona.rotate(angle=theta, axis=(1,0,0), origin=(0,0,0))
