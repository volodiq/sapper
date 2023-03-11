from keyboard import add_hotkey, wait
from random import randint
from os import system

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

flag           = "\033[1m\033[35m" + "F" # Флаг

frame          = "\033[1m\033[30m" + "=" # Выбранная клетка с 8 минами в округе

gameover      = "\033[1m\033[31m" + "Game Over"

# Очистка экрана и цвета символов
print(unselected_no)
system("cls")

# =========================== Выбор сложности =================================

print("1 - для лопухов, 2 - для смешариков, 3 - для четких пацанов")

choose_dificulty = input("Выберите сложность: ")

match choose_dificulty:

    # Лопухи
    case "1":
        Y_SIZE = 8
        X_SIZE = 10
        MINES_COUNT = 80
    # Смешарики
    case "2":
        Y_SIZE = 13
        X_SIZE = 15
        MINES_COUNT = 30
    # Четкие пацанчики
    case "3":
        Y_SIZE = 17
        X_SIZE = 18
        MINES_COUNT = 30

# =========================== Создание поля ===================================

# Поле с значениями
playground = [[unselected_no] * X_SIZE for i in range(Y_SIZE)]

# Поле игрока
player = [[unselected_no] * X_SIZE for i in range(Y_SIZE)]

# Создание мин
for i in range(MINES_COUNT):
    playground[randint(0, Y_SIZE - 1)][randint(0, X_SIZE - 1)] = mine

# =========================== Расстановка цифр ================================
bomb_index = 0

# Функция проверки клетки
def mine_check(y, x):
    global bomb_index
    if playground[y][x] == mine : bomb_index +=1

# Фунция проверки смежных клеток
def check(y, x):

    if playground[y][x] == mine : return mine

    global bomb_index
    bomb_index = 0

    # Проверка слева
    if x > 0 : 
        mine_check(y, x - 1)

    # Проверка слева снизу
    if x > 0:
        if (y < Y_SIZE - 1):
            mine_check(y + 1,x - 1)
    
    # Проверка слева сверху
    if x > 0 & y > 0 : 
        mine_check(y - 1,x - 1)

    # Проверка сверху
    if  y > 0 : 
        mine_check(y - 1,x)

    # Проверка снизу
    if y < Y_SIZE - 1 : 
        mine_check(y + 1,x)

    # Проверка справа 
    if x < X_SIZE - 1 : 
        mine_check(y,x + 1)

    # Проверка справа снизу 
    if x < X_SIZE - 1 & y < Y_SIZE - 1: 
        mine_check(y + 1,x + 1)

    # Проверка справа сверху
    if x < X_SIZE - 1 & y > 0 : 
        mine_check(y - 1,x + 1)

    # Возвращение значения
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

# Расстановка цифр
for y in range(Y_SIZE):
    for x in range(X_SIZE):
        playground[y][x] = check(y , x)

# =========================== Функция для открытия нулей ======================

def open_nulls(y, x):

    player[y][x] = playground[y][x]

    # Проверка слева
    if x > 0:
        if player[y][x - 1] != unselected_nil:
            if playground[y][x - 1] == unselected_nil:
                open_nulls(y , x - 1)

            else: player[y][x - 1] = playground[y][x - 1]
    
    # Проверка справа
    if x < X_SIZE - 1 :
        if player[y][x + 1] != unselected_nil:
            if playground[y][x + 1] == unselected_nil:
                open_nulls(y , x + 1)

            else: player[y][x + 1] = playground[y][x + 1]

    # Проверка снизу
    if y < Y_SIZE - 1:
        if player[y + 1][x] != unselected_nil:
            if playground[y + 1][x] == unselected_nil:
                open_nulls(y + 1, x)

            else: player[y + 1][x] = playground[y + 1][x]
    
    # Проверка сверху
    if y > 0 :
        if player[y - 1][x] != unselected_nil:
            if playground[y - 1][x] == unselected_nil:
                open_nulls(y  - 1, x)

            else: player[y - 1][x] = playground[y - 1][x]

# =========================== Управление ======================================

# Функции окрашивания

def unpaint():
    # Отменяем выделение выбранной клетки
    if   player[y][x] == selected_nil: player[y][x] = unselected_nil
    elif player[y][x] == selected_no:  player[y][x] = unselected_no
    elif player[y][x] == selected_one: player[y][x] = unselected_one
    elif player[y][x] == selected_two: player[y][x] = unselected_two
    elif player[y][x] == selected_thr: player[y][x] = unselected_thr
    elif player[y][x] == selected_fou: player[y][x] = unselected_fou
    elif player[y][x] == selected_fiv: player[y][x] = unselected_fiv

def paint():
    # Окрашиваем выбранный символ
    if   player[y][x] == unselected_nil: player[y][x] = selected_nil
    elif player[y][x] == unselected_no:  player[y][x] = selected_no
    elif player[y][x] == unselected_one: player[y][x] = selected_one
    elif player[y][x] == unselected_two: player[y][x]= selected_two
    elif player[y][x] == unselected_thr: player[y][x] = selected_thr
    elif player[y][x] == unselected_fou: player[y][x] = selected_fou
    elif player[y][x] == unselected_fiv: player[y][x] = selected_fiv

# =========================== Движение ========================================

# Координаты выбранной игроком клетки
x = 0
y = 0

# Декоратор для функций движения
def move(function_to_decorate):

    def function_decorated():
        unpaint()
        function_to_decorate()
        paint()
        draw_frame()

    return function_decorated

# Движение влево
@move
def left():
    global x
    if x > 0: x -= 1

add_hotkey("a", left)

# Движение вправо
@move
def right():
    global x
    if x < (X_SIZE - 1) : x += 1

add_hotkey("d", right)

# Движение вниз
@move
def down():
    global y
    if y < (Y_SIZE - 1) : y += 1

add_hotkey("s", down)

# Движение вверх
@move
def up():
    global y
    if y > 0 : y -= 1

add_hotkey("w", up)

# =========================== Установка флагов ================================

flag_num = MINES_COUNT

def put_flag():
    global flag_num

    if flag_num> 0:
        player[y][x] = flag
        flag_num -= 1
        draw_frame()

add_hotkey("F", put_flag)

# =========================== Выбор клетки ====================================

def select():
    player[y][x] = playground[y][x]
    if playground[y][x] == unselected_nil : open_nulls(y, x)
    draw_frame()
    if player[y][x] == mine : game_over()

add_hotkey("E", select)

# =========================== Отрисовка =======================================

def draw_frame():
    system("cls")
    for y in range(Y_SIZE):
        for x in range(X_SIZE):
            print(player[y][x], end="  ")
        print() # Перенос на новую строку

# Game Over
def game_over():
    print(gameover)
    exit()
# Изначальная отрисовка
draw_frame()

# Выход
wait("q")