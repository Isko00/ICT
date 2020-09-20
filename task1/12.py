import math

print("Enter first latitude: ")
t1 = math.radians(float(input()))
print("Enter first longitude: ")
g1 = math.radians(float(input()))
print("Enter second latitude: ")
t2 = math.radians(float(input()))
print("Enter second longitude: ")
g2 = math.radians(float(input()))

distance = 6371.01 * math.acos(math.sin(t1) * math.sin(t2) 
		+ math.cos(t1) * math.cos(t2) * math.cos(g1 - g2))
print("Distance: " + "%.2f" % distance + "km")