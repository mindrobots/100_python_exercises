# calculate liquid volume in a sphere unsing 
# partially-filled sphere formulas
# points 2 

from math import pi

def volume(h, r=10):
    v = ((4 * pi * r**3) / 3) - (pi * h**2 * (3*r - h) / 3)
    return v

print(volume(2))