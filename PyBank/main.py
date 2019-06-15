# Import Modules
import os
import csv

# Path the CSV file
budget_csv = os.path.join("budget_data.csv")

# Create lists for data and assign values
dates = []
pl = []
net_total = 0

# funciton to return month and amount for greatest increase and greatest decrease
def print_maxmin(budget):
    month = str(budget[0])
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
    
    # Skip Header
    next(csvreader)    

    # Loop through the CSV file to add to arrays
    for row in csvreader:
        dates.append(row[0])
        pl.append(row[1])  
        
    # Loop through pl to sum net total
    for i in pl:
        net_total = sum(int(i) for i in pl)
     
    # Subtract monthly values in pl(profit/losses) array for difference. Then average the difference for the average change
    value1 = (pl[1:])
    value2 = (pl)
    diff = [int(value1) - int(value2) for value1, value2 in zip(value1, value2)]
    average_change= (sum(diff)/len(diff))     
   
    #--------------------
    #Print Analysis
    #--------------------
    print("Financial Analysis")
    print("----------------------------")

    # dates is the count of row[0]
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

    # Change pl(profit/losses) array to integers in order to find the true max and min increases
    pl_int = [int(j) for j in pl]
    max_value = max(pl_int)
    min_value = min(pl_int)
    
    #Reset CSV Loop
    data.seek(0)
    
    # Print from the print_minmax function for greatest increase and decrease
    for row in csvreader:
        if str(max_value) == row[1]:
            print_maxmin(row)

        if str(min_value) == row[1]:
            print_maxmin(row)