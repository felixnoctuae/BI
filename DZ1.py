import math

# Напишите по 5 преобразований из целых чисел в дробные,
# из дробных в целые, из каждого из этих типов в строку и наоборот (5 баллов)
# В данных заданиях ввод с помощью input, вывод ответа с помощью print


a =[]
for i in range(5):
    a.append(input())
    print(float(a[i]))
    print(int(float(a[i])))
    print(str(int(float(a[i]))))
    print(int(str(int(float(a[i])))))
    print(float(int(str(int(float(a[i]))))))


# Выберите 3 формулы (математические/физические, какие угодно)
# и имлементируйте их, приведите 3 примера вычисления с их помощью (9 баллов)


m = int(input())
c = 349000
E = m*c*c
print('E = mc^2; E =', E)

m = int(input())
g = 10
F = m*g
print('F = mg; F =', F)

a = int(input('Введите длину короткого катета '))
b = int(input('Введите длину длинного катета '))
c = math.sqrt((a*a)+(b*b))
print('c^2 = a^2 + b^2; c =', c)


# Выведите таблицы истинности для
# not

print('   | A')
print(' 1 | 0')
print(' 0 | 1')

# or

print('AB | 0 | 1')
print(' 0 | 0 | 1')
print(' 1 | 1 | 1')

# xor

print('AB | 0 | 1')
print(' 0 | 0 | 1')
print(' 1 | 1 | 0')

# nor

print('AB | 0 | 1')
print(' 0 | 1 | 0')
print(' 1 | 0 | 0')

# and

print('AB | 0 | 1')
print(' 0 | 0 | 0')
print(' 1 | 0 | 1')

# nand

print('AB | 0 | 1')
print(' 0 | 1 | 1')
print(' 1 | 1 | 0')

# (15 баллов)

# Вариация старой задачки fizzbuzz - сделайте программу,
# на вход которой поступает целое число, если это число
# делится на 3 выводится fizz, если на 5 - buzz,
# а если на 15 - fizzbuzz. Если не делится нацело
# ни на одно из них, выведите это же число (8 баллов)

n = input()
a = int(n)
if a%15 == 0:
    print('fizzbuzz')
elif a%5 == 0:
    print('buzz')
elif a%3 == 0:
    print('fizz')
else: print(a)