## B5.6 крестики-нолики
import random
# размерность игрового поля
iCol = 3
# инициализация игрового поля
arrSteps = [[0] * iCol for i in range(iCol)]
# arrSteps = [['X',0,0],[0,'X',0],[0,0,'X']]
print(arrSteps)

def showBorder():
  for iRow in arrSteps:
    print(' '.join(['-' if not i else i for i in iRow])) #list(map(str,iRow))))
  print('======')

def getPlayer(who):
  # по значению bool(who) возвращаем строковое значение
  if not who:
    res = 'X'
  else:
    res = 'O'
  return res

def getRandomXY(max_, who):
  # возращаяем random значения координат
  x = random.randint(0, max_-1)
  y = random.randint(0, max_-1)
  return x, y

def inputCoord(coord, max_):
  # обработка пользовательского ввода
  while True:
    try:
      num = int(input(f'Введите координату {coord} от 1 до {max_}: ')) - 1
    except ValueError:
      print(f'Значение {num} неверно. Повторите ввод.')
      num = -1
    if -1 < num <= max_:
      break
    else:
      print(f'Значение {num} должно быть в диапазоне от 1 до {max_} включительно. Повторите ввод.')
  return num

def getUserXY(max_, who):
  # ввод координат пользователем
  # max_ - максимальное значение (type int)
  # who - первый игрок bool(who)
  print(f'Ходит игрок "{getPlayer(who)}"')
  x = inputCoord('X', max_)
  y = inputCoord('Y', max_)
  return x, y

def checkWinner(x, y, who):
  ## проверка победы игрока
  who = getPlayer(who)

  # проверка строки
  checkRow = [1 for i, x in enumerate(arrSteps[y]) if x == who ]
  if checkRow.count(1) == 3 and any(checkRow):
    return True

  # проверка колонки
  checkRow.clear()
  for i in range(3):
    if arrSteps[i][x] == who:
      checkRow.append(1)
  if checkRow.count(1) == 3 and len(checkRow):
    return True

  # проверка диагонали 0,0 - 2,2
  checkRow.clear()
  if (not x and not y) or (x == 2 and y == 2) or (x == 1 and y == 1):
    for i in range(3):
      if arrSteps[i][i] == who:
        checkRow.append(1)
  if checkRow.count(1) == 3 and len(checkRow):
      return True

  # проверка диагонали 0,2 - 2,0
  checkRow.clear()
  if (x == 2 and not y) or (not x and y == 2) or (x == 1 and y == 1):
    for i in range(3):
      if arrSteps[2-i][i] == who:
        checkRow.append(1)
  if checkRow.count(1) == 3 and len(checkRow):
      return True

  return False

## карта ходов для тестирования
def setBoard(iCol, workMode = 0):
  # определяем кто первый ходит (1 - нолик, 0 - крестик)
  if not workMode:
    workMode = getRandomXY
  else:
    workMode = getUserXY

  who = bool(random.randint(0, 1))
  has_winner = False


  for step in range(0, 9):

    isFree = True
    while isFree:
      x, y = workMode(iCol, who)
      showBorder()
      if not arrSteps[y][x]:
        if not step % 2:
          arrSteps[y][x] = getPlayer(not who)
          has_winner = checkWinner(x, y, not who)
        else:
          arrSteps[y][x] = getPlayer(who)
          has_winner = checkWinner(x, y, who)
        isFree = False

    if step > 3:
      print(f'шаг {step + 1}')

    showBorder()

    if has_winner:
      str_ = 'Поздравляем!\nВыиграл игок '
      if not step % 2:
        str_ += getPlayer(not who)
      else:
        str_ += getPlayer(who)
      str_ += '\nGame OVER!'
      print(str_)
      break
  if not has_winner:
    print('0:0 ничья')
setBoard(iCol, 0)

# show_border()


# print(arrSteps)
# print(all(arrSteps[0]))
# print(all(arrSteps[1]))
# print(all(arrSteps[2]))
# arrBoard = [[0] * iCol for i in range(iCol)]
# def set_board(iCol):
#   for i in range(iCol):
#     for j in range(iCol):
#       print()
#       if not random.randint(0,1):
#         arrBoard[i][j] = [1,'']
#       else:
#         arrBoard[i][j] = ['',1]
# set_board(iCol)
# print(arrBoard)
# arrBoard = [
#             [[0,1],[0,1],[0,1]],
#             [[0,1],[0,1],[0,1]],
#             [[0,1],[0,1],[0,1]]
#            ]
# def get_layer(player=0):
#   for row in range(3):
#     str_ = ''
#     for col in arrBoard[row]:
#       str_ += str(col[player])
#     print(str_)
#     # str_ = list(map(str,arrBoard[row]))
#     # print(''.join(str_))
# get_layer()

# def print_row(row=0):
#   if not row:
#     # for item in [' ', 0, 1, 2]:
#     print(' 0123')
#   else:
#     print(row)
# def print_board():
#   print_row()
#   for item in range(2):
#     print(print_row(str(item)))

# print_board()
# print({chr(a):a for a in range (20,128)})


## B5.4.5 Вывести длину каждого элемента в списке
# a = ["asd", "bbd", "ddfa", "mcsa"]
# print(map(lambda x: len(x), a)) #map(len(str),a))
# print(list(map(len, a)))
# print(list(map(str.upper, a)))

## B5.5.4 сортировка по результату функции
# (вес, рост) масса тела в кг деланная на рост в метрах в квадрате
# data = [
#    (82, 191),
#    (68, 174),
#    (90, 189),
#    (73, 179),
#    (76, 184)
# ]
# print(min(data, key = lambda x: x[0] / ((x[1] / 100) ** 2)))

## B5.5.3 сортировка по результату функции
# (вес, рост) масса тела в кг деланная на рост в метрах в квадрате
# data = [
#    (82, 191),
#    (68, 174),
#    (90, 189),
#    (73, 179),
#    (76, 184)
# ]
# print(sorted(data, key = lambda x: x[0] / ((x[1] / 100) ** 2)))

## использование filter
# def get_only_even_number(number):
#   return number % 2 == 0
#
# result = filter(get_only_even_number,[-2, -1, 0, 1, -3, 2, -3])
# print(list(result))

## использование map
# L = ['THIS', 'IS', 'LOWER', 'STRING']
# print(list(map(str.lower, L)))

## типа авторизация для доступа к БД
# B5.4.15
# USERS = ['admin','guest','director','root','superstar']

# yesno = input("""Введите Y, если хотите авторизироваться или N, \n если хотите продолжить работу как анонимный пользователь => """).lower()
#
# auth = yesno == 'y'
#
# if auth:
#   username = input('Введите ваш username: => ')
#
# def has_access(func):
#   def wrapper():

#     if username in USERS:
#       print('Есть такой пользователь')
#       func()
#     else:
#       print('user name not found')
#   return wrapper
#
# def is_auth(func):
#   def wrapper():
#     if auth:
#       print('Пользователь авторизирован')
#       func()
#     else:
#       print('Пользователь неавторизирован. Функция выполнена не будет')
#   return wrapper
#
# @is_auth
# @has_access
# def from_db():
#   print('some data from database')
#
# from_db()

## исключение StopIteration
# iter_obj = iter('hello!!!!!')
# for i in range(100):
#   print(next(iter_obj))

## B5.4.13
# вычисление числа e (2.7181652432261854)
## e_n = (1 + 1/n)**n
# def e():
#   n = 1
#   while n < 110000:
#     yield (1 + 1 / n) ** n
#     n += 1
# last = 0
# for a in e(): # e() - генератор
#   if (a - last) < 0.00000001:
#     print(a)
#     break
#   else:
#     last = a


## B5.4.11
# реализовать рекурсивную функцию equal(N, S), проверяющую, совпадает ли сумма цифр числа N с числом S.
# При написании программы следует обратить внимание на то, что, если S стала отрицательной, то необходимо сразу вернуть False.
# N = 123
# S = 7
# def equal(N, S):
#   if S < 0:
#     return False
#   if N < 10:
#     return N == S
#   return equal(N // 10, S - N % 10)
# print(equal(N, S))
#№ разворот числа зеркально B5.4.10
# num = 123456789
# def mirror(a, res=0):
#     return mirror(a // 10, res*10 + a % 10) if a else res
# print(mirror(num))
# str_ = ""
# print(n,type(n),"    ",n[:-1])
# # for i in n[::-1]:
# #   str_ += i
# def rev(s):
#   if len(s) == 0:
#     return ""
#   return str_+rev(s[:-1])
# print(rev(n))
# def reverse_num(n):
  # return n.reverse

# reverse_num(num)

# # нахождение наименьшего числа в списке (массиве)
# def min_list(L):
#     if len(L) == 1:
#         return L[0]
#     return L[0] if L[0] < min_list(L[1:]) else min_list(L[1:])
# print(min_list(L))

# mm = ""
# def mmin(l):
#   nonlocal mm
#   if not len(l):
#     return mm
#   else:
#     if l[-1] < mm:
#       mm = l[-1]
#   return mmin(l[-1])
# m = mmin(list_)
# print(f"минимальный элемент: {m}")

# def quadratic_solve(a, b, c):
#   return f"a = {a}, b = {b}, c = {c}"
#
# M = {'b' : 0,
#      'c' : -1,
#      'a' : 1
#     }
#
# print(quadratic_solve(**M))
# print(quadratic_solve(*M.values()))

# # решаем квадратное уравнение
# # a*x**2 + b*x + c = 0
# def discriminant(a, b, c):
#   return b**2 - 4*a*c

# def quadratic_solve(a,b,c):
#   d_ = discriminant(a, b, c)
#   if d_ < 0:
#     return 'Нет вещественных корней'
#   elif not d_:
#     return -b/(2*a)
#   else:
#     return (-b-d_**0.5)/(2*a), (-b+d_**0.5)/(2*a)

# result = quadratic_solve(1, 5, 4)
# print(result,type(result))
# функция деления
#  def linear_solve(a, b):
#   if a:
#     return b/a
#   elif not a and not b:
#     print('бесконечное число кореней')
#   else:
#     return 'нет корней'
# print(linear_solve(0, 0))

# text = "aaabbccccdaa"
# t_list = []
# current_chr = ""
# for char in text:
#   if current_chr != char:
#     if current_chr:
#       t_list.append(dict_)
#     current_chr = char
#     dict_ = {char: 1}
#   else:
#     dict_[char] += 1
# t_list.append(dict_)
#   #print(char)
# # index = 0
# # t_list = []
# # current_chr = ""
# # while index < len(str_)-1:
# #

# #   index = index + 1
# #t_list = [{'a':'3'},{'b':'2'}]
# print(t_list, type(t_list))
# str_ = ""
# for item in t_list:
#   print(item, type(item))
#   for key, val in item.items():
#     str_ = str_ + key + str(val)

# print(str_)


# dict_ = {}
# n =[{i} for i in str]
# print(n)
# print(list(str))

# L = [i for i in range(10)]
# # 0 1 2 3 4 5 6 7 8 9
# M = [i for i in range(10,0,-1)]
# # 10 9 8 7 6 5 4 3 2 1
# for a, b in zip(L,M):
# #  print('a =', a, 'b =', b)
#   print(a*b)

# N = [a * b for a,b in zip(L,M)]
# print(N,type(N))

# L = [int(input()) % 2 == 0 for i in range(5)]
# print(L)
# # print(any[L] and not all[L])

# таблица умножения
#table = [[i * j] for j in range(1,11) for i in range(1,11)]
#print(table)

# a = list(map(int,input().split()))
# print(not any(a))
# a = int(input('numb: '))

# if type(a) == int and 100 <= a <= 999 and a % 2 == 0 and a % 3 == 0:
#     print('число удовлетворяет условиям')
# if all([type(a) == int,
#        100 <= a <= 999,
#        a % 2 == 0,
#        a % 3 == 0]):
#     print('число удовлетворяет условиям')
# if any([type(a) == int,
#        100 <= a <= 999,
#        a % 2 == 0,
#        a % 3 == 0]):
#     print('число удовлетворяет условиям')

# a = ''
# b = False
# if a and b:
#     print("Обе переменные истинные")
#     print(a,b)
# elif a or b:
#     print("Одна из переменных истинная")
#     print(a or b) # печать значения одной переменной, которая является истинной
# else:
#     print("обе переменных ложны")

#  a = '' # пустая строка
# b = a or 1
# print(b,type(b),'  ',a, type(a))
# a = input("Введите первую строку: ")
# b = input("Введите вторую строку: ")

# print(a.split(' '), b.split(' '))
# a_set, b_set = set(a.split(' ')), set(b.split(' ')) # используем множественное присваивание

# a_and_b = a_set.symmetric_difference(b_set)
# print(a_set,b_set)
# print(a_and_b)

# a_set = set(list(input("1: ")))
# b_set = set(list(input("2: ")))
# print(a_set)
# print(b_set)
# print(' '.join(a_set.difference(b_set)))
# abons = {"Иванов", "Петров", "Васильев", "Антонов"}

# debtors = {"Петров", "Антонов", "Сидоров"}

# non_debtors = abons.difference(debtors)

# print("оюъединение ", abons.union(debtors))
# print("пересечение ", abons.intersection(debtors))
# print("разность ", abons.difference(debtors))
# print("симметричная разность ", abons.symmetric_difference(debtors))

# def my_shiny_new_decorator(function_to_decorate):
#   def the_wrapper_around_the_original_function():
#     print("Я - код, который отработает до вызова функции")
#     function_to_decorate() # Сама функция
#     print("А я - код, срабатывающий после")
#   return the_wrapper_around_the_original_function

# #@my_shiny_new_decorator
# def stand_alone_function():
#   print("Я простая одинокая функция, ты ведь не посмеешь меня изменять?")

# stand_alone_function()

# stand_alone_function_decorated = my_shiny_new_decorator(stand_alone_function)
# stand_alone_function_decorated()

# @my_shiny_new_decorator
# def another_stand_alone_function():
#   print("Оставь меня в покое")

# another_stand_alone_function()

# import sys
# def f_decor(func):
#   dict_ = {}
#   def wrapper(n):
#     nonlocal dict_
#     if n not in dict_:
#       dict_[n] = func(n)
#       print(f"Добавление ключа {n} со значением {dict_[n]}")
#     else:
#       print(f"Ипользование сохраненного ключа {n} со значением {dict_[n]}")
#     print(f"Словарь: {dict_}")
#     return dict_[n]
#   return wrapper

# @f_decor
# def f_calc(n):
#   return n * 123456789

#  f_calc(1)
#  f_calc(2)
#  f_calc(1)

# import time
# def decorator_time(fn_name):
#   count = 0
#   def wrapper():
#     nonlocal count
#     print(f"Запустилась функция {fn_name}")
#     t0 = time.time()
#     result = fn_name()
#     dt = time.time() - t0
#     print(f"Функция выполнилась. Время {dt:.10f}")
#     count += 1
#     print(f"функция была вызвана {count} раз")
#     return dt
#   return wrapper
#
# def pow_2():
#   return 10000000 ** 2
#
# def in_build_pow():
#   return pow(10000000,2)
#
# pow_2 = decorator_time(pow_2)
# in_build_pow = decorator_time(in_build_pow)
#
# #var_1 = pow_2()
# #print(var_1)
# time_work_pow_2, time_work_ibp = 0, 0
# for i in range(5):
#   time_work_pow_2 += pow_2()
#   time_work_ibp += in_build_pow()
# print(f"avg(time_work_pow_2) =  {time_work_pow_2/100:.10f}")
# print(f"avg(time_work_ibp) = {time_work_ibp/100:.10f}")

# import sys
# def repeat_list(list_):
#    list_values = list_.copy()
#    while True:
#        value = list_values.pop(0)
#        list_values.append(value)
#        yield value

# for i in repeat_list([1, 2, 3]):
#    print(i)
# print(' '.join(var))
# def generator()
  # yield

# def num_nature(n_start=1, n_trace=1):
#   counter = n_start
#   while True:
#     yield counter
#     n_start += n_trace
# for num in num_nature():
#   print(num)

# def fib():
#   a, b = 0, 1
#   yield a
#   yield b
#   while True:
#     a, b = b, b + a
#     yield b
# for num in fib():
#   print(num)

# var = 123
# def f_rec(n):
#   if n < 10:
#     return n
#   else:
#     return n % 10 + f_rec(n//10)
# print(f_rec(var))

# def sum_recurse(str_):
#   if len(str_) == 0:
#     return ""
#   else :
#     return str_[-1] + sum_recurse(str_[:-1]) #str[n - 1]#n + sum_recurse(n - 1)
# print(sum_recurse("qwerty"))
# print('qwerty'[:-1])
# def multiply(*nums):
#   if not nums:
#     result = 0
#   elif len(nums) == 1:
#     result = nums[0]
#   else:
#     result = 1
#     for i in nums:
#       result *= i
#   return result

# print(multiply(2,3,4))

# def get_mul_func(m):
#    nonlocal_m = m
#    def local_mul(n):
#        return n * nonlocal_m

#    return local_mul

# two_mul = get_mul_func(3)  # возвращаем функцию, которая будет умножать числа на 2
# print(two_mul(5))  # 5 * 2
# def check_palindrome(text, b='ola-la'):
#   text = text.lower()
#   text = text.replace(' ','')
#   return str(text == text[::-1]) +' '+ b
# text = 'test'
# print('"',text,'" isPalindrome? - ',check_palindrome(text))
# text = 'Кит на море не романтик'
# print('"',text,'" isPalindrome? - ',check_palindrome(text,' bla-bla'))
# def consider(val):
#   count = 0
#   for i in range(1, val + 1):
#     if val % i == 0:
#       print(val,'%',i,'=',i)
#       count += 1
#   return count
# print(consider(5))
# print(consider(4))
# def print_pine(cnt):
#   while cnt>0:
#     print("*" * cnt)
#     cnt -= 1

# print_pine(4)
# print()
# print_pine(5)
# def print_2_add_2():
#   print(2+2)

# print_2_add_2()
# heads = 35  # количество голов
# legs = 94  # количество ног

# for r in range(heads + 1):  # количество кроликов
#     for ph in range(heads + 1):  # количество фазанов
#         #  если суммарное количество голов превышено или ног превышено, то переходим на следующий шаг цикла
#         if (r + ph) > heads or \
#             (r * 4 + ph * 2) > legs:
#             continue
#         if (r + ph) == heads and (r * 4 + ph * 2) == legs:
#             print("Количество кроликов", r)
#             print("Количество фазанов", ph)
#             print("---")
# n = int(input("введите число: "))
# iter = 0
# while True:
#   if n % 2 == 0:
#     n = n // 2
#   else:
#     n = (n * 3 + 1) // 2
#   print('n=',n)
#   if n == 1:
#     break
#   iter += 1
#   if iter > 1000:
#     break
# print("--  end  --")

# text = """
# У лукоморья дуб зелёный;
# Златая цепь на дубе том:
# И днём и ночью кот учёный
# Всё ходит по цепи кругом;
# Идёт направо -- песнь заводит,
# Налево -- сказку говорит.
# Там чудеса: там леший бродит,
# Русалка на ветвях сидит;
# Там на неведомых дорожках
# Следы невиданных зверей;
# Избушка там на курьих ножках
# Стоит без окон, без дверей;
# Там лес и дол видений полны;
# Там о заре прихлынут волны
# На брег песчаный и пустой,
# И тридцать витязей прекрасных
# Чредой из вод выходят ясных,
# И с ними дядька их морской;
# Там королевич мимоходом
# Пленяет грозного царя;
# Там в облаках перед народом
# Через леса, через моря
# Колдун несёт богатыря;
# В темнице там царевна тужит,
# А бурый волк ей верно служит;
# Там ступа с Бабою Ягой
# Идёт, бредёт сама собой,
# Там царь Кащей над златом чахнет;
# Там русский дух... там Русью пахнет!
# И там я был, и мёд я пил;
# У моря видел дуб зелёный;
# Под ним сидел, и кот учёный
# Свои мне сказки говорил.
# """

# text = text.lower()
# text = text.replace(" ", "")
# text = text.replace("\n", "")
# print(text)
# count = {}  # для подсчета символов и их количества
# for char in text: # цикл по символам строки
#    if char in count:  # если символ уже встречался, то увеличиваем его количество на 1
#        count[char] += 1
#    else:
#        count[char] = 1
# for char, cnt in count.items():
#    print(f"Символ {char} встречается {cnt} раз")
# list_ = [-5, 2, 4, 8, 12, -7, 5]
# # Объявим переменную, в которой будем хранить индекс отрицательного элемента
# index_negative = None

# for i,value in enumerate(list_): # range(len(list_)):
#     if value < 0:
#         print("Отрицательное число: ", value)
#         index_negative = i  # перезаписываем значение индекса
#         print("Новый индекс отрицательного числа: ", index_negative)
#     else:
#         print("Положительное число: ", value)
#     print("---")
# print("Конец цикла")
# print()
# print("Ответ: индекс последнего отрицательного элемента = ", index_negative)
# random_matrix = [
#    [9, 2, 1],
#    [2, 5, 3],
#    [4, 8, 5]
# ]

# mean_value_rows = []  # здесь будут храниться средние значения для каждой строки
# min_value_rows = []  # здесь будут храниться минимальные значения для каждой строки
# min_index_rows = []  # здесь будут храниться индексы минимальных значений для каждой строки
# max_value_rows = []  # здесь будут храниться максимальные значения для каждой строки
# max_index_rows = []  # здесь будут храниться индексы максимальных значений для каждой строки

# for row in random_matrix:  # здесь мы целиком берем каждую сроку
#    min_index = 0  # в качестве минимального значения возьмем первый элемент строки
#    max_index = 0
#    min_value = row[min_index]  # начальное минимальное значение для каждой строки будет новое
#    max_value = row[max_index]  # для максимального значения тоже самое
#    for index_col in range(len(row)):
#        if row[index_col] < min_value:
#            min_value = row[index_col]
#            min_index = index_col
#        if row[index_col] > max_value:
#            max_value = row[index_col]
#            max_index = index_col
#    min_value_rows.append(min_value)
#    min_index_rows.append(min_index)
#    max_value_rows.append(max_value)
#    max_index_rows.append(max_index)

# print(min_value_rows)
# print(min_index_rows)
# print(max_value_rows)
# print(max_index_rows)
# S = 1  # заводим переменную счетчик, в которой мы будем считать сумму
# n = 1  # текущее натуральное число

# # заводим цикл while, который будет работать пока сумма не превысит 500
# while True:  # делай пока ...
#   # n**2 >= 1000:
#   print(n)
#   n += 1
#   if n**2 > 999:
#     break
# S = 1  # заводим переменную счетчик, в которой мы будем считать сумму
# N = 5
# # ss = 0
# # заводим цикл for в котором мы будем проходить по всем числам от одного до N
# print(N,chr(10))
# for i in range(1,N+1):  # равносильно выражению for i in [1, 2, 3, ... , N -1, N]:
#   print('*'*i)
# print("Конец цикла")
# pr÷int()
# print("Ответ: сумма равна = ", S)
# x = 12344321
# x_str = str(x)
# print(str(x) == str(x)[::-1])
# words = ['hello', 'daddy', 'hello', 'mum']
# hello = set(list('hello'))
# word = set(list('word'))
# print(hello)
# print(type(hello))
# print(word.difference(hello))
# print(len(words) == len(set(words)))
# login_list = [
#    'root',
#    'username1'
#    ]

# password_list = {
#    'root': '1q2w3e4r',
#    'username1': 'qwerty123'
# }

# username = input('Введите логин:\n')

# if username in login_list:
#   password = input("Введите пароль:"+chr(10))
#   if password_list[username] == password:
#     print("вход разрешен")
#   else:
#     print("запрет входа")
# else:
#     print("неверный логин")
# sys.exit
# wind = int(input("введитe скорость ветра: "))
# #y = int(input("введите y: "))
# if 1 <= wind <=4:
#   print("слабый")
# if 5 <= wind <=10:
#   print("умеренный")
# if 11 <= wind <= 18:
#   print("сильный")
# if wind >= 19:
#   print("ураганный")

# book_name = input("введите название книги: ")
# book_autor = input("введите автора книги: ")
# book_year = int(input("введите год выпуска книги: "))

# d = { "name": book_name
#     , "autor": book_autor
#     , "year": book_year}

# print(d)

# все операции - деление строки по пробелам, преобразование к числам
# и приведение объекта map к типу список, можно делать в одной строке
# L = list(map(float, input().split()))

# обмениваем первое и последнее число
# с помощью множественного присваивания
# L[0], L[-1] = L[-1], L[0]

# находим сумму и добавляем ее в конец списка
# L.append(sum(L))

# print(L)
# string = input("Введите числа через пробел:")
# list_of_strings = string.split() # список строковых представлений чисел
# list_of_numbers = list(map(int, list_of_strings)) # cписок чисел
# temp_items = list_of_numbers[0]
# list_of_numbers[0] = list_of_numbers[-1]
# list_of_numbers[-1] = temp_items
# print(list_of_numbers)
# list_of_numbers.append(sum(list_of_numbers)) # sum() вычисляет сумму элементов списка
# print(list_of_numbers)

# print('1 1 2 3 5 8 13 21 34 55')
# L = ['3.3', '4.4', '5.5', '6.6']
# print (list (map ( float , L)))
# L = ["а", "б", "в", 1, 2, 3, 4]
# print(L[1:4])
# print(L[::3])
# print(L[3::-1])
# print(L[:3:-1])
# hours = 3
# minutes = 30
# seconds = 3
# print("%02d:%02d:%02d" % (hours, minutes, seconds))
#print(sys.prefix)
#print (round(3.14159**2/2))
# pi = 31.4159265
# print ("%.4e" % (pi))
# a = input().split()
# n = chr(10).join(a)
# print(n)
# for ch in a:
#   print(ch)

# first_name = input("Введите ваше имя:")
# last_name = input("Введите вашу фамилию:")
# age = input("Введите ваш возраст:")
# city = input("Введите город проживания:")

# Выводим пустую строку
# print("")

# # Выводим приветствие, подставляя имя и фамилию пользователя,
# # которые он ввел с клавиатуры
# print("Привет,", first_name, last_name, "!")

# # Выводим пустую строку
# print("")

# # Выводим фиксированный текст для удобства просмотра
# print("Ваш профиль:")

# # Выводим возраст и город, которые указал пользователь
# print("Возраст:", age)
# print("Город:", city)