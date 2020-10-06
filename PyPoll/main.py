# Dependencies
import os
import csv

# Import file
csvpath = os.path.join(".","Resources", "electiondata.csv")

# Define auxiliary lists
totalcandidatevotes = []
uniquecandidatelist = []

# Initialize votes per candidate
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

# Open file and read it
with open(csvpath, newline='') as election:
    reader = csv.reader(election, delimiter=',')
    csv_header = next(reader)    

    # Get unique candidates and a list with all votes
        # A complete list of candidates who received votes
        # The total number of votes cast 

    for row in reader:
        totalcandidatevotes.append(row[2])
        if row[2] not in uniquecandidatelist:
            uniquecandidatelist.append(row[2])
        
        #Get total votes for each candidate                        
        if row[2] == 'Khan':     khanvotes += 1
        elif row[2] == 'Correy': correyvotes += 1
        elif row[2] == 'Li':     livotes += 1
        else:                    otooleyvotes += 1
    
    # Calculate
        # The total number of votes each candidate won
        # The percentage of votes each candidate won
    totalvotes = len(total_candidate_votes)
    votespercandidate = [khanvotes, correyvotes, livotes, otooleyvotes]
    percentagevotes = [(div / totalvotes)*100 for div in votespercandidate]
    
    # Get the winner of the election based on popular vote.
    max_votes = max(votes_per_candidate)        
    winner = uniquecandidatelist[ votespercandidate.index(maxvotes) ]        

    # PRINT results to Terminal
    report = (  '\n'
                'Election Results\n'
                '---------------------------\n'
                f'Total Votes: {total_votes}\n'
                f'Khan: {votespercandidate[0]} {percentagevotes[0]:.3f} %\n'
                f'Correy: {votespercandidate[1]} {percentagevotes[1]:.3f} %\n'
                f'Li: {votespercandidate[2]} {percentagevotes[2]:.3f} %\n'
                f"O'Tooley: {votespercandidate[3]} {percentagevotes[3]:.3f} %\n"
                '---------------------------\n'
                f'Winner is: {winner}'
            )
    print(report)


# Define an Output path and a filename for that output.
outputfile = os.path.join(".", "Analysis", "electionresults.txt")


with open(outputfile,"w") as file:
    
    # Write methods to print to Financial Analysis.
    file.write(report)