"""

You have n boxes labeled from 0 to n - 1. You are given four arrays: status, candies, keys, and containedBoxes where:

status[i] is 1 if the ith box is open and 0 if the ith box is closed,
candies[i] is the number of candies in the ith box,
keys[i] is a list of the labels of the boxes you can open after opening the ith box.
containedBoxes[i] is a list of the boxes you found inside the ith box.
You are given an integer array initialBoxes that contains the labels of the boxes you initially have. You can take all the candies in any open box and you can use the keys in it to open new boxes and you also can use the boxes you find in it.

Return the maximum number of candies you can get following the rules above.

 

Example 1:

Input: status = [1,0,1,0], candies = [7,5,4,100], keys = [[],[],[1],[]], containedBoxes = [[1,2],[3],[],[]], initialBoxes = [0]
Output: 16
Explanation: You will be initially given box 0. You will find 7 candies in it and boxes 1 and 2.
Box 1 is closed and you do not have a key for it so you will open box 2. You will find 4 candies and a key to box 1 in box 2.
In box 1, you will find 5 candies and box 3 but you will not find a key to box 3 so box 3 will remain closed.
Total number of candies collected = 7 + 4 + 5 = 16 candy.
Example 2:

Input: status = [1,0,0,0,0,0], candies = [1,1,1,1,1,1], keys = [[1,2,3,4,5],[],[],[],[],[]], containedBoxes = [[1,2,3,4,5],[],[],[],[],[]], initialBoxes = [0]
Output: 6
Explanation: You have initially box 0. Opening it you can find boxes 1,2,3,4 and 5 and their keys.
The total number of candies will be 6.
 """


class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        
        def dfs(i):
            ans = candies[i]
            status[i] = 0
            
            for k in keys[i]:
                status[k] |= 1
                if status[k] == 3:
                    ans += dfs(k)
                    
            for j in containedBoxes[i]:
                status[j] |= 2
                if status[j] == 3:
                    ans += dfs(j)
                    
            return ans
        
        total_candies_collected = 0
        
        for i in initialBoxes:
            status[i] |= 2
            if status[i] == 3:
                total_candies_collected += dfs(i)
                
        return total_candies_collected


"""
from typing import List

"""
To simplify code, reuse status:
- 0: closed and not 'had' (initial state or processed)
- 1: open (key applied), but not 'had' (not discovered yet)
- 2: 'had' (discovered), but closed (no key yet)
- 3: open AND 'had' (can be processed)
"""
class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        
        # This DFS function recursively explores boxes, collects candies, and updates box statuses.
        # It assumes the current box 'i' is already in state 3 (open and had).
        def dfs(i):
            # Collect candies from the current box.
            ans = candies[i]
            
            # Mark the current box as processed by setting its status to 0.
            # This prevents recounting candies and infinite loops.
            status[i] = 0
            
            # Process keys found in the current box.
            for k in keys[i]:
                # Use bitwise OR to set the 'open' bit (1) for box 'k'.
                # If status[k] was 0 or 2, it becomes 1 or 3 respectively.
                status[k] |= 1
                
                # If box 'k' is now both open (1) and had (2) (status == 3),
                # recursively call DFS to process it and add its candies to the total.
                if status[k] == 3:
                    ans += dfs(k)
                    
            # Process boxes found inside the current box.
            for j in containedBoxes[i]:
                # Use bitwise OR to set the 'had' bit (2) for box 'j'.
                # If status[j] was 0 or 1, it becomes 2 or 3 respectively.
                status[j] |= 2
                
                # If box 'j' is now both open (1) and had (2) (status == 3),
                # recursively call DFS to process it and add its candies to the total.
                if status[j] == 3:
                    ans += dfs(j)
                    
            # Return the total candies collected from this branch of the DFS.
            return ans
        
        total_candies_collected = 0
        
        # Iterate through the initially available boxes.
        for i in initialBoxes:
            # Mark each initial box as 'had' by setting the 2 bit in its status.
            # This means we possess these boxes from the start.
            status[i] |= 2
            
            # If an initial box is now both open (original status was 1) and had (now 2),
            # its status will be 3, meaning we can open and process it immediately.
            if status[i] == 3:
                # Start the DFS traversal from this box and add the collected candies
                # to our running total.
                total_candies_collected += dfs(i)
                
        # Return the grand total of all candies collected.
        return total_candies_collected
"""

"""
Problem: Maximum Candies You Can Get from Boxes
You are given a set of n boxes. Each box has the following properties:

status[i]: Indicates if the box is initially open (1) or closed (0).
candies[i]: The number of candies inside the box.
keys[i]: A list of box labels. If you open box i, you gain the keys to these boxes, meaning their status can change from 0 to 1 (if they were 0 and you didn't already have a key for them).
containedBoxes[i]: A list of box labels. If you open box i, you find these boxes inside. This means you now "have" these boxes.
You start with a set of initialBoxes. Your goal is to maximize the total number of candies you can collect. You can only collect candies from open boxes. When you open a box, you get its candies, its keys (which can open other boxes), and any boxes contained within it.

The challenge lies in the dependencies: you need a key to open a closed box, and you might find keys or new boxes inside other boxes. This suggests a graph-like traversal where the state of boxes (open, closed, discovered, etc.) changes as you explore.

Explanation of the Code
The provided Python code uses a Depth-First Search (DFS) approach to explore the boxes and collect candies. The core idea is to keep track of the state of each box using the status array. The original problem defines status as 0 for closed and 1 for open. The solution cleverly reuses and extends this status array to represent more complex states:

status[i] = 0: Box i is closed and not yet "had" (not discovered). (Initial state or after processing)
status[i] = 1: Box i is open (a key has been applied to it), but it hasn't been "had" yet.
status[i] = 2: Box i is "had" (discovered, either from initialBoxes or inside another box), but it's currently closed.
status[i] = 3: Box i is both open (a key has been applied) AND "had" (discovered). This is the only state where a box can be opened and its contents processed.
Let's break down the functions:

dfs(i) function:

This function is a recursive helper that performs the DFS traversal starting from box i. It assumes that status[i] is already 3 (meaning box i is both open and had), and therefore can be processed.

ans = candies[i]: Initialize the ans (candies from the current traversal path) with the candies from the current box i.
status[i] = 0: Once box i is processed (candies collected, keys and contained boxes handled), its status is set to 0. This effectively marks it as "visited" or "processed" to prevent infinite loops and recounting candies.
Processing keys[i]:
for k in keys[i]:: Iterate through each key k found in box i.
status[k] |= 1: This is a bitwise OR operation. It sets the "open" bit for box k.
If status[k] was 0 or 2, it becomes 1 or 3 respectively. This means you now have a key for box k.
if status[k] == 3: ans += dfs(k): If after gaining the key, box k is now both open (1) and had (2), meaning status[k] is 3, then recursively call dfs(k) to process box k and add its candies to ans.
Processing containedBoxes[i]:
for j in containedBoxes[i]:: Iterate through each box j found inside box i.
status[j] |= 2: This is a bitwise OR operation. It sets the "had" bit for box j.
If status[j] was 0 or 1, it becomes 2 or 3 respectively. This means you now "have" box j.
if status[j] == 3: ans += dfs(j): If after discovering box j, it is now both open (1) and had (2), meaning status[j] is 3, then recursively call dfs(j) to process box j and add its candies to ans.
return ans: Return the total candies collected from this branch of the DFS.
Main logic:

cnt = 0: Initialize a variable cnt to store the total candies collected.
for i in initialBoxes:: Iterate through each box provided in initialBoxes.
status[i] |= 2: For each initial box i, mark it as "had" by setting the 2 bit in its status. Since you initially have these boxes, they are considered "had".
if status[i] == 3:: If an initialBox is already open (its original status was 1) and now marked as had (2), then its status becomes 3. In this case, you can immediately start processing it.
cnt += dfs(i): Call dfs(i) to collect candies from this initial open and had box.
return cnt: Return the final cnt, which represents the maximum candies collected.
Example Walkthrough: status = [1,0,1,0], candies = [7,5,4,100], keys = [[],[],[1],[]], containedBoxes = [[1,2],[3],[],[]], initialBoxes = [0]
Initial State:

status = [1, 0, 1, 0] (Original status values)
candies = [7, 5, 4, 100]
keys = [[], [], [1], []]
containedBoxes = [[1, 2], [3], [], []]
initialBoxes = [0]
Processing initialBoxes:

We start with initialBoxes = [0].

Box 0:
i = 0.
status[0] |= 2: status[0] was 1. 1 | 2 = 3. So, status becomes [3, 0, 1, 0].
if status[0] == 3: This condition is True.
cnt += dfs(0): Call dfs(0).
Inside dfs(0):

ans = candies[0] = 7.

status[0] = 0: status becomes [0, 0, 1, 0]. (Box 0 is processed)

Process keys[0]: keys[0] is []. Nothing to do.

Process containedBoxes[0]: containedBoxes[0] is [1, 2].

Box 1:

j = 1.
status[1] |= 2: status[1] was 0. 0 | 2 = 2. So, status becomes [0, 2, 1, 0].
if status[1] == 3: status[1] is 2, so this is False. (Box 1 is "had" but not open yet).
Box 2:

j = 2.
status[2] |= 2: status[2] was 1. 1 | 2 = 3. So, status becomes [0, 2, 3, 0].
if status[2] == 3: This condition is True.
ans += dfs(2): Call dfs(2).
Inside dfs(2):

ans_dfs2 = candies[2] = 4.

status[2] = 0: status becomes [0, 2, 0, 0]. (Box 2 is processed)

Process keys[2]: keys[2] is [1].

Box 1 (from key):
k = 1.
status[1] |= 1: status[1] was 2. 2 | 1 = 3. So, status becomes [0, 3, 0, 0].
if status[1] == 3: This condition is True.
ans_dfs2 += dfs(1): Call dfs(1).
Inside dfs(1):

ans_dfs1 = candies[1] = 5.

status[1] = 0: status becomes [0, 0, 0, 0]. (Box 1 is processed)

Process keys[1]: keys[1] is []. Nothing to do.

Process containedBoxes[1]: containedBoxes[1] is [3].

Box 3:
j = 3.
status[3] |= 2: status[3] was 0. 0 | 2 = 2. So, status becomes [0, 0, 0, 2].
if status[3] == 3: status[3] is 2, so this is False. (Box 3 is "had" but not open yet).
return ans_dfs1 = 5.

Back in dfs(2):

ans_dfs2 was 4. Now ans_dfs2 += 5, so ans_dfs2 becomes 9.
Process containedBoxes[2]: containedBoxes[2] is []. Nothing to do.

return ans_dfs2 = 9.

Back in dfs(0):

ans was 7. Now ans += 9, so ans becomes 16.
return ans = 16.
Back in main logic:

cnt was 0. Now cnt += 16, so cnt becomes 16.
Final Result:

return cnt = 16.

This matches the example output and demonstrates how the status array, combined with the DFS traversal, correctly identifies and processes reachable and openable boxes to maximize candy collection.
"""
