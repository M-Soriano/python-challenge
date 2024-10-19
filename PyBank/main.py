# Dependecy
import os
import csv

#Loding files  and outputing files
fl= os.path.join("Resources", "budget_data.csv")# input file
fo= os.path.join("analysis","analysis_results.txt")# output file

#variables
total_month = 0
total_net = 0
average_change = 0
greatest_increase =0
greatest_decrease =0
changes =[]
date=[]


with open(fl) as fd: # fd is financial data
    data = csv.reader(fd, delimiter=",")# finding the delimiter

    #skipping that header
    header = next(data)
    # extracting first row to avoid appending to netchange list
    row_one = next(data)
    # adding  a count because first row is beeen skip according to the starter code (would start count are one, but starter code has it as o)
    total_month += 1  
    # adding first to totalnet and making it an float for number with decimals.
    total_net += int(row_one[1])
    #setting the initial value for profit/loss
    change = float(row_one[1])
    










    for row in data:
        total_month += 1     
        total_net += int(row[1])
        
        #calculation of change        
        change = float(row[1]) - change
        
        #adding change to list called changes
        changes.append(float(change))
        #adding the month of change to list called date
        date.append(row[0])

        #refresh initial value for change
        change= float(row[1])

      
       



#finding average change with help of python built in function -sum and -len
average_change = sum(changes)/len(changes)
 #finding greatest increase and decrease in profit by using python built-in function
greatest_increase = int(max(changes))
greatest_decrease =int(min(changes))

#finding the date for the two variable about (list[list.index(element)])
date_inc = date[changes.index(greatest_increase)]
date_dec = date[changes.index(greatest_decrease)]




#putting print statements in result variable
results= (
    f"\nFinancial Analysis\n\n---------------------------------------\n\n"
    f"Total Months: {total_month}\n\n"
    f"Total: ${total_net}\n\n"
    f"Total Months: ${average_change:.2f}\n\n"
    f"Greatest Increase in profits: {date_inc} (${greatest_increase})\n\n"
    f"Greatest Decrease in Profits: {date_dec} (${greatest_decrease})"
)

print(results)

#writing results to a text file
with open(fo,"w" ) as txt_file:
    txt_file.write(results)
    



