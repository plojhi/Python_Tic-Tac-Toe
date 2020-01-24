def field():
    global cells

    print(f"""
    ---------
    | {cells[0][0]} {cells[0][1]} {cells[0][2]} |
    | {cells[1][0]} {cells[1][1]} {cells[1][2]} |
    | {cells[2][0]} {cells[2][1]} {cells[2][2]} |
    ---------
    """)

def input_coordinates_x():
    global cells
    while True:
        coordinates = input("Enter the coordinates: ").split()

        try:
            coordinates = [int(i) for i in coordinates]
        except ValueError:
            print("You should enter numbers!")
            continue

        if len(coordinates) != 2:
            print("Please input two coordinates")
            continue
        elif coordinates[0] > 3 or coordinates[1] > 3 or coordinates[0] < 1 or coordinates[1] < 1:
            print("Coordinates should be from 1 to 3!")
            continue

        else:



            coordinates = transfer_coordinates(coordinates)

            if cells[coordinates[0]][coordinates[1]] == "X" or cells[coordinates[0]][coordinates[1]] == "O":
                print("This cell is occupied! Choose another one!")
                continue
            else:
                cells[coordinates[0]][coordinates[1]] = "X"
                break

def input_coordinates_o():
    global cells
    while True:
        coordinates = input("Enter the coordinates: ").split()

        try:
            coordinates = [int(i) for i in coordinates]
        except ValueError:
            print("You should enter numbers!")
            continue

        if len(coordinates) != 2:
            print("Please input two coordinates")
            continue
        elif coordinates[0] > 3 or coordinates[1] > 3 or coordinates[0] < 1 or coordinates[1] < 1:
            print("Coordinates should be from 1 to 3!")
            continue

        else:



            coordinates = transfer_coordinates(coordinates)

            if cells[coordinates[0]][coordinates[1]] == "X" or cells[coordinates[0]][coordinates[1]] == "O":
                print("This cell is occupied! Choose another one!")
                continue
            else:
                cells[coordinates[0]][coordinates[1]] = "O"
                break


def transfer_coordinates(coordinates):
    if coordinates == [1, 1]:
        return [2, 0]
    elif coordinates == [1, 2]:
        return [1, 0]
    elif coordinates == [1, 3]:
        return [0, 0]
    elif coordinates == [2, 1]:
        return [2, 1]
    elif coordinates == [2, 2]:
        return [1, 1]
    elif coordinates == [2, 3]:
        return [0, 1]
    elif coordinates == [3, 1]:
        return [2, 2]
    elif coordinates == [3, 2]:
        return [1, 2]
    elif coordinates == [3, 3]:
        return [0, 2]



def result():
    global cells

    count_x = 0
    count_o = 0
    count_space = 0
    for i in range(3):
        for j in range(3):
            if cells[i][j] == "X":
                count_x +=1
            elif cells[i][j] == "O":
                count_o +=1
            elif cells[i][j] == " ":
                count_space +=1

    # columes
    win_x = 0
    win_o = 0
    for i in range(3):
        if cells[0][i] == cells[1][i] and cells[1][i] == cells[2][i]:
            if cells[0][i] == "X":
                win_x += 1
            elif cells[0][i] == "O":
                win_o += 1

    # rows
    for i in range(3):
        if cells[i][0] == cells[i][1] and cells[i][1] == cells[i][2]:
            if cells[i][0] == "X":
                win_x += 1
            elif cells[i][0] == "O":
                win_o += 1

    # diagonals
    if cells[0][0] == cells[1][1] and cells[1][1] == cells[2][2]:
        if cells[0][0] == "X":
                win_x += 1
        elif cells[0][0] == "O":
            win_o += 1

    if cells[0][2] == cells[1][1] and cells[1][1] == cells[2][0]:
        if cells[0][2] == "X":
                win_x += 1
        elif cells[0][2] == "O":
            win_o += 1



    if (count_x - count_o) > 1 or (count_o - count_x) > 1:
        print("Impossible")
        return "end"
    elif win_x == 1 and win_o == 1:
        print("Impossible")
        return "end"
    elif win_x == 1 and win_o == 0:
        print("X wins")
        return "end"
    elif win_x == 0 and win_o == 1:
        print("O wins")
        return "end"
    elif count_space == 0 and win_x == 0 and win_o == 0:
        print("Draw")
        return "end"
    elif count_space != 0 and win_x == 0 and win_o == 0:
        print()



cells = ("         ")
cells = [[cells[0], cells[1], cells[2]],
            [cells[3], cells[4], cells[5]],
            [cells[6], cells[7], cells[8]]]
status = ""
while True:
    field()
    input_coordinates_x()
    field()
    status = result()
    if status == "end":
        break
    input_coordinates_o()
    field()
    status = result()
    if status == "end":
        break
