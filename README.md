# PayScale Salary Analysis

A Python project that scrapes and analyses college major salary data from PayScale's 2008 survey of 1.2 million Americans with bachelor's degrees.

## What This Project Does

1. **Scrapes** salary data from the Wayback Machine archive of PayScale.com using Selenium
2. **Analyses** the data using pandas and exports insights to Excel

## Key Questions Answered

- Which college majors have the highest starting salaries?
- Which majors have the highest mid-career earnings?
- Which degrees show the most salary growth over a career?
- Which majors have the highest percentage of graduates who find their work meaningful?

## Project Structure
payscale-salary-analysis/
main.py # Selenium scraper
analysis.py # Pandas analysis
highest_salaries_by_major.csv # Raw scraped data
salary_analysis.xlsx # Analysis output (4 sheets)
requirements.txt # Dependencies
.gitignore


## Output

The `salary_analysis.xlsx` file contains 4 sheets:
- **Early Career Pay** → Top 5 and Bottom 5 majors by starting salary
- **Mid-Career Pay** → Top 5 and Bottom 5 majors by mid-career salary
- **Salary Growth** → Top 5 and Bottom 5 majors by salary increase over career
- **High Meaning** → Top 5 and Bottom 5 majors by % of graduates who find work meaningful

## Technologies Used

- Python 3
- Selenium → web scraping
- Pandas → data analysis
- openpyxl → Excel export

## Data Source

PayScale College Salary Report (2008) via Wayback Machine:
https://web.archive.org/web/20180704193224/https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors
