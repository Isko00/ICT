import sys

print("Enter air temperature: ")
t = float(input())
if (t > 10):
    sys.exit("Temperature MUST be less than 10")
print("Enter wind speed: ")
v = float(input())
if (v < 4.8):
    sys.exit("Wind speeds MUST exceeding  4.8")
print("Wind chill index: " + "%.0f" % (13.12 + 0.6215 * t 
        - 11.37 * (v ** 0.16) + 0.3965 * t * (v ** 0.16)))
