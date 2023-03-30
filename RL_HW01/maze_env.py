"""
Reinforcement learning maze example.

Green rectangle:        explorer.
Black rectangles:       hells       [reward = -1].
Red rectangle:          paradise    [reward = +1].
All other states:       ground      [reward = 0].

This script is the environment part of this example. The RL is in RL_brain.py.

View more on my tutorial page: https://morvanzhou.github.io/tutorials/
"""


import numpy as np
import time
import sys
import tkinter as tk

# if sys.version_info.major == 2:
#     import Tkinter as tk
# else:
#     import tkinter as tk


UNIT = 40   # pixels
# MAZE_H = 4  # grid height
# MAZE_W = 4  # grid width


class Maze(tk.Tk, object):
    def __init__(self,n=3,startX=0,startY=0,endX=2,endY=2,hellX_1=0,hellY_1=1,hellX_2=0,hellY_2=2,hellX_3=1,hellY_3=2):
        super(Maze, self).__init__()
        self.action_space = ['u', 'd', 'l', 'r']
        self.n_actions = len(self.action_space)
        self.title('maze')
        self.MAZE_H=n
        self.MAZE_W=n
        self.start_X=startX
        self.start_Y=startY
        self.end_X=endX
        self.end_Y=endY
        self.hell_x1=hellX_1
        self.hell_y1=hellY_1
        self.hell_x2=hellX_2
        self.hell_y2=hellY_2
        self.hell_x3=hellX_3
        self.hell_y3=hellY_3
        self.geometry('{0}x{1}'.format(self.MAZE_W * UNIT, self.MAZE_H * UNIT))
        self._build_maze()

    def _build_maze(self):
        self.canvas = tk.Canvas(self, bg='white',
                           height=self.MAZE_H * UNIT,
                           width=self.MAZE_W * UNIT)

        # create grids
        for c in range(0, self.MAZE_W * UNIT, UNIT):
            x0, y0, x1, y1 = c, 0, c, self.MAZE_H * UNIT
            self.canvas.create_line(x0, y0, x1, y1)
        for r in range(0, self.MAZE_H * UNIT, UNIT):
            x0, y0, x1, y1 = 0, r, self.MAZE_W * UNIT, r
            self.canvas.create_line(x0, y0, x1, y1)

        # create origin
        origin = np.array([20, 20])

        # hell
        hell1_center = origin + np.array([UNIT * self.hell_y1, UNIT * self.hell_x1])
        self.hell1 = self.canvas.create_rectangle(
            hell1_center[0] - 15, hell1_center[1] - 15,
            hell1_center[0] + 15, hell1_center[1] + 15,
            fill='black')
        # hell
        hell2_center = origin + np.array([UNIT * self.hell_y2, UNIT * self.hell_x2])
        self.hell2 = self.canvas.create_rectangle(
            hell2_center[0] - 15, hell2_center[1] - 15,
            hell2_center[0] + 15, hell2_center[1] + 15,
            fill='black')
        
        # hell
        hell3_center = origin + np.array([UNIT * self.hell_y3, UNIT * self.hell_x3])
        self.hell3 = self.canvas.create_rectangle(
            hell3_center[0] - 15, hell3_center[1] - 15,
            hell3_center[0] + 15, hell3_center[1] + 15,
            fill='black')

        # create red rect as end Position
        end_center = origin + np.array([UNIT * self.end_Y, UNIT * self.end_X])
        self.oval = self.canvas.create_rectangle(
            end_center[0] - 15, end_center[1] - 15,
            end_center[0] + 15, end_center[1] + 15,
            fill='red')

        # create green rect as start Position
        start_center = origin + np.array([UNIT * self.start_Y, UNIT * self.start_X])
        self.rect = self.canvas.create_rectangle(
            start_center[0] - 15, start_center[1] - 15,
            start_center[0] + 15, start_center[1] + 15,
            fill='green')

        # pack all
        self.canvas.pack()

    def reset(self):
        self.update()
        time.sleep(0.5)
        self.canvas.delete(self.rect)
        origin = np.array([20, 20])
        # create green rect as start Position
        start_center = origin + np.array([UNIT * self.start_Y, UNIT * self.start_X])
        self.rect = self.canvas.create_rectangle(
            start_center[0] - 15, start_center[1] - 15,
            start_center[0] + 15, start_center[1] + 15,
            fill='green')
        # return observation
        return self.canvas.coords(self.rect)

    def step(self, action):
        s = self.canvas.coords(self.rect)
        base_action = np.array([0, 0])
        if action == 0:   # up
            if s[1] > UNIT:
                base_action[1] -= UNIT
        elif action == 1:   # down
            if s[1] < (self.MAZE_H - 1) * UNIT:
                base_action[1] += UNIT
        elif action == 2:   # right
            if s[0] < (self.MAZE_W - 1) * UNIT:
                base_action[0] += UNIT
        elif action == 3:   # left
            if s[0] > UNIT:
                base_action[0] -= UNIT

        self.canvas.move(self.rect, base_action[0], base_action[1])  # move agent

        s_ = self.canvas.coords(self.rect)  # next state

        # reward function
        if s_ == self.canvas.coords(self.oval):
            reward = 1
            done = True
            s_ = 'terminal'
        elif s_ in [self.canvas.coords(self.hell1), self.canvas.coords(self.hell2),self.canvas.coords(self.hell3)]:
            reward = -1
            done = True
            s_ = 'terminal'
        else:
            reward = 0
            done = False

        return s_, reward, done

    def render(self):
        time.sleep(0.1)
        self.update()


def update():
    for t in range(10):
        s = env.reset()
        while True:
            env.render()
            a = 1
            s, r, done = env.step(a)
            if done:
                break

if __name__ == '__main__':
    env = Maze()
    env.after(100, update)
    env.mainloop()