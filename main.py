#main.py

from read_csv import load_csv
from query import select, print_format, count

"""
These are comments
Find # of rows
View specific cols
View specific range of rows 
Find max (greatest number) of specific column
Find min, avg, mean
Group by column (increasing order/dec)
Where column value =, <=, >=, <, >, !=
From which database

Explain flair
load database

--viewing (which to see)

--modifier what rows to see based on column value
where col >(symbol) number/value 

range idx idx

--func--
max col_name, min col_name, avg ..., mean.., rcount



load database  --> ref database
mandatory
EXPLAIN VIEW/DELETE <col1> <col2> ..., WHERE <col1> <symbol> <number/value>, 
        mandatory               optional                                

RANGE <idx1> <idx2>, MAX <col>, MIN <col>, AVG <col>, MEAN <col>, RCOUNT,
optional

Delete
INSERT <val> <val> <val>
Explain
UPDATE - do this later

"""



def main():
    #print statements
    print("Database")
    print("Commands:")
    print("  load <csv_path>")
    print("  rows")
    print("  count <Header> <Value>")
    print("  select <col1> <col2> ...")
    print("  exit")

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
                if columns[0] == "*":
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