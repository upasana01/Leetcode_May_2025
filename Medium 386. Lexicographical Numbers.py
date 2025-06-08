'''
Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.

You must write an algorithm that runs in O(n) time and uses O(1) extra space. 

 

Example 1:

Input: n = 13
Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]
Example 2:

Input: n = 2
Output: [1,2]

'''

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []
        current_num = 1

        for _ in range(n):
            result.append(current_num)

            # Try to go deeper (e.g., from 1 to 10)
            if current_num * 10 <= n:
                current_num *= 10
            # Try to go sideways or backtrack (e.g., from 1 to 2, or from 19 to 2, from 12 to 13)
            else:
                # If we are at 'n' or the last digit is 9, we need to backtrack
                # For example, if n=13 and current_num=13, we can't go deeper or sideways
                # or if n=19 and current_num=19, we can't go deeper or sideways
                while current_num % 10 == 9 or current_num + 1 > n:
                    current_num //= 10  # Go up one level (e.g., from 13 to 1, or from 19 to 1)
                current_num += 1  # Go sideways at the higher level (e.g., from 1 to 2)
        
        return result
