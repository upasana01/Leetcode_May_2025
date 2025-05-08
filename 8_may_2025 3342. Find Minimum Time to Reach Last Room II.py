'''
3342. Find Minimum Time to Reach Last Room II
Solved
Medium
Topics
Companies
Hint
There is a dungeon with n x m rooms arranged as a grid.

You are given a 2D array moveTime of size n x m, where moveTime[i][j] represents the minimum time in seconds when you can start moving to that room. You start from the room (0, 0) at time t = 0 and can move to an adjacent room. Moving between adjacent rooms takes one second for one move and two seconds for the next, alternating between the two.

Return the minimum time to reach the room (n - 1, m - 1).

Two rooms are adjacent if they share a common wall, either horizontally or vertically.

 

Example 1:

Input: moveTime = [[0,4],[4,4]]

Output: 7

Explanation:

The minimum time required is 7 seconds.

At time t == 4, move from room (0, 0) to room (1, 0) in one second.
At time t == 5, move from room (1, 0) to room (1, 1) in two seconds.
Example 2:

Input: moveTime = [[0,0,0,0],[0,0,0,0]]

Output: 6

Explanation:

The minimum time required is 6 seconds.

At time t == 0, move from room (0, 0) to room (1, 0) in one second.
At time t == 1, move from room (1, 0) to room (1, 1) in two seconds.
At time t == 3, move from room (1, 1) to room (1, 2) in one second.
At time t == 4, move from room (1, 2) to room (1, 3) in two seconds.
Example 3:

Input: moveTime = [[0,1],[1,2]]

Output: 4

 

Constraints:

2 <= n == moveTime.length <= 750
2 <= m == moveTime[i].length <= 750
0 <= moveTime[i][j] <= 109
'''
import heapq

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n = len(moveTime)
        m = len(moveTime[0])
        # dist[r][c][k] stores the minimum time to reach cell (r, c)
        # where k=0 means the last move took 2 seconds, and k=1 means the last move took 1 second.
        dist = [[[float('inf')] * 2 for _ in range(m)] for _ in range(n)]
        # Initialize the starting cell (0, 0) with time 0.
        # We can consider the initial state as having made a "virtual" move of 2 seconds
        # so the first actual move will be 1 second.
        dist[0][0][0] = 0
        # Priority queue to store (time, row, col, last_move_cost).
        # last_move_cost: 0 for 2 seconds, 1 for 1 second.
        pq = [(0, 0, 0, 0)]

        while pq:
            # Get the state with the minimum time from the priority queue.
            current_time, r, c, last_move_cost = heapq.heappop(pq)

            # If the current time is greater than the already found minimum time to reach this state, skip it.
            if current_time > dist[r][c][last_move_cost]:
                continue

            # Define the possible moves (up, down, left, right).
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            # Iterate through each possible next move.
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                # Check if the next cell is within the grid boundaries.
                if 0 <= nr < n and 0 <= nc < m:
                    # Determine the cost of the next move. It alternates between 1 and 2.
                    next_move_cost = 2 if last_move_cost == 1 else 1

                    # The earliest time we can start moving to the next room is moveTime[nr][nc].
                    # We arrive at the next room at max(moveTime[nr][nc], current_time) + next_move_cost.
                    arrival_time = max(moveTime[nr][nc], current_time) + next_move_cost

                    # Determine the last move cost for the next state.
                    next_last_move_cost = 1 if next_move_cost == 1 else 0

                    # If the calculated arrival time is less than the current minimum time to reach the next cell
                    # with the corresponding last move cost, update the distance and add it to the priority queue.
                    if arrival_time < dist[nr][nc][next_last_move_cost]:
                        dist[nr][nc][next_last_move_cost] = arrival_time
                        heapq.heappush(pq, (arrival_time, nr, nc, next_last_move_cost))

        # The minimum time to reach the last room (n-1, m-1) will be the minimum of the times
        # when the last move was 1 second or 2 seconds.
        return min(dist[n - 1][m - 1][0], dist[n - 1][m - 1][1])

'''

import heapq: Imports the heapq module, which provides an implementation of the heap queue algorithm (also known as the priority queue algorithm). 1  This is used for Dijkstra's algorithm to efficiently retrieve the state with the smallest time.   

class Solution:: Defines a class named Solution where the minTimeToReach method will be implemented.

def minTimeToReach(self, moveTime: List[List[int]]) -> int:: Defines the method minTimeToReach that takes a 2D list moveTime as input and is expected to return an integer representing the minimum time to reach the last room.

n = len(moveTime): Gets the number of rows in the moveTime grid.

m = len(moveTime[0]): Gets the number of columns in the moveTime grid.

dist = [[[float('inf')] * 2 for _ in range(m)] for _ in range(n)]: Initializes a 3D list dist to store the minimum time to reach each cell. dist[r][c][k] represents the minimum time to reach cell (r, c) where k indicates the cost of the last move (0 for 2 seconds, 1 for 1 second). It's initialized with infinity for all cells except the starting cell.

dist[0][0][0] = 0: Sets the minimum time to reach the starting cell (0, 0) with a "virtual" last move cost of 2 seconds (so the first move will be 1 second) to 0.

pq = [(0, 0, 0, 0)]: Initializes a priority queue pq with the starting state: (time=0, row=0, col=0, last_move_cost=0).

while pq:: Starts the main loop of Dijkstra's algorithm, which continues as long as there are states in the priority queue to explore.

current_time, r, c, last_move_cost = heapq.heappop(pq): Pops the state with the smallest current_time from the priority queue. This gives us the state we should explore next.

if current_time > dist[r][c][last_move_cost]:: Checks if the current time to reach the cell (r, c) with the given last_move_cost is greater than the already recorded minimum time. If it is, it means we have found a shorter path to this state before, so we can skip this state.

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]: Defines a list of possible moves to adjacent cells (right, left, down, up).

for dr, dc in directions:: Iterates through each possible direction to move from the current cell.

nr, nc = r + dr, c + dc: Calculates the coordinates of the next cell.

if 0 <= nr < n and 0 <= nc < m:: Checks if the next cell's coordinates are within the bounds of the grid.

next_move_cost = 2 if last_move_cost == 1 else 1: Determines the cost of the next move. If the last_move_cost was 1 second, the next_move_cost will be 2 seconds, and vice versa.

arrival_time = max(moveTime[nr][nc], current_time) + next_move_cost: Calculates the time of arrival at the next cell (nr, nc). We can only start moving to this cell at or after moveTime[nr][nc]. So, the start time of the move is max(moveTime[nr][nc], current_time), and adding next_move_cost gives the arrival time.

next_last_move_cost = 1 if next_move_cost == 1 else 0: Determines the last_move_cost for the next state, which will be the opposite of the next_move_cost in terms of its representation (1 for 1 second, 0 for 2 seconds).

if arrival_time < dist[nr][nc][next_last_move_cost]:: Checks if the calculated arrival_time is less than the current minimum time recorded to reach the next cell (nr, nc) with the corresponding next_last_move_cost.

dist[nr][nc][next_last_move_cost] = arrival_time: If a shorter time is found, update the minimum time to reach the next cell.

heapq.heappush(pq, (arrival_time, nr, nc, next_last_move_cost)): Add the new state (arrival time, next row, next column, next last move cost) to the priority queue for further exploration.

return min(dist[n - 1][m - 1][0], dist[n - 1][m - 1][1]): After the Dijkstra's algorithm finishes, the minimum time to reach the last room (n - 1, m - 1) will be the minimum of the times recorded when the last move to that room was 2 seconds (dist[n - 1][m - 1][0]) or 1 second (dist[n - 1][m - 1][1]).

Example Walkthrough:

Let's use moveTime = [[0, 4], [4, 4]].

Initialization:

n = 2, m = 2
dist = [[[inf, inf], [inf, inf]], [[inf, inf], [inf, inf]]]
dist[0][0][0] = 0
pq = [(0, 0, 0, 0)]
Iteration 1:

Pop (0, 0, 0, 0) from pq. current_time = 0, r = 0, c = 0, last_move_cost = 0.
Move to (0, 1):
nr = 0, nc = 1
next_move_cost = 1 (since last_move_cost was 0)
arrival_time = max(moveTime[0][1], 0) + 1 = max(4, 0) + 1 = 5
next_last_move_cost = 1
arrival_time (5) < dist[0][1][1] (inf), so dist[0][1][1] = 5, pq.append((5, 0, 1, 1)) -> pq = [(5, 0, 1, 1)]
Move to (1, 0):
nr = 1, nc = 0
next_move_cost = 1
arrival_time = max(moveTime[1][0], 0) + 1 = max(4, 0) + 1 = 5
next_last_move_cost = 1
arrival_time (5) < dist[1][0][1] (inf), so dist[1][0][1] = 5, pq.append((5, 1, 0, 1)) -> pq = [(5, 0, 1, 1), (5, 1, 0, 1)]
Iteration 2:

Pop (5, 0, 1, 1) from pq. current_time = 5, r = 0, c = 1, last_move_cost = 1.
Move to (0, 0):
nr = 0, nc = 0
next_move_cost = 2
arrival_time = max(moveTime[0][0], 5) + 2 = max(0, 5) + 2 = 7
next_last_move_cost = 0
arrival_time (7) > dist[0][0][0] (0), so no update.
Move to (1, 1):
nr = 1, nc = 1
next_move_cost = 2
arrival_time = max(moveTime[1][1], 5) + 2 = max(4, 5) + 2 = 7
next_last_move_cost = 0
arrival_time (7) < dist[1][1][0] (inf), so dist[1][1][0] = 7, pq.append((7, 1, 1, 0)) -> pq = [(5, 1, 0, 1), (7, 1, 1, 0)]
Iteration 3:

Pop (5, 1, 0, 1) from pq. current_time = 5, r = 1, c = 0, last_move_cost = 1.
Move to (0, 0):
nr = 0, nc = 0
next_move_cost = 2
arrival_time = max(moveTime[0][0], 5) + 2 = max(0, 5) + 2 = 7
next_last_move_cost = 0
arrival_time (7) > dist[0][0][0] (0), so no update.
Move to (1, 1):
nr = 1, nc = 1
next_move_cost = 2
arrival_time = max(moveTime[1][1], 5) + 2 = max(4, 5) + 2 = 7
next_last_move_cost = 0
arrival_time (7) < dist[1][1][0] (7) is false, so no update.
Iteration 4:

Pop (7, 1, 1, 0) from pq. current_time = 7, r = 1, c = 1, last_move_cost = 0.
No further moves from the destination are necessary.
Finally, return min(dist[1][1][0], dist[1][1][1]) = min(7, inf) = 7.

The algorithm correctly finds the minimum time to reach the last room.
'''
