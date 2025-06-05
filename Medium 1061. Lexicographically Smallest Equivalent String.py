

"""

You are given two strings of the same length s1 and s2 and a string baseStr.

We say s1[i] and s2[i] are equivalent characters.

For example, if s1 = "abc" and s2 = "cde", then we have 'a' == 'c', 'b' == 'd', and 'c' == 'e'.
Equivalent characters follow the usual rules of any equivalence relation:

Reflexivity: 'a' == 'a'.
Symmetry: 'a' == 'b' implies 'b' == 'a'.
Transitivity: 'a' == 'b' and 'b' == 'c' implies 'a' == 'c'.
For example, given the equivalency information from s1 = "abc" and s2 = "cde", "acd" and "aab" are equivalent strings of baseStr = "eed", and "aab" is the lexicographically smallest equivalent string of baseStr.

Return the lexicographically smallest equivalent string of baseStr by using the equivalency information from s1 and s2.

 

Example 1:

Input: s1 = "parker", s2 = "morris", baseStr = "parser"
Output: "makkek"
Explanation: Based on the equivalency information in s1 and s2, we can group their characters as [m,p], [a,o], [k,r,s], [e,i].
The characters in each group are equivalent and sorted in lexicographical order.
So the answer is "makkek".
Example 2:

Input: s1 = "hello", s2 = "world", baseStr = "hold"
Output: "hdld"
Explanation: Based on the equivalency information in s1 and s2, we can group their characters as [h,w], [d,e,o], [l,r].
So only the second letter 'o' in baseStr is changed to 'd', the answer is "hdld".
Example 3:

Input: s1 = "leetcode", s2 = "programs", baseStr = "sourcecode"
Output: "aauaaaaada"
Explanation: We group the equivalent characters in s1 and s2 as [a,o,e,r,s,c], [l,p], [g,t] and [d,m], thus all letters in baseStr except 'u' and 'd' are transformed to 'a', the answer is "aauaaaaada".
 

Constraints:

1 <= s1.length, s2.length, baseStr <= 1000
s1.length == s2.length
s1, s2, and baseStr consist of lowercase English letters.
"""
from collections import defaultdict

class Solution(object):
    def smallestEquivalentString(self, s1, s2, baseStr):
        adj = defaultdict(list)

        # Build graph: connect equivalent characters
        for char1, char2 in zip(s1, s2):
            adj[char1].append(char2)
            adj[char2].append(char1)

        def dfs(start_char, visited_chars):
            visited_chars.add(start_char)
            min_char_in_component = start_char

            # Explore neighbors, find the smallest character in this connected component
            for neighbor in adj[start_char]:
                if neighbor not in visited_chars:
                    min_char_in_component = min(min_char_in_component, dfs(neighbor, visited_chars))
            
            return min_char_in_component

        result_chars = []
        # For each character in baseStr, find and append its smallest equivalent
        for char_in_base in baseStr:
            # A fresh `visited` set is crucial for each DFS to explore its component fully
            visited = set()
            result_chars.append(dfs(char_in_base, visited))
        
        return ''.join(result_chars)

'''
Problem Description: Explain what the problem asks us to do, including the concept of equivalent characters and lexicographical ordering.
Equivalence Relation: Elaborate on the properties of an equivalence relation (reflexivity, symmetry, transitivity) and how they apply here.
Core Idea of the Solution: Explain the main approach used in the provided code, which is to leverage a graph (or Disjoint Set Union - DSU) to find connected components of equivalent characters and then use the smallest character in each component.
Code Explanation: Go through the Python code line by line, explaining the purpose of each part:
defaultdict(list) for the adjacency list.
Building the graph from s1 and s2.
The dfs function: its parameters, purpose (finding the smallest character in a connected component), and how it uses visited to avoid cycles.
Iterating through baseStr and calling dfs.
Constructing the result string.
Example Walkthrough: Choose one of the provided examples (e.g., Example 1: s1 = "parker", s2 = "morris", baseStr = "parser") and trace the execution of the code step-by-step to show how the output is derived.
Problem Description
The problem "Lexicographically Smallest Equivalent String" asks us to transform a given baseStr into its lexicographically smallest equivalent string based on character equivalencies derived from two other strings, s1 and s2.

We are given s1 and s2 of the same length. For each index i, the characters s1[i] and s2[i] are declared equivalent. This equivalency relationship has three key properties, forming an equivalence relation:

Reflexivity: Any character is equivalent to itself (e.g., 'a' == 'a').
Symmetry: If 'a' is equivalent to 'b', then 'b' is equivalent to 'a' (e.g., if 'a' == 'b', then 'b' == 'a').
Transitivity: If 'a' is equivalent to 'b', and 'b' is equivalent to 'c', then 'a' is also equivalent to 'c' (e.g., if 'a' == 'b' and 'b' == 'c', then 'a' == 'c').
These properties imply that equivalent characters form groups or connected components. Within each such group, any character can be considered equivalent to any other character in that same group.

Our goal is to take each character in baseStr and replace it with the lexicographically smallest character from its equivalence group. For example, if 'a', 'c', and 'e' are equivalent, and 'a' is the smallest among them, then any 'c' or 'e' in baseStr would be replaced by 'a'. The final string after all such replacements must be the lexicographically smallest possible.

Core Idea of the Solution
The problem can be modeled as finding connected components in a graph.
Each lowercase English letter ('a' through 'z') can be thought of as a node in a graph. An edge exists between two characters if they are declared equivalent by s1 and s2 (e.g., s1[i] and s2[i]). Due to transitivity, if 'a' is connected to 'b', and 'b' is connected to 'c', then 'a', 'b', and 'c' all belong to the same equivalence group.

The strategy is as follows:

Build a Graph: Represent the equivalencies as an undirected graph using an adjacency list. For every pair (s1[i], s2[i]), add an edge between s1[i] and s2[i].
Find Smallest in Component: For each character ch in baseStr, perform a traversal (Depth-First Search - DFS or Breadth-First Search - BFS) starting from ch to find all characters reachable from ch. This set of reachable characters forms an equivalence group. From this group, identify the lexicographically smallest character.
Replace and Construct: Replace ch in baseStr with this smallest character found. Repeat for all characters in baseStr to construct the final result string.
A more optimized approach, often used for equivalence relations, is Disjoint Set Union (DSU). However, the provided solution uses DFS, which is also a valid way to find connected components and works effectively given the small alphabet size (26 characters).

Code Explanation
Let's break down the provided Python code:

Python

from collections import defaultdict

class Solution(object):
    def smallestEquivalentString(self, s1, s2, baseStr):
        """
        :type s1: str
        :type s2: str
        :type baseStr: str
        :rtype: str
        """
        adj = defaultdict(list)

        # Step 1: Build the graph
        # Iterate through s1 and s2 simultaneously.
        # For each pair (a, b) at the same index, they are equivalent.
        # Add an undirected edge between 'a' and 'b' in the adjacency list.
        for a, b in zip(s1, s2):
            adj[a].append(b)
            adj[b].append(a)

        # This dictionary will store the lexicographically smallest character
        # for each character encountered, effectively caching results for components.
        # However, the current DFS implementation recalculates, so this cache isn't explicitly used
        # in the return logic, but rather `dfs` returns the min for the current component.
        # For a truly optimized version, one might populate a `mapping` here.
        # But as is, `dfs` does the work.

        def dfs(ch, visited):
            # Mark the current character as visited to avoid infinite loops in cyclic graphs.
            visited.add(ch)
            # Initialize the smallest character found so far in this component with the current character itself.
            min_ch = ch
            
            # Explore all neighbors of the current character.
            for nei in adj[ch]:
                # If a neighbor has not been visited yet, explore it.
                if nei not in visited:
                    # Recursively call DFS on the neighbor.
                    # The recursive call will return the smallest character found in the component
                    # reachable from 'nei' (which is the same component as 'ch').
                    candidate = dfs(nei, visited)
                    # Update min_ch if the candidate from the neighbor's exploration is smaller.
                    min_ch = min(min_ch, candidate)
            # After visiting all reachable characters in the component, return the overall smallest character found.
            return min_ch

        result = []
        # Step 3: Transform baseStr
        # Iterate through each character in the base string.
        for ch in baseStr:
            # For each character, start a fresh DFS traversal to find its equivalent component.
            # A new `visited` set is crucial for each character in `baseStr` because
            # we want to find the smallest for *its specific component* starting from *itself*,
            # not globally across all components traversed previously.
            # If we reused `visited`, after processing 'p' for example, 'k' might
            # already be in `visited` if 'p' and 'k' are in the same component,
            # and `dfs('k', visited)` would return immediately without exploring.
            # While this might work if `dfs` *caches* the component's min value,
            # the current `dfs` implementation recomputes it each time.
            visited = set()
            # Call DFS to find the lexicographically smallest character in the component
            # that `ch` belongs to.
            result.append(dfs(ch, visited))
        
        # Join the list of characters to form the final result string.
        return ''.join(result)

Example Walkthrough: s1 = "parker", s2 = "morris", baseStr = "parser"
Input:
s1 = "parker"
s2 = "morris"
baseStr = "parser"

Step 1: Build the Graph (Adjacency List adj)

We iterate through s1 and s2 simultaneously:

s1[0]='p', s2[0]='m': Add edges p <-> m adj = {'p': ['m'], 'm': ['p']}
s1[1]='a', s2[1]='o': Add edges a <-> o adj = {'p': ['m'], 'm': ['p'], 'a': ['o'], 'o': ['a']}
s1[2]='r', s2[2]='r': Add edges r <-> r (self-loop, doesn't change connectivity) adj = {'p': ['m'], 'm': ['p'], 'a': ['o'], 'o': ['a'], 'r': ['r']}
s1[3]='k', s2[3]='r': Add edges k <-> r adj = {'p': ['m'], 'm': ['p'], 'a': ['o'], 'o': ['a'], 'r': ['r', 'k'], 'k': ['r']}
s1[4]='e', s2[4]='i': Add edges e <-> i adj = {'p': ['m'], 'm': ['p'], 'a': ['o'], 'o': ['a'], 'r': ['r', 'k'], 'k': ['r'], 'e': ['i'], 'i': ['e']}
s1[5]='r', s2[5]='s': Add edges r <-> s adj = {'p': ['m'], 'm': ['p'], 'a': ['o'], 'o': ['a'], 'r': ['r', 'k', 's'], 'k': ['r'], 'e': ['i'], 'i': ['e'], 's': ['r']}
Final adj (cleaned up, order doesn't matter for neighbors):

adj = {
    'p': ['m'],
    'm': ['p'],
    'a': ['o'],
    'o': ['a'],
    'r': ['k', 's'],  # 'r' to 'r' is redundant, but harmless
    'k': ['r'],
    'e': ['i'],
    'i': ['e'],
    's': ['r']
}
Equivalence Groups (Mental View based on adj):

[m, p] (smallest: 'm')
[a, o] (smallest: 'a')
[k, r, s] (smallest: 'k')
[e, i] (smallest: 'e')
Step 2 & 3: Iterate through baseStr and transform

baseStr = "parser"
result = []

ch = 'p'

visited = set()
Call dfs('p', visited):
visited = {'p'}. min_ch = 'p'.
Neighbors of 'p': ['m'].
'm' not in visited. Call dfs('m', {'p'}):
visited = {'p', 'm'}. min_ch = 'm'.
Neighbors of 'm': ['p'].
'p' is in visited. Skip.
Return 'm'.
candidate = 'm'. min_ch = min('p', 'm') = 'm'.
Return 'm'.
result.append('m') -> result = ['m']
ch = 'a'

visited = set()
Call dfs('a', visited):
visited = {'a'}. min_ch = 'a'.
Neighbors of 'a': ['o'].
'o' not in visited. Call dfs('o', {'a'}):
visited = {'a', 'o'}. min_ch = 'o'.
Neighbors of 'o': ['a'].
'a' is in visited. Skip.
Return 'o'.
candidate = 'o'. min_ch = min('a', 'o') = 'a'.
Return 'a'.
result.append('a') -> result = ['m', 'a']
ch = 'r'

visited = set()
Call dfs('r', visited):
visited = {'r'}. min_ch = 'r'.
Neighbors of 'r': ['k', 's'].
Process 'k':
'k' not in visited. Call dfs('k', {'r'}):
visited = {'r', 'k'}. min_ch = 'k'.
Neighbors of 'k': ['r'].
'r' is in visited. Skip.
Return 'k'.
candidate = 'k'. min_ch = min('r', 'k') = 'k'.
Process 's':
's' not in visited. Call dfs('s', {'r', 'k'}):
visited = {'r', 'k', 's'}. min_ch = 's'.
Neighbors of 's': ['r'].
'r' is in visited. Skip.
Return 's'.
candidate = 's'. min_ch = min('k', 's') = 'k'. (since 'k' is smaller than 's')
Return 'k'.
result.append('k') -> result = ['m', 'a', 'k']
ch = 's'

visited = set()
Call dfs('s', visited):
visited = {'s'}. min_ch = 's'.
Neighbors of 's': ['r'].
'r' not in visited. Call dfs('r', {'s'}):
visited = {'s', 'r'}. min_ch = 'r'.
Neighbors of 'r': ['k', 's'].
Process 'k':
'k' not in visited. Call dfs('k', {'s', 'r'}):
visited = {'s', 'r', 'k'}. min_ch = 'k'.
Neighbors of 'k': ['r'].
'r' is in visited. Skip.
Return 'k'.
candidate = 'k'. min_ch = min('r', 'k') = 'k'.
Process 's':
's' is in visited. Skip.
Return 'k'.
candidate = 'k'. min_ch = min('s', 'k') = 'k'.
Return 'k'.
result.append('k') -> result = ['m', 'a', 'k', 'k']
ch = 'e'

visited = set()
Call dfs('e', visited):
visited = {'e'}. min_ch = 'e'.
Neighbors of 'e': ['i'].
'i' not in visited. Call dfs('i', {'e'}):
visited = {'e', 'i'}. min_ch = 'i'.
Neighbors of 'i': ['e'].
'e' is in visited. Skip.
Return 'i'.
candidate = 'i'. min_ch = min('e', 'i') = 'e'.
Return 'e'.
result.append('e') -> result = ['m', 'a', 'k', 'k', 'e']
ch = 'r'

visited = set()
Call dfs('r', visited): (This will repeat the process for 'r' as in step 3, and will again return 'k')
... (details skipped for brevity, similar to step 3) ...
Returns 'k'.
result.append('k') -> result = ['m', 'a', 'k', 'k', 'e', 'k']
Final Result: "".join(result) = "makkek"

This walkthrough demonstrates how the graph is built, how DFS is used to find all equivalent characters for a given starting character, and how the lexicographically smallest among them is selected to form the output string. 
The crucial part is re-initializing visited for each character in baseStr to ensure a fresh exploration of its equivalence component.
'''
