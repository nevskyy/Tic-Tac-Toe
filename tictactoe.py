# 1) My Solution

digits = '0123456789'
# n = [x for x in input("Enter cells: > ").replace('_', ' ')]
n = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
matrix1 = [[0 for j in range(3)] for i in range(3)]

matrix1[0][0] = n[6]
matrix1[0][1] = n[3]
matrix1[0][2] = n[0]
matrix1[1][0] = n[7]
matrix1[1][1] = n[4]
matrix1[1][2] = n[1]
matrix1[2][0] = n[8]
matrix1[2][1] = n[5]
matrix1[2][2] = n[2]

matrix_set = [matrix1[0][2] + matrix1[1][2] + matrix1[2][2], matrix1[0][1] + matrix1[1][1] + matrix1[2][1],
              matrix1[0][0] + matrix1[1][0] + matrix1[2][0], matrix1[0][2] + matrix1[0][1] + matrix1[0][0],
              matrix1[1][2] + matrix1[1][1] + matrix1[1][0], matrix1[2][2] + matrix1[2][1] + matrix1[2][0],
              matrix1[0][2] + matrix1[1][1] + matrix1[2][0], matrix1[2][2] + matrix1[1][1] + matrix1[0][0]]

print("---------")
print('| ' + matrix1[0][2], matrix1[1][2], matrix1[2][2] + ' |')
print('| ' + matrix1[0][1], matrix1[1][1], matrix1[2][1] + ' |')
print('| ' + matrix1[0][0], matrix1[1][0], matrix1[2][0] + ' |')
print("---------")

flag = 1
count = 0

while True:
    if 'XXX' in matrix_set:
        print("X wins")
        break
    elif 'OOO' in matrix_set:
        print("O wins")
        break
    elif count == 9 and ('XXX' not in matrix_set or 'OOO' not in matrix_set):
        print("Draw")
        break

    coordinates = input("Enter the coordinates: > ").split()
    if coordinates[0] not in digits or coordinates[1] not in digits:
        print("You should enter numbers!")
    elif int(coordinates[0]) > 3 or int(coordinates[0]) < 1 or 1 > int(coordinates[1]) or int(coordinates[1]) > 3:
        print("Coordinates should be from 1 to 3!")
    elif matrix1[int(coordinates[0]) - 1][int(coordinates[1]) - 1] != ' ':
        print("This cell is occupied! Choose another one!")
    else:
        if matrix1[int(coordinates[0]) - 1][int(coordinates[1]) - 1] == ' ' and flag == 1:
            matrix1[int(coordinates[0]) - 1][int(coordinates[1]) - 1] = 'X'
            matrix_set = [matrix1[0][2] + matrix1[1][2] + matrix1[2][2], matrix1[0][1] + matrix1[1][1] + matrix1[2][1],
                          matrix1[0][0] + matrix1[1][0] + matrix1[2][0], matrix1[0][2] + matrix1[0][1] + matrix1[0][0],
                          matrix1[1][2] + matrix1[1][1] + matrix1[1][0], matrix1[2][2] + matrix1[2][1] + matrix1[2][0],
                          matrix1[0][2] + matrix1[1][1] + matrix1[2][0], matrix1[2][2] + matrix1[1][1] + matrix1[0][0]]
            flag = 0
            count += 1

            print("---------")
            print('| ' + matrix1[0][2], matrix1[1][2], matrix1[2][2] + ' |')
            print('| ' + matrix1[0][1], matrix1[1][1], matrix1[2][1] + ' |')
            print('| ' + matrix1[0][0], matrix1[1][0], matrix1[2][0] + ' |')
            print("---------")

        if matrix1[int(coordinates[0]) - 1][int(coordinates[1]) - 1] == ' ' and flag == 0:
            matrix1[int(coordinates[0]) - 1][int(coordinates[1]) - 1] = 'O'
            matrix_set = [matrix1[0][2] + matrix1[1][2] + matrix1[2][2], matrix1[0][1] + matrix1[1][1] + matrix1[2][1],
                          matrix1[0][0] + matrix1[1][0] + matrix1[2][0], matrix1[0][2] + matrix1[0][1] + matrix1[0][0],
                          matrix1[1][2] + matrix1[1][1] + matrix1[1][0], matrix1[2][2] + matrix1[2][1] + matrix1[2][0],
                          matrix1[0][2] + matrix1[1][1] + matrix1[2][0], matrix1[2][2] + matrix1[1][1] + matrix1[0][0]]
            flag = 1
            count += 1

            print("---------")
            print('| ' + matrix1[0][2], matrix1[1][2], matrix1[2][2] + ' |')
            print('| ' + matrix1[0][1], matrix1[1][1], matrix1[2][1] + ' |')
            print('| ' + matrix1[0][0], matrix1[1][0], matrix1[2][0] + ' |')
            print("---------")


# 2) Other nice short approach

# field = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
# # print(f"_________\n"
# #       f"| {field[0]} {field[1]} {field[2]} |\n"
# #       f"| {field[3]} {field[4]} {field[5]} |\n"
# #       f"| {field[6]} {field[7]} {field[8]} |\n"
# #       f"--------- ")
# print(f'''_________
# | {field[0]} {field[1]} {field[2]} |
# | {field[3]} {field[4]} {field[5]} |
# | {field[6]} {field[7]} {field[8]} |
# _________''')
# coordinates_list = [13, 23, 33, 12, 22, 32, 11, 21, 31]
# while True:
#     coordinates = ''.join(input("Enter the coordinates: ").split())
#     if not coordinates.isdigit(): # if input is not a number
#         print("You should enter numbers!")
#         continue
#     elif int(coordinates) not in coordinates_list: # if input is not [1; 3]
#         print("Coordinates should be from 1 to 3!")
#         continue
#     step_index = coordinates_list.index(int(coordinates))
#     # print(step_index)
#     if field[step_index] != ' ': # if cell is occupied
#         print("This cell is occupied! Choose another one!")
#         continue
#     if abs(len([x for x in field if x == 'X']) - len([o for o in field if o == 'O'])) == 0: # if amount of X is more than O
#         field[step_index] = 'X'
#     else:
#         field[step_index] = 'O'
#     print(f'''_________
# | {field[0]} {field[1]} {field[2]} |
# | {field[3]} {field[4]} {field[5]} |
# | {field[6]} {field[7]} {field[8]} |
# _________''')
#     winner_combo = [(field[0] + field[1] + field[2]),
#                            (field[3] + field[4] + field[5]),
#                            (field[6] + field[7] + field[8]),
#                            (field[2] + field[4] + field[6]),
#                            (field[0] + field[4] + field[8]),
#                            (field[0] + field[3] + field[6]),
#                            (field[1] + field[4] + field[7]),
#                            (field[2] + field[5] + field[8])]
#     if "XXX" in winner_combo:
#         print("X wins")
#         break
#     elif "OOO" in winner_combo:
#         print("O wins")
#         break
#     elif ' ' not in field:
#         print("Draw")
#         break
