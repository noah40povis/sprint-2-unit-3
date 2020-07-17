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
SELECT 
    CategoryName, 
        Count(DISTINCT ProductName) as Unique_Products 
FROM Product
Join Category ON Category.Id = Product.CategoryId
GROUP BY CategoryName
ORDER by Unique_Products DESC
LIMIT 1; 

"""
curs.execute(query)
print(curs.fetchall())
### Part 4 - Questions (and your Answers)

# Answer the following questions, baseline ~3-5 sentences each, as if they were
# interview screening questions (a form you fill when applying for a job):


# #- In the Northwind database, what is the type of relationship between the
#  `Employee` and `Territory` tables?
#Many to many 
#- What is a situation where a document store (like MongoDB) is appropriate, and#
# what is a situation where it is not appropriate?
#MongoDB is appropriate for companies like a startup looking for an easily scalable document storage system for a new product. 
#It is not appropriate where there is a company that has huge amounts of data and a rigid storage system structure. 
#- What is "NewSQL", and what is it trying to achieve?
# NewSql is a class of relational database managment. It tries to merge the benefits of a nosql and a traditional relational database system. 

# - (*Stretch*) Who's the employee with the most territories? Use `TerritoryId`
#   (not name, region, or other fields) as the unique identifier for territories.
