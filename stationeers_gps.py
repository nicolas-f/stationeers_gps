from math import *

base = [0, 0, 0]

location = [342, 0, -210]

dist = sqrt((base[0] - location[0])**2 + (base[2] - location[2]) ** 2)

dir_x = - (base[0] - location[0]) / dist
dir_y = (base[2] - location[2]) / dist
print(dir_x, dir_y)
angle = atan2(dir_y , dir_x) + pi
print((angle / pi) * 180)