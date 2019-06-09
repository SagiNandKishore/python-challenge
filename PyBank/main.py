import os
import csv

def print_output(text, filepointer):
    print(text)
    print(text, file=filepointer)

csvfile = os.path.join("Resources","budget_data.csv")

with open(csvfile, mode="r") as csv_fp:
    csvreader = csv.reader(csv_fp,delimiter=",")

    # Extract the header row
    header=next(csvreader)
    #print(header)

    timeperiod = []
    amount = []
    change=[]

    for record in csvreader:
        timeperiod.append(record[0])
        amount.append(int(record[1]))
        totalAmount = '${:,.2f}'.format(sum(amount))                #Format the totalAmount variable to be recognized as currency
        if len(timeperiod) > 1:
            change.append(amount[-1] - amount[-2])                  #The change is the last "amount" list value - second last "amount" list value
    
    averageChange = '${:,.2f}'.format(sum(change)/len(change))      #Format the totalAmount variable to be recognized as currency
    
    maxAmountIncrease='${:,.2f}'.format(max(change))                #max of data in change array is the max amount increase
    maxAmountPeriod = timeperiod[change.index(max(change)) + 1]     #The first element in change array corresponds to second timeperiod. Since it is not mentioned that the start of the budget_data.csv corresponds to the start of the company, we cannot assume that the first record in budget_data.csv corresponds to a change equal to first record in budget_data.csv. So to get the actual time period, lookup the index of maximum change and the time period would the index + 1 element in the "timeperiod" list.

    minAmountDecrease='${:,.2f}'.format(min(change))
    minAmountPeriod = timeperiod[change.index(min(change)) + 1]

output_file = os.path.join("Output", "budget_data_output.txt")

with open(output_file,"w") as outfile:
    print_output("Financial Analysis", outfile)
    print_output("-" * 28, outfile)
    print_output(f"Total Months: {len(timeperiod)}", outfile)
    print_output(f"Total: {totalAmount}", outfile)
    print_output(f"Average Change: {averageChange}", outfile)
    print_output(f"Greatest Increase in Profits: {maxAmountPeriod} ({maxAmountIncrease})", outfile)
    print_output(f"Greatest Decrease in Profits: {minAmountPeriod} ({minAmountDecrease})", outfile)