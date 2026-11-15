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







