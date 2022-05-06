import random
import pandas as pd

contestants = []
ticket = []
totalList = []

#Reading Data and Getting Contestants Using Pandas
workbook = pd.read_excel('giveTest.xlsx', sheet_name = 'Sheet1')
numContestants = len(workbook)

#Input Net Sales and Divides and Rounds to Find Total Sales Per Person
for i in range(numContestants):
    ticket.append(workbook['Net Sales'].loc[i])
    ticket[i] = int(ticket[i]//13.99)

#Inputs Data to Contestants Array
for i in range(numContestants):
    contestants.append(workbook['CMS Account ID'].loc[i])
    
#Multiplied Contestants with Tickets
for i in range(numContestants):
    totalList.append((contestants[i] + "\n" )* ticket[i])
    
#Outputs Contestants to Text File      
with open("newishoutput.txt", "w") as txt_file:
    for line in totalList:
        txt_file.write('%s' % line)

print("Here are the Contestants!! \n")

#Prints Total Contestants In GiveAway
for i in range(numContestants):
    print(totalList[i])
    
#Reads Text File and Outputs Winner!
giveWinner= open('newishoutput.txt').read().splitlines()
winner = random.choice(giveWinner)
print("\nAnd the Winner Is " + winner)


