import pygame
import pgzrun
import random

WIDTH = 1200
HEIGHT = 600

ship = Actor('ship')
bug = Actor('bug')
bullet = Actor('bullet')

ship.pos = (WIDTH//2, 500) # Absolute division (//) rounds up the decimal
speed = 5

enemies = []
bullets = []

for i in range(8):
    for j in range (4):
        enemies.append(Actor('bug'))
        enemies[-1].x = 100 + 50 * i
        enemies[-1].y = 80 + 50 * j

def on_key_down(key):
    if key == keys.SPACE:
        bullets.append(Actor('bullet'))
        bullets[-1].x = ship.x
        bullets[-1].y = ship.y - 50

def draw():
    screen.clear()
    screen.fill('black')
    for i in enemies:
        i.draw()
    ship.draw()
    for i in bullets:
        i.draw()

pgzrun.go()