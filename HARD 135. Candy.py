'''
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.

 

Example 1:

Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
Example 2:

Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.
 

Constraints:

n == ratings.length
1 <= n <= 2 * 10^4
0 <= ratings[i] <= 2 * 10^4

Example Walk through 
Example 2: ratings = [1, 2, 2] in detail, focusing on why the third child gets 1 candy.

The Conditions Revisited:

Each child must have at least one candy. (Base minimum)
Children with a higher rating get more candies than their neighbors. This is key. It means:
If ratings[i] > ratings[i-1], then candies[i] > candies[i-1].
If ratings[i] > ratings[i+1], then candies[i] > candies[i+1].
Crucial Point: "Higher rating"

The condition is only applied when a child has a higher rating than their neighbor. It does not state that if ratings are equal, candies must be equal or different. Nor does it state that if a child has a lower rating, they must get fewer candies (though this often naturally happens to minimize candies).

Let's apply this to ratings = [1, 2, 2] with the two-pass algorithm.

Walkthrough of ratings = [1, 2, 2]
Initial State (After Step 1: Initialize all candies to 1)

ratings = [1, 2, 2]
candies = [1, 1, 1]

Left-to-Right Pass (Step 2: for i in range(1, n)):

This pass ensures candies[i] > candies[i-1] if ratings[i] > ratings[i-1].

i = 1 (Child with rating 2, comparing with Child 0 with rating 1):

ratings[1] (2) > ratings[0] (1)? Yes.
Therefore, candies[1] must be candies[0] + 1.
candies[1] = 1 + 1 = 2.
candies becomes [1, 2, 1]
i = 2 (Child with rating 2, comparing with Child 1 with rating 2):

ratings[2] (2) > ratings[1] (2)? No. (2 is not greater than 2)
The condition ratings[i] > ratings[i-1] is not met. So, no adjustment is made based on the left neighbor in this pass for candies[2].
candies remains [1, 2, 1]
After Left-to-Right Pass: candies = [1, 2, 1]

Right-to-Left Pass (Step 3: for i in range(n - 2, -1, -1)):

This pass ensures candies[i] > candies[i+1] if ratings[i] > ratings[i+1]. It also uses max to preserve prior adjustments.

i = 1 (Child with rating 2, comparing with Child 2 with rating 2):

ratings[1] (2) > ratings[2] (2)? No. (2 is not greater than 2)
The condition ratings[i] > ratings[i+1] is not met. So, no adjustment is made based on the right neighbor for candies[1].
candies remains [1, 2, 1]
i = 0 (Child with rating 1, comparing with Child 1 with rating 2):

ratings[0] (1) > ratings[1] (2)? No. (1 is not greater than 2)
The condition ratings[i] > ratings[i+1] is not met. So, no adjustment is made based on the right neighbor for candies[0].
candies remains [1, 2, 1]
After Right-to-Left Pass: candies = [1, 2, 1]

Final Step (Step 4: Sum all candies):

Total candies = 1+2+1=4.
'''

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n  # Step 1: Give each child 1 candy initially

        # Step 2: Left to Right pass
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # Step 3: Right to Left pass
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        # Step 4: Return total candies
        return sum(candies)


'''
Code Explanation
class Solution(object):
This defines a class named Solution. In competitive programming platforms like LeetCode, solutions are often wrapped in a class.

def candy(self, ratings):
This defines a method (a function within a class) named candy.

self: A reference to the current instance of the class (standard for Python methods).
ratings: This is the input parameter, a list of integers representing the rating of each child.
""" Docstring """: This is a docstring, providing a brief description of what the function does, its argument types (:type ratings: List[int]), and its return type (:rtype: int).
n = len(ratings)
This line calculates the number of children (or ratings) and stores it in the variable n. This is useful for loop boundaries.

candies = [1] * n (Step 1: Give each child 1 candy initially)

This is a crucial initialization step. It creates a list called candies of the same length as ratings (i.e., n elements).
[1] * n efficiently creates a list where all n elements are initialized to 1.
Purpose: This directly addresses the first requirement: "Each child must have at least one candy." By starting everyone with 1 candy, we guarantee this base condition.
for i in range(1, n): (Step 2: Left to Right pass)

This initiates a for loop that iterates from i = 1 up to n - 1.
Purpose: This loop processes the children from left to right, starting from the second child (index 1) because each child needs to compare with their left neighbor (index i-1).
if ratings[i] > ratings[i - 1]: This condition checks if the current child's rating (ratings[i]) is higher than their immediate left neighbor's rating (ratings[i - 1]).
candies[i] = candies[i - 1] + 1 If the condition is true (current child has a higher rating than the left neighbor), then the current child must receive one more candy than their left neighbor. We update candies[i] accordingly. Example: If ratings = [1, 2, 0]
Initial candies = [1, 1, 1]
i = 1: ratings[1] (2) > ratings[0] (1) is true. So, candies[1] = candies[0] + 1 = 1 + 1 = 2. candies becomes [1, 2, 1]
i = 2: ratings[2] (0) > ratings[1] (2) is false. No change. candies remains [1, 2, 1] After this pass, all children who have a higher rating than their left neighbor will have more candies than that neighbor.
for i in range(n - 2, -1, -1): (Step 3: Right to Left pass)

This initiates another for loop that iterates from i = n - 2 down to 0 (inclusive).
n - 2: Starts from the second-to-last child.
-1: The loop stops before reaching -1 (so it includes 0).
-1: This is the step, meaning it decrements i by 1 in each iteration.
Purpose: This loop processes the children from right to left, starting from the second-to-last child (index n-2) because each child needs to compare with their right neighbor (index i+1).
if ratings[i] > ratings[i + 1]: This condition checks if the current child's rating (ratings[i]) is higher than their immediate right neighbor's rating (ratings[i + 1]).
candies[i] = max(candies[i], candies[i + 1] + 1) If the condition is true, this is the most critical part. The current child must receive more candies than their right neighbor.
candies[i + 1] + 1: This is the minimum number of candies candies[i] should have to satisfy the right neighbor condition.
max(candies[i], ...): We use max because candies[i] might have already been increased during the left-to-right pass. We need to ensure that candies[i] satisfies both conditions (left neighbor and right neighbor). By taking the maximum, we either keep the value derived from the left pass (if it's already sufficient) or increase it to satisfy the right pass condition. Example (continuing from previous): ratings = [1, 2, 0], current candies = [1, 2, 1]
i = 1: ratings[1] (2) > ratings[2] (0) is true. candies[1] = max(candies[1], candies[2] + 1) = max(2, 1 + 1) = max(2, 2) = 2. candies remains [1, 2, 1] (no change here, as it already satisfied)
i = 0: ratings[0] (1) > ratings[1] (2) is false. No change. candies remains [1, 2, 1] Consider ratings = [1, 0, 2] from the problem example:
Initial candies = [1, 1, 1]
Left-to-Right:
i = 1: ratings[1] (0) > ratings[0] (1) is false. candies = [1, 1, 1]
i = 2: ratings[2] (2) > ratings[1] (0) is true. candies[2] = candies[1] + 1 = 1 + 1 = 2. candies = [1, 1, 2]
Right-to-Left:
i = 1: ratings[1] (0) > ratings[2] (2) is false. candies = [1, 1, 2]
i = 0: ratings[0] (1) > ratings[1] (0) is true. candies[0] = max(candies[0], candies[1] + 1) = max(1, 1 + 1) = max(1, 2) = 2. candies = [2, 1, 2]
return sum(candies) (Step 4: Return total candies)

Finally, after both passes, the candies list holds the minimum required candies for each child to satisfy all conditions.
sum(candies) calculates the total number of candies needed across all children.
'''
