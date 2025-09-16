from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 400
y = 90
r = 234
theta = 0
state = 0 #0일때 사각형 움직임, 1일때 원 움직임.

character_move_type = 0 #0일때 오른쪽으로 가고, 1일때 위로 올라가고, 2일때 왼쪽으로 가고, 3일때 아래로 내려가서 반복

while(1):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x,y)
    #character.draw_now(784,558)
    #character.draw_now(16,90)

    if state == 0:
        if (x == 784 and y == 90):
            character_move_type = 1
        elif (x == 784 and y == 558):
            character_move_type = 2
        elif (x == 16 and y == 558):
            character_move_type = 3
        elif (x == 16 and y == 90):
            character_move_type = 0

        if (character_move_type == 0):
            x += 2
        elif (character_move_type == 1):
            y += 2
        elif (character_move_type == 2):
            x -= 2
        elif (character_move_type == 3):
            y -= 2

        if(x == 400 and y == 90):
            state = 1
    elif(state == 1):
        x = 400 + r * math.sin(theta / 360 * 2 * math.pi)
        y = 324 + r * math.cos(theta / 360 * 2 * math.pi)
        theta += 1

        if (theta == 360):
            theta = 0
            x = 400
            y = 90
            character_move_type = 0
            state = 0




        # character.draw_now(400 + r * math.sin(0 / 360 * 2 * math.pi), 324 + r * math.cos(0 / 360 * 2 * math.pi))
        #print(math.sin(x / 360 * 2 * math.pi))


    delay(0.01)


