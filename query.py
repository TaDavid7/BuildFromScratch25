#operations
#filtering, aggregations, group by
import csv
def compare(init, operator, condition):
    try:
        init = float(init)
        condition = float(condition)
    except ValueError:
        pass
    if operator == "=":
        return init == condition
    elif operator == "!=":
        return init != condition
    elif operator == ">":
        return init > condition
    elif operator == "<":
        return init < condition
    elif operator == ">=":
        return init >= condition
    elif operator == "<=":
        return init <= condition
    else:
        raise ValueError("Invalid Operator")

def print_format(header, rows, func, values, every):
    if not header:
        return ""
    if not rows:
        return ""
    result = []

    indexCol = []
    for index, col in enumerate(every):
        if col in header:
            indexCol.append(index)
    #format header
    merged_header = header + func
    formatted_header = [
        f"{col:<{15}}" for col in merged_header #list of strings
    ]
    first_row = "".join(formatted_header)# string
    result.append(first_row)
    result.append(("-" * len(header)*15) + "|" + ("-"*len(func)*15))

    #format rows
    firstTime = True
    for row in rows:
        if(firstTime):
            merged_row = [row[i] for i in indexCol] + values
            formatted_row = [f"{item:<{15}}" for item in merged_row]
            firstTime = False
            result.append(("").join(formatted_row))
            continue
        formatted_row = [f"{item:<{15}}" for item in [row[i] for i in indexCol]]
        result.append(("").join(formatted_row))


    result.append("")
    return "\n".join(result)


def select(path, columns):

    #open file
    with open(path, encoding="utf-8") as f:
        #.read() converts f into string 
        reader = csv.DictReader(f)
        #change into set with title columns
        titles = set(reader.fieldnames)
        filter = set(columns)
    
        if not filter.issubset(titles):
            raise ValueError("Invalid columns")

        result = []
        for row in reader:
            selected = {}
            for col in columns:
                selected[col] = row[col]
            result.append(selected)
    return result

def max(rows, col):
    max = rows[0][col]
    for row in rows:
        if row[col] > max:
            max = row[col]
    return max

def min(rows, col):
    min = rows[0][col]
    for row in rows:
        if row[col] < min:
            min = row[col]
    return min

def avg(rows, col):
    sum = 0    #I might change this later so its safe integer bounds
    count = 0
    for row in rows:
        sum += int(row[col])
        count += 1
    return round((sum/count), 2)

def rcount(rows):
    return len(rows)

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
    #check for matches
    for j in range(len(rows)):
        if rows[j][index] == data:
            total += 1
    return total

def clear(path):
    with open(path, 'w', newline='\n') as f:
        pass #does nothing, just clears

def insertRow(path, row):
    with open(path, 'a', newline='\n') as f:
        writer = csv.writer(f)
        writer.writerows(row)
    
def createHeader(path, header):
    with open(path, 'w', newline='\n') as f:
        writer = csv.writer(f)
        writer.writerows(header)

def updateFile(rows, column, edit, header, path, old_rows):
    if column not in header:
        print("Column not found")
        return
    for i in range(len(header)):
        if(header[i] == column):
            index = i
    for row in rows:
        row[index] = edit
    with open(path, "w", newline = "", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for old_row in old_rows:
            if old_row in rows:
                writer.writerow(old_row)
            else:
                writer.writerow(old_row)

def updateRow(path):
    row = []
    with open(path, "r") as f:
        lines = f.read().splitlines()
    
    for line in lines[1:]:
        row.append(line.split(","))
    return row

def deleteCol(col_idx, symbol, value, path):
    updated_row = []
    with open(path, "r", newline = "") as f:
        reader = csv.reader(f)
        for row in reader:
            if not compare(row[col_idx], symbol, value):
                updated_row.append(row)
    return updated_row
