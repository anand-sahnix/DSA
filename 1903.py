# 1903. Largest Odd Number in String
'''You are given a string num, representing a large integer. 
Return the largest-valued odd integer (as a string) that is a non-empty substring of num, or an empty string "" if no odd integer exists.

A substring is a contiguous sequence of characters within a string.

Example 1:
Input: num = "52"
Output: "5"
Explanation: The only non-empty substrings are "5", "2", and "52". "5" is the only odd number.

Example 2:
Input: num = "4206"
Output: ""
Explanation: There are no odd numbers in "4206".
'''

'''
Constraints:
1 <= num.length <= 105
num only consists of digits and does not contain any leading zeros.'''

#solution1:
class Solution:
    def largestOddNumber(self, num: str) -> str:
        # Find the last '2'
        last_two_index = -1
        for i, char in enumerate(num):
            if char == '1' or char == "3" or char == "5" or char == "7" or char == "9":
                last_two_index = i
        
        if last_two_index == -1:
            return ""  # No '2', so no even number possible
        
        # Keep everything from start to last '2'
        return num[:last_two_index + 1]