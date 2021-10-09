#import csv and os
import os
import csv

#path for file
cvspathpypoll=os.path.join("Resources","election_data.csv")

#open with and creating path

with open(cvspathpypoll) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header=next(csvreader)

    # setting varables to 0 to prepare to calculate
    totalvotes=0
    khan=0
    Correy=0
    Li=0
    Otooley=0
    winner=""
    Unique_list=[]
   
    #loop for counting
    for row in csvreader:
        totalvotes+= 1
        if row[2] not in Unique_list:
            Unique_list.append(row[2])
        if str(row[2])=="Khan":
            khan+=1
        if str(row[2])=="Correy":
            Correy+=1
        if str(row[2])=="Li":
            Li+=1
        if str(row[2])=="O'Tooley":
            Otooley+=1
if khan > Li and khan > Correy and khan > Otooley:
     winner="Khan"
elif Li> khan and Li > Correy and Li > Otooley:
    winner="Li"
elif Correy > khan and Correy > Li and Correy > Otooley:
    winner="Correy"
elif Otooley > khan and Otooley > Li and Otooley > Correy:
    winner="O'Tooley"

khanpercent= (khan/totalvotes)*100       
correypercent=(Correy/totalvotes)*100
lipercent=(Li/totalvotes)*100
otooleypercent=(Otooley/totalvotes)*100


#printing output
print(Unique_list)
output=f'''text
List of Candidates {Unique_list}
  Election Results
  -------------------------
  Total Votes: {totalvotes}
  -------------------------
  Khan: {khanpercent:,.3f}% ({khan})
  Correy: {correypercent:,.3f}% ({Correy})
  Li: {lipercent:,.3f}% ({Li})
  O'Tooley: {otooleypercent:,.3f}% ({Otooley})
  -------------------------
  Winner: {winner}
  -------------------------
  '''
print(output)

with open("output.txt", "a") as f:
    print(output, file=f)