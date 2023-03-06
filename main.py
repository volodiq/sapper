import keyboard
import random
import time
import os


# =========================== Коды цветов =====================================

unselected_no  = "\033[1m\033[33m" + "?" # Не выбранная, неоткрытая клетка
selected_no    = "\033[1m\033[35m" + "?" # Не выбранная, неоткрытая клетка

unselected_nil = "\033[1m\033[32m" + "0" # Не выбранная клетка без мин в округе
selected_nil   = "\033[1m\033[35m" + "0" # Выбранная клетка без мин в округе

unselected_one = "\033[1m\033[34m" + "1" # Не выбранная клетка с 1 миной в округе
selected_one   = "\033[1m\033[35m" + "1" # Выбранная клетка с 1 миной в округе

unselected_two = "\033[1m\033[36m" + "2" # Не выбранная клетка с 2 минами в округе
selected_two   = "\033[1m\033[35m" + "2" # Выбранная клетка с 2 минами в округе

unselected_thr = "\033[1m\033[31m" + "3" # Не выбранная клетка с 3 минами в округе
selected_thr   = "\033[1m\033[35m" + "3" # Выбранная клетка с 3 минами в округе

unselected_fou = "\033[1m\033[31m" + "4" # Не выбранная клетка с 4 минами в округе
selected_fou   = "\033[1m\033[35m" + "4" # Выбранная клетка с 4 минами в округе

unselected_fiv = "\033[1m\033[31m" + "5" # Не выбранная клетка с 5 минами в округе
selected_fiv   = "\033[1m\033[35m" + "5" # Выбранная клетка с 5 минами в округе

unselected_six = "\033[1m\033[31m" + "6" # Не выбранная клетка с 6 минами в округе
selected_six   = "\033[1m\033[35m" + "6" # Выбранная клетка с 6 минами в округе

unselected_sev = "\033[1m\033[31m" + "7" # Не выбранная клетка с 4 минами в округе
selected_sev   = "\033[1m\033[35m" + "7" # Выбранная клетка с 4 минами в округе

unselected_eig = "\033[1m\033[31m" + "8" # Не выбранная клетка с 8 минами в округе
selected_eig   = "\033[1m\033[35m" + "8" # Выбранная клетка с 8 минами в округе

mine           = "\033[1m\033[37m" + "B" # Выбранная клетка с 8 минами в округе

frame          = "\033[1m\033[30m" + "=" # Выбранная клетка с 8 минами в округе

game_over      = "\033[1m\033[31m" + "Game Over"

print(unselected_no)
os.system("cls")

# =========================== Выбор сложности =========================


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
playground = [[unselected_no] * X_SIZE for i in range(Y_SIZE)]

# Поле игрока
player = [[unselected_no] * X_SIZE for i in range(Y_SIZE)]

# Создание мин
for i in range(MINES_COUNT):
    playground[random.randint(0, Y_SIZE - 1)][random.randint(0, X_SIZE - 1)] = mine

# Фунция проверки смежных клеток
def check(y, x):

    bomb_index = 0

    if playground[y][x] == mine : return mine

    # Проверка слева
    if x > 0 : 
        if playground[y][x - 1] == mine : bomb_index +=1

    # Проверка слева снизу
    if x > 0 :
        if y < Y_SIZE - 1: 
            if playground[y + 1][x - 1] == mine : bomb_index +=1
    
    # Проверка слева сверху
    if x > 0 & y > 0 : 
        if playground[y - 1][x - 1] == mine : bomb_index +=1

        # Проверка сверху
    if  y > 0 : 
        if playground[y - 1][x] == mine : bomb_index +=1

    # Проверка снизу
    if y < Y_SIZE - 1 : 
        if playground[y + 1][x] == mine : bomb_index +=1

    # Проверка справа 
    if x < X_SIZE - 1 : 
        if playground[y][x + 1] == mine : bomb_index +=1

    # Проверка справа снизу 
    if x < X_SIZE - 1 & y < Y_SIZE - 1: 
        if playground[y - 1][x + 1] == mine : bomb_index +=1

    # Проверка справа сверху
    if x > 0 & y > 0 : 
        if playground[y - 1][x + 1] == mine : bomb_index +=1

    match bomb_index:
        case 0: return unselected_nil
        case 1: return unselected_one
        case 2: return unselected_two
        case 3: return unselected_thr
        case 4: return unselected_fou
        case 5: return unselected_fiv
        case 6: return unselected_six
        case 7: return unselected_sev
        case 8: return unselected_eig

#Функция для открытия нулей
local_x = 0
local_y = 0
def open_nulls(y, x):
    global local_y, local_x
    # Проверка слева
    if x > 0 : 
        if playground[y][x - 1] == unselected_nil : open_nulls(local_y, local_x - 1)

    # Проверка слева снизу
    if x > 0 :
        if y < Y_SIZE - 1: 
            if playground[y + 1][x - 1] == unselected_nil : open_nulls(local_y , local_x - 1)

    # Проверка слева сверху
    if x > 0 & y > 0 : 
        if playground[y - 1][x - 1] == unselected_nil : open_nulls(local_y - 1 , local_x - 1)

        # Проверка сверху
    if  y > 0 : 
        if playground[y - 1][x] == unselected_nil : open_nulls(local_y - 1 , local_x)

    # Проверка снизу
    if y < Y_SIZE - 1 : 
        if playground[y + 1][x] == unselected_nil : open_nulls(local_y + 1 , local_x)

    # Проверка справа 
    if x < X_SIZE - 1 : 
        if playground[y][x + 1] == unselected_nil: open_nulls(local_y , x + local_1)

    # Проверка справа снизу 
    if x < X_SIZE - 1 & y < Y_SIZE - 1: 
        if playground[y - 1][x + 1] == unselected_nil : open_nulls(local_y - 1 , local_x + 1)

    # Проверка справа сверху
    if x > 0 & y > 0 : 
        if playground[y - 1][x + 1] == unselected_nil : open_nulls(local_y - 1 , local_x + 1)
    
    else:
        return 0 



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
            print(player[y][x], end="  ")
        print() # Перенос на новую строку

draw_frame()



# =========================== Выбор клеток ========================

x = 0 
y = 0



# управление
latency = 0.03 # Задержка в секундах

x = 0
y = 0

# Движение влево
def left():
    global x
    if   player[y][x] == selected_nil: player[y][x] = unselected_nil
    elif player[y][x] == selected_no:  player[y][x] = unselected_no
    elif player[y][x] == selected_one: player[y][x] = unselected_one
    elif player[y][x] == selected_two: player[y][x] = unselected_two
    elif player[y][x] == selected_thr: player[y][x] = unselected_thr
    elif player[y][x] == selected_fou: player[y][x] = unselected_fou
    elif player[y][x] == selected_fiv: player[y][x] = unselected_fiv
    if x > 0: x -= 1
    # Окрашиваем выбранный символ
    if   player[y][x] == unselected_nil: player[y][x] = selected_nil
    elif player[y][x] == unselected_no:  player[y][x] = selected_no
    elif player[y][x] == unselected_one: player[y][x] = selected_one
    elif player[y][x] == unselected_two: player[y][x]= selected_two
    elif player[y][x] == unselected_thr: player[y][x] = selected_thr
    elif player[y][x] == unselected_fou: player[y][x] = selected_fou
    elif player[y][x] == unselected_fiv: player[y][x] = selected_fiv
    draw_frame()
    time.sleep(latency)

keyboard.add_hotkey("a", left)

# Движение вверх
def up():
    global y
    if   player[y][x] == selected_nil: player[y][x] = unselected_nil
    elif player[y][x] == selected_no:  player[y][x] = unselected_no
    elif player[y][x] == selected_one: player[y][x] = unselected_one
    elif player[y][x] == selected_two: player[y][x] = unselected_two
    elif player[y][x] == selected_thr: player[y][x] = unselected_thr
    elif player[y][x] == selected_fou: player[y][x] = unselected_fou
    elif player[y][x] == selected_fiv: player[y][x] = unselected_fiv
    if y > 0: y -= 1
    # Окрашиваем выбранный символ
    if   player[y][x] == unselected_nil: player[y][x] = selected_nil
    elif player[y][x] == unselected_no:  player[y][x] = selected_no
    elif player[y][x] == unselected_one: player[y][x] = selected_one
    elif player[y][x] == unselected_two: player[y][x]= selected_two
    elif player[y][x] == unselected_thr: player[y][x] = selected_thr
    elif player[y][x] == unselected_fou: player[y][x] = selected_fou
    elif player[y][x] == unselected_fiv: player[y][x] = selected_fiv
    draw_frame()
    time.sleep(latency)

keyboard.add_hotkey("w", up)

# Движение вниз
def down():
    global y
    if   player[y][x] == selected_nil: player[y][x] = unselected_nil
    elif player[y][x] == selected_no:  player[y][x] = unselected_no
    elif player[y][x] == selected_one: player[y][x] = unselected_one
    elif player[y][x] == selected_two: player[y][x] = unselected_two
    elif player[y][x] == selected_thr: player[y][x] = unselected_thr
    elif player[y][x] == selected_fou: player[y][x] = unselected_fou
    elif player[y][x] == selected_fiv: player[y][x] = unselected_fiv
    if y < Y_SIZE-1: y += 1
    # Окрашиваем выбранный символ
    if   player[y][x] == unselected_nil: player[y][x] = selected_nil
    elif player[y][x] == unselected_no:  player[y][x] = selected_no
    elif player[y][x] == unselected_one: player[y][x] = selected_one
    elif player[y][x] == unselected_two: player[y][x]= selected_two
    elif player[y][x] == unselected_thr: player[y][x] = selected_thr
    elif player[y][x] == unselected_fou: player[y][x] = selected_fou
    elif player[y][x] == unselected_fiv: player[y][x] = selected_fiv
    draw_frame()
    time.sleep(latency)

keyboard.add_hotkey("s", down)

# Движение вправо
def right():
    global x
    if   player[y][x] == selected_nil: player[y][x] = unselected_nil
    elif player[y][x] == selected_no:  player[y][x] = unselected_no
    elif player[y][x] == selected_one: player[y][x] = unselected_one
    elif player[y][x] == selected_two: player[y][x] = unselected_two
    elif player[y][x] == selected_thr: player[y][x] = unselected_thr
    elif player[y][x] == selected_fou: player[y][x] = unselected_fou
    elif player[y][x] == selected_fiv: player[y][x] = unselected_fiv
    if x < X_SIZE-1: x += 1
    # Окрашиваем выбранный символ
    if   player[y][x] == unselected_nil: player[y][x] = selected_nil
    elif player[y][x] == unselected_no:  player[y][x] = selected_no
    elif player[y][x] == unselected_one: player[y][x] = selected_one
    elif player[y][x] == unselected_two: player[y][x]= selected_two
    elif player[y][x] == unselected_thr: player[y][x] = selected_thr
    elif player[y][x] == unselected_fou: player[y][x] = selected_fou
    elif player[y][x] == unselected_fiv: player[y][x] = selected_fiv
    draw_frame()
    time.sleep(latency)

keyboard.add_hotkey("d", right)

# Фунция выбора клетки
def select():
    player[y][x] = playground[y][x]
    if playground[y][x] == unselected_nil : open_nulls(y, x)
    draw_frame()
    
keyboard.add_hotkey("e", select)


keyboard.wait("q")



