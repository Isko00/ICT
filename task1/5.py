print("Enter number of containers holding one liter or less: ")
less = float(input())
print("Enter number of containers holding more than one liter: ")
more = float(input())
refund = less * 0.1 + more * 0.25
print("Refund: $" + "%.2f" % refund)