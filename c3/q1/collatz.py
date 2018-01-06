try:
    number = int(input("Enter number:"))
    while True:
        if number % 2 == 0:
            number = number // 2
        else:
            number = 3 * number + 1
        print(number)
        if number == 1:
            break
except ValueError as ve:
    print("必须传入一个整数：" + str(ve))
