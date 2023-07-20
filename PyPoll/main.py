
import os
import csv 

#set paths
csvpollpath = os.path.join('Resources','election_data.csv')
polloutput_path = os.path.join('Analysis','poll_main.txt')

#set variables
vote_count = []
vote_stockham = []
vote_degette = []
vote_doane = [] 

#open and read csv
with open(csvpollpath) as pollcsvfile:
    pollcsvreader = csv.reader(pollcsvfile,delimiter=",")

    header = next(pollcsvreader)

    #loop and conditionals to populate lists
    for row in pollcsvreader:

        vote_count.append(row[0])

        if row[2] == "Charles Casper Stockham":
            vote_stockham.append(row[0])
        if row[2] == "Diana DeGette":
            vote_degette.append(row[0])
        if row[2] == "Raymon Anthony Doane":
            vote_doane.append(row[0])

#calculate votes and percent of votes
total_vote = len(vote_count)
total_stockham = len(vote_stockham)
total_degette = len(vote_degette)
total_doane = len(vote_doane)

pct_stockham = total_stockham/total_vote
pct_degette = total_degette/total_vote
pct_doane = total_doane/total_vote

#create dictionary and locate winner
candidate_dictionary = {"Charles Casper Stockham": total_stockham,"Diana DeGette": total_degette,"Raymon Anthony Doane": total_doane}

winner_key = max(candidate_dictionary, key=candidate_dictionary.get)

#print results
print(f'Total Votes: {total_vote}')
print(f'Charles Casper Stockham: {pct_stockham:.2%} ({total_stockham})')
print(f'Diana DeGette: {pct_degette:.2%} ({total_degette})')
print(f'Raymon Anthony Doane: {pct_doane:.2%} ({total_doane})')
print(f'Winner: {winner_key}')

#write results to text file
with open(polloutput_path, 'w') as file:
    file.write('Election Results')
    file.write("\n")
    file.write(f'Total Votes: {str(total_vote)}')
    file.write("\n")
    file.write(f'Charles Casper Stockham: {pct_stockham:.2%} ({str(total_stockham)})')
    file.write("\n")
    file.write(f'Diana DeGette: {pct_degette:.2%} ({str(total_degette)})')
    file.write("\n")
    file.write(f'Raymon Anthony Doane: {pct_doane:.2%} ({str(total_doane)})')
    file.write("\n")
    file.write(f'Winner: {winner_key}')