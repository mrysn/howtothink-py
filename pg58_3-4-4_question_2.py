# 2. You go on a wonderful holiday (perhaps to jail, if you don’t like happy exercises) leaving on day number 3 (a Wednesday). You return home after 137 sleeps. Write a general version of the program which asks for the starting day number, and the length of your stay, and it will tell you the name of day of the week you will return on.

days = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]

user_start_day = int(input("What day did you go on holiday (pick from 0-6)?: "))
if user_start_day in range(7):
    print("Holiday start day: ", str.title(days[user_start_day]))
    user_nights = int(input("How many nights were you on holiday?: "))
    day = (user_nights + user_start_day ) % 7
    print("Holiday end day:   ",str.title(days[day]))
else:
    print("Wrong selection, pick a number from 0-6. You picked:", user_start_day)
