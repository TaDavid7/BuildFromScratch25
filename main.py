#main.py

from read_csv import load_csv

def main():
    #print statements
    print("Database")
    print("Commands:")
    print("  load <csv_path>")
    print("  rows")
    print("  exit")

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
        
if __name__ == "__main__":
    main()