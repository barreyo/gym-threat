"""TODO."""

import time

import gym
import gym_threat  # noqa

env = gym.make("threat-v0")

print env.reset()

for i in range(20):
    env.render(mode='rgb_array')
    o, r, done, info = env.step(0)

    time.sleep(2)
    print "Observation: ", o
    print "Reward: ", r
    print "Done: ", done
    print "Info: ", info
