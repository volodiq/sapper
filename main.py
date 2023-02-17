
# =========================== Выбор сложности =========================


# =========================== Создание поля =========================
Y_SIZE = 10
X_SIZE = 10

playground = [["#"] * X_SIZE] * Y_SIZE

for y in range(Y_SIZE):
    for x in range(X_SIZE):
        print(playground[y][x], end=" ")
    print() # Перенос на новую строку
