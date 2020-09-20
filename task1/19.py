import math

print("Enter height: ")
height = float(input())
speed = 0
while (height > 0):
    speed += 9.8
    height -= speed
print("Speed: " + "%.1f" % speed)