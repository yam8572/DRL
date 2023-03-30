"""
Reinforcement learning maze example.

Red rectangle:          explorer.
Black rectangles:       hells       [reward = -1].
Yellow bin circle:      paradise    [reward = +1].
All other states:       ground      [reward = 0].

This script is the main part which controls the update method of this example.
The RL is in RL_brain.py.

View more on my tutorial page: https://morvanzhou.github.io/tutorials/
"""

from maze_env import Maze
from RL_brain import QLearningTable
import argparse
import sys

def update():
    for episode in range(100):
        # initial observation
        observation = env.reset()

        while True:
            # fresh env
            env.render()

            # RL choose action based on observation
            action = RL.choose_action(str(observation))

            # RL take action and get next observation and reward
            observation_, reward, done = env.step(action)

            # RL learn from this transition
            RL.learn(str(observation), action, reward, str(observation_))

            # swap observation
            observation = observation_

            # break while loop when end of this episode
            if done:
                break

    # end of game
    print('game over')
    env.destroy()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Set gridword inital parameter')
    parser.add_argument('--n',
                        type=int,
                        help='set numbers of grid',
                        required=True)
    parser.add_argument('--startX',
                        type=int,
                        help='set startX',
                        )
    parser.add_argument('--startY',
                        type=int,
                        help='set startY',
                        )
    parser.add_argument('--endX',
                        type=int,
                        help='set endX',
                        )
    parser.add_argument('--endY',
                        type=int,
                        help='set endY',
                        )
    parser.add_argument('--blockX_1',
                        type=int,
                        help='set blockX_1',
                        )
    parser.add_argument('--blockY_1',
                        type=int,
                        help='set blockY_1',
                        )
    parser.add_argument('--blockX_2',
                        type=int,
                        help='set blockX_2',
                        )
    parser.add_argument('--blockY_2',
                        type=int,
                        help='set blockY_2',
                        )
    parser.add_argument('--blockX_3',
                        type=int,
                        help='set blockX_3',
                        )
    parser.add_argument('--blockY_3',
                        type=int,
                        help='set blockY_3',
                        )
    args = parser.parse_args()
    env = Maze(args.n,args.startX,args.startY,args.endX,args.endY,args.blockX_1,args.blockY_1,args.blockX_2,args.blockY_2,args.blockX_3,args.blockY_3)
    RL = QLearningTable(actions=list(range(env.n_actions)))
    print(list(range(env.n_actions)))
    # print(RL)

    env.after(100, update)
    env.mainloop()