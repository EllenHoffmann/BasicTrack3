Start_of_trip = float(input("Assume the days of the week are numbered 0 (Sunday) to 6 (Saturday). On which day are you leaving for holidays?"))
Length_of_trip = float(input("How many nights are you going to be away?"))

if Start_of_trip == 0:
    print("You are leaving on "+"Sunday")
elif Start_of_trip == 1:
    print("You are leaving on "+"Monday")
elif Start_of_trip == 2:
    print("You are leaving on " + "Tuesday")
elif Start_of_trip == 3:
    print("You are leaving on " + "Wednesday")
elif Start_of_trip == 4:
    print("You are leaving on " + "Thursday")
elif Start_of_trip == 5:
    print("You are leaving on " + "Friday")
elif Start_of_trip == 6:
    print("You are leaving on " + "Saturday")

Weekday_end = print((Length_of_trip)%7)
#how can I say, "if it surpasses 6, start over at 0?