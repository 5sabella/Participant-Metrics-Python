import csv # The import function here is used to bring in the CSV module, which provides functionality to read from and write to CSV files.

filename = 'Ex3_dataset.csv' # This line defines a variable named 'filename' and assigns it the string value 'Ex3_dataset.csv', which is the name of the CSV file to be processed.

with open('Ex3_dataset.csv', 'r') as data: # The 'with' statement is used to open the specified CSV file in read mode, as per the 'r'. The file object is assigned to the variable 'data', which will be used to read the contents of the file.
    dictlist = [] # An empty list named 'dictlist' is created to store dictionaries representing each row of the CSV file.
    for line in csv.DictReader(data): # The 'csv.DictReader' function is used to read the CSV file, where each row is converted into a dictionary with keys corresponding to the column headers. The loop iterates over each row (dictionary) in the CSV file. The dictionary keys will be the column headers from the CSV file, and the values will be the corresponding data for each row.
        dictlist.append(line) # Each dictionary (row) is appended to the 'dictlist', resulting in a list of dictionaries representing the entire CSV file.
        print(line) # This line prints each dictionary (row) as it is read from the CSV file.

print(dictlist) # After reading the entire CSV file, this line prints the complete 'dictlist', which contains all the rows as dictionaries, which I have test run and confirmed works as intended by printing the full list of dictionaries.

m1 = [] # For Metric 1, I've created an empty list to store the responses.
m1_participants = [] # I've created a list to store participant IDs for Metric 1
# m1_dict = {} - Here, I'm struggling to figure out how to make a dictionary of participant IDs and their responses for Metric 1, yet I know using a dictionary is a better starting point for metric mapping.

for part_dict in dictlist: # The for loop iterates over each dictionary (row) in the 'dictlist'.
    value = part_dict["Metric 1 "] # For each dictionary, it retrieves the value associated with the key "Metric 1 ".

    if value != "NaN" : # The if value here checks if the retrieved value is not equal to the string "NaN", indicating that it is a valid response. But if it is "NaN", it skips to the next iteration and completely disregards it.
        m1response = int(value) # If the value is valid, it converts the value to an integer and assigns it to the variable 'm1response'.
        m1.append(m1response) # The valid integer response is then appended/added to the 'm1' list.
        m1_participants.append(part_dict["Participant"]) # The participant ID associated with the valid response is appended to the 'm1_participants' list.

m1max = max(m1) # This line calculates the maximum value from the 'm1' list using the 'max()' function and assigns it to the variable 'm1max'.
m1min = min(m1) # This line calculates the minimum value from the 'm1' list using the 'min()' function and assigns it to the variable 'm1min'.

m1_total = sum(m1) # This line calculates the total sum of all values in the 'm1' list using the 'sum()' function and assigns it to the variable 'm1_total' calculating the average.
for response in m1: # This for loop iterates over each response in the 'm1' list.
    m1_total += response # It adds each response to the 'm1_total' variable.
    average = m1_total / len(m1) # After the loop, it calculates the average by dividing the total sum ('m1_total') by the number of responses (length of 'm1' list) using 'len(m1)' and assigns it to the variable 'average'.
    

print("Metric 1: " + str(m1min.append(m1_participant)) + ", " + str(m1max.append(m1_participants)), ", " + str(average)) # Finally, the print statement delivers the results for Metric 1, displaying the minimum value, maximum value, and average of the valid responses, along with the associated participant IDs.


m2 = [] # For Metric 2, I've created an empty list to store the responses.
m2_participants = [] # I've created a list to store participant IDs for Metric 2
# m2_dict = {} - Here, I'm struggling to figure out how to make a dictionary of participant IDs and their responses for Metric 1, yet I know using a dictionary is a better starting point for metric mapping.


for part_dict in dictlist: # The for loop is used here to iterate over each dictionary (row) in the 'dictlist'.
    value = part_dict["Metric 2"] # For each dictionary, it retrieves the value associated with the key "Metric 2".

    if value != "NaN" : # The if value here checks if the retrieved value is not equal to the string "NaN", indicating that it is a valid response. But if it is "NaN", it skips to the next iteration and completely disregards it.
        m2response = float(value) # The m2response variable is assgined to the float conversion of the valid value. It is a float because Metric 2 responses can be decimal values, and having it as an integer would make this line invalid. 
        m2.append(m2response) # The valid float response is then appended/added to the 'm2' list.
        m2_total = 0 # Here I've put the value of m2_total inside the loop to reset it for each participant.
        for response in m2: # The for function iterates over each response in the 'm2' list.
            m2_total += response # It then will add each response to the 'm2_total' variable.
            m2average = m2_total / len(m2) # After the loop, it calculates the average by dividing the total sum ('m2_total') by the number of responses (length of 'm2' list) using 'len(m2)' and assigns it to the variable 'm2average'.
        m2_participants.append(part_dict["Participant"]) # The participant ID associated with the valid response is appended to the 'm2_participants' list as per how I did for Metric 1, which can also be seen inside the append function.


m2max = max(m2) # This line calculates the maximum value from the 'm2' list using the 'max()' function and assigns it to the variable 'm2max'.
m2min = min(m2) # This line calculates the minimum value from the 'm2' list using the 'min()' function and assigns it to the variable 'm2min'.

print("Metric 2: " + str(m2min.append(m2_participants)) + ", " + str(m2max.append(m2_participants)) + ", " + str(m2average)) # Finally, the print statement delivers the results for Metric 2, displaying the minimum value, maximum value, and average of the valid responses, along with the associated participant IDs.

m3 = [] # For Metric 3, I've created an empty list to store the responses.

for part_dict in dictlist: # The for loop is used here to iterate over each dictionary (row) in the 'dictlist'.

    response = part_dict["Metric 3"].lower() # For each dictionary, it retrieves the value associated with the key "Metric 3" and converts it to lowercase using the .lower() method to ensure consistency in comparison.
    if response.startswith("y"): # The if statement checks if the response starts with the letter "y" (indicating a "yes" response).
        m3.append("y") # If the response starts with "y", it appends "y" to the 'm3' list.

    elif response.startswith("n"): # The elif statement checks if the response starts with the letter "n" (indicating a "no" response).
        m3.append("n") # If the response starts with "n", it appends "n" to the 'm3' list.

    else: # If the response does not start with either "y" or "n", it is considered invalid and would be skipped.
        continue # The continue statement skips to the next iteration of the loop without taking any action for invalid responses.

    yes_count = 0 # This variable is used to count the number of "yes" responses.
    no_count = 0 # This variable is used to count the number of "no" responses.

for response in m3: # This for loop iterates over each response in the 'm3' list.
    if response == "y": # The if statement checks if the response is "y".
        yes_count += 1 # If the response is "y", it increases the 'yes_count' by 1.
    elif response == "n": # The elif statement checks if the response is "n".
        no_count += 1 # If the response is "n", it increases the 'no_count' by 1.

print("Metric 3: " + str(yes_count) + " yes, " + str(no_count) + " no") # Finally, the print statement delivers the results for Metric 3, displaying the total counts of "yes" and "no" responses.




    
  