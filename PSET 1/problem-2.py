def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:
    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.
    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    trips = []
    power_list = sorted(get_partitions(cows), key = len)
    possibilities = []
    for i in power_list:
        ship = []
        for j in i:
            ship_weights = []
            for k in j:
                ship_weights.append(cows[k])
            ship.append(sum(ship_weights))
        if all(d <= limit for d in ship):
            possibilities.append(i)
    min_list_len = min(map(len, possibilities))
    for l in possibilities:
        if len(l) == min_list_len:
            return l
            