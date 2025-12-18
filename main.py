#main.py

from read_csv import load_csv
from query import count


def main():
    #print statements
    print("Database")
    print("Commands:")
    print("  load <csv_path>")
    print("  rows")
    print("  exit")
    print("  count <Header> <Value>")

    header = []
    rows = []

    while True:
        cmd = input("> ")

        if cmd == "exit":
            break
        
        if cmd.startswith("load "):
            path = cmd.split(" ")[1]
            header, rows = load_csv(path)
            print("File Loaded")
            print("Columns: ", header)

        elif cmd == "rows":
            print("Number of rows: ", len(rows))

        elif cmd.startswith("count "):
            column = cmd.split()[1]
            value = cmd.split()[2]
            print("Header: " + column + ", Value: " + value)
            print(str(count(column, value, header, rows)) + " matches found")
        
        
        print("--------------------------------")

if __name__ == "__main__":
    main()