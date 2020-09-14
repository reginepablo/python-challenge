#Regine Pablo
#Python HW - pybank.py

import csv
import os

csvpath = os.path.join("..", "Pybank", "Resources", "budget_data.csv")
with open (csvpath, "r") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    print(csv_reader)
    header = next(csv_reader)
    
    total_month = []
    total_profit = []
    profit_change = []

#calculate total_month    
    for row in csv_reader:
        total_month.append(row[0])
        total_profit.append(int(row[1]))
        
#calculate profit_change
    for i in range(len(total_profit)-1):
        profit_change.append(total_profit[i+1]-total_profit[i])
                      
#calc profit_increase
inc = max(profit_change)
profit_increase = profit_change.index(max(profit_change)) + 1

#calc profit_decrease    
dec = min(profit_change)
profit_decrease = profit_change.index(min(profit_change)) + 1
     
#print result    
print("Financial Analysis")
print("----------------------------")
print(f'Total Months: {len(total_month)}')
print(f'Total: $ {sum(total_profit)}')
print(f'Average Change: ${round(sum(profit_change)/len(profit_change),2)}')
print(f'Greatest Increase in Profits: {total_month[profit_increase]} (${(str(inc))})')
print(f'Greatest Decrease in Profits: {total_month[profit_decrease]} (${(str(dec))})') 

#print result to analysis_summary.txt file
output_file = os.path.join('..', "Pybank", "Resources", 'analysis_summary.txt')
with open(output_file, "w") as file:
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(total_month)}")
    file.write("\n")
    file.write(f"Total: ${sum(total_profit)}")
    file.write("\n")
    file.write(f"Average Change: ${round(sum(profit_change)/len(profit_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_month[profit_increase]} (${(str(inc))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {total_month[profit_decrease]} (${(str(dec))})")
