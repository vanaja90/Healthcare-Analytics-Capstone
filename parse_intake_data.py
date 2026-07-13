import pandas as pd

# Load the patient intake CSV file
csv_file_path = "patient_intake.csv"

# Read the CSV file into a DataFrame
df_csv = pd.read_csv(csv_file_path)

# Display the first few rows
print("First few rows of the CSV data:")
print(df_csv.head())
