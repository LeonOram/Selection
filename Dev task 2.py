#Leon Oram
#29-09-2014
#Selection dev task 2

water_temp = int(input("Please enter the tempreature of the water: "))

if water_temp <= 0:
    print("The water is frozen")
elif water_temp >= 100:
    print("The water is boiling")
else:
    print("It's just water")
