# Given list of ints, return True if any two nums in list sum to 0.
# *CORRECT*

def add_to_zero(nums):

    for num in nums: 

        if len(nums) ==  0:
            return False

        for num1 in nums:
            if num + num1 == 0:
                return True
            
    return False

    #OR   O(1) better with set

    set_nums = set(lst)

    for num in set_nums:
        if -num in set_nums:
            return True
        
    return False


#Find the largest integer in a list of integers.

def largest_num(nums):

    largest = nums[0]

    for num in nums:
        if num > largest:
            largest = num

    return largest


#You should sum up these numbers You should return the sum of these two numbers in the same “reverse-digit” format.
#For 123 + 456, this should return 579, in the form of a list like this:   9--> 7--> 5--> None

def add_linked_lists(l1, l2):

    current1 = l1
    current2 = l2

    while current1 or current2:
        if current1:
            current1 = l1.data
            current1 = l1.next
        else:
            current1 = 0

        if current2:
            current2 = l2.data
            current2 = l2.next
        else:
            current2 = 0




#Given a string, return True or False depending on whether that string has balanced parentheses.
# *CORRECT*
def has_balanced_parens(string):

    count1 = 0
    count2 = 0

    for char in string:
        if char == "(":
            count1 += 1
        elif char == ")":
            count2 += 1

    return count1 == count2


#Given a string with a month and a year (separated by a space), return the number of days in that month.
# *CORRECT*
def days_in_month(date):

    date_list = date.split(" ")    #OR   month, year = date.split()
    month = int(date_list[0])
    year = int(date_list[1])

    if month == 2:
        if is_leap_year(year):
            return 29
        else:
            return 28
        
    if month in {1, 3, 5, 7, 8, 10, 12}:
        return 31
    if month in {4, 6, 9, 11}:
        return 30
    
def is_leap_year(year):

    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True

#Given a list of numbers, return the smallest and the largest number.
#For an empty list, it should return None as both smallest and largest:
#Make sure it works with a list of one item, which is both smallest and largest:

# *CORRECT*
def find_range(nums):

    if len(nums) == 0:
        return(None, None)
    
    if len(nums) == 1:
        return(nums[0], nums[0])
    
    smallest = nums[0]
    largest = nums[0]

    for num in nums:
        if num < smallest:
            smallest = num

        elif num > largest:
            largest = num

    return(smallest, largest)


#You will be given a list of integers, some even and some odd:
#Write a function that returns the indices (0-based, as usual in Python) of all the numbers which are even.
# *CORRECT*
def show_evens(nums):

    if nums == []:
        return None
    
    even_indices = []
    
    for idx, num in enumerate(nums):
        if num % 2 == 0:
            even_indices.append(idx)

    return even_indices


    #OR Not using enumerate

    even_indices = []

    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            even_indices.append(i)

    return even_indices

#Compute the sum of a list of numbers.
# *CORRECT*
def sum_list(nums):

    total = 0

    for num in nums:
        total += num

    return total



#In this challenge, you should create a function that works like that built-in Python .split() method 1.
# *CORRECT* but study further.
def split_string(string, splitter):
    
    split_list = []
    index = 0

    while index <= len(string):

        start_index = index
        index = string.find(splitter, index)    #Find method finds the 'element' and optional index start and end if supplied.  Here supplied start.

        if index != -1:
            split_list.append(string[start_index:index])
            index += len(splitter)

        else:
            split_list.append(string[start_index:])
            break

    return split_list
    
    