import sqlite3


connection = sqlite3.connect("data/job_postings.db")
cursor = connection.cursor()


print("DUPLICATE JOB IDS")

query = """
SELECT
    job_id,
    COUNT(*) AS occurrences
FROM job_postings
GROUP BY job_id
HAVING COUNT(*) > 1;
"""

cursor.execute(query)

for row in cursor.fetchall():
    print(row)


print("\nMISSING COMPANY NAMES")

query = """
SELECT
    row_id,
    job_id,
    company_name
FROM job_postings
WHERE company_name IS NULL
   OR company_name = '';
"""

cursor.execute(query)

for row in cursor.fetchall():
    print(row)

print("\nIMPOSSIBLE DATES")

query = """
SELECT
    row_id,
    job_id,
    posted_date,
    closing_date
FROM job_postings
WHERE closing_date < posted_date;
"""

cursor.execute(query)

for row in cursor.fetchall():
    print(row)
print("\nINVALID SALARY RANGES")

query = """
SELECT
    row_id,
    job_id,
    salary_min,
    salary_max
FROM job_postings
WHERE salary_min > salary_max;
"""

cursor.execute(query)

for row in cursor.fetchall():
    print(row)
print("\nMISSING JOB TITLES")

query = """
SELECT
    row_id,
    job_id,
    job_title
FROM job_postings
WHERE job_title IS NULL
   OR job_title = '';
"""

cursor.execute(query)

for row in cursor.fetchall():
    print(row)
connection.close()
