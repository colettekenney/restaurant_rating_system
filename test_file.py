############################################################
# Looping through a list of lists
list = [['a', 'b', 'c'], ['d', 'e'], ['f']]

for item in list:
    for subitem in item:
        print(subitem)

############################################################

# Sorting list of inner lists at inner list position [2] 'in place' 
# Sorting in place means that the memory address of the old list is reused

l = [[0, 1, 'f'], [4, 2, 't'], [9, 4, 'afsd']]
l.sort(key=lambda x: x[2])
print(l)

# Sorting list of inner lists at inner list position [2] 'not in place'
# Sorting not in place means that a new memory address is used for the sorted list

sorted(l, key=lambda x: x[2])
print(l)

############################################################

# You can zip two lists together to create a dictionary of keys and values    

list_of_keys = ['key1', 'key2', 'key3']
list_of_values = ['value1', 'value2', 'value3']    
new_dict = dict(zip(list_of_keys, list_of_values))
print(new_dict)

############################################################

# In a single line of code you can set key : value pairs into a dictionary using .setdefault()
# This won't work here in this test_file because it needs the info from opened_file_list
# But you can go to restaurants.py to see it in action

# Creating the name_to_rating dict:
# This sets the current restaurant name as the key and an int of the rating as the value
# name_to_rating.setdefault(opened_file_list[i], int(opened_file_list[i+1].strip('%'))) 