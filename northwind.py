### Part 2 - The Northwind Database 
import sqlite3
conn = sqlite3.connect('/Users/noahpovis/Documents/GitHub/sprint 2 unit 3/northwind_small.sqlite3')
curs = conn.cursor()

# - What are the ten most expensive items (per unit price) in the database?
query = """
SELECT DISTINCT ProductId 
FROM Orderdetail 
ORDER BY UnitPrice DESC
LIMIT 10; 
"""
curs.execute(query)
print(curs.fetchall())
# - What is the average age of an employee at the time of their hiring? (Hint: a
#   lot of arithmetic works with dates.)
query = """
SELECT round(AVG(HireDate-BirthDate))
FROM Employee
"""

# - (*Stretch*) How does the average age of employee at hire vary by city?
query = """
SELECT round(AVG(HireDate-BirthDate)) , City
FROM Employee
GROUP BY City
; 
"""

### Part 3 - Sailing the Northwind Seas
# - What are the ten most expensive items (per unit price) in the database *and*
#   their suppliers?
query = """
SELECT UnitPrice, ProductName, CompanyName
from Product
INNER JOIN Supplier
GROUP BY UnitPrice 
ORDER BY UnitPrice DESC
LIMIT 10; 
"""
curs.execute(query)
print(curs.fetchall())

# - What is the largest category (by number of unique products in it)?
query = """
SELECT COUNT(CategoryId)  AS Num , ProductName, CategoryName
FROM Product
Join Category
GROUP BY ProductName 
ORDER by Num DESC
LIMIT 1; 
"""

### Part 4 - Questions (and your Answers)

Answer the following questions, baseline ~3-5 sentences each, as if they were
interview screening questions (a form you fill when applying for a job):

- In the Northwind database, what is the type of relationship between the
  `Employee` and `Territory` tables?

- What is a situation where a document store (like MongoDB) is appropriate, and
  what is a situation where it is not appropriate?
- What is "NewSQL", and what is it trying to achieve?


# - (*Stretch*) Who's the employee with the most territories? Use `TerritoryId`
#   (not name, region, or other fields) as the unique identifier for territories.
