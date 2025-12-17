#load csv file
def load_csv(path):

    #open file
    with open(path, "r") as f:
        #.read() converts f into string 
        lines = f.read().splitlines()
    
    header = lines[0].split(",")
    rows = []

    for line in lines[1:]:
        rows.append(line.split(","))

    return header, rows