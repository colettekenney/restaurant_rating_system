# names_final = []
# names_matching_price = ['Queen St. Cafe', 'Dumplings R Us', 'Deep Fried Everything']
# names_of_cuisine = [['Queen St. Cafe', 'Dumplings R Us', 'Deep Fried Everything'], ['Georgie Porgie']]
 
# for item in names_of_cuisine:
#     j = 0
#     k = 0
#     for j in range(len(names_of_cuisine[j][k])):
#         print(names_of_cuisine[j][k])
#         if names_of_cuisine[j][k] in names_matching_price:
#             names_final.append(names_of_cuisine[j][k])
#             k = k + 1
#         else:
#             k = k + 1

list = [['a', 'b', 'c'], ['d', 'e'], ['f']]


for item in list:
    for subitem in item:
        print(subitem)
        