

import pandas as pd
import json

# -----------------------------
# Read CSV File
# -----------------------------
print("Reading CSV File...\n")

csv_file = "patient_intake.csv"

df_csv = pd.read_csv(csv_file)

print("CSV Data:")
print(df_csv)

print("\nExtracted Fields from CSV:")

for index, row in df_csv.iterrows():
    print(f"""
Patient ID       : {row['Patient_ID']}
Age              : {row['Age']}
Gender           : {row['Gender']}
Primary Complaint: {row['Primary_Complaint']}
""")

# -----------------------------
# Read JSON File
# -----------------------------
print("\n==============================")
print("Reading JSON File...\n")

json_file = "patient_intake.json"

with open(json_file, "r") as file:
    patients = json.load(file)

print("Extracted Fields from JSON:")

for patient in patients:
    print(f"""
Patient ID       : {patient['Patient_ID']}
Age              : {patient['Age']}
Gender           : {patient['Gender']}
Primary Complaint: {patient['Primary_Complaint']}
""")

print("\nParsing completed successfully!")