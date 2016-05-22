import math


def distance(pos1, pos2):
    return math.sqrt(math.pow(pos1[0] - pos2[0], 2) + math.pow(pos1[1] - pos2[1], 2))


def delta_y(pos1, pos2):
    return math.fabs(pos1[1] - pos2[1])
