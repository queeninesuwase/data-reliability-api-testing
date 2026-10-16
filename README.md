# Revelio Labs QA Build Task

## Overview

This project was created as part of the Revelio Labs QA Engineer application task.

It demonstrates two main areas of quality assurance:

1. Automated API testing using Python and pytest.
2. Data-quality testing using SQL on a synthetic job-posting dataset.

The project also includes a data-quality report and a sample bug report based on issues identified during testing.

---

## Technologies Used

- Python
- pytest
- requests
- SQL
- SQLite
- Git
- GitHub

---

## Project Structure

```text
revelio-qa-task/
├── api_tests/
│   └── test_weather_api.py
│
├── data/
│   ├── job_postings.csv
│   └── job_postings.db
│
├── reports/
│   ├── bug_report.md
│   └── data_quality_report.md
│
├── sql/
│   └── data_quality_checks.sql
│
├── generate_job_data.py
├── setup_db.py
├── run_sql_checks.py
├── requirements.txt
└── README.md
```

---

# Part 1: API Testing

## API Used

The automated tests use the public Open-Meteo weather API.

The API allows weather information to be requested using parameters such as latitude, longitude, weather variables and timezone.

---

## Test Coverage

A total of 11 automated API tests were created.

The tests cover:

- Successful API requests
- Expected response fields
- Response data types
- Hourly data consistency
- Invalid latitude
- Invalid longitude
- Non-numeric latitude input
- Missing required latitude
- Invalid weather variables
- Boundary-value testing
- Timezone handling

The test suite includes positive, negative and boundary test scenarios.

For example, latitude `90` was tested as a valid boundary value, while a value above the valid range was tested to confirm that the API correctly rejects invalid input.

---

## Running the API Tests

### 1. Create a virtual environment

```bash
uv venv env
```

### 2. Activate the environment

```bash
source env/bin/activate
```

### 3. Install the dependencies

```bash
uv pip install -r requirements.txt
```

### 4. Run the tests

```bash
python -m pytest api_tests/test_weather_api.py -v
```

The API tests require an internet connection because they send requests to a live public API.

---

# Part 2: Data Quality Testing

## Dataset

The project contains a synthetic job-posting dataset with 605 records.

The dataset includes the following fields:

- job_id
- company_name
- job_title
- location
- posted_date
- closing_date
- salary_min
- salary_max

The dataset was intentionally created with several data-quality issues so that SQL validation checks could be written to detect them.

---

## Generate the Dataset

Run:

```bash
python generate_job_data.py
```

This creates:

```text
data/job_postings.csv
```

---

## Create the SQLite Database

Run:

```bash
python setup_db.py
```

This loads the CSV records into an SQLite database.

The generated database is:

```text
data/job_postings.db
```

---

## SQL Data Quality Checks

The SQL checks look for:

1. Duplicate job IDs
2. Missing company names
3. Missing job titles
4. Closing dates earlier than posting dates
5. Minimum salaries greater than maximum salaries

The SQL queries are stored in:

```text
sql/data_quality_checks.sql
```

---

## Run the SQL Checks

Run:

```bash
python run_sql_checks.py
```

---

## Data Quality Findings

The checks identified the following issues:

| Data Quality Issue | Result |
|---|---:|
| Duplicate job IDs | 5 |
| Missing company names | 3 |
| Missing job titles | 3 |
| Impossible date combinations | 3 |
| Invalid salary ranges | 3 |

These issues demonstrate problems related to data uniqueness, completeness and validity.

---

## Why These Issues Matter

Duplicate records can cause job-posting counts and hiring trends to be overstated.

Missing company names can make it difficult to connect job postings to company-level analysis.

Missing job titles can affect job-category and hiring-trend analysis.

Closing dates earlier than posting dates can create incorrect calculations of how long a job was available.

Invalid salary ranges can affect salary averages, distributions and compensation analysis.

---

## Data Quality Report

A detailed explanation of the findings, their possible impact and how they could be prevented is available in:

```text
reports/data_quality_report.md
```

---

# Sample Bug Report

The project also contains a sample bug report based on one of the invalid date records detected by the SQL checks.

It includes:

- Bug title
- Environment
- Steps to reproduce
- Expected result
- Actual result
- Severity
- Impact
- Suggested fix
- Retesting approach

The report is available in:

```text
reports/bug_report.md
```

---

# QA Approach

The project tests both software behaviour and data quality.

For API testing, I checked whether the API:

- Accepts valid requests
- Rejects invalid requests
- Returns the expected response structure
- Returns appropriate data types
- Handles missing parameters
- Handles boundary values correctly

For data-quality testing, I checked:

- Uniqueness
- Completeness
- Validity
- Logical consistency

The goal was not only to check whether the software runs successfully, but also whether the data returned and stored by the system makes sense and can be trusted.


