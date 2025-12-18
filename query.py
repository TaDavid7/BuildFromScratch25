#query.py
def count(column, data, header, rows):
    index = -1
    total = 0
    #find column index
    for i in range(len(header)):
        if header[i] == column:
            index = i
            break
    #user input error test
    if index == -1:
        print("Header not found")
        return 0
    target = data
    #check for matches
    for j in range(len(rows)):
        if rows[j][index] == data:
            total += 1
    return total


    