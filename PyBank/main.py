# Import Modules
import os
import csv

# Path to the CSV file
budget_csv = os.path.join("budget_data.csv")

# Create lists for data and assign values
dates = []
pl = []
net_total = 0

# Funciton to return month and amount for greatest monthly increase and decrease
def print_maxmin(budget):
    month = budget[0]
    amount = int(budget[1])

    if amount > 0:
        print(f'Greatest Increase in Profits: {month} (${amount})')
        textfile.write(f'Greatest Increase in Profits: {month} (${amount})\n')

    else:
        print(f'Greatest Decrease in Profits: {month} (${amount})')
        textfile.write(f'Greatest Decrease in Profits: {month} (${amount})')

# Read the CSV file
data = open(budget_csv, 'r')
with data as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip header
    next(csvreader)    

    # Loop through the CSV file to add to lists
    for row in csvreader:
        dates.append(row[0])
        pl.append(row[1]) 


    # Loop through pl(profit/losses) to sum net total
    for i in pl:
        net_total = sum(int(i) for i in pl)
     
    # Subtract monthly values in pl(profit/losses) list of monthly differences
    value1 = (pl[1:])
    value2 = (pl)

    diff = [int(value1) - int(value2) for value1, value2 in zip(value1, value2)]

    # Average the difference for the average change
    average_change= (sum(diff)/len(diff))
    
    # Return the max and min differences between 2 months for greatest increase and decrease
    max_diff = max(diff)
    min_diff = min(diff)   
    
    #--------------------
    # Print Analysis
    #--------------------
    print("Financial Analysis")
    print("----------------------------")

    # Dates is the count of row[0]
    print(f'Total Months: {len(dates)}')
    print(f'Total: ${net_total}')
    print(f'Average Change: ${round(average_change,2)}')

    # Create and write results to text file
    textfile = open("Financial Analysis.txt", "w")

    textfile.write("Financial Analysis\n")
    textfile.write("----------------------------\n")
    textfile.write(f'Total Months: {len(dates)}\n')
    textfile.write(f'Total: ${net_total}\n')
    textfile.write(f'Average Change: ${round(average_change,2)}\n')

     
    # Create new table with zip to compare dates and monthly differences
    new_table = zip(dates[1:], diff)

    # Print from the print_minmax function for greatest monthly increase and decrease
    for j in new_table:
        if max_diff == j[1]:
            print_maxmin(j)
        
        if min_diff == j[1]:
            print_maxmin(j)  