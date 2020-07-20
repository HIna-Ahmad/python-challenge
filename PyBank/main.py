#Your task is to create a Python script that analyzes 
# the records to calculate each of the following:

#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The average of the changes in "Profit/Losses" over the entire period
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period

# Path to collect data from the Resources folder
import os
import csv
total_months = 0
total_net = 0
#sum of all changes, then divide by total number of months minus one
curr_profit = 0
prev_profit = 0
sum_changes = 0

#dirname = os.path.dirname(__file__)
#budget_data = os.path.join(dirname, "budget_data.csv")

with open ("../PyBank/Resources/budget_data.csv") as data:
    data = csv.reader(data)
    csvheader = next(data)
  
    first_row = next(data)
    #runs once 
    total_months = 1
    #assigning net value to item in first row data
    total_net = int(first_row[1])
    #keeping track of whats in first row data
    prev_profit = int(first_row[1])
    max_profit = int(first_row[1])
    max_date = str(first_row[0])
    min_profit = int(first_row[1])
    min_date = str(first_row[0])
    
    
    for row in data:
        
        curr_profit = int(row[1])
        curr_date = str(row[0])
        sum_changes += abs(curr_profit - prev_profit) 
        total_months = total_months + 1
        total_net += int(row[1])
        prev_profit = curr_profit

       #going through each row to find max value 
        if curr_profit > max_profit:
            max_profit = curr_profit
            max_date = curr_date
            
        if curr_profit < min_profit:
            min_profit = curr_profit
            min_date = curr_date
   
   

            
            

print("Financial Analysis")
print("-------------------------------------------")
print(f"Total Months: {str(total_months)}")
print(f"Total: ${str(total_net)}")
print(f"Average change: ${int(sum_changes/(total_months-1))}")
print(f"Greatest Increase in Profit: {max_date} (${max_profit})")
print(f"Greatest Decrease in Profit: {min_date} (${min_profit})")



filepathtosave = ("python-challenge/PyBank/analysis/analysis.txt")
with open(filepathtosave, 'w', newline="") as text:
    text.write("Financial Analysis\n")
    text.write("-------------------------------------------\n")
    text.write(f"Total Months: {str(total_months)}\n")
    text.write(f"Total: ${str(total_net)}\n")
    text.write(f"Average change: ${int(sum_changes/(total_months-1))}\n")
    text.write(f"Greatest Increase in Profit: {max_date} (${max_profit})\n")
    text.write(f"Greatest Decrease in Profit: {min_date} (${min_profit})\n")