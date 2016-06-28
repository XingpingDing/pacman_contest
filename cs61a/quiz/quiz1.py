#  Name:
#  Email:

# Q1.

from doctest import run_docstring_examples

def overlaps(low0, high0, low1, high1):
    """Return whether the open intervals (LOW0, HIGH0) and (LOW1, HIGH1)
    overlap.

    >>> overlaps(10, 15, 14, 16)
    True
    >>> overlaps(10, 15, 1, 5)
    False
    >>> overlaps(10, 10, 9, 11)
    False
    >>> result = overlaps(1, 5, 0, 3)  # Return, don't print
    >>> result
    True
    """
    "*** YOUR CODE HERE ***"
    for num1 in range(low0,high0):
        for num2 in range(low1,high1):
            if num1 == num2:
                return True
    return False

# Q2.

import math
def last_square(x):
    """Return the largest perfect square less than X, where X>0.

    >>> last_square(10)
    9
    >>> last_square(39)
    36
    >>> last_square(100)
    81
    >>> result = last_square(2) # Return, don't print
    >>> result
    1
    """
    "*** YOUR CODE HERE ***"
    return pow(math.floor(math.sqrt(x-1)),2)

# Q3.

def ordered_digits(x):
    """Return True if the (base 10) digits of X>0 are in non-decreasing
    order, and False otherwise.

    >>> ordered_digits(5)
    True
    >>> ordered_digits(11)
    True
    >>> ordered_digits(127)
    True
    >>> ordered_digits(1357)
    True
    >>> ordered_digits(21)
    False
    >>> result = ordered_digits(1375) # Return, don't print
    >>> result
    False
    """
    "*** YOUR CODE HERE ***"
    numbers = []
    while x:
        numbers.append(x%10)
        x = (x-x%10)/10
    for index in range(0,len(numbers)-1):
        if numbers[index]<numbers[index+1]:
            return False
    return True

if __name__ == "__main__":
    run_docstring_examples(overlaps, globals(), True)
    run_docstring_examples(last_square, globals(), True)
    run_docstring_examples(ordered_digits, globals(), True)

