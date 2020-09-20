import math

print("Enter mass of water: ")
mass = int(input())
print("Enter temperature change: ")
temperatureChange = int(input())
heatCapacity = 4.186
energy = mass * temperatureChange * heatCapacity
print("Energy: " + str(energy) + "J")
print("Cost: " + "%.2f" % (energy / (3.6 * (10 ** 6)) * 8.9) + " cents")
