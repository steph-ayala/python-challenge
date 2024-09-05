
import os
import csv 
import sys 


script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

csvpath = os.path.join('Resources', 'budget_data.csv')
#csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    #The total number of months included in the dataset
    csvrows = []    
    for row in csvreader:
        #print(row)
        csvrows.append(row)

with open(os.path.join("Analysis", "Analysis.txt"), "w") as file:         
    num_of_months = len(csvrows)
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {num_of_months}")
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {num_of_months}\n")


    #The net total amount of "Profit/Losses" over the entire period
    #print(csvrows[0][1])
    sum = 0
    for row in csvrows:
        row[1] = int(row[1])
        sum += row[1]
    print(f"Total: ${sum}")
    file.write(f"Total: ${sum}\n")

    #The changes in "Profit/Losses" over the entire period, and then the average of those changes
    net_change_lst = []
    total_net_change = 0

    for i in range(1, len(csvrows)):
        current_profit_loss = int(csvrows[i][1])
        previous_profit_loss = int(csvrows[i - 1][1])
        net_change = current_profit_loss - previous_profit_loss
        net_change_lst.append(net_change)
        total_net_change += net_change


    average_change = total_net_change / (len(csvrows) - 1)
    print(f"Average Change: ${round(average_change, 2)}")
    file.write(f"Average Change: ${round(average_change, 2)}\n")


    #The greatest increase in profits (date and amount) over the entire period
    greatest_increase = 0
    greatest_increase_date = ""

    for i in range(1, len(csvrows)):
        current_profit_loss = int(csvrows[i][1])
        previous_profit_loss = int(csvrows[i - 1][1])
        net_change = current_profit_loss - previous_profit_loss

        if net_change > greatest_increase:
            greatest_increase = net_change
            greatest_increase_date = csvrows[i][0]

    print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
    file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")

    #The greatest decrease in profits (date and amount) over the entire period
    greatest_decrease = 0
    greatest_decrease_date = ""

    for i in range(1, len(csvrows)):
        current_profit_loss = int(csvrows[i][1])
        previous_profit_loss = int(csvrows[i - 1][1])
        net_change = current_profit_loss - previous_profit_loss  

        if net_change < greatest_decrease:
            greatest_decrease = net_change
            greatest_decrease_date = csvrows[i][0]

    print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")