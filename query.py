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

def print_format(result):
    if not result:
        return ""
    columns = list(result[0].keys())
    lines = []
    header = " | ".join(columns)
    lines.append(header)
    lines.append("-------------")
    for row in result:
        values = []
        for col in columns:
            values.append(row[col])
        lines.append(" | ".join(values))
    return "\n".join(lines)

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
    

def compare(val1, sym, val2):
    if sym == "<":
        return (val1<val2)
    elif sym == ">":
        return (val1>val2)
    elif sym == "<=":
        return (val1<=val2)
    elif sym == ">=":
        return (val1>=val2)
    elif sym == "==":
        return (val1==val2)
    elif sym == "!=":
        return (val1!=val2)
    else:
        return False




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



    
