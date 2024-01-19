from pygame import *
from random import randint

screen = display.set_mode((700, 500))
display.set_caption('змейка')
screen.fill((59, 100, 47))
clock = time.Clock()

play = True
head = Rect(350,250, 30,30)
speed = 10
direction = [0,-speed]
color = (100, 0, 0)
def random_color():
    r = randint(0,255)
    g = randint(0,205)
    b = randint(0,155)
    return(r, g, b)

def move(head):
    global direction, color
    KEY = key.get_pressed()
    if head.bottom > 500 or KEY[K_w]:
        direction = [0,-speed]
        color = random_color()
    elif head.top < 0 or KEY[K_s]:
        direction = [0, speed]
        color = random_color()
    elif head.left < 0 or KEY[K_a]:
        direction = [speed, 0]
        color = random_color()
    elif head.right > 700 or KEY[K_d]:
        direction = [-speed, 0]
        color = random_color()
    head.move_ip(direction)


while play:
    for e in event.get():
        if e.type == QUIT:
            play = False
    
    draw.rect(screen, color, head)
    move(head)

    display.update()
    clock.tick(60)
