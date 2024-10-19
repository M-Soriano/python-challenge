import csv
import os
#code from starter code  from line 1 to 7(make some changes)
# Files to load and output (update with correct file paths)
fl = os.path.join("Resources", "election_data.csv")  # Input file path
fo = os.path.join("analysis", "election_analysis.txt")  # Output file path

#initial variable
votes = 0
candidates=[]







with open(fl) as ed: # ed is election data
    data = csv.reader(ed, delimiter=",")# finding the delimiter

    #skip the header
    header = next(data)

    #looping through row
    for row in data:
        votes += 1








output = (f"\nElection Results\n\n"
          f"-------------------------\n\n"
          f"Total Votes: {votes}\n\n"
          
          
          
          
          
          
          )

print(output)


        
      