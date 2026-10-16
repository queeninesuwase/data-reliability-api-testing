SELECT
    job_id,
    COUNT(*) AS occurrences
FROM job_postings
GROUP BY job_id
HAVING COUNT(*) > 1;

SELECT
    row_id,
    job_id,
    company_name
FROM job_postings
WHERE company_name IS NULL
   OR company_name = '';

SELECT
    row_id,
    job_id,
    posted_date,
    closing_date
FROM job_postings
WHERE closing_date < posted_date;
SELECT
    row_id,
    job_id,
    salary_min,
    salary_max
FROM job_postings
WHERE salary_min > salary_max;

SELECT
    row_id,
    job_id,
    job_title
FROM job_postings
WHERE job_title IS NULL
   OR job_title = '';