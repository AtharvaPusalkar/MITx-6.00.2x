def r_squared(y, estimated):
    """
    Calculate the R-squared error term.
    Args:
        y: list with length N, representing the y-coords of N sample points
        estimated: a list of values estimated by the regression model
    Returns:
        a float for the R-squared error term
    """
    mean = sum(y)/len(y)
    numerator = 0
    denominator = 0
    for i in range(len(estimated)):
        numerator += (y[i] - estimated[i])**2
    for i in range(len(estimated)):
        denominator += (y[i] - mean)**2
    return 1 - numerator/denominator
    