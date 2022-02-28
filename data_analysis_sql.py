import sqlite3

conn = sqlite3.connect("Hospital.db")
c = conn.cursor()

c.execute('''
SELECT ownership, AVG(rating) AS avg_rating
FROM hospital_info
GROUP BY ownership
ORDER BY avg_rating DESC
LIMIT 1
''')
print(c.fetchall())

c.execute('''
SELECT state, AVG(rating) AS avg_rating
FROM hospital_info
GROUP BY state
ORDER BY avg_rating DESC
LIMIT 5
''')
print(c.fetchall())

c.execute('''
SELECT state, county, AVG(rating) AS avg_rating
FROM hospital_info
WHERE state = 'SD'
GROUP BY county
ORDER BY avg_rating DESC
LIMIT 3
''')
print(c.fetchall())

conn.close()
