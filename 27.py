# function to calculate acceleration given:
# v1, v2 and T1, t2
# points 1

def accel(v1, v2, t1, t2):
    return (v2-v1)/(t2-t1)

print(accel(0, 10, 0, 20))
