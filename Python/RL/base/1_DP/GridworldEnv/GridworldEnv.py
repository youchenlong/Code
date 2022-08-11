import numpy as np
from gym.envs.toy_text import discrete


UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

DONE_LOCATION = 8

class GridworldEnv(discrete.DiscreteEnv):
    def __init__(self, shape=[5,5]):
        if not isinstance(shape, (list, tuple)) or not len(shape)==2:
            raise ValueError("shape argument must be a list/tuple of length 2")
        self.shape = shape
        nS = np.prod(shape)
        nA = 4
        MAX_Y = shape[0]
        MAX_X = shape[1]
        P = {}
        grid = np.arange(nS).reshape(shape)
        it = np.nditer(grid, flags=['multi_index'])
        while not it.finished:
            s = it.iterindex
            y, x = it.multi_index
            P[s] = {a:[] for a in range(nA)}
            is_done = lambda s: s==DONE_LOCATION
            reward = 0.0 if is_done(s) else -1.0
            if is_done(s):
                P[s][UP] = [(1, s, reward, True)]
                P[s][RIGHT] = [(1, s, reward, True)]
                P[s][DOWN] = [(1, s, reward, True)]
                P[s][LEFT] = [(1, s, reward, True)]
            else:
                ns_up = s if y==0 else s-MAX_X
                ns_right = s if x==(MAX_X-1) else s+1
                ns_down = s if y==(MAX_Y-1) else s+MAX_X
                ns_left = s if x==0 else s-1
                P[s][UP] = [(1,ns_up, reward, is_done(ns_up))]
                P[s][RIGHT] = [(1,ns_right, reward, is_done(ns_right))]
                P[s][DOWN] = [(1,ns_down, reward, is_done(ns_down))]
                P[s][LEFT] = [(1,ns_left, reward, is_done(ns_left))]
            it.iternext()
        isd = np.ones(nS)/nS
        self.P = P
        super(GridworldEnv, self).__init__(nS, nA, P, isd)