"""
2434. Using a Robot to Print the Lexicographically Smallest String

You are given a string s and a robot that currently holds an empty string t. Apply one of the following operations until s and t are both empty:

Remove the first character of a string s and give it to the robot. The robot will append this character to the string t.
Remove the last character of a string t and give it to the robot. The robot will write this character on paper.
Return the lexicographically smallest string that can be written on the paper.

 

Example 1:

Input: s = "zza"
Output: "azz"
Explanation: Let p denote the written string.
Initially p="", s="zza", t="".
Perform first operation three times p="", s="", t="zza".
Perform second operation three times p="azz", s="", t="".
Example 2:

Input: s = "bac"
Output: "abc"
Explanation: Let p denote the written string.
Perform first operation twice p="", s="c", t="ba". 
Perform second operation twice p="ab", s="c", t="". 
Perform first operation p="ab", s="", t="c". 
Perform second operation p="abc", s="", t="".
Example 3:

Input: s = "bdda"
Output: "addb"
Explanation: Let p denote the written string.
Initially p="", s="bdda", t="".
Perform first operation four times p="", s="", t="bdda".
Perform second operation four times p="addb", s="", t="".
 

Constraints:

1 <= s.length <= 105
s consists of only English lowercase letters.

"""

from collections import Counter

class Solution:
    def robotWithString(self, s: str) -> str:
        freq = Counter(s)  # 1. Stores the frequency of each character remaining in `s`.
        st = []            # 2. This acts as our temporary string `t` (a stack).
        res = []           # 3. This will store the characters written on paper.
        
        def min_char(freq):
            # Helper function to find the smallest character currently available in `s`.
            for i in range(26):
                ch = chr(ord('a') + i)
                if freq[ch] > 0:
                    return ch
            return 'a' # Should not be reached if s is not empty initially, but good for robustness.

        for ch in s:
            st.append(ch)  # Operation 1: Move character from `s` to `t` (append to stack).
            freq[ch] -= 1  # Decrement frequency as this character is no longer in `s`.
            
            # This is the core greedy decision.
            # While the stack `st` is not empty AND the last character in `st`
            # is less than or equal to the smallest character remaining in `s`:
            while st and st[-1] <= min_char(freq):
                res.append(st.pop()) # Operation 2: Move character from `t` to paper (pop from stack).

        # After processing all characters from `s`, any remaining characters in `st`
        # must be moved to `res` in reverse order (since `t` is a stack and we pop from end).
        while st:
            res.append(st.pop())

        return ''.join(res) # Join the characters to form the final string.


"""
This problem asks us to find the lexicographically smallest string that can be formed by a robot. We start with a given string s and an empty string t. The robot can perform two operations:

Move from s to t: Take the first character from s and append it to t.
Move from t to paper: Take the last character from t and write it on paper.
Our goal is to make the string written on paper as small as possible lexicographically. This means we want to put smaller characters earlier in the output string.

Let's break down the logic. At any point, we have some characters remaining in s, some characters on a temporary stack t, and some characters already written on paper (which form our res string).

The key insight is to realize that to get the lexicographically smallest string, we should always try to output the smallest possible character right now. The smallest possible character can come from two places:

The top of the stack t (its last character).
Any character that is still in s (even if it's not the first one in s).
We can't directly access characters in s that aren't at the front. However, we can find the smallest character that will eventually appear in s. This is where the frequency count comes in handy.

The Code Explained
The provided Python code implements this greedy strategy:

Python

from collections import Counter

class Solution:
    def robotWithString(self, s: str) -> str:
        freq = Counter(s)  # 1. Stores the frequency of each character remaining in `s`.
        st = []            # 2. This acts as our temporary string `t` (a stack).
        res = []           # 3. This will store the characters written on paper.
        
        def min_char(freq):
            # Helper function to find the smallest character currently available in `s`.
            for i in range(26):
                ch = chr(ord('a') + i)
                if freq[ch] > 0:
                    return ch
            return 'a' # Should not be reached if s is not empty initially, but good for robustness.

        for ch in s:
            st.append(ch)  # Operation 1: Move character from `s` to `t` (append to stack).
            freq[ch] -= 1  # Decrement frequency as this character is no longer in `s`.
            
            # This is the core greedy decision.
            # While the stack `st` is not empty AND the last character in `st`
            # is less than or equal to the smallest character remaining in `s`:
            while st and st[-1] <= min_char(freq):
                res.append(st.pop()) # Operation 2: Move character from `t` to paper (pop from stack).

        # After processing all characters from `s`, any remaining characters in `st`
        # must be moved to `res` in reverse order (since `t` is a stack and we pop from end).
        while st:
            res.append(st.pop())

        return ''.join(res) # Join the characters to form the final string.
Detailed Breakdown:

freq = Counter(s): We initialize a Counter to keep track of the frequency of each character in the original string s. 
This allows us to quickly determine the smallest character remaining in s at any given time.
st = []: This list acts as our temporary string t. Since we remove the last character from t and append characters to t, a stack (LIFO) is the perfect data structure.
Python lists' append() and pop() methods work perfectly for this.
res = []: This list will store the characters written on paper, in the order they are written.
min_char(freq) function: This helper function iterates from 'a' to 'z' and returns the first character it finds that still has a count greater than 0 in freq. 
This effectively tells us the smallest character that is yet to be processed from the original string s.
for ch in s: loop: This loop simulates processing the characters of s one by one.
st.append(ch): We always move the current character ch from s to t. This is operation 1.
freq[ch] -= 1: We decrement the frequency of ch because it's no longer in s.
while st and st[-1] <= min_char(freq):: This is the crucial greedy decision.
st and st[-1]: Checks if the stack st is not empty.
st[-1] <= min_char(freq): This is the core condition. If the last character on our stack t (st[-1]) is less than or equal to the smallest character that is still available in the original string s 
(or rather, the characters that haven't been moved from s yet), it means we can output st[-1] now without jeopardizing the lexicographical order of the remaining characters. 
Why? Because st[-1] is already smaller than or equal to anything we could eventually put on the stack from s. So, it's optimal to write it down immediately.
res.append(st.pop()): If the condition is met, we perform operation 2: pop the character from t and append it to our result string.
while st:: After processing all characters from s, there might be characters remaining in our temporary stack st. Since there are no more characters to get from s 
(meaning min_char(freq) would return 'a' if s was empty, or would be irrelevant if s is empty and freq is all zeros), we must now move all remaining characters from st to res. 
Because st is a stack, popping them all will put them in reverse order of how they were pushed, which is the only way to output them now.
return ''.join(res): Finally, join the characters in res to form the resulting string.
Example Walkthrough: s = "bac"
Initially: s = "bac", t = "", p = "", freq = {'b': 1, 'a': 1, 'c': 1}

ch = 'b' (from s)

st.append('b') -> st = ['b']
freq['b'] -= 1 -> freq = {'b': 0, 'a': 1, 'c': 1}
min_char(freq) returns 'a'.
st[-1] ('b') is NOT <= 'a'.
while loop condition is false.
ch = 'a' (from s)

st.append('a') -> st = ['b', 'a']
freq['a'] -= 1 -> freq = {'b': 0, 'a': 0, 'c': 1}
min_char(freq) returns 'c'.
st[-1] ('a') IS <= 'c'.
while loop executes:
res.append(st.pop()) -> res = ['a'], st = ['b']
st[-1] ('b') is NOT <= 'c'.
while loop condition is false.
ch = 'c' (from s)

st.append('c') -> st = ['b', 'c']
freq['c'] -= 1 -> freq = {'b': 0, 'a': 0, 'c': 0}
min_char(freq) would return 'a' (as all counts are 0, this case isn't problematic as st is not empty).
st[-1] ('c') is NOT <= 'a'. (This is where the logic about min_char needs to be thought through. If min_char returns 'a' when all counts are 0, then the check st[-1] <= 'a' would often be false unless st[-1] is 'a'.)
Correction/Refinement: In practice, once freq has all 0s, it means there are no more characters to pull from s to compare against. The min_char logic essentially determines the smallest character that can still be obtained from s. 
If s is empty, then effectively there are no characters to come from s to affect future comparisons, so the only source of characters is t.
In our example, min_char(freq) will return 'a' (or whatever the default smallest character is, given all counts are 0). st[-1] ('c') is NOT <= 'a'.
while loop condition is false.
End of for loop. s is now empty.

Process remaining characters in st: st = ['b', 'c']

while st: is true.
res.append(st.pop()) -> res = ['a', 'c'], st = ['b']
while st: is true.
res.append(st.pop()) -> res = ['a', 'c', 'b'], st = []
while st: is false.
Return "".join(res) which is "acb".

Wait, the example output is "abc". Let's re-evaluate the min_char logic. The problem statement says s consists of only lowercase English letters. If freq has all 0s,
it means all characters from the original s have been moved to t. In this case, min_char(freq) effectively represents the smallest character that could have been pulled from s.
But more importantly, the while st and st[-1] <= min_char(freq) condition is about what's coming. If nothing is coming (all s chars are in t), then any character on t is "safe" to pop if it's the current minimum.

Let's trace Example 2 from the problem statement: s = "bac", Output: abc

Initially: p="", s="bac", t="", freq = {'b':1, 'a':1, 'c':1}

ch = 'b' (from s)

st.append('b') -> st = ['b']
freq['b'] = 0 -> freq = {'a':1, 'c':1}
min_char(freq) = 'a'
st[-1] ('b') is NOT <= 'a'.
while loop skips.
ch = 'a' (from s)

st.append('a') -> st = ['b', 'a']
freq['a'] = 0 -> freq = {'c':1}
min_char(freq) = 'c'
st[-1] ('a') IS <= 'c'.
while loop executes:
res.append(st.pop()) -> res = ['a'], st = ['b']
Now st = ['b']. min_char(freq) is still 'c'.
st[-1] ('b') IS <= 'c'.
while loop executes again:
res.append(st.pop()) -> res = ['a', 'b'], st = []
Now st = []. while loop condition st is false. Loop terminates.
ch = 'c' (from s)

st.append('c') -> st = ['c']
freq['c'] = 0 -> freq = {} (effectively all counts are zero)
min_char(freq) would return 'a' (because it iterates 'a' through 'z' and finds no counts > 0, so 'a' is the first character it tries to return).
st[-1] ('c') is NOT <= 'a'.
while loop skips.
End of for loop. s is now empty.

Process remaining characters in st: st = ['c']

while st: is true.
res.append(st.pop()) -> res = ['a', 'b', 'c'], st = []
while st: is false.
Return "".join(res) which is "abc".

This trace matches the example output! The min_char(freq) behavior when freq is all zeros (meaning all characters from s have been moved to t) 
correctly implies that any character currently on t is a candidate for output if it's smaller than 'a' (which it won't be, since it's a lowercase letter). In essence, once s is empty, 
min_char(freq) is irrelevant because there are no more characters to compare against from s. 
All comparisons then depend on what's on the stack. The loop while st and st[-1] <= min_char(freq) will continue to pop characters if st[-1] is the smallest 
possible character or smaller than anything that could come from s (which is now empty). When min_char(freq) effectively returns 'a', st[-1] <= 'a' means st[-1] must be 'a'. If st[-1] is any other character, 
it won't satisfy the condition. This ensures that only the smallest character on t is popped if it's truly the smallest among all available options.

The logic holds. The min_char(freq) allows us to look ahead and only pop from t if the character on top of t is guaranteed to be smaller than or equal to any character we might still get from s.
If it is, we pop it. If not, we keep pulling characters from s onto t until a better opportunity arises, or until s is empty and we have to empty t.
"""
