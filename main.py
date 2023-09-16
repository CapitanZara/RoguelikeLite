import os

room = [
    ".", ".", ".", ".",
    '.', '.', ".", ".",
    ".", ".", ".", ".",
    '.', '.', ".", "."

]

player_mark = "P"
player_index = 1

room[player_index] = player_mark


def show_display():
    """Отображает комнату в столбик"""
    count = 1
    # 0 1 2 3 4 5 6 7 8 9 10 ... 15
    for i in range(len(room)):  # цикл for  переменная i
        if count == 4:
            print(room[i], end="")
            print()
            count = 0
        else:
            print(room[i], end="")

        count = count + 1


show_display()  # вызов функции
input()
os.system("cls")
# двигаем вниз
print("Персонаж идет вниз")
old_player_index = player_index
player_index = player_index + 4

room[old_player_index] = "."
room[player_index] = player_mark
show_display()

input()
os.system("cls")
# двигаем вправо
print("Персонаж идет вправо")
old_player_index = player_index
player_index = player_index + 1
room[old_player_index] = "."
room[player_index] = player_mark
show_display()

input()
os.system("cls")
# двигаем влево
print("Персонаж идет влево")
old_player_index = player_index
player_index = player_index - 1
room[old_player_index] = "."
room[player_index] = player_mark
show_display()
input()
os.system("cls")

# двигаем вверх
print("Персонаж идет вверх")
old_player_index = player_index
player_index = player_index - 4
room[old_player_index] = "."
room[player_index] = player_mark
show_display()
