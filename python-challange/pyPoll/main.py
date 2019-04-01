import os
import csv

path = "C:\\Users\\Ryan\\Desktop"
csvPath = os.path.join(path, "polling.csv")

totalVotes = 0
canidates = []

voter_count_Khan = 0
voter_count_Correy = 0
voter_count_Li = 0
voter_count_Otooley = 0

vote_percent_Khan = 0
vote_percent_Correy = 0
vote_percent_Li = 0
vote_percent_Otooley = 0

with open(csvPath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    header = next(csvreader)

    for row in csvreader:
#sum total number of voters
        totalVotes = totalVotes + 1

#Get unique canidate names in list
        if row[2] not in canidates:
            canidates.append(row[2])
        if row[2] == "Khan":
            voter_count_Khan = voter_count_Khan + 1
        if row[2] == "Correy":
            voter_count_Correy = voter_count_Correy + 1
        if row[2] == "Li":
            voter_count_Li = voter_count_Li + 1
        if row[2] == "O'Tooley":
            voter_count_Otooley = voter_count_Otooley + 1

# Canidate Vote percentage
    vote_percent_Khan = round((100*(voter_count_Khan / totalVotes)),2)
    vote_percent_Correy = round((100*(voter_count_Correy / totalVotes)),2)
    vote_percent_Li = round((100*(voter_count_Li / totalVotes)),2)
    vote_percent_Otooley = round((100*(voter_count_Otooley / totalVotes)),2)

#create key:value pairs for canidate names and their vote count
    max_winner = {"Khan" : voter_count_Khan,
            "Correy" : voter_count_Correy,
            "Li" : voter_count_Li,
            "O'Tooley" : voter_count_Otooley
            }

#print statments
print("----------------------------------")
print("         Election Results")
print("----------------------------------")
print(f"Total Votes: {totalVotes}")
print(f"{canidates[0]}: {vote_percent_Khan}% ({voter_count_Khan})")
print(f"{canidates[1]}: {vote_percent_Correy}% ({voter_count_Correy})")
print(f"{canidates[2]}: {vote_percent_Li}% ({voter_count_Li})")
print(f"{canidates[3]}: {vote_percent_Otooley}% ({voter_count_Otooley})")
#return Key for max value within dict
print(f"Winner: {max(max_winner, key=max_winner.get)}")

def polling_data_writer():
    print("----------------------------------", file=open("PyPollReults.txt", "a"))
    print("         Election Results", file=open("PyPollReults.txt", "a"))
    print("----------------------------------", file=open("PyPollReults.txt", "a"))
    print(f"Total Votes: {totalVotes}", file=open("PyPollReults.txt", "a"))
    print(f"{canidates[0]}: {vote_percent_Khan}% ({voter_count_Khan})", file=open("PyPollReults.txt", "a"))
    print(f"{canidates[1]}: {vote_percent_Correy}% ({voter_count_Correy})", file=open("PyPollReults.txt", "a"))
    print(f"{canidates[2]}: {vote_percent_Li}% ({voter_count_Li})", file=open("PyPollReults.txt", "a"))
    print(f"{canidates[3]}: {vote_percent_Otooley}% ({voter_count_Otooley})", file=open("PyPollReults.txt", "a"))
    #return Key for max value within dict
    print(f"Winner: {max(max_winner, key=max_winner.get)}", file=open("PyPollReults.txt", "a"))

polling_data_writer()    
