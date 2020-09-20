import math

seconds = 0
print("Enter number of days: ")
seconds += int(input()) * 24 * 60 * 60
print("Enter number of hours: ")
seconds += int(input()) * 60 * 60
print("Enter number of minutes: ")
seconds += int(input()) * 60
print("Enter number of seconds: ")
seconds += int(input())
print("Time: " + str(seconds) + " seconds")