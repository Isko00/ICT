import math

print("Enter length of first side: ")
firstLength = int(input())
print("Enter length of second side: ")
secondLength = int(input())
print("Enter length of third side: ")
thirdLength = int(input())
s = (firstLength + secondLength + thirdLength) / 2 
print("Area: " + "%.2f" % (math.sqrt(s * (s - firstLength) * (s - secondLength) * (s - thirdLength))))