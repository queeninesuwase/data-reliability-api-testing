# Data Quality Report

## Dataset

The dataset contains 605 synthetic job-posting records. It was created to simulate common data-quality problems that could affect workforce analytics.

## Finding 1: Duplicate Job IDs

The SQL duplicate check identified 5 job IDs that appear more than once.

### Why this matters

Duplicate records can cause job-posting counts to be overstated and may affect hiring trend analysis.

### Possible prevention

A uniqueness check should be applied to job IDs before records are added to the final dataset.

## Finding 2: Missing Company Names

The dataset contains 3 records with missing company names.

### Why this matters

Without a company name, the job posting may not be correctly grouped or linked to company-level analysis.

### Possible prevention

Required fields such as company name should be validated before the data is accepted.

## Finding 3: Missing Job Titles

The dataset contains 3 records with missing job titles.

### Why this matters

Missing job titles can reduce the accuracy of job-category, skills and hiring-trend analysis.

### Possible prevention

Job title should be treated as a required field and checked before records are loaded into the dataset.

## Finding 4: Impossible Dates

The dataset contains 3 records where the closing date is earlier than the posting date.

### Why this matters

This could create incorrect calculations for how long a job was open and affect time-based analysis.

### Possible prevention

A validation rule should ensure that:

closing_date >= posted_date

## Finding 5: Invalid Salary Ranges

The dataset contains 3 records where salary_min is greater than salary_max.

### Why this matters

Invalid salary ranges could affect salary averages, distributions and other compensation analysis.

### Possible prevention

A validation rule should require:

salary_min <= salary_max

## Conclusion

The checks show how SQL can be used to identify issues related to uniqueness, completeness and validity before data is used for analysis. Running these checks before a dataset is released would help prevent incorrect information from reaching users.
