#Leon Oram
#02-10-2014
#Selection S&C task 1

month = int(input("Please enter a month as a number between 1-12: "))
year = input("Please enter a year: ")

if month == 1:
    print("January")
elif month == 2:
    print("February")
elif month == 3:
    print("March")
elif month == 4:
    print("April")
elif month == 5:
    print("May")
elif month == 6:
    print("June")
elif month == 7:
    print("July")
elif month == 8:
    print("August")
elif month == 9:
    print("September")
elif month == 10:
    print("October")
elif month == 11:
    print("November")
elif month == 12:
    print("December")
else:
    print("Invalid input")

#get last two numbers to check if century
last_two = year[2:4]
print(last_two)
year = int(year)

if last_two == "00":
    if year % 400 == 0:
        print("That is a leap year")
    else:
        print("That is not a leap year")
else:
    if year % 4 == 0:
        print("That is a leap year")
    else:
        print("That is not a leap year")
