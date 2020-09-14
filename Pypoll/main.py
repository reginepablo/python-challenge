#Regine Pablo
#Python HW - pypoll.py

import os
import csv

csvpath = os.path.join('..',"Pypoll", "Resources",'election_data.csv')
with open(csvpath, "r") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    print(csv_reader)
    csv_header = next(csv_reader)
    
    votes = 0 
    khan = 0
    correy = 0
    li = 0
    otooley = 0
    
    for row in csv_reader: 
        
        votes +=1

        if row[2] == "Khan": 
            khan +=1
        elif row[2] == "Correy":
            correy +=1
        elif row[2] == "Li": 
            li +=1
        elif row[2] == "O'Tooley":
            otooley +=1
#dict
candidates = ["Khan", "Correy", "Li","O'Tooley"]
list = [khan, correy,li, otooley]


dict_c_and_v = dict(zip(candidates,list))
key = max(dict_c_and_v, key=dict_c_and_v.get)

#calc percentages per candidates
khan_percentage = (khan/votes) *100
correy_percentage = (correy/votes) * 100
li_percentage = (li/votes)* 100
otooley_percentage = (otooley/votes) * 100

#print result   
print("Election Results")
print("----------------------------")
print(f'Total Votes: {votes}')
print("----------------------------")
print(f"Khan: {khan_percentage:.3f}% ({khan})")
print(f"Correy: {correy_percentage:.3f}% ({correy})")
print(f"Li: {li_percentage:.3f}% ({li})")
print(f"O'Tooley: {otooley_percentage:.3f}% ({otooley})")
print("----------------------------")
print(f'Winner: {key}')
print("----------------------------")

#print result to election_summary.txt file
output_file = os.path.join("..", "Pypoll", "election_summary.txt")
with open(output_file,"w") as file:


    file.write("Election Results")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Votes: {votes}")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Khan: {khan_percentage:.3f}% ({khan})")
    file.write("\n")
    file.write(f"Correy: {correy_percentage:.3f}% ({correy})")
    file.write("\n")
    file.write(f"Li: {li_percentage:.3f}% ({li})")
    file.write("\n")
    file.write(f"O'Tooley: {otooley_percentage:.3f}% ({otooley})")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Winner: {key}")
    file.write("\n")
    file.write("----------------------------")