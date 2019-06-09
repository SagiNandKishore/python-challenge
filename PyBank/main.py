import os
import csv

#Your task is to create a Python script that analyzes the records to calculate each of the following:
#
#The total number of months included in the dataset
#
#The net total amount of "Profit/Losses" over the entire period
#
#The average of the changes in "Profit/Losses" over the entire period
#
#The greatest increase in profits (date and amount) over the entire period
#
#The greatest decrease in losses (date and amount) over the entire period

csvfile = os.path.join("Resources","budget_data.csv")

with open(csvfile, mode="r") as csv_fp:
    csvreader = csv.reader(csv_fp,delimiter=",")


    # Extract the header row
    header=next(csvreader)
    print(header)

    timeperiod = []
    amount = []

    for record in csvreader:
        timeperiod.append(record[0])
        amount.append(int(record[1]))
    
    totalAmount = sum(amount)
    print(f"Total amount is {totalAmount}")
    
    print(timeperiod[:5])
    print(amount[:5])