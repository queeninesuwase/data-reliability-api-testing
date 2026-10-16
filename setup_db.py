import csv
import sqlite3


connection = sqlite3.connect("data/job_postings.db")
cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS job_postings")

cursor.execute("""
CREATE TABLE job_postings (
    row_id INTEGER PRIMARY KEY AUTOINCREMENT,
    job_id TEXT,
    company_name TEXT,
    job_title TEXT,
    location TEXT,
    posted_date TEXT,
    closing_date TEXT,
    salary_min INTEGER,
    salary_max INTEGER
)
""")

with open("data/job_postings.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        cursor.execute("""
        INSERT INTO job_postings (
            job_id,
            company_name,
            job_title,
            location,
            posted_date,
            closing_date,
            salary_min,
            salary_max
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            row["job_id"],
            row["company_name"] or None,
            row["job_title"],
            row["location"],
            row["posted_date"],
            row["closing_date"],
            int(row["salary_min"]),
            int(row["salary_max"])
        ))

connection.commit()

cursor.execute("SELECT COUNT(*) FROM job_postings")
count = cursor.fetchone()[0]

print(f"Database created successfully with {count} records.")

connection.close()
