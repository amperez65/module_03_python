import  csv

csv_path = "Resources/election_data.csv"

votes = 0

candidates = {}

with open(csv_path) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        # print(row)

        votes += 1

        # get the candidate
        # if the candidate is in the dictionary, we want to add 1 to the value
        # else, init with a vote of one

        candidate = row[2]
        if candidate in candidates.keys():
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

winner = max(candidates, key=candidates.get)




output = f"""Election Results
===================================
Total Votes: {votes}
==================================="""

for key in candidates.keys():
    perc = round(100*candidates[key]/votes,3)
    newline = f"""
{key}: {perc}% ({candidates[key]})"""
    output += newline

lastline = f"""
===================================
Winner: {winner}
===================================
"""
print(output)
print(lastline)


