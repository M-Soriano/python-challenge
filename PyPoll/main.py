import csv
import os
#code from starter code  from line 1 to 7(make some changes)
# Files to load and output (update with correct file paths)
fl = os.path.join("Resources", "election_data.csv")  # Input file path#generic starter code, some modifications 
fo = os.path.join("analysis", "election_analysis.txt")  # Output file path#generic starter code, some modifications 


#initial variable
votes = 0
#list of candidates
candidates=[]
#dictionary for candiates votes
candicates_votes = {}
#dictionary for candiates percentage
percent = {}
# inittializing percentage_out as string
percentage_out =""
# inittializing winner as string
winner = ""

with open(fl) as ed: # ed is election data #generic starter code, some modifications 

    data = csv.reader(ed, delimiter=",")# finding the delimiter #generic starter code, some modifications 


    #skip the header
    header = next(data)#generic starter code, some modifications 

    

    #looping through row
    for row in data:
         # Print a loading indicator (for large datasets)
        #print(". ", end="")
        
        #All votes count
        votes += 1

        #find candidates by if statement with not in
        if row[2] not in  candidates:
            candidates.append(row[2])
            # adding key and  value dictionary
            candicates_votes[row[2]]= 1
        else:
            # adding to a value of a key to keep count
            candicates_votes[row[2]] += 1


    # calculating the percent of votes for each canditates
    for outcome in candidates:
        pt = float(candicates_votes[outcome])/float(votes)
        
        #saving the percent in dictionary for quick reference/ not needed
        percent[outcome] = pt

  #saving the percent in dictionary for quick reference
        #inputing a print funtcion to a variable of the result to make it easier to print with output print statement
        percentage_out += f"\n{outcome}: {pt:.3%} ({votes})\n"

#getting the winner by using max and get() function. 
#use example to get this result
#reference website https://note.nkmk.me/en/python-dict-value-max-min/
winner = max(percent,key=percent.get)

output = (f"\nElection Results\n\n"
          f"-------------------------\n\n"
          f"Total Votes: {votes}\n\n"
          f"{percentage_out}\n\n"
          f"-------------------------\n\n"
          f"Winner: {winner}\n\n"       
          f"-------------------------\n\n"   
          )

print(output)

#writing results to a text files
with open(fo,"w") as txt_file:#generic starter code, some modifications 

    txt_file.write(output)