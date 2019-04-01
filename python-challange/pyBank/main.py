#import dependencies
import os
import csv
#define path to csv file
path = "C:\\Users\\Ryan\\Desktop"
csvPath = os.path.join(path, "budget_data.csv")
#define variables
totalMonths = 0
net_total = 0
monthly_difference = []
date = []
revenue = []
#open and read csv file
with open(csvPath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    header = next(csvreader)
#iterate over each row of data and count the rows
    for row in csvreader:
        net_total = net_total + int(row[1])
        totalMonths = totalMonths + 1

#total of difference between all row of column "Revenue" and found total revnue change. Also found out max revenue change and min revenue change.
        revenue.append(float(row[1]))
    for i in range(1,len(revenue)):
        monthly_difference.append(revenue[i] - revenue[i-1])
        average_difference = round(((sum(monthly_difference)) / (len(monthly_difference))),2)

        max_difference = max(monthly_difference)
        min_difference = min(monthly_difference)

        date.append(row[0])
        max_difference_date = str(date[monthly_difference.index(max(monthly_difference))])
        min_difference_date = str(date[monthly_difference.index(min(monthly_difference))])

print("Financial Analysis")
print("--------------------------")
print(f"Total Months: {totalMonths}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_difference}")
print(f"Greatest Increase in Profits: {max_difference_date}: ${max_difference}")
print(f"Greatest Decrease in Profits: {min_difference_date}: ${min_difference}")

def writer_function():
    print("Financial Analysis",file=open("PyBankReults.txt", "a"))
    print("--------------------------",file=open("PyBankReults.txt", "a"))
    print(f"Total Months: {totalMonths}",file=open("PyBankReults.txt", "a"))
    print(f"Total: ${net_total}",file=open("PyBankReults.txt", "a"))
    print(f"Average Change: ${average_difference}",file=open("PyBankReults.txt", "a"))
    print(f"Greatest Increase in Profits: {max_difference_date}: ${max_difference}",file=open("PyBankReults.txt", "a"))
    print(f"Greatest Decrease in Profits: {min_difference_date}: ${min_difference}",file=open("PyBankReults.txt", "a"))
writer_function()
