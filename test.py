import gymnasium as gym
env = gym.make("BipedalWalker-v3", hardcore=True, render_mode="rgb_array")
env


