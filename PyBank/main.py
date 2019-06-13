# Import Modules
import os
import csv

# Path the CSV file
budget_csv = os.path.join("budget_data.csv")

# Read in the CSV file
with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip Header
    next(csvreader)
    
    #Count the number of rows for total month count
    total_months = list(csvreader)

    
    
    #for row in csvreader:
        #total_months[row[0]].append(row)
        #print(total_months)


    # Final print of financial analysis
    print("Financial Analysis")
    print("----------------------------")
    print(f'Total Months: {len(total_months)}')
    
