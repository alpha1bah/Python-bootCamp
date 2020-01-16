#
import math
def volume_cylinder(height, radius):
    pi=math.pi
    return (pi*radius**2*height)

print(volume_cylinder(1,1))


def cone_volume(h,r):
    volume=(h/3) * math.pi *(r**2)
    return volume


print(cone_volume(1,1))
print(f"1/3 pi = {math.pi/3}")