'''
You are given two positive integers n and limit.

Return the total number of ways to distribute n candies among 3 children such that no child gets more than limit candies.

 

Example 1:

Input: n = 5, limit = 2
Output: 3
Explanation: There are 3 ways to distribute 5 candies such that no child gets more than 2 candies: (1, 2, 2), (2, 1, 2) and (2, 2, 1).
Example 2:

Input: n = 3, limit = 3
Output: 10
Explanation: There are 10 ways to distribute 3 candies such that no child gets more than 3 candies: (0, 0, 3), (0, 1, 2), (0, 2, 1), (0, 3, 0), (1, 0, 2), (1, 1, 1), (1, 2, 0), (2, 0, 1), (2, 1, 0) and (3, 0, 0).
 
'''

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        def h3(n):
            return 0 if n<0 else (n+2)*(n+1)//2
        return h3(n)-3*h3(n-limit-1)+3*h3(n-2*(limit+1))-h3(n-3*(limit+1))

'''
Problem Explanation
You are given two positive integers:

n: The total number of candies to distribute.
limit: The maximum number of candies any single child can receive.
You need to find the total number of distinct ways to distribute these n candies among 3 children, subject to the constraint that no child receives more than limit candies.

Key things to note:

The children are distinct (Child 1, Child 2, Child 3). So, (1, 2, 2) is different from (2, 1, 2).
The number of candies for each child must be a non-negative integer.
Example Walkthrough: n = 5, limit = 2
We need to find combinations of (candies for child 1, candies for child 2, candies for child 3) such that:

c1 + c2 + c3 = 5
0 <= c1 <= 2
0 <= c2 <= 2
0 <= c3 <= 2
Let's manually list them out systematically:

Start with Child 1 getting the minimum possible (0 candies) and increase:

If c1 = 0: Then c2 + c3 = 5.
If c2 = 0, c3 = 5 (Invalid: c3 > limit)
If c2 = 1, c3 = 4 (Invalid: c3 > limit)
If c2 = 2, c3 = 3 (Invalid: c3 > limit)
No valid combinations when c1 = 0. This makes sense, as the sum needs to be 5, and max for each is 2, so at least one child must get more than 2 if another gets 0.
Try c1 = 1: Then c2 + c3 = 4.

If c2 = 0, c3 = 4 (Invalid: c3 > limit)
If c2 = 1, c3 = 3 (Invalid: c3 > limit)
If c2 = 2, c3 = 2 (Valid: (1, 2, 2))
So, one way: (1, 2, 2)
Try c1 = 2: Then c2 + c3 = 3.

If c2 = 0, c3 = 3 (Invalid: c3 > limit)
If c2 = 1, c3 = 2 (Valid: (2, 1, 2))
If c2 = 2, c3 = 1 (Valid: (2, 2, 1))
So, two ways: (2, 1, 2), (2, 2, 1)
Total Valid Ways: 3
These are (1, 2, 2), (2, 1, 2), and (2, 2, 1). This matches the example output.

Code Explanation: Principle of Inclusion-Exclusion
The provided code uses a mathematical technique called the Principle of Inclusion-Exclusion to solve this problem.

First, let's understand the h3(n) helper function.

h3(n) Helper Function
Python

        def h3(n):
            return 0 if n<0 else (n+2)*(n+1)//2
This function calculates the number of ways to distribute n identical items into 3 distinct bins, where each bin can hold any non-negative number of items. This is a classic stars and bars problem.

The formula for distributing n identical items into k distinct bins is given by "stars and bars": C(n+k−1,k−1) or C(n+k−1,n).

In our case, k = 3 children. So, the formula becomes:
C(n+3−1,3−1)=C(n+2,2)= 
2!(n+2−2)!
(n+2)!
​
 = 
2
(n+2)(n+1)
​
 

If n < 0, it's impossible to distribute a negative number of candies, so it returns 0.
Otherwise, it returns (n+2)*(n+1)//2. The //2 ensures integer division.
This h3(n) function represents the "total number of ways to distribute n candies among 3 children without any upper limit on candies per child."

The Main Logic (Inclusion-Exclusion)
The full formula h3(n) - 3*h3(n-limit-1) + 3*h3(n-2*(limit+1)) - h3(n-3*(limit+1)) is an application of the Principle of Inclusion-Exclusion to handle the upper limit constraint.

Let:

x 
1
​
 ,x 
2
​
 ,x 
3
​
  be the number of candies for Child 1, Child 2, and Child 3, respectively.
We want to find the number of solutions to x 
1
​
 +x 
2
​
 +x 
3
​
 =n where 0≤x 
i
​
 ≤limit for each i.
Total Unrestricted Solutions (P 
0
​
 ):
First, find the total number of ways to distribute n candies among 3 children with no upper limit (only x 
i
​
 ≥0). This is h3(n).

Subtract Cases Where at Least One Child Exceeds Limit (P 
1
​
 ):
We need to subtract the cases where at least one child receives more than limit candies.
Let's say Child 1 violates the limit, meaning x 
1
​
 ≥limit+1.
To enforce this, we can give limit + 1 candies to Child 1 upfront.
Let x 
1
′
​
 =x 
1
​
 −(limit+1). Then x 
1
′
​
 ≥0.
The equation becomes (x 
1
′
​
 +limit+1)+x 
2
​
 +x 
3
​
 =n.
x 
1
′
​
 +x 
2
​
 +x 
3
​
 =n−(limit+1).
The number of solutions for this is h3(n - (limit + 1)).

Since any of the 3 children could be the one violating the limit, and these are distinct cases, we multiply by 3.
So, we subtract 3×h3(n−(limit+1)).

Add Back Cases Where at Least Two Children Exceed Limit (P 
2
​
 ):
When we subtracted the cases where one child exceeds the limit, we double-counted scenarios where two children exceed the limit. For example, if Child 1 and Child 2 both exceed the limit, this case was subtracted when considering Child 1 violating, and again when considering Child 2 violating. We need to add these back.

Suppose Child 1 and Child 2 both violate the limit:
x 
1
​
 ≥limit+1 and x 
2
​
 ≥limit+1.
Give limit + 1 candies to Child 1 and limit + 1 candies to Child 2 upfront.
Remaining candies to distribute: n−2×(limit+1).
The number of solutions for this is h3(n - 2 * (limit + 1)).

There are C(3,2)=3 ways to choose which two children violate the limit.
So, we add 3×h3(n−2×(limit+1)).

Subtract Cases Where All Three Children Exceed Limit (P 
3
​
 ):
Similar to the above, we've now over-corrected and added back scenarios where all three children exceed the limit too many times. We need to subtract these cases one last time.

Suppose Child 1, Child 2, and Child 3 all violate the limit:
x 
1
​
 ≥limit+1, x 
2
​
 ≥limit+1, x 
3
​
 ≥limit+1.
Give limit + 1 candies to each child upfront.
Remaining candies to distribute: n−3×(limit+1).
The number of solutions for this is h3(n - 3 * (limit + 1)).

There is C(3,3)=1 way to choose which three children violate the limit.
So, we subtract 1×h3(n−3×(limit+1)).

Putting it all together:

Total ways = (Total unrestricted ways)
- (Ways where at least 1 child violates)
+ (Ways where at least 2 children violate)
- (Ways where at least 3 children violate)

This translates directly to the given formula:
h3(n) - 3 * h3(n - (limit + 1)) + 3 * h3(n - 2 * (limit + 1)) - h3(n - 3 * (limit + 1))

Walkthrough of n = 5, limit = 2 with the formula:
limit + 1 = 3

h3(n) = h3(5)
h3(5) = (5+2)*(5+1)//2 = 7*6//2 = 42//2 = 21
(This is the total ways to distribute 5 candies among 3 children with no upper limit.)

3 * h3(n - (limit + 1)) = 3 * h3(5 - 3) = 3 * h3(2)
h3(2) = (2+2)*(2+1)//2 = 4*3//2 = 12//2 = 6
3 * 6 = 18

3 * h3(n - 2 * (limit + 1)) = 3 * h3(5 - 2*3) = 3 * h3(5 - 6) = 3 * h3(-1)
h3(-1) = 0 (due to the n<0 check)
3 * 0 = 0

h3(n - 3 * (limit + 1)) = h3(5 - 3*3) = h3(5 - 9) = h3(-4)
h3(-4) = 0
1 * 0 = 0

Total: 21−18+0−0=3.

This matches our manual walkthrough and the example output.


'''
