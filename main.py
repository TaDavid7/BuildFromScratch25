#main.py


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
from read_csv import load_csv
from query import print_format, compare, max, min, avg, rcount, insertRow, createHeader, updateFile, updateRow



def main():
    #print statements
    print("Database")
    print("Commands:")
    print("  load <csv_path>")
    print("  UPDATE <col> <row> <value>")
    print("  CREATE <filename>")
    print("  INSERT <val1> <val2> ...")
    print("  VIEW <col1> <col2> ...")
    print("  WHERE <col> <symbol <value>")
    print("  RANGE <idx1> <idx2>")
    print("  MAX <col> MIN <col> AVG<col> RCOUNT")
    print("  exit")

    header = []
    rows = []

    while True:
        cmd = input("> ")

        if cmd == "exit":
            break
        
        elif cmd.startswith("load "):
            path = "data/" + cmd.split(" ")[1] + ".csv"
            header, rows = load_csv(path)
            print("File Loaded")
            print("Columns: ", header, "\n")

        elif cmd == "rows":

            print("Number of rows: ", len(rows))

        elif cmd.startswith("UPDATE "):
            update = cmd.split()
            update_block = update[1:4]
            col = update_block[0]
            data = update_block[2]
            new_row = []                           #make sure the WHERE and RANGE limit select first. The array is updated but not the print
            if "WHERE" in update:
                where_index = update.index("WHERE")
            else:
                where_index = -1
            if where_index != -1:
                where_block = update[where_index + 1:where_index + 4]      
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
            updateFile(new_row, col, data, header, path, rows)
            view = print_format(header, new_row, [], [], header)
            print(view)

        elif cmd.startswith("CREATE "):
            create = cmd.split()
            path = "data/" + create[1] + ".csv"
            cols = create[2:]
            colsnew = []
            colsnew.append(cols)
            createHeader(path, colsnew)
            print(f"File '{path}' created successfully")

        elif cmd.startswith("INSERT "):
            if not header:
                print("No data", "\n")
                continue
            values = cmd.split()
            values_block = values[1:]
            row_block = []
            row_block.append(values_block)
            if len(values_block) != len(header):
                print("Please insert a valid row")
                continue
            insertRow(path, row_block)
            header, rows = load_csv(path)
            view = print_format(header, rows, [], [], header)
            print(view)
            rows = updateRow(path)

        elif cmd.startswith("VIEW "):
            if not rows:
                print("No data", "\n")
                continue
            tokens = cmd.split() 
            if "*" in tokens:
                selected_cols = header
            else:
                selected_cols = []
                for index in tokens[1:]:
                    if index in ("WHERE", "RANGE", "MAX", "MIN", "AVG", "RCOUNT"):
                        continue
                    if index not in header:
                        print("Invalid Syntax: column not found in file")
                        continue
                    selected_cols.append(index)
            
            #start of WHERE and RANGE block
            new_row = []                           #make sure the WHERE and RANGE limit select first. The array is updated but not the print
            if "WHERE" in tokens:
                where_index = tokens.index("WHERE")
            else:
                where_index = -1
            if where_index != -1:
                where_block = tokens[where_index + 1:where_index + 4]      
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
                range_block = tokens[range_index + 1:range_index + 3]
                if len(range_block) != 2:
                    print("Invalid syntax for RANGE clause")
                    continue
                index1, index2 = map(int, range_block)
                if(index2>len(new_row)):
                    index2 = len(new_row)-1
                for i in range(index1, index2+1):
                    newer_row.append(new_row[i])
            else:
                newer_row = new_row
            #newer_row is the final filtered version of rows

            func_names = []
            values = []
            col_call = 0
            col_name = ""
            if "MAX" in tokens:
                max_index = tokens.index("MAX")
            else:
                max_index = -1
            if max_index != -1:
                col_name = tokens[max_index+1]
                col_call = header.index(col_name)
                max_result = max(newer_row, col_call)
                func_names.append(("MAX " + col_name))
                values.append(max_result)

            if "MIN" in tokens:
                min_index = tokens.index("MIN")
            else:
                min_index = -1
            if min_index != -1:
                col_name = tokens[min_index+1]
                col_call = header.index(col_name)
                min_result = min(newer_row, col_call)
                func_names.append(("MIN " + col_name))
                values.append(min_result)

            if "AVG" in tokens:
                avg_index = tokens.index("AVG")
            else:
                avg_index = -1
            if avg_index != -1:
                col_name = tokens[avg_index+1]
                col_call = header.index(col_name)
                avg_result = avg(newer_row, col_call)
                func_names.append(("AVG " + col_name))
                values.append(avg_result)

            if "RCOUNT" in tokens:
                rcount_index = tokens.index("RCOUNT")
            else:
                rcount_index = -1
            if rcount_index != -1:
                rcount_result = rcount(newer_row)
                func_names.append("RCOUNT")
                values.append(rcount_result)

            view = print_format(selected_cols, newer_row, func_names, values, header)
            print(view)


        elif cmd.startswith("count "):
            
            column = cmd.split()[1]
            value = cmd.split()[2]
            print("Header: " + column + ", Value: " + value)
            print(str(compare(column, value, header, rows)) + " matches found")
        
        
        else:
            print("Not a valid command")

if __name__ == "__main__":
    main()