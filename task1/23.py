import math

print("Enter length of a side: ")
s = int(input())
print("Enter the number of sides: ")
n = int(input())
print("Area: " + "%.2f" % (n * (s * s / (4 * math.tan(math.pi / n)))))