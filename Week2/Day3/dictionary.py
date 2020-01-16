# Dictionary

# Example of a dictionary
my_personal_info = {
    "name" : "Alpha",
    "DOB" : "01/01/2020",
    "School" : "Hostos CC",
    "GPA" : 0.5
    }

# Dictionaries are known for their "key-value" pair system

# Checking if a key exists in a dictionary
if "name" in my_personal_info:
    print(my_personal_info["name"])
    pass
else:
    print("Name is not in there.")

    
if "job" in my_personal_info:
    print("Yes, he has a job.")
else:
    print("Nope, he has not a job.")

for key in my_personal_info:
    print(key)