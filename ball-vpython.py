from visual import *

scene.autoscale = False

pelota = sphere(pos=(-5,0,0),radius=0.25,color=color.cyan)

pelota.trail = curve(color=pelota.color)

wallR = box(pos=(6,0,0),size=(0.2,12,12),color=color.red)
wallL = box(pos=(-6,0,0),size=(0.2,12,12),color=color.red)
wallT = box(pos=(0,6,-0.1),size=(12,0.2,12),color=color.red)
wallB = box(pos=(0,-6,0.1),size=(12,0.2,12),color=color.red)


pelota.velocity = vector(25,2,1)
deltat = 0.005
t = 0

vscale = 0.15
velocity_arrow = arrow(pos=pelota.pos, axis=vscale*pelota.velocity, color=color.blue)


while t < 10:
    rate(100)
    if(pelota.pos.x > wallR.pos.x):
        pelota.velocity.x = -pelota.velocity.x

    if(pelota.pos.x < wallL.pos.x):
        pelota.velocity.x = -pelota.velocity.x
        
    pelota.pos = pelota.pos + pelota.velocity * deltat
    pelota.trail.append(pos=pelota.pos)
    velocity_arrow.pos = pelota.pos
    velocity_arrow.axis = vscale*pelota.velocity
    t = t + deltat
    
