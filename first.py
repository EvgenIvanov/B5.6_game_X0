## B5.6 крестики-нолики
## основная функция setBoard(iCol, workMode = 0)
## принимаетмые параметры:
#  iCol - задается размерность игрового поля
#  workMode - режим игры (0 - для тестирования, ходит компьютер / 1 - обычный режим)
#
import random
# размерность игрового поля
iCol = 3
# инициализация игрового поля
arrSteps = [[0] * iCol for i in range(iCol)]

def showBorder():
  for iRow in arrSteps:
    print(' '.join(['-' if not i else i for i in iRow])) #list(map(str,iRow))))
  print('======')

showBorder()

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

def checklList(list_):
  if list_.count(1) == 3 and len(list_):
    return True
  return False

def checkWinner(x, y, who):
  ## проверка победы игрока
  who = getPlayer(who)

  # проверка строки
  checkRow = [1 for i, x in enumerate(arrSteps[y]) if x == who ]
  if checklList(checkRow):
    return True

  # проверка колонки
  checkRow.clear()
  for i in range(3):
    if arrSteps[i][x] == who:
      checkRow.append(1)
  if checklList(checkRow):
    return True

  # проверка диагонали 0,0 - 2,2
  checkRow.clear()
  if (not x and not y) or (x == 2 and y == 2) or (x == 1 and y == 1):
    for i in range(3):
      if arrSteps[i][i] == who:
        checkRow.append(1)
  if checklList(checkRow):
    return True

  # проверка диагонали 0,2 - 2,0
  checkRow.clear()
  if (x == 2 and not y) or (not x and y == 2) or (x == 1 and y == 1):
    for i in range(3):
      if arrSteps[2-i][i] == who:
        checkRow.append(1)
  if checklList(checkRow):
    return True

  return False

def setBoard(iCol, workMode = 0):
  ## старт игры
  # iCol - размерность
  # workMode - режим работы функции (0-тестирование / 1-игра)
  if not workMode:
    workMode = getRandomXY
  else:
    workMode = getUserXY
  # определяем кто первый ходит (1 - нолик, 0 - крестик)
  who = bool(random.randint(0, 1))
  has_winner = False

  for step in range(0, 9):
    isFree = True
    while isFree:
      x, y = workMode(iCol, who)
      if not arrSteps[y][x]:
        arrSteps[y][x] = getPlayer(who) #(not who)
        if step > 3:
          has_winner = checkWinner(x, y, who) #not who)
        isFree = False

    if step > 3:
      print(f'шаг {step + 1}')

    showBorder()

    if has_winner:
      print(f'Поздравляем!\nВыиграл игок {getPlayer(who)}\nGame OVER!')
      break
    who = not who
  if not has_winner:
    print('0:0 ничья')
setBoard(iCol, 12)