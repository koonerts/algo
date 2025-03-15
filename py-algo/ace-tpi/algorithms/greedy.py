def find_min_coins(v):
    """
    This function finds the minimum number of coins
    :param v: Total amount
    :return: A list of total coins
    """
    result = []
    while v // 25 >= 1:
        result.append(25)
        v -= 25

    while v // 10 >= 1:
        result.append(10)
        v -= 10

    while v // 5 >= 1:
        result.append(5)
        v -= 5

    while v // 1 >= 1:
        result.append(1)
        v -= 1
    return result


def min_cost(pipes):
    """
    Calculates the minimum cost of connecting pipes
    :param pipes: A list where its length is the number of pipes and indexes are the specific lengths of the pipes.
    :return: The minimum cost
    """
    pass


def egyptian_fraction(numerator, denominator):
    """
    Finds the egyptian fraction denominators
    :param numerator: Numerator of the fraction
    :param denominator: Denominator of the fraction
    :return: A list of denominators of the egyptian fraction
    """
    pass


def find_largest_number(number_of_digits, sum_of_digits):
    """
    Finds the largest number with given number of digits and sum of Digits
    :param number_of_digits: Number of digits
    :param sum_of_digits: Sum of digits
    :return: Possible largest number
    """
    pass
