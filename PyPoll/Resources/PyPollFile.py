
"""
    The total number of votes cast // int ballot_ct


    A complete list of candidates who received votes // str[] candidates


    The percentage of votes each candidate won // int percent_won 


    The total number of votes each candidate won


    The winner of the election based on popular vote.
"""

import os
import csv

dirname = os.path.dirname(__file__)
poll_csv = os.path.join(dirname, "election_data.csv")


ballot_ct = 0
candidate_info = {}
with open(poll_csv) as data:
    data = csv.reader(data)
    next(data)
    for row in data:
        name = str(row[2])
        ballot_ct += 1
        
        if not name in candidate_info:
            candidate_info[name] = 1
        else:
            candidate_info[name] += 1
    print('--- 1st cabdidate info')

    
    for name in candidate_info:
        candidate_info[name] = round((candidate_info[name] / ballot_ct) * 100)
    print('--- 2nd cabdidate info')
    print(candidate_info)

print(ballot_ct)
print(candidate_info.keys())
print(candidate_info.values())