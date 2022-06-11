# 1. Assume the days of the week are numbered 0,1,2,3,4,5,6 from Sunday to Saturday. Write a program that asks a day number, and prints the day name (a string).

days = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]

user_day = int(input("Pick a number from 0-6 for a day, where 0 is Sunday and 6 is Saturday: "))
if user_day in range(7):
    print(days[user_day])
else:
    print("Wrong selection, pick a number from 0-6. You picked:", user_day)
