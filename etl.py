# dictionary method

def transform(dict):
    new_values=[]
    new_keys=[]
   
    #extract two list from the dictionary that include letters and correspondant scores
    for (key,value) in dict.items():
        for item in value:
            new_keys.append(item.lower())
            new_values.append(key)

    #create a new dictionary having letters as keys, and scores as values
    new_data = {new_keys[i]: new_values[i] for i in range(len(new_keys))}
    return new_data



