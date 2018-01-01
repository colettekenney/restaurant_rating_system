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