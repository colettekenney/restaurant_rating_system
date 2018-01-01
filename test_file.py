list_of_cuisines = [['Canadian', 'Pub Food'], ['Malaysian', 'Thai'], ['Chinese'], ['Mexican'], ['Pub Food']]
unique_cuisines = []

for c in list_of_cuisines:
    for item in c:
        unique_cuisines.append(item)
unique_cuisines = set(unique_cuisines)
print(unique_cuisines)

