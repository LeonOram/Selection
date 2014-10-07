#Leon Oram
#05-10-2014
#Selection S&D Task 3

full_date = input("Please enter the date in format d m yy: ")

#seperate string
if len(full_date) == 6: #two single
    day = full_date[0:1]
    month = full_date[2:3]
    year = full_date[4:6]
elif len(full_date) == 7: #one single
    if full_date[1:2] == " ": #single number day
        day = full_date[0:1]
        month = full_date[2:4]
        year = full_date[5:7]
    else: #single number month 
        day = full_date[0:2]
        month = full_date[3:4]
        year = full_date[5:7]
elif len(full_date) == 8: #all double  
    day = full_date[0:2]
    month = full_date[3:5]
    year = full_date[6:8]
else:
    print("Error in date format")

if day[:1] == "0":
    day = day[1:]
day_int = int(day)

#finding how many days in said month
if month == "4" or month == "6" or day == "9" or day == "11":
    max_day = 30
elif month == "2":
    max_day = 29
else:
    max_day = 31

#Add to end of date e.g. 1*st*
if day == "1" or day == "21" or day == "31" and day_int <= max_day  :
    day_add = "st"
elif day == "2" or day == "22":
    day_add = "nd"
elif day == "3" or day == "23":
    day_add = "rd"
elif day_int <= max_day:
    day_add = "th"
else:
    print("Error in day input")

#find the month

if month == "1":
    month_text = "January"
elif month == "2":
    month_text = "February"
elif month == "3":
    month_text = "March"
elif month == "4":
    month_text = "April"
elif month == "5":
    month_text = "May"
elif month == "6":
    month_text = "June"
elif month == "7":
    month_text = "July"
elif month == "8":
    month_text = "August"
elif month == "9":
    month_text = "September"
elif month == "10":
    month_text = "October"
elif month == "11":
    month_text = "November"
elif month == "12":
    month_text = "December"
else:
    print("Error Invalid format")

# Finding if year = 1900s or 2000s
year_int = int(year)
#print(year)
if year_int <= 30:
    cent = "20"
elif 30 < year_int >= 00:
    cent = "19"
else:
    print("Invalid year")

#Outputs

print("{0}{1} {2} {3}{4}".format(day,day_add,month_text,cent,year))
