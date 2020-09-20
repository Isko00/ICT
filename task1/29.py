print("Enter temperature in Celsius: ")
celsius = float(input())
print("Temperature in Fahrenheit: " + "%.2f" % ((celsius * 9 / 5) + 32))
print("Temperature in Kelvin: " + "%.2f" % (celsius + 273.15))