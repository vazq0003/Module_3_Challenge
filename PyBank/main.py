
import os
import csv 

#set paths
csvbankpath = os.path.join('Resources','budget_data.csv')
bankoutput_path = os.path.join('Analysis','bank_main.txt')

#set variables
monthscount = []
totalprofitloss = []
profitlosschange = []
avg_change = 0 

#open and read csv
with open(csvbankpath) as bankcsvfile:
    bankcsvreader = csv.reader(bankcsvfile, delimiter=",")

    header = next(bankcsvreader)

    #loops to populate lists for calculations
    for row in bankcsvreader:

        monthscount.append(row[0])
        totalprofitloss.append(int(row[1]))

    for i in range(0,85):
        profitlosschange.append(totalprofitloss[i+1] - totalprofitloss[i])

#calculate max increse/decrease and average change
max_increase_profitloss = max(profitlosschange)
max_decrease_profitloss = min(profitlosschange)
avg_change = round(sum(profitlosschange)/len(profitlosschange),2)

#locate months in which max increse/decrease happened
location_max_increase = profitlosschange.index(max_increase_profitloss)
location_max_decrease = profitlosschange.index(max_decrease_profitloss)

max_increase_month = monthscount[location_max_increase + 1]
max_decrease_month = monthscount[location_max_decrease + 1]

#print requested values
print('Total Months: ' + str(len(monthscount)))
print('Total Profit/Loss: ' + str(sum(totalprofitloss)))
print('Average Change: ' + str(avg_change))
print('Greatest Increase in Profits:' + ' ' + max_increase_month + ' ' + str(max_increase_profitloss))
print('Greatest Decrease in Profits:' + ' ' + max_decrease_month + ' ' + str(max_decrease_profitloss))


#write answers to text file
with open(bankoutput_path, 'w') as file:
    file.write('Financial Analysis')
    file.write("\n")
    file.write(f'Total Months: {str(len(monthscount))}')
    file.write("\n")
    file.write(f'Total Profit/Loss: {str(sum(totalprofitloss))}')
    file.write("\n")
    file.write(f'Average Change: {str(avg_change)}')
    file.write("\n")
    file.write(f'Greatest Increase in Profits: {max_increase_month} {str(max_increase_profitloss)}')
    file.write("\n")
    file.write(f'Greatest Decrease in Profits: {max_decrease_month} {str(max_decrease_profitloss)}')
