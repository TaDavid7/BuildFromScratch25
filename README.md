# Tiny Query Language Engine
A lightweight, human readable data query engine inspired by databases, designed to make query execution and data operations easier to understand for beginners.
Instead of complex grammar, this project uses a **keyword‑based pipeline syntax** that clearly shows how data is processed step by step. The system supports full CRUD operations, filtering, grouping, aggregation, and an educational **EXPLAIN mode** that reveals internal execution logic.

---
## Features
- Load and query CSV data
- Full **CRUD operations**
  - Create (INSERT, IMPORT)
  - Read (VIEW)
  - Update
  - Delete
- Keyword‑based query language
- Filtering with multiple conditions (`WHERE`, `AND`)
- Range slicing (`RANGE`)
- Aggregations (`COUNT`, `AVG`, `MIN`, `MAX`)
- **EXPLAIN mode** to show execution steps instead of running the query
- 
---
## Command Grammar
The query language is keyword‑based and executed as a left‑to‑right pipeline.
Each keyword represents a data operation.
### Core Commands
CREATE <database_name>  
LOAD <database_name>  
INSERT \<value1>\<value2> ...  
UPDATE \<column> = \<value> WHERE \<condition>  
DELETE WHERE \<condition>  
VIEW \<columns> WHERE \<conditions> RANGE \<start> \<end> \<aggregation>\<col>  # note WHERE and RANGE are both optional
EXPLAIN <any command>

---
### How it works
To start playing around with a database run
1. Clone the repository
2. Make sure Python 3 (or latest version is installed)
3. Run python main.py in the terminal
4. Load a CSV file or create one:
5. Start running queries!
Type these commands to get started with your own database
   
```graphql
CREATE database_name
load database_name
```
After that, the different commands you can do depends on what main operations you want to do (VIEW, UPDATE, DELETE, INSERT). Note these main commands cannot be used together.
```graphql
VIEW col1 col2 ... WHERE ... RANGE ... MAX ...
```
```graphql
UPDATE col = val WHERE ...
```
```graphql
DELETE WHERE ...
```
```graphql
INSERT val1 val2 ...
```
---

## Project Structure

├── main.py # Command loop and user interface 

├── read_csv.py # CSV loading and database creation

├── query.py # Query execution logic (VIEW, UPDATE, DELETE, INSERT)

├── /data # Folder that holds csv (database files)

└── README.md

---

## Example Commands
```graphql
VIEW * WHERE city = SanJose AND age = 18  
```
```graphql
VIEW * WHERE score > 80 RANGE 1 5   #gives indexed rows 1-5 based on filter
```
```graphql
UPDATE age = 19 WHERE name = David
```
```graphql
DELETE WHERE score < 70
```
```graphql
EXPLAIN VIEW * WHERE name = DAVID AND age = 16 RANGE 1 5 RCOUNT
```
---

## Future Work
- Multi-table engine
- More aggregations / group-by expansions

---

