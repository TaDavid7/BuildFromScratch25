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

def print_format(header, rows, func, values):
    if not header:
        return ""
    if not rows:
        return ""
    result = []

    #format header
    merged_header = header + func
    formatted_header = [
        f"{col:<{10}}" for col in merged_header
    ]
    first_row = "".join(formatted_header) # col1    col2     col3 ...
    result.append(first_row)
    result.append(("-" * len(header)*10) + "|" + ("-"*len(func)*10))

    #format rows
    firstTime = True
    for row in rows:
        if(firstTime):
            merged_row = row + values
            formatted_row = [f"{item:<{10}}" for item in merged_row]
            firstTime = False
            result.append((" ").join(formatted_row))
            continue
        formatted_row = [f"{item:<{10}}" for item in row]
        result.append((" ").join(formatted_row))


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
        sum += row[col]
        count += 1
    return (sum/count)

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
    target = data
    #check for matches
    for j in range(len(rows)):
        if rows[j][index] == data:
            total += 1
    return total



    
