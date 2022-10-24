from random import randint
a = int(input("Введите степень k: "))

lst = []
for i in range(1, a +2):
    lst.append(randint(-100, 101))
    symbol = randint(0, 1)

equation = []

for i in range(len(lst)):
    if a == 0:
       equation.append(f'{lst[i]}')
    elif a == 1:
        equation.append(f'{lst[i]}*x')
    else:
        equation.append(f'{lst[i]}*x^{a}')

    if symbol == 1:
        equation.append('+')
    elif symbol == 0:
        equation.append('-')
    a -= 1

equation.append('=0')
equation.pop(-2)


file = open('file.txt', 'w')
file.write(''.join(equation))
result=''.join(equation).replace('+-','-').replace('--','+')
print(result)
