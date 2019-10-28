a = ('Hi', 5, True)
b = ('Bye', False, 14)
aa = set(a)
bb = set(b)
c = set.union(aa, bb)
c = set.intersection(aa, bb)
c = set.difference(aa, bb)
c = set.symmetric_difference(aa, bb)
print(set.issubset(aa, bb))
print(c)

# Создайте пустой словарь, заполните его элементами,
# удалите часть элементов, обратитесь к нескольким элементам
# и сделайте с ними какое-нибудь действие (5 баллов)

d = {}
d[0] = 'Hello'
d[1] = 5
d[2] = True
del d[0]
print(dict.items(d))
print(d[1], d[2])

# Проитерируйтесь по заданному вами словарю и выведите его
# ключи и элементы (какой способ кажется вам лучшим?)
# (5 баллов * число способов)

for i in range(len(d)):
    print(d)

# Создайте программу, принимающую на вход строку и выводящую,
# начинается ли строка с заглавной буквы, число букв в строке,
# заканчивается ли она на '!!', число встречаний строки 'fire',
# а также эту же строку, где все буквы большие, маленькие и вариант,
# в котором все слова начинаются с большой буквы (8 баллов)

a = input()
if a[0].isupper: #help.....
    print(a)
else:
    print(a, a)
print()
if a[-2] == '!!':
    print('Yes')
else:
    print('No')



#Напишите программу, принимающую на вход строку и
# выводящую с чего эта строка начинается
#(цифра, буква, пробел) (5 баллов)

a = input()
if a[0]

#Сконвертируйте список, кортеж, сэт и строку
# друг в друга всеми возможными способами
# (строка -> лист, строка -> кортеж, ...) (6 баллов)

a_list = list('Henlo')
print(a_list)
a_tuple = tuple(a_list)
print(a_tuple)
a_set = set(a_tuple)
print(a_set)
a_string = str(a_set)
print(a_string)
a_set = set(a_list)
print(a_set)
a_str = str(a_tuple)
print(a_str)

#Разверните строку всеми известными вам способами

s = 'agatacaca'

print(s[::-1])

rev = ''
for l in range(len(s)+1):
    rev += s[-l]
print(rev[1:])