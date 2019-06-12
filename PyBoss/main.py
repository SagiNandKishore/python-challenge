import os
import csv
from datetime import datetime

#Define the mapping between state name and state code
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',

}

#Get a pointer to the CSVFile and Read the data from CSVFile
csvfile = os.path.join("employee_data.csv")

#Read the data from CSVFile
with open(csvfile, "r") as fp:
    csvreader = csv.reader(fp, delimiter =",")

    #Skip the header
    header = next(csvreader)
    print(header)

    #Generate the converted data using list comprehension
    converted_data = []
    converted_data = [[int(emprecords[0]),
                       emprecords[1].rsplit(" ")[0], 
                       emprecords[1].rsplit(" ")[1], 
                       datetime.strptime(emprecords[2],"%Y-%m-%d").strftime("%m/%d/%Y"), 
                       "***-**-"+emprecords[3][-4:],
                       us_state_abbrev[emprecords[4]]]
                    for emprecords in csvreader]
    
    #print(converted_data[:5], sep = "\n")

#Write the converted data back to a output file
outputfile = os.path.join("Output", "converted_employee_data.csv")
with open(outputfile, "w") as outfile:
    csvwriter = csv.writer(outfile, dialect="excel", delimiter = ",")
    csvwriter.writerows(converted_data)