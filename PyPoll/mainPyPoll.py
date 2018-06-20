#main.py pyBank for python-challenge HW

import csv
import os

csvpath = os.path.join("C:\\","Users","SS3","Desktop","GTBC","GTBC_HW","3-Python","election_data.csv")
#csvpath = os.path.join("C:\\","Users","smithtrain","Desktop","GTBC","GTBC_HW","3-Python","election_data.csv")
#print(csvpath)



with open(csvpath,"r",newline='') as csvfile:
    #print(csvfile)
    csvreader = csv.reader(csvfile,delimiter =",")

    numVotes = 0
    numCands = 0
    DataList=[]
    CandsList=[]
    VoteList=[]
    
    next(csvreader)
    for row in csvreader:        
        
        numVotes += 1        
        DataList.append(row)
    
    DataList.sort(key=lambda x: x[2])  
    
   # for ctr in range(numVotes-1000,numVotes):
   #     print(DataList[ctr])
    
    rowCtr = 0
   
    for entry in DataList:        
        
        
        if rowCtr == 0:
            CandsList.append(entry[2])
            #print(CandsList)
            
            numCands = 1
            #print(CandsList[numCands-1])
            
        elif DataList[rowCtr][2] != CandsList[(numCands-1)]: 
            CandsList.append(entry[2])
            numCands += 1
            #print(CandsList)
        
        VoteList.append(entry[2])
        rowCtr += 1
        
   #         prevPL = int(row[1])
            #print(str(currChange))
        
   #     ChangeList.append(currChange)
        #print(ChangeList)
    
    print("Election Results")
    print("---------------------")
    print("Total Votes: " + str(numVotes))
    print("---------------------")
    
    VoteCount = 0
    VoteCountList =[]
    
    for Cand in CandsList:
        VoteCount = VoteList.count(Cand)
        VotePcnt = VoteCount/numVotes
        print(Cand + ": " + "{:,.3f}%".format(VotePcnt*100) + " (" + str(VoteCount)+ ")")
        VoteCountList.append(VoteCount)
        VoteCount = 0
    
    WinnerCount = max(VoteCountList)
    
    print("---------------------")
    print("Winner: " + str(CandsList[VoteCountList.index(WinnerCount)]))
    print("---------------------")
   
with open("PyPoll_Summary.txt", "w") as text_file:
    text_file.write("Election Results" + "\n")
    text_file.write("---------------------" + "\n")
    text_file.write("Total Votes: " + str(numVotes) + "\n")
    text_file.write("---------------------" + "\n")
    
    for Cand in CandsList:
        VoteCount = VoteList.count(Cand)
        VotePcnt = VoteCount/numVotes
        text_file.write(Cand + ": " + "{:,.3f}%".format(VotePcnt*100) + " (" + str(VoteCount)+ ") \n")
        VoteCountList.append(VoteCount)
        VoteCount = 0
    
    WinnerCount = max(VoteCountList)
    
    text_file.write("---------------------" + "\n")
    text_file.write("Winner: " + str(CandsList[VoteCountList.index(WinnerCount)]) + "\n")
    text_file.write("---------------------" + "\n")
   