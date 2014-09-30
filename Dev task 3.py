#Leon Oram
#30-09-2014
#selection dev task 4

worked = int(input("Please enter your hours worked: "))
pay = int(input("Please enter your hourly pay: "))

if worked > 0 and worked <= 60:
    if worked <= 40:
        total_pay = worked * pay
    else:
        total_pay = 40 * pay + (worked - 40)* (pay * 1.5)
    print("Your total pay is {0}".format(total_pay))
else:
    print("Error: You have not worked or have worked too much")
