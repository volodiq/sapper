import keyboard
import random
import os

# =========================== Выбор сложности =========================
os.system("cls")

print("1 - для лопухов, 2 - для смешариков, 3 - для четких пацанов")

choose_dificulty = input("Выберите сложность: ")

match choose_dificulty:
    # Лопухи
    case "1":
        Y_SIZE = 8
        X_SIZE = 10
        MINES_COUNT = 63
    # Смешарики
    case "2":
        Y_SIZE = 13
        X_SIZE = 15
        MINES_COUNT = 20
    # Четкие пацанчики
    case "3":
        Y_SIZE = 17
        X_SIZE = 18
        MINES_COUNT = 30

# =========================== Создание поля =========================

# Поле с значениями
playground = [["?"] * X_SIZE for i in range(Y_SIZE)]

# Поле игрока
player = [["?"] * X_SIZE for i in range(Y_SIZE)]

# Создание мин
for i in range(MINES_COUNT):
    playground[random.randint(0, Y_SIZE - 1)][random.randint(0, X_SIZE - 1)] = "B"

# Фунция проверки смежных клеток
def check(y, x):

    bomb_index = 0

    if playground[y][x] == "B" : return "B"

    # Проверка слева
    if x > 0 : 
        if playground[y][x - 1] == "B" : bomb_index +=1

    # Проверка слева снизу
    if x > 0 :
        if y < Y_SIZE - 1: 
            if playground[y + 1][x - 1] == "B" : bomb_index +=1
    
    # Проверка слева сверху
    if x > 0 & y > 0 : 
        if playground[y - 1][x - 1] == "B" : bomb_index +=1

        # Проверка сверху
    if  y > 0 : 
        if playground[y - 1][x] == "B" : bomb_index +=1

    # Проверка снизу
    if y < Y_SIZE - 1 : 
        if playground[y + 1][x] == "B" : bomb_index +=1

    # Проверка справа 
    if x < X_SIZE - 1 : 
        if playground[y][x + 1] == "B" : bomb_index +=1

    # Проверка справа снизу 
    if x < X_SIZE - 1 & y < Y_SIZE - 1: 
        if playground[y - 1][x + 1] == "B" : bomb_index +=1

    # Проверка справа сверху
    if x > 0 & y > 0 : 
        if playground[y - 1][x + 1] == "B" : bomb_index +=1
    return (str(bomb_index))


# Расстановка цифр
for i in range(Y_SIZE):
    for j in range(X_SIZE):
        playground[i][j] = check(i , j)


# =========================== Отрисовка ========================

# Функция отрисовки кадра
def draw_frame():
    os.system("cls")
    for y in range(Y_SIZE):
        for x in range(X_SIZE):
            print(player[y][x], end=" ")
        print() # Перенос на новую строку

draw_frame()



# =========================== Выбор клеток ========================

x = 0 
y = 0



# лево
def left():
    global y
    global x
    if x > 0: x -= 1
    draw_frame()

# право 

def right():
    global y
    global x
    if x < X_SIZE: x += 1
    draw_frame()

# вниз

def down():
    global y    
    global x
    if y < Y_SIZE: y += 1
    draw_frame()

# вверх

def up():
    global y
    global x
    if y > 0 : y -= 1
    draw_frame()


keyboard.add_hotkey("w", up)

keyboard.add_hotkey("a", left)

keyboard.add_hotkey("s", down)

keyboard.add_hotkey("d", right)

def select():
    player[y][x] = playground[y][x]
    draw_frame()
keyboard.add_hotkey("e", select)


keyboard.wait("q")


