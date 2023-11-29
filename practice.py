# Given list of ints, return True if any two nums in list sum to 0.

def add_to_zero(lst):

    for num in lst:

        if len(lst) ==  0:
            return False

        for num1 in lst:
            if num + num1 == 0:
                return True
            
    return False