# Import Modules
import os
import csv

# Path to the CSV file
budget_csv = os.path.join("election_data.csv")

# Create lists for data and assign values
votes = []
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

# Function to count the candidate name that occurs most in votes list and return the winners name 
def printwinner(votes):
    return max(set(votes), key = votes.count)

# Read the CSV file
data = open(budget_csv, 'r')
with data as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
   
    # Skip header
    next(csvreader)

    # Loop through the CSV file to add to lists
    for row in csvreader:
        votes.append(row[2]) 
    
    # Tally votes for each candidate
    for vote in votes:
        if vote == "Khan":
            khan_votes += 1
        if vote == "Correy":
            correy_votes += 1
        if vote == "Li":
            li_votes += 1
        if vote == "O'Tooley":
            otooley_votes += 1
 
    #--------------------
    # Print Results
    #--------------------
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {len(votes)}")
    print("-------------------------")
    # calculate and print % of votes by taking candidate votes / total votes
    print (f"Khan: {'{0:.3%}'.format(int(khan_votes) / len(votes))} ({khan_votes})")
    print (f"Correy: {'{0:.3%}'.format(int(correy_votes) / len(votes))} ({correy_votes})")
    print (f"Li: {'{0:.3%}'.format(int(li_votes) / len(votes))} ({li_votes})")
    print (f"O'Tooley: {'{0:.3%}'.format(int(otooley_votes) / len(votes))} ({otooley_votes})")
    print("-------------------------")   
    print(f"Winner: {printwinner(votes)}")
    print("-------------------------")

    # Create and write results to text file
    textfile = open("Election Results.txt", "w")

    textfile.write("Election Results\n")
    textfile.write("-------------------------\n")
    textfile.write(f"Total Votes: {len(votes)}\n")
    textfile.write("-------------------------\n")
    textfile.write (f"Khan: {'{0:.3%}'.format(int(khan_votes) / len(votes))} ({khan_votes})\n")
    textfile.write (f"Correy: {'{0:.3%}'.format(int(correy_votes) / len(votes))} ({correy_votes})\n")
    textfile.write (f"Li: {'{0:.3%}'.format(int(li_votes) / len(votes))} ({li_votes})\n")
    textfile.write (f"O'Tooley: {'{0:.3%}'.format(int(otooley_votes) / len(votes))} ({otooley_votes})\n")
    textfile.write("-------------------------\n")   
    textfile.write(f"Winner: {printwinner(votes)}\n")
    textfile.write("-------------------------\n")