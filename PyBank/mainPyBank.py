#main.py pyBank for python-challenge HW

import csv
import os

csvpath = os.path.join("C:\\","Users","SS3","Desktop","GTBC","GTBC_HW","3-Python","budget_data.csv")
#csvpath = os.path.join("C:\\","Users","smithtrain","Desktop","GTBC","GTBC_HW","3-Python","budget_data.csv")
print(csvpath)



with open(csvpath,"r",newline='') as csvfile:
    print(csvfile)
    csvreader = csv.reader(csvfile,delimiter =",")

    print(csvreader)
    
    #csv_header = next(csvreader)
    #print(csv_header)
    numMonths = 0
    Total_PL = 0
    minPos=0
    maxPos=0
    ChangeList=[]
    OrigList=[]
    
    next(csvreader)
    for row in csvreader:
        
        OrigList.append(row)
        
        numMonths += 1
        Total_PL = Total_PL + int(row[1])
        
        
        
        if numMonths == 1:
            currChange = 0
            prevPL = int(row[1])  
            #print(str(prevPL))
        else:
            currChange = (int(row[1]) - prevPL)
            prevPL = int(row[1])
            #print(str(currChange))
        
        ChangeList.append(currChange)
        #print(ChangeList)
          
     
    maxPos = ChangeList.index(max(ChangeList))
    print(maxPos)   
    print(max(ChangeList)) 
    
    minPos = ChangeList.index(min(ChangeList))        
    print(minPos)   
    print(min(ChangeList))  
        
        
        
        
        
    print("Financial Analysis")
    print("------------------")
    print("Total Months: " + str(numMonths))
    print("Total Profit & Loss: " + str(Total_PL))
    print("Greatest Month on Month increase in P&L: " + str(OrigList[maxPos][0]) + " (" + str(ChangeList[maxPos]) + ")")
    print("Greatest Month on Month decrease in P&L: " + str(OrigList[minPos][0]) + " (" + str(ChangeList[minPos]) +")")
    
    #csv.writer()
    # store in string with \n for new lines
    