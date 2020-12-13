
import math


def memoize(f):

    class memodict(dict):
        def __init__(self, f):
            self.f = f
        def __call__(self, *args):
            return self[args]
        def __missing__(self, key):
            ret = self[key] = self.f(*key)
            return ret
    return memodict(f)


@memoize
def build_stair(reserve, previous_step):
    if reserve == 0:
        return 1


    min_brick = (-1+math.sqrt(1+8*reserve)) / 2
    min_brick = int(math.ceil(min_brick))

    if previous_step == -1:
        max_bricks = reserve
    else:
        max_bricks = previous_step
    max_bricks = min(max_bricks, reserve+1)

    nb_stairs = 0
    for i in range(min_brick, max_bricks):
            nb_stairs += build_stair(reserve-i, i)
    return nb_stairs


def answer(n):
    return build_stair(n, -1)

print answer(200)