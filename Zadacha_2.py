num = int(input("Введите число: "))
lst = []
nut = num
i = 2
while i <= num:
    if num % i == 0:
        lst.append(i)
        num //= i
    else:
        i += 1
print(f'простые множители числа {nut} :{lst}')



