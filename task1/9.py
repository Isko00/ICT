print("Enter amount of money deposited: ")
amount = float(input())
for i in range(3):
	amount *= 1.04
	print("After " + str(i) + " year: $" + "%.2f" % amount)