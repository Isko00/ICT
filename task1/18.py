import math

print("Enter radius: ")
radius = float(input())
print("Enter height: ")
height = float(input())
volume = math.pi * radius ** 2 * height
print("Volume: " + "%.1f" % volume)
