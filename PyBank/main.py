# Import Modules
import os
import csv

# Path the CSV file
budget_csv = os.path.join("budget_data.csv")

# Read the CSV file
with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip Header
    next(csvreader)

    # Count the number of rows for total month count
    total_months = list(csvreader)

    # Read the CSV file
with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')    
    
    # Define net total
    net_total = 0

    # sum row1
    for row in csvreader:
        net_total = sum(int(row[1]) for row in csvreader)

# Read the CSV file
with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',') 
    
        #print(list1)

list2 = []

with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',') 
    


    #Test for regular Average
    #average = (int(net_total) / len(total_months))
    #print(average)


    # Final print of financial analysis
    #print("Financial Analysis")
    #print("----------------------------")
    #print(f'Total Months: {len(total_months)}')
    print(f'Total: ${net_total}')