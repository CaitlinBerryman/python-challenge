# import modules, sys is for writing output to text
import os
import csv
import sys

# file path
csvpath = os.path.join("..", "..", "3_H_election_data.csv")

# read csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # skip header
    next(csvreader,None)

    # voter count
    voters = 0

    # lists for candidates and their respective votes
    candidates = []
    candvotes = []

    for row in csvreader:
        # each row is a vote
        voters += 1

        # if cand isn't in list yet, add them
        if row[2] not in candidates:
            candidates.append(row[2])
            candvotes.append(0)
        # append(0) because this part of the code will now run and add 1
        if row[2] in candidates:
            candvotes[candidates.index(row[2])] += 1


    # print(candidates)
    # print(candvotes)
    # print(voters)

    #find winning name based on corresponding index of highest votes
    winner = candidates[candvotes.index(max(candvotes))]

    # set up print function for each candidate so i don't repeat myself
    def percentages(x):
        name = str(candidates[x])
        votes_received = int(candvotes[x])
        vote_percent = round((votes_received / voters * 100),2)

        print(f"{name}: {vote_percent}% ({votes_received})")

# output
print(f"""Election Results
-------------------------
Total Votes: {voters}
-------------------------""")
for x in range(len(candidates)):
    percentages(x)
print(f"""-------------------------
Winner: {winner} 
""")

# txt file path
output_path = os.path.join("analysis", "output.txt")

# write file
stdoutOrigin = sys.stdout
sys.stdout = open(output_path, "w")
print(f"""Election Results
-------------------------
Total Votes: {voters}
-------------------------""")
for x in range(len(candidates)):
    percentages(x)
print(f"""-------------------------
Winner: {winner} 
""")

sys.stdout.close()
sys.stdout = stdoutOrigin
