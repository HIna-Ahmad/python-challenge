

#The total number of votes cast // int ballot_ct
#A complete list of candidates who received votes // str[] candidates
#The percentage of votes each candidate won // int percent_won 
#The total number of votes each candidate won
#The winner of the election based on popular vote.


import os
import csv

ballot_ct = 0
candidate_info = {}
candidate_count = {}
candidate_emptylist = [] 

with open("python-challenge/PyPoll/Resources/election_data.csv") as data:
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
out_put1 = (f"Election Results\n" + f"-----------------\n" + f"Total Votes: {ballot_ct}\n")
elections = list(set(candidate_emptylist))
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
election_results = ""

for name in candidate_count:
    candidate_results = (f"{name}: {candidate_info[name]}%  {candidate_count[name]}\n")
    election_results += candidate_results
    
print(election_results)
print("--------------------")
print(f"Winner: {khan}")
print("--------------------")

poll_winner = (f"--------------------\n" + f"Winner: {khan}\n" + f"--------------------\n")
out_put = (out_put1 + election_results + poll_winner)

filepathtosave = ("python-challenge/PyPoll/analysis/analysis.txt")
with open(filepathtosave, 'w') as txt_file:
    txt_file.write(out_put)
