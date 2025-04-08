number = int(input())

if (number % 2 == 0) and (number > 0):
    print("положительное четное число")
elif (number % 2 == 0) and (number < 0):
    print("отрицательное четное число")
elif number % 2 != 0:
    print("число не является четным")
else:
    print("нулевое")