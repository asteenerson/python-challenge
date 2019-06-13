# Import Modules
import os
import csv

# Path the CSV file
budget_csv = os.path.join("budget_data.csv")

# Create Titles for Rows
date = str(budget_csv[0])
profit_loss = int(budget_csv[1])

