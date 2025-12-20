#main.py

from read_csv import load_csv
from query import select, print_format, compare, count, max, min, avg, rcount

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

        elif cmd.startswith("VIEW "):
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
            
            #start of WHERE and RANGE block
            new_row = []
            tokens = cmd.split()                            #make sure the WHERE and RANGE limit select first. The array is updated but not the print
            if "WHERE" in tokens:
                where_index = tokens.index("WHERE")
            else:
                where_index = -1
            if where_index != -1:
                where_block = tokens[where_index + 1:]      
                if len(where_block) != 3:
                    print("Invalid syntax for WHERE clause")
                    continue
                column, symbol, value = where_block
                if column not in header:
                    print("Column not found")
                    continue
                col_index = header.index(column)
                for row in rows:
                    if compare(row[col_index], symbol, value):
                        new_row.append(row)
            else:
                new_row = rows
            #new_row is rows but now filtered with WHERE condition
            newer_row = []
            if "RANGE" in tokens:
                range_index = tokens.index("RANGE")
            else:
                range_index = -1
            if range_index != -1:
                range_block = tokens[range_index + 1:]
                if len(range_block) != 2:
                    print("Invalid syntax for RANGE clause")
                    continue
                index1, index2 = map(int, range_block)
                index1 -= 1
                for i in range(index1, index2):
                    newer_row.append(new_row[i])
            else:
                newer_row = new_row
            #newer_row is the final filtered version of rows
            if "MAX" in tokens:
                max_index = tokens.index("MAX")
            else:
                max_index = -1
            if max_index != -1:
                max_col = tokens[max_index+1]
                max(newer_row, max_col)

            if "MIN" in tokens:
                min_index = tokens.index("MIN")
            else:
                min_index = -1
            if min_index != -1:
                min_col = tokens[min_index+1]
                min(newer_row, min_col)

            if "AVG" in tokens:
                avg_index = tokens.index("AVG")
            else:
                avg_index = -1
            if avg_index != -1:
                avg_col = tokens[avg_index+1]
                avg(newer_row, avg_col)

            if "RCOUNT" in tokens:
                rcount_index = tokens.index("AVG")
            else:
                avg_index = -1
            if avg_index != -1:
                rcount(newer_row)


        elif cmd.startswith("count "):
            
            column = cmd.split()[1]
            value = cmd.split()[2]
            print("Header: " + column + ", Value: " + value)
            print(str(compare(column, value, header, rows)) + " matches found")
        
        
        else:
            print("Not a valid command")

if __name__ == "__main__":
    main()