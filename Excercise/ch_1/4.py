# lst_input = [
#     ["-","-","-","-","-"],
#     ["-","-","-","-","-"],
#     ["-","-","#","-","-"]
#     ["-","-","-","-","-"],
#     ["-","-","-","-","-"]
# ]

DIMENSION = 5

direction = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1), (0, 0), (0, 1),
    (1, -1), (1, 0), (1, 1)
]

def num_grid(lst):

    ans = []

    for row in range(DIMENSION):
        row_ans = []
        for col in range(DIMENSION):
            '''Check if that position is a bomb'''
            if lst[row][col] == '#':
                row_ans.append('#')
                continue

            sum = 0
            for row_shift, col_shift in direction:
                new_row = row + row_shift
                new_col = col + col_shift
                if 0 <= new_row < DIMENSION and 0 <= new_col < DIMENSION and lst[new_row][new_col] == '#':
                    sum += 1
            
            row_ans.append(str(sum))
        ans.append(row_ans)

    return ans




lst_input = []

print("*** Minesweeper ***")


input_list = input("Enter input(5x5) : ").split(",")

for e in input_list:
  lst_input.append([i for i in e.split()])

print("\n",*lst_input,sep = "\n")
print("\n",*num_grid(lst_input),sep = "\n")