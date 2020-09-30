ask_user = float(input("Assume the days of the week are numbered 0 (Sunday) to 6 (Saturday). What day is total in terms of numbers?"))
if ask_user == 0:
    print("Today is "+"Sunday")
elif ask_user == 1:
    print("Today is "+"Monday")
elif ask_user == 2:
    print("Today is " + "Tuesday")
elif ask_user == 3:
    print("Today is " + "Wednesday")
elif ask_user == 4:
    print("Today is " + "Thursday")
elif ask_user == 5:
    print("Today is " + "Friday")
elif ask_user == 6:
    print("Today is " + "Saturday")
else:
    print("I do not understand, please try again.")

