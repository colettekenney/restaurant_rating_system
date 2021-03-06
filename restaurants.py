'''
A restaurant rating system.

Here are some example dictionaries. These correspond to the information in 
restaurants_small.txt

Restaurant name to rating:
# dict of {str: int}
{'Georgie Porgie': 87,
 'Queen St. Cafe': 82,
 'Dumplings R Us': 71,
 'Mexican Grill': 85,
 'Deep Fried Everything': 52}

Price to list of restaurant names:
# dict of {str, list of str}
{'$': ['Queen St. Cafe', 'Dumplings R Us', 'Deep Fried Everything'],
 '$$': ['Mexican Grill'],
 '$$$': ['Georgie Porgie'],
 '$$$$': []}

Cuisine to list of restaurant names:
# dict of {str, list of str}
{'Canadian': ['Georgie Porgie'],
 'Pub Food': ['Georgie Porgie', 'Deep Fried Everything'],
 'Malaysian': ['Queen St. Cafe'],
 'Thai': ['Queen St. Cafe'],
 'Chinese': ['Dumplings R Us'],
 'Mexican': ['Mexican Grill']}

With this data, for a price of '$' and cuisines of ['Chinese', 'Thai'], the
program produces this list:

[[82, 'Queen St. Cafe'], [71, 'Dumplings R Us']]
'''

# This is the file containing the restaurant data
FILENAME = 'restaurants_small.txt'
# This is a second test file that you can use to read restaurant data
#FILENAME = 'restaurants_large.txt'
# Open the file and read all contents into variable opened_file_list with all newlines \n removed
# Format of opened & .splitlines() file is:
# [i] Name
# [i+1] Rating
# [i+2] Price
# [i+3] Cuisine
# [i+4] ''

# Open the file and read all contents into a list with all newlines \n removed
with open(FILENAME) as file:
    opened_file_list = file.read().splitlines()

# This is the main program, which is a restaurant recommendation function
def recommend(file, price, cuisines_list):
    '''(file open for reading, str, list of str) -> list of [int, str] list

    Find restaurants in file that are priced according to price and that are
    tagged with any of the items in cuisines_list. Return a list of lists in 
    the form of [rating%, restaurant name], sorted by rating%.
    '''

    # Read the file and build the data structures:
    # - a dict of {restaurant name: rating%}
    # - a dict of {price: list of restaurant names}
    # - a dict of {cuisine: list of restaurant names}
    name_to_rating, price_to_names, cuisine_to_names = read_restaurants(file)

    # Look up the list of restaurant names for the price requested.
    names_matching_price = price_to_names[price]

    # Now we have a list of restaurants in the right price range.
    # Need a new list of restaurants that serve one of the cuisines in the user's cuisines_list
    names_final = filter_by_cuisine(names_matching_price, cuisine_to_names, cuisines_list)

    # Now we have a list of restaurants that are in the right price range and serve
    # the requested cuisine.
    # Need to look at ratings and sort the list by ratings.
    result = build_rating_list(name_to_rating, names_final)

    # We're done! Return the sorted list:
    return result

# This is the read_restaurants function:
def read_restaurants(file):
    ''' (file) -> (dict, dict, dict) 
    
    Open the file and return a tuple of three dictionaries based on the info in the file:

    - a dict of {restaurant name: rating%}
    - a dict of {price: list of restaurant names}
    - a dict of {cuisine: list of restaurant names}
    '''
    
    # Initializing all required items
    i = 0
    name_to_rating = {}
    price_to_names = {'$' : [], '$$' : [], '$$$' : [], '$$$$' : []}
    cuisine_to_names = {}

    # The read file has name at [i], rating at [i+1], price at [i+2], cuisine at [i+3], \n at [i+4]
    # so we are stepping through the file by a count of 5 to get to each unique set 
    for i in range(0, len(opened_file_list), 5):
        
        # Creating the name_to_rating dict:
        # This sets the current restaurant name as the key and an int of the rating as the value
        name_to_rating.setdefault(opened_file_list[i], int(opened_file_list[i+1].strip('%')))
                
        # This looks for all cuisine types at [i+3] (separated by ',') associated to name at [i]
        # so we can create the cuisine_to_names dict in the next step:  
        while opened_file_list[i+3].find(',') and opened_file_list[i+3] != '':
            if opened_file_list[i+3].find(',') != -1:
                location = opened_file_list[i+3].find(',')
                cuisine = opened_file_list[i+3][: location]
                opened_file_list[i+3] = opened_file_list[i+3][location + 1 :]
            else:
                cuisine = opened_file_list[i+3]
                opened_file_list[i+3] = ''
            
            # Now we can create the cuisine_to_names dict:
            # This sets the current cuisine as the key and the current restaurant name as the value
            cuisine_to_names.setdefault(cuisine, []).append(opened_file_list[i])
             
        # Creating the price_to_names dict:
        # This appends the current restaurant name to it's assocated price in the price_to_names dict
        if opened_file_list[i+2] in price_to_names:
            price_to_names[opened_file_list[i+2]].append(opened_file_list[i])
    
    return name_to_rating, price_to_names, cuisine_to_names

# This is names_matching_price function:
# Look up the list of restaurant names for the price requested.
def names_matching_price(price):
    '''(str) -> list of str

    Returns a list of restaurant names from the price_to_names dictionary that is 
    in the price range provided by the user

    >>>price_to_names = {
        '$': ['Queen St. Cafe', 'Dumplings R Us', 'Deep Fried Everything'],
        '$$': ['Mexican Grill'],
        '$$$': ['Georgie Porgie'],
        '$$$$': []}
    >>>names_matching_price('$')
    ['Queen St. Cafe', 'Dumplings R Us', 'Deep Fried Everything']
    '''
    names_matching_price = price_to_names[price]
    return names_matching_price

# This is the filter_by_cuisine function:
# Now we have a list of restaurants in the right price range.
# We want to return a new list of restaurants that serve one of the cuisines
# from the user's provided cuisines_list.
def filter_by_cuisine(names_matching_price, cuisine_to_names, cuisines_list):
    '''(list of str, dict of {str : str}, list of str) -> list of str

    Returns a list of restaurant names that are in both the user's specified 
    price range and cuisine type

    >>>names_matching_price = ['Queen St. Cafe', 'Dumplings R Us', 'Deep Fried Everything']
    >>>cuisine_to_names = {
        'Canadian': ['Georgie Porgie'], 
        'Pub Food': ['Georgie Porgie', 
        'Deep Fried Everything'], 
        'Malaysian': ['Queen St. Cafe'], 
        'Thai': ['Queen St. Cafe'], 
        'Chinese': ['Dumplings R Us'], 
        'Mexican': ['Mexican Grill']}
    >>>cuisines_list = ['Chinese', 'Thai']
    >>>filter_by_cuisine(names_matching_price, cuisine_to_names, cuisines_list)
    ['Dumplings R Us', 'Queen St. Cafe']
    '''
    names_final = []
    names_of_cuisine = []
    # This checks if cuisine is in cuisine_to_names dict, and if it is, it appends to
    # an interim list of names_of_cuisine (this could potentially be a list of lists)
    for cuisine in cuisines_list:
        if cuisine in cuisine_to_names:
            names_of_cuisine.append(cuisine_to_names[cuisine])
    # Because names_of_cuisine is in the form of a list of lists, we have to iterate
    # through the inner lists and append to the names_final list 
    for item in names_of_cuisine:
        for subitem in item:
            names_final.append(subitem)    
    
    return names_final

# Now we have a list of restaurants that are in the right price range and serve
# the requested cuisine.
# Need to look at ratings and sort the list by ratings.
def build_rating_list(name_to_rating, names_final):
    '''(dict of {str: int}, list of str) -> list of [int, str] list
    
    Return a sorted list of [int, str] list where int is restaurant rating and str is restaurant name

    >>>name_to_rating = {
        'Georgie Porgie': 87, 
        'Queen St. Cafe': 82, 
        'Dumplings R Us': 71, 
        'Mexican Grill': 85, 
        'Deep Fried Everything': 52}
    >>>names_final = ['Dumplings R Us', 'Queen St. Cafe']
    >>>build_rating_list(name_to_rating, names_final)
    [[82, 'Queen St. Cafe'], [71, 'Dumplings R Us']]
    '''
    pre_result = []
    result = []
    # This creates the pre_results list, which is a list of ratings followed by names 
    for name in names_final:
        if name in name_to_rating:
            pre_result.append(name_to_rating[name])
            pre_result.append(name)
    
    # This groups each 2 elements in the order they appear in the pre_result list 
    # into inner lists of 2 elements each
    result = [pre_result[i:i+2] for i in range(0, len(pre_result), 2)]
    
    # This sorts the pre_result list of inner lists according to the the inner list position [0]
    result.sort(key=lambda x: x[0], reverse=True)
    return result

print(recommend(file, '$', ['Chinese', 'Thai']))