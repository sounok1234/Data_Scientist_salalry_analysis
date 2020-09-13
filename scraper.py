import glassdoor_scraper as gs
import pandas as pd

path = "C:/Users/sounok.sarkar/Desktop/DS_salaries/chromedriver.exe"

df = gs.get_jobs('data scientist', 15, False, path, 15)

df.to_csv('data_scientist_jobs.csv', index=False)