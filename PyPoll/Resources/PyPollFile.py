

#The total number of votes cast // int ballot_ct
#A complete list of candidates who received votes // str[] candidates
#The percentage of votes each candidate won // int percent_won 
#The total number of votes each candidate won
#The winner of the election based on popular vote.


import os
import csv

dirname = os.path.dirname(__file__)
poll_csv = os.path.join(dirname, "election_data.csv")


ballot_ct = 0
candidate_info = {}
candidate_count = {}
candidate_emptylist = [] 


with open(poll_csv) as data:
    data = csv.reader(data)
    csvheader = next(data)

    for row in data:
        candidate_emptylist.append(row[2])
        name = str(row[2])
        ballot_ct += 1
        
        if not name in candidate_count:
                candidate_count[name] = 1
        else:
            candidate_count[name] += 1
      
elections =list(set(candidate_emptylist))
elections.sort()      
vote_count = []

for hina in elections:
    vote_count.append(candidate_emptylist.count(hina))

    
    for name in candidate_count:
        candidate_info[name] = round((candidate_count[name] / ballot_ct) * 100)
winner = elections[vote_count.index(max(vote_count))]
khan = winner
        


print("Election Results")
print("--------------------")
print(f"Total Votes: {ballot_ct}")
print("--------------------")

for name in candidate_count:
    print(f"{name}: {candidate_info[name]}%  {candidate_count[name]}")
print("--------------------")
print(f"Winner: {khan}")
print("--------------------")