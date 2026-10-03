import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import os

URL = "https://web.archive.org/web/20180704193224/https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors?page=33"

# GO WITH SELENIUM
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

# Click "See Full List" button
btn_element = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary.btn-block")
btn_element.click()

time.sleep(3)
table_element = driver.find_element(By.CSS_SELECTOR, ".table.table-bordered.table-striped.table-condensed")
# print(table_element) # Found table.

time.sleep(2)
row_ids = table_element.find_elements(By.XPATH, ".//*[@id]")

rows_data = []
for i in range(len(row_ids)):
    row = table_element.find_element(By.ID, f"datatable-{i}")
    cells = row.find_elements(By.CLASS_NAME, "hidden-xs")
    rows_data.append(cells)

time.sleep(1)
all_majors = []
for row in rows_data:
    row_data = []
    for cell in row:
        row_data.append(cell.text)
    all_majors.append(row_data)

driver.quit()

# Write header only if file is empty
file_exists = os.path.exists("highest_salaries_by_major.csv")

with open("highest_salaries_by_major.csv", mode="a", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    if not file_exists:
        writer.writerow(["Index", "Major", "Degree Type", "Early Career Pay", "Mid-Career Pay", "% High Meaning"]) # "% High Meaning" alumni who say their work makes the world a better place
    for row in all_majors:
        writer.writerow(row)
