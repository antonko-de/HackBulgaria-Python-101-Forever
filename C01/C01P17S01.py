

matrix = [
    ["i", "v", "a", "n"],
    ["e", "v", "n", "h"],
    ["i", "n", "a", "v"],
    ["m", "v", "v", "n"],
    ["q", "r", "i", "t"]
]

len_cols = 3
len_rows = 5

def row_check(row_num,step):
    if step > len_cols:
        step = 0
        return (row_num + 1, step )

    else:
        return (row_num, step)


def check_horizontal_forward(matrix, row_num, step):
        if matrix[row_num][step] == "i":
            if len(matrix[row_num][step:]) >=4:
                return "".join(matrix[row_num][step:step+4]) == "ivan"

step = 0
row_num = 0
counter = 0
while not (row_num == 4 and step == 3) :
    row_num, step = row_check(row_num, step)
    if check_horizontal_forward(matrix,row_num, step):
        counter + 1
    step += 1
        
    


