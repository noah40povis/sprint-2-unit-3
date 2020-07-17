import sqlite3
sl_conn = sqlite3.connect('demo_data.sqlite3')
sl_curs = sl_conn.cursor()

create_table = """
CREATE TABLE demo (
    s VARCHAR(1),
    x INTEGER, 
    y INTEGER
);
"""
insert = """
INSERT INTO demo ( s, x, y) 
VALUES 
    ('g', 3, 9),
    ('v', 5, 7),
    ('f', 8, 7); 
"""

sl_curs.execute(create_table)
sl_curs.execute(insert)
sl_conn.commit()

#Count how many rows you have - it should be 3!
QUERY = """
SELECT COUNT(*)
FROM demo
"""
sl_curs.execute(QUERY)
print(sl_curs.fetchall())
# How many rows are there where both `x` and `y` are at least 5?
QUERY = """
SELECT COUNT(*) as 'Greater than 5'
FROM demo
WHERE x>5 and y>5
"""
sl_curs.execute(QUERY)
print(sl_curs.fetchall())
# - How many unique values of `y` are there (hint - `COUNT()` can accept a keyword
#   `DISTINCT`)?
Query = """
SELECT COUNT(DISTINCT y) 
FROM demo
"""
sl_curs.execute(Query)
print(sl_curs.fetchall())

