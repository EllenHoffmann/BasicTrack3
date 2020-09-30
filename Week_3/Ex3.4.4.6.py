numbers = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]

for numbers in range(len(numbers)):
    if numbers >= 75:
        grade = "First"
    elif numbers == 75 > x >= 70:
        grade = "Upper Second"
    elif numbers == 70 > x >= 60:
        grade = "Second"
    elif numbers == 60 > x >= 50:
        grade = "Third"
    elif numbers == 50 > x >= 45:
        grade = "F1 Supp"
    elif numbers == 45 > x >= 40:
        grade = "F2"
    else:
        grade = "F3"

    print("Your mark is " + str(numbers) + ", which equals the grade " + grade)