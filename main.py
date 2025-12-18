#main.py

from read_csv import load_csv
from query import select, print_format, count

def main():
    #print statements
    print("Database")
    print("Commands:")
    print("  load <csv_path>")
    print("  rows")
    print("  select <col1> <col2> ...")
    print("  exit")
    print("  count <Header> <Value>")

    header = []
    rows = []

    while True:
        cmd = input("> ")

        if cmd == "exit":
            break
        
        elif cmd.startswith("load "):
            path = cmd.split(" ")[1]
            header, rows = load_csv(path)
            print("File Loaded")
            print("Columns: ", header)

        elif cmd == "rows":
            print("Number of rows: ", len(rows))

        elif cmd.startswith("select "):
            if not rows:
                print("No data")
                continue
            
            columns = cmd.split(" ")[1:]
            try:
                if len(columns) == 1 and columns[0] == "*":
                    print(header, "\n", rows)
                else:
                    result = select(path, columns)
                    print(print_format(result)) 
            except ValueError as e:
                print(e)

        elif cmd.startswith("count "):
            column = cmd.split()[1]
            value = cmd.split()[2]
            print("Header: " + column + ", Value: " + value)
            print(str(count(column, value, header, rows)) + " matches found")
        
        
        else:
            print("Not a valid command")

if __name__ == "__main__":
    main()