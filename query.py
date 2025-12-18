#operations
#filtering, aggregations, group by
import csv

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