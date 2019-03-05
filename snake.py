import random
import curses # some graphics stuff?

s = curses.initscr() #init screen
curses.curs_set(0) #set curser off screen
sh, sw = s.getmaxyx()  #get screensize
w = curses.newwin(sh,sw,0,0)  #make new window
w.keypad(1) #accept keyinput
w.timeout(100) #refresh ever 100ms

# snake starting point
#snk_x = sw/4
#snk_y = sh/2
snk_x = 10
snk_y = 10

# snake body
snake = [
    [snk_y, snk_x],
    [snk_y, snk_x-1],
    [snk_y, snk_x-2]
]

# initialize food
food = [5, 5]
w.addch(5, 5, 'f')

key = curses.KEY_RIGHT

# gameloop
while True:
    next_key = w.getch()
    key = key if next_key ==-1 else next_key

    if snake[0][0] in [0,sh] or snake[0][1] in [0,sw] or snake[0] in snake[1:]:
        curses.endwin()
        quit()

    new_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    snake.insert(0,new_head)

    if snake[0] == food:
        food = None
        while food is None:
            newfood = [
                random.randint(1, 20),
                random.randint(1, 20)
                ]
            food = newfood if newfood not in snake else None
        w.addch(food[0], food[1], 'f')

    else:
        tail = snake.pop()
        w.addch(int(tail[0]), int(tail[1]), ' ')

    w.addch(int(snake[0][0]), int(snake[0][1]), 's')
