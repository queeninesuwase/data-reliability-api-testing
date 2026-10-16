import csv
import random
from datetime import date, timedelta
from pathlib import Path


random.seed(42)

OUTPUT_FILE = Path("data/job_postings.csv")

companies = [
    "Apex Systems",
    "BrightPath",
    "CloudPeak",
    "Delta Finance",
    "EcoWorks",
    "FinEdge",
    "GreenGrid",
    "Horizon Retail",
    "Insight Labs",
    "Jambo Logistics"
]

job_titles = [
    "Software Engineer",
    "QA Engineer",
    "Data Analyst",
    "Data Engineer",
    "Product Manager",
    "Backend Engineer",
    "Frontend Engineer",
    "DevOps Engineer"
]

locations = [
    "Nairobi",
    "Kigali",
    "Lagos",
    "Accra",
    "Cape Town",
    "Remote"
]

rows = []

start_date = date(2026, 1, 1)

for i in range(1, 601):
    posted_date = start_date + timedelta(days=random.randint(0, 200))
    closing_date = posted_date + timedelta(days=random.randint(7, 40))

    salary_min = random.randint(30000, 80000)
    salary_max = salary_min + random.randint(5000, 40000)

    rows.append([
        f"JOB{i:04d}",
        random.choice(companies),
        random.choice(job_titles),
        random.choice(locations),
        posted_date.isoformat(),
        closing_date.isoformat(),
        salary_min,
        salary_max
    ])


rows[9][1] = ""
rows[19][1] = ""
rows[29][1] = ""

rows[99][2] = ""
rows[109][2] = ""
rows[119][2] = ""

for index in [39, 49, 59]:
    posted = date.fromisoformat(rows[index][4])
    rows[index][5] = (posted - timedelta(days=5)).isoformat()


for index in [69, 79, 89]:
    rows[index][6] = 100000
    rows[index][7] = 70000

rows.extend([
    rows[4].copy(),
    rows[14].copy(),
    rows[24].copy(),
    rows[34].copy(),
    rows[44].copy()
])


with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow([
        "job_id",
        "company_name",
        "job_title",
        "location",
        "posted_date",
        "closing_date",
        "salary_min",
        "salary_max"
    ])

    writer.writerows(rows)


print(f"Created {len(rows)} job-posting records.")
print(f"Saved to {OUTPUT_FILE}")