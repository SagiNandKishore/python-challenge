import os
import csv

#Create a function that will print both to a terminal and also write the text
#to a separate file
def print_output(text, outfile):
    print(text)
    print(text, file=outfile)

csvfile = os.path.join("Resources", "election_data.csv")

with open(csvfile, mode="r") as csv_fp:
    csvreader = csv.reader(csv_fp,delimiter=",")

    # Extract the header row
    header=next(csvreader)
    #print(header)

    #Capture the summary tabulations of 
    #voter per candidate in a dictionary variable
    electionResults={}
    totalVotes = 0
    for record in csvreader:
        totalVotes += 1

        #If a candidate had already received a vot, then increment
        #their vote count else initialize the vote count to 1
        if record[2] in electionResults:
            electionResults[record[2]] += 1
        else:
            electionResults[record[2]] = 1

outputFile = os.path.join("Output","election_results_summary.txt")
headerLength = 35   #Determines the number of "-" character to be printed in the output

with open(outputFile, "w") as outfile:
    print_output("Election Results", outfile)
    print_output("-" * headerLength, outfile)
    print_output(f"Total Votes: {totalVotes:,d}", outfile)
    print_output("-" * headerLength, outfile)

    winnerVoteCount = 0
    winner=""
    for candidate in electionResults:
        print_output(f"{candidate:9}: {electionResults[candidate]/totalVotes:2.3%} ({electionResults[candidate]:,d})", outfile)
        if electionResults[candidate] >= winnerVoteCount:
            winnerVoteCount = electionResults[candidate]
            winner = candidate
    print_output("-" * headerLength, outfile)
    print_output(f"Winner: {winner}", outfile)
    print_output("-" * headerLength, outfile)