numbers = [1, 2, 3]
print("Enter first number: ")
numbers[0] = int(input())
print("Enter second number: ")
numbers[1] = int(input())
print("Enter third number: ")
numbers[2] = int(input())
print(str(min(numbers)) + " " + str(numbers[0] + numbers[1] 
    + numbers[2] - min(numbers) - max(numbers)) + " " + str(max(numbers)))