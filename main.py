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

# ===================================================================


# =========================== Создание поля =========================

# Поле с значениями
playground = [["❓"] * X_SIZE for i in range(Y_SIZE)]

# Поле игрока
player = [["❓"] * X_SIZE for i in range(Y_SIZE)]

# Создание мин
for i in range(MINES_COUNT):
    playground[random.randint(0, Y_SIZE - 1)][random.randint(0, X_SIZE - 1)] = "💣"

# Фунция проверки смежных клеток
def check(y, x):

    bomb_index = 0

    if playground[y][x] == "💣" : return "💣"

    # Проверка слева
    elif playground[y][x - 1] == "💣" : bomb_index +=1


    # Проверка слева снизу
    elif playground[y + 1][x - 1] == "💣" : bomb_index +=1


    # Проверка слева сверху
    elif playground[y ][x - 1] == "💣" : bomb_index +=1


    # Проверка слева
    elif playground[y][x - 1] == "💣" : bomb_index +=1

# Расстановка цифр
# ...


# =========================== Отрисовка ========================

# Функция отрисовки кадра
def draw_frame():
    os.system("cls")
    for y in range(Y_SIZE):
        for x in range(X_SIZE):
            print(playground[y][x], end=" ")
        print() # Перенос на новую строку

draw_frame()