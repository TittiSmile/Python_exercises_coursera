"""
Below, we have provided a nested dictionary. Index into the dictionary to create variables that we have listed in the 
ActiveCode window.
"""




sports = {'swimming': ['butterfly', 'breaststroke', 'backstroke', 'freestyle'], 'diving': ['springboard', 'platform', 'synchronized'], 'track': ['sprint', 'distance', 'jumps', 'throws'], 'gymnastics': {'women':['vault', 'floor', 'uneven bars', 'balance beam'], 'men': ['vault', 'parallel bars', 'floor', 'rings']}}

# Assign the string 'backstroke' to the name v1
for key, value in sports.items():
    if key == "swimming":
        if "backstroke" in value:
            v1 = value[2]

# Assign the string 'platform' to the name v2
for key, value in sports.items():
    if key == "diving":
        if "platform" in value:
            v2 = value[1]
            
# Assign the list ['vault', 'floor', 'uneven bars', 'balance beam'] to the name v3
for key, value in sports.items():
    if key == "gymnastics":
        for key2, value2 in value.items():
            if key2 == "women":
                v3 = value2
# Assign the string 'rings' to the name v4
for key, value in sports.items():
    if key == "gymnastics":
        for key2, value2 in value.items():
            if key2 == "men":
                v4 = value2[3]
