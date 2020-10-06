# Dependencies
import os
import csv

# Import file
csvpath = os.path.join(".","Resources","budget_data.csv")

# Define auxiliary lists
totalmonths = []
totalprofit = []
monthlychange = []

# Initialize variables
totalnetamount = 0
averagechange = 0
maxincrease = 0
maxdecrease = 0 

# Open file and read it
with open(csvpath) as budget:
    csvreader = csv.reader(budget, delimiter=',')
# with open(csvpath, newline='') as budget:
    # csvreader = csv.reader(budget, delimiter=',')
# with open(csvpath) as budget:
    # csvreader = csv.reader(budget)
    
    csvheader = next(csvreader)

for row in csvreader: 
    print(row)
            
# Calculate each of the following

    # total number of months included in the dataset
    totalmonths.append(row[0])            

    # net total amount of "Profit/Losses" over the entire period
    totalprofit.append(int(row[1]))
    totalnetamount += int(row[1])    

    # average of the changes in "Profit/Losses" over the entire period
for i in range(len(totalprofit)-1):        
    monthlychange.append(totalprofit[i+1]-totalprofit[i])
    
for i in range(len(monthlychange)):

    # averagechange = averagechange + monthlychange[i] 
    averagechange += monthlychange[i] 

    # greatest increase in profits (date and amount) over the entire period

if monthlychange[i] > maxincrease:
    maxincrease = monthlychange[i]

    # sum of monthly changes 
    maxincreaseindex = monthlychange.index(maxincrease) + 1

    # greatest decrease in losses (date and amount) over the entire period

if monthlychange[i] < maxdecrease:
    maxdecrease = monthlychange[i]
            
    maxdecreaseindex = monthlychange.index(maxdecrease) + 1
 
# Print the analysis
    
    report = (  "\n"
                "Financial Analysis\n"
                "------------------------------------\n"
                f'Total Months: {len(totalmonths)}\n'
                f'Total: ${totalnetamount}\n'
                f'Average Change: ${averagechange}\n'
                f'Greates Increase in Profits: ${maxincrease} in {totalmonths[maxincreaseindex]}\n'
                f'Greates Decrease in Profits: ${maxdecrease} in {totalmonths[maxdecreaseindex]}\n'
            )
    print(report)


# Define an output path and filename

output_file = os.path.join(".", "Analysis", "analysis.txt")

with open(outputfile,"w") as file:
    
    # Write methods to print to Financial Analysis.
    file.write(report)

    