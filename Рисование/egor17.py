from pygame import *

screen = display.set_mode((700, 500))
display.set_caption('змейка')
screen.fill((59, 100, 47))
clock = time.Clock()

play = True
r1 = Rect(0,0, 700,250)
r2 = Rect(0,250, 700,500)
r3 = Rect(250,200, 200,200)
r4 = Rect(10,75, 200,100 )


draw.rect(screen, (20, 70, 250), r1)
draw.rect(screen, (0, 250, 0), r2)
draw.rect(screen, (0, 6, 50), r3)
draw.circle(screen, (200, 200, 0), [700,0], 100)
draw.polygon(screen, (100, 0, 0), [[200,200], [500,200], [350,100]])
draw.ellipse(screen, (255, 255, 255), r4)
draw.circle(screen, (255, 255, 255), [170,120], 40)
draw.circle(screen, (255, 255, 255), [50,120], 40)
draw.circle(screen, (255, 255, 255), [115,105], 50)
draw.line(screen, (200, 200, 0), [585,100], [535,150], 7)
draw.line(screen, (200, 200, 0), [550,30], [500,70], 7)
draw.line(screen, (200, 200, 0), [660,120], [610,170], 7)
while play:
    for e in event.get():
        if e.type == QUIT:
            play = False

    display.update()
    clock.tick(60)

