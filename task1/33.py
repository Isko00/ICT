import sys

print("Enter the number of loaves of day-old bread: ")
number = float(input())
print("Regular price: $" + "%.2f" % (number * 3.49))
print("Discount: $" + "%.2f" % (number * 3.49 * 0.6))
print("Total price: $" + "%.2f" % (number * 3.49 * 0.4))