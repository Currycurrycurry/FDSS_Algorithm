def addTwoNumbers(num1, num2):
    while True:
        sum_num = num1 ^ num2
        carry_num = (num1 & num2) << 1
        num1 = sum_num
        num2 = carry_num
        if num2 == 0:
            return num1

print(addTwoNumbers(1, 10))
    




    