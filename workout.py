import os # work with file paths(in our computer)
Base = os.path.dirname(os.path.abspath(__file__))# get the path of the current file and store it under base

def read_workout_file():
    path = os.path.join(Base, "Workout_log.csv") # directing path to workout log file
    library = {}                                # empty dictionary to store the exercies and weights 
    with open(path) as file:                    # open the workout log as file
        lines = file.readlines()                #Read all the line and store them in lines 
    for line in lines[1:]:                      #For loop that goes through all the line starting from the second line (skips the header)
        parts = line.strip().split(",")         # It will strip and the split the lines by adding comma and store them under parts
        if parts[0] == "":                      #clause that checks if the first place is empty and if it is it will skip the line and go to the next line because 
            continue
        exercise = parts[0]                    # if the first place is not empty it will store the first place under type of exercise
        weights = []                          #creating empty list 
        for w in parts[1:]:
            weights.append(int(w))            # it will store the rest of the line under weights and add to the list of wights
        library[exercise] = weights           
    return library

library = read_workout_file()
print(library)

#Question 1: Am I making progress on my exercises from week 1 to week 3?
for exercise, weights in library.items():
    if weights[-1] > weights[0]: # checking if the last weight is greater then the first weight
        print("Making Great Progress on" , exercise, "from week 1 to week 3")
    elif weights[-1] == weights[0]: # checking if the last weight is equal to the first weight
        print("Mantaining the same weight on", exercise, "from week 1 to week 3")
    else: 
        print("making less progress on", exercise, "from week 1 to week 3")

#Question 2: what is the avergae weight for each exerise over the course of the 3 weeks?
for exercise, weights in library.items():
    average_weight = float(sum(weights)/ len(weights)) # calculating average and converting to float so get exact number
    print("the average weight for", exercise, "over the course of 3 weeks is ", average_weight)

#Question 3: What is the total weight lifted for each exercise over the course of 3 weeks and can we display it in a bar chart?
import matplotlib.pyplot as plt
totals = {}
for exercise, weights in library.items():
    totals[exercise] = sum(weights)
    print("the total weight lifted for", exercise, "over the course of 3 weeks is", totals[exercise])
plt.bar(totals.keys(), totals.values())
plt.xlabel("Exercises")
plt.ylabel("Total Weight Lifted")
plt.title("Workout Progress")
plt.show()

#SElF-CHECK:
assert len(library) > 0, "no records loaded"
assert max(library['Leg_Press']) == 105, "max weight for leg press should be 105 "
print("All checks passed!")

