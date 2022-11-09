import pandas as pd
import glob

# Store the files paths in a list
filepaths = glob.glob("invoices/*.xlsx")  # get everything that ends with a. xlsx

# Read the individual files
for individual_filepath in filepaths:
    df = pd.read_excel(individual_filepath, sheet_name="Sheet 1")
    print(df)