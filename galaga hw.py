import pygame
import pgzrun
import random

WIDTH = 1200
HEIGHT = 600

jet = Actor('jet')
bomb = Actor('bomb')
bullet = Actor('bullet')

jet.pos = (WIDTH//2, 500) # Absolute division (//) rounds up the decimal
speed = 5

enemies = []
bullets = []
game = True

for i in range(8):
    for j in range (4):
        enemies.append(Actor('bomb'))
        enemies[-1].x = 100 + 50 * i
        enemies[-1].y = 80 + 50 * j

def on_key_down(key):
    global game, bullets
    if key == keys.SPACE:
        bullets.append(Actor('bullet'))
        bullets[-1].x = jet.x
        bullets[-1].y = jet.y - 50

def draw():
    global game
    screen.clear()
    screen.fill('black')
    if game:
        for i in enemies:
            i.draw()
        jet.draw()
        for i in bullets:
            i.draw()
    if len (enemies) == 0:
        game = False
        screen.draw.text('Game Over, You have shot all the enemies', (400, 300), fontsize = 50)
    if game == "lost":
        screen.fill('black')
        screen.draw.text('Sorry, you lost', (400,300), fontsize = 50)

def update():
    global game
    if keyboard.left:
        jet.x -= 10
    if keyboard.right:
        jet.x += 10

    for i in bullets:
        i.y -= 10
    
    for i in enemies:
        i.y += 0.5
        for j in bullets:
            if j.colliderect(i):
                bullets.remove(j)
                enemies.remove(i)
        if i.colliderect(jet):
            game = 'lost'

pgzrun.go()