#this is question 3.4.4.4-2

numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]

#a)
for element in range(len(numbers)):
    print(numbers[element])

#b)
for element in range(len(numbers)):
    print(numbers[element], numbers[element]**0.5)

#c) #help
total = 0

for element in range(len(numbers)):
    total2 = sum(numbers[element % len(numbers)])
    print(total2)

#d)

import math
print(math.prod(numbers))
