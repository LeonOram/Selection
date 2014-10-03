#Leon Oram
#03-10-2014
#Selection S & C task 2

full_date = input("Please enter the date in format dd mm yy: ")

#seperate string
day = full_date[0:2]
month = full_date[3:5]
year = full_date[6:8]

if day[:1] == "0":
    day = day[1:]

#Add to end of date e.g. 1*st*
if day == "1" or day == "21" or day == "31":
    day_add = "st"
elif day == "2" or day == "22":
    day_add = "nd"
elif day == "3" or day == "23":
    day_add = "rd"
else:
    day_add = "th"

#find the month

if month == "01":
    month_text = "January"
elif month == "02":
    month_text = "February"
elif month == "03":
    month_text = "March"
elif month == "04":
    month_text = "April"
elif month == "05":
    month_text = "May"
elif month == "06":
    month_text = "June"
elif month == "07":
    month_text = "July"
elif month == "08":
    month_text = "August"
elif month == "09":
    month_text = "September"
elif month == "10":
    month_text = "October"
elif month == "11":
    month_text = "November"
elif month == "12":
    month_text = "December"
else:
    print("Error")

#Outputs

print("{0}{1} {2} 20{3}".format(day,day_add,month_text,year))
