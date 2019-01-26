def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated
    """
    # TODO
    longest_runs = []
    for i in range(numTrials):
        rolls = [die.roll() for j in range(numRolls)]
        size = 1
        max_size = 0
        for i in range(len(rolls)-1):
            if rolls[i+1] == rolls[i]:
                size += 1
            else:
                size = 1
            if max_size < size:
                max_size = size
        if max_size > 0:
            longest_runs.append(max_size)
        else:
            longest_runs.append(1)
    makeHistogram(longest_runs, numBins = 10, xLabel = 'Length of longest run', yLabel = 'frequency', title = 'Histogram of longest runs')
    return sum(longest_runs)/len(longest_runs)
    