
import os 
import csv

# csvpath = os.path.join('Resources', 'election_data.csv') 
csvpath = os.path.join('PyPoll', 'Resources', 'election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

# The total number of votes cast
    csvrows = []    
    for row in csvreader:
        #print(row)
        csvrows.append(row)

num_of_votes = len(csvrows)
#print(f"Total Votes: {num_of_votes}")


#A complete list of candidates who received votes
candidate_votes =  {"Charles Casper Stockham": 0,
                    "Diana DeGette": 0,
                    "Raymon Anthony Doane": 0
}

# Calculation of total votes per candidate
for row in csvrows:
    candidate = row[2]

    if candidate in candidate_votes:
        candidate_votes[candidate] += 1
    else:
        candidate_votes[candidate] = 1



with open("Analysis.txt", "w") as file:
    num_of_votes = len(csvrows)
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {num_of_votes}")   
    print("-------------------------")

    file.write("Election Results")
    file.write("-------------------------")
    file.write(f"Total Votes: {num_of_votes}")   
    file.write("-------------------------")

    # Calculation of percentage of votes each candidate won
    for candidate, votes in candidate_votes.items():
        percentage = (votes / num_of_votes) * 100
        print(f"{candidate}: {percentage:.3f}% ({votes})")
        file.write(f"{candidate}: {percentage:.3f}% ({votes})")
   
    # Winner based on maximun votes
    winner = max(candidate_votes, key=candidate_votes.get)
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")

    file.write("-------------------------")
    file.write(f"Winner: {winner}")
    file.write("-------------------------")