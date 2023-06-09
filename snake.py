import random
import curses
import time

s = curses.initscr()
curses.curs_set(0)
sh, sw = s.getmaxyx()
w = curses.newwin(sh, sw, 0, 0)
w.keypad(1)
w.timeout(100)

snk_x = sw//4
# snk_x = sw-9
snk_y = sh//2
# snk_y = sh-1
snake = [
  [snk_y, snk_x],
  [snk_y, snk_x-1],
  [snk_y, snk_x-2],
  [snk_y, snk_x-3]
]

food = [sh//2, sw//2]
w.addch(int(food[0]), int(food[1]), curses.ACS_PI)
key = curses.KEY_RIGHT

while True:
  next_key = w.getch()
  prev_key = key

  # disabling the opposite key 
  if next_key == curses.KEY_DOWN and key == curses.KEY_UP:
    key = key
  elif next_key == curses.KEY_UP and key == curses.KEY_DOWN:
    key = key
  elif next_key == curses.KEY_LEFT and key == curses.KEY_RIGHT:
    key = key
  elif next_key == curses.KEY_RIGHT and key == curses.KEY_LEFT:
    key = key
  else :
    key = key if next_key == -1 else next_key

  if snake[0] in snake[1:]:
    curses.endwin()
    quit()


  new_head = [snake[0][0], snake[0][1]]
  
  if key == curses.KEY_DOWN:
    new_head[0] += 1
  if key == curses.KEY_UP:
    new_head[0] -= 1
  if key == curses.KEY_LEFT:
    new_head[1] -= 2
  if key == curses.KEY_RIGHT:
    new_head[1] += 2

  body = [new_head[0], new_head[1]-1]
  snake.insert(0, body)
  snake.insert(0, new_head)

  if snake[0][0] in [0,sh] or snake[0][1] in [0,sw]\
    or snake[1][1] in [0, sw]\
    or snake[0][1] in [0,sw-1]:
    curses.endwin()
    quit()

  if snake[0] == food or snake[1] == food:
    food = None
    while food is None:
      nf = [
        random.randint(1, sh-2),
        random.randint(1, sw-2)
      ]
      food = nf if nf not in snake else None
    w.addch(food[0], food[1], curses.ACS_PI)
  else:
    tail_1 = snake.pop()
    tail_2 = snake.pop()
    w.addch(int(tail_1[0]), int(tail_2[1]), ' ')
    w.addch(int(tail_2[0]), int(tail_1[1]), ' ')

  w.addch(int(snake[1][0]), int(snake[1][1]), curses.ACS_CKBOARD)
  w.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD)
  # time.sleep(0.4)