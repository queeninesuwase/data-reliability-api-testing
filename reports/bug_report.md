# Sample Bug Report

## Title

Job posting JOB0040 has a closing date earlier than its posted date

## Environment

- Dataset: data/job_postings.csv
- Database: SQLite
- Validation method: SQL data-quality check

## Steps to Reproduce

1. Load the job-posting dataset into the database.
2. Run the impossible-date SQL query.
3. Locate the record with job_id JOB0040.
4. Compare the posted_date and closing_date values.

## Expected Result

The closing date should be equal to or later than the posted date.

## Actual Result

- job_id: JOB0040
- posted_date: 2026-02-18
- closing_date: 2026-02-13

The closing date is 5 days earlier than the posted date.

## Severity

Medium

## Impact

This issue can cause incorrect calculations of how long a job posting was active and may affect time-based workforce analysis.

## Suggested Fix

Add a validation rule requiring:

closing_date >= posted_date

Records that fail this rule should be rejected, corrected, or flagged for review before release.

## Retesting

After the issue is fixed, run the impossible-date SQL check again and confirm that JOB0040 is no longer returned.
