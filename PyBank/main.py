#import csv and os
import os
import csv

#path for file
cvspathpybank=os.path.join("Resources","budget_data.csv")

#open with and creating path

with open(cvspathpybank) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header=next(csvreader)

    #putting varables to 0 to prepare to calculate 
    month=0 
    total=0
    prev_rev = 0
    ch_total = 0
    pre_change=0
    pre_change_min=0
    max_date=0
    min_date=0

    # for loop to count the number of month (rows) and make the date into a list
    for i,row in enumerate(csvreader):
        rev =  float(row[1])
        total+= rev
        month += 1 
        #getting rid of the first change bc it is zero
        if i == 0:
            prev_rev = rev
        
        #finding average change
        change = rev - prev_rev
        ch_total += change
        prev_rev = rev

        #finding greatest profit increase
        if change > pre_change:
            pre_change=change
            max_date= row[0]

        #finding decrease in profits
        if change < pre_change_min:
            pre_change_min = change
            min_date= row[0]
#output 
output = f'''
     Financial Analysis
  ----------------------------
  Total Months: {month}
  Total: ${total:,.0f}
  Average  Change: $ {ch_total/(month-1):,.2f}
  Greatest Increase in Profits: {max_date} ({pre_change:,.2f})
  Greatest Decrease in Profits: {min_date}({pre_change_min:,.2f})
 '''

print(output)

with open("output.txt", "a") as f:
    print(output, file=f)


