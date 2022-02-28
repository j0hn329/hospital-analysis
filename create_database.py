import sqlite3
import pandas as pd
from pandas import DataFrame

conn = sqlite3.connect("Hospital.db")
c = conn.cursor()

c.executescript('''
    DROP TABLE IF EXISTS hospital_info;
    DROP TABLE IF EXISTS quality_of_care;
    DROP TABLE IF EXISTS reviews;
    ''')

c.execute('''CREATE TABLE IF NOT EXISTS hospital_info
        (
        provider_id INTEGER PRIMARY KEY,
        hospital_name TEXT,
        city TEXT,
        state TEXT,
        county TEXT,
        type TEXT,
        ownership TEXT,
        rating INTEGER
        );''')

c.execute('''CREATE TABLE IF NOT EXISTS quality_of_care
        (
        qoc_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        provider_id INTEGER,
        mortality_nat_comparison TEXT,
        safety_of_care_nat_comparison TEXT,
        readmission_nat_comparison TEXT,
        patient_experience_nat_comparison TEXT,
        effectiveness_of_care_nat_comparison TEXT,
        timeliness_of_care_nat_comparison TEXT,
        efficient_imaging_nat_comparison TEXT,
        FOREIGN KEY (provider_id) REFERENCES hospital_info(provider_id)
        );''')

c.execute('''CREATE TABLE IF NOT EXISTS reviews
        (
         rev_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
         provider_id INTEGER,
         number_of_reviews INTEGER,
         last_review INTEGER,
         reviews_per_month INTEGER,
         FOREIGN KEY (provider_id) REFERENCES hospital_info(provider_id)
        );''')

conn.commit()

read_hospital_data = pd.read_csv(
    'DSA8002 (2021-2022)-dataset.csv', encoding='unicode_escape')
read_hospital_data.to_sql("Hospital", conn, if_exists='append', index=False)

conn.commit()

c.execute('''
INSERT INTO hospital_info (provider_id, hospital_name, city, state,
    county, type, ownership, rating)
SELECT DISTINCT Hospital.`Provider ID`, Hospital.`Hospital Name`, Hospital.City,
    Hospital.State, Hospital.`County Name`, Hospital.`Hospital Type`,
    Hospital.`Hospital Ownership`, Hospital.`Hospital overall rating`
FROM Hospital
''')

c.execute('''
INSERT INTO quality_of_care(provider_id,
    mortality_nat_comparison, safety_of_care_nat_comparison,
    readmission_nat_comparison, patient_experience_nat_comparison,
    effectiveness_of_care_nat_comparison, timeliness_of_care_nat_comparison,
    efficient_imaging_nat_comparison)
SELECT DISTINCT Hospital.`Provider ID`,
    Hospital.`Mortality national comparison`, Hospital.`Safety of care national comparison`,
    Hospital.`Readmission national comparison`, Hospital.`Patient experience national comparison`,
    Hospital.`Effectiveness of care national comparison`, Hospital.`Timeliness of care national comparison`,
    Hospital.`Efficient use of medical imaging national comparison`
FROM Hospital
''')

c.execute('''
INSERT INTO reviews(provider_id, number_of_reviews, last_review, reviews_per_month)
SELECT DISTINCT Hospital.`Provider ID`, Hospital.`Hospital-number_of_reviews`,
    Hospital.last_review, Hospital.reviews_per_month
FROM Hospital
''')

c.execute('''
DELETE FROM hospital_info
WHERE rating ='Not Available'
''')

conn.commit()
