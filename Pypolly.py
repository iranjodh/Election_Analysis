import os
import csv
csvpath = os.path.join('Resources','election_results.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    print(csvreader)
    header = next(csvreader)
    print(header)


    #for row in csvreader:
    #print(row)
file_to_save = os.path.join("Resources", "election_analysis.txt")
outfile = open(file_to_save, "w")
outfile.write ("Hello World")
outfile.close()


