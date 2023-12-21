#Example 1:
"""Input: candies = [2,3,5,1,3], extraCandies = 3
Output: [true,true,true,false,true] 
Explanation: If you give all extraCandies to:
- Kid 1, they will have 2 + 3 = 5 candies, which is the greatest among the kids.
- Kid 2, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
- Kid 3, they will have 5 + 3 = 8 candies, which is the greatest among the kids.
- Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest among the kids.
- Kid 5, they will have 3 + 3 = 6 candies, which is the greatest among the kids."""

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        results = []

        largest = max(candies)

        for candy in candies:
            if candy + extraCandies >= largest:
                results.append(True)
            else:
                results.append(False)

        return results
    

    
    """You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true"""

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        flowerbed = [0] + flowerbed + [0]

        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                n -= 1

            if n <= 0:
                return True

        return False



"""Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Example 1:

Input: s = "hello"
Output: "holle"""

class Solution:
    def reverseVowels(self, s: str) -> str:

        vowels = "AEIOUaeiou"
        split_string = list(s) 
        vowel_list = []             

        for char in split_string:   
            if char in vowels:      
                vowel_list.append(char) 

        for idx,char in enumerate(split_string):        
            if char in vowels:             
                replace = vowel_list.pop()
                split_string[idx] = replace

        reverse_string = "".join(split_string)

        return reverse_string



"""Given the head of a singly linked list, reverse the list, and return the reversed list.
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        current = head
        previous = None

        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next

        return previous
    


"""You are given two strings word1 and word2. Merge the strings by adding 
letters in alternating order, starting with word1. If a string is longer than the other,
 append the additional letters onto the end of the merged string.
Return the merged string.

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        result = ""

        len1 = len(word1)
        len2 = len(word2)

        for i in range(min(len1, len2)):
            result += word1[i]
            result += word2[i]

        if len1 > len2:
            result += word1[len2:]

        if len2 > len1:
            result += word2[len1:]

        return result
    


"""Given an input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
Return a string of the words in reverse order concatenated by a single space.
Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the
"""

class Solution:
    def reverseWords(self, s: str) -> str:

        split_string = s.split()
        reversed_list = []

        for word in split_string:
        
            reversed_list.insert(0, word)

        result = " ".join(reversed_list)

        return result 


    """There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes.
      The biker starts his trip on point 0 with altitude equal 0.
You are given an integer array gain of length n where gain[i] is the net gain in altitude between points
 i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.

Example 1:

Input: gain = [-5,1,5,0,-7]
Output: 1
Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1."""  

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

        current = 0    
        altitudes = [0]

        for i in range(len(gain)):
            current = current + (gain[i])
            altitudes.append(current)
            
        altitudes.sort()     

        return altitudes[-1]


        
        