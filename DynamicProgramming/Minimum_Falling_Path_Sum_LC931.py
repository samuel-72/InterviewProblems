from typing import List

class Solution:

    def __init__(self):
        self.A = None
        self.R = None
        self.C = None
        self.d = {}

    def find_min_path(self, row, col):
        if self.d.get((row,col),None) is not None:
            return self.d[(row,col)]
        if row >= self.R:
            return 0
        if col < 0 or col >= self.C:
            return float('inf')
        next_row_same_col = self.A[row][col] + self.find_min_path(row + 1, col)
        next_row_col_to_left = self.A[row][col] + self.find_min_path(row + 1, col - 1)
        next_row_col_to_right = self.A[row][col] + self.find_min_path(row + 1, col + 1)
        self.d[(row,col)]  = min(next_row_same_col, next_row_col_to_left, next_row_col_to_right)
        return self.d[(row,col)]

    def minFallingPathSum(self, A: List[List[int]]) -> int:
        self.A = A
        self.R, self.C = len(A), len(A[0])
        min_sum = float('inf')
        for col_no in range(self.C):
            sum_of_path = self.find_min_path(0, col_no)
            if sum_of_path < min_sum:
                min_sum = sum_of_path
        return min_sum
        

def test(A, expected_output):
    s = Solution() 
    assert s.minFallingPathSum(A) == expected_output


def main():
    A = [[-19,-1,-96,48,-94,36,16,55,-42,37,-59,6,-32,96,95,-58,13,-34,94,85],[17,44,36,-29,84,80,-34,50,-99,64,13,91,-27,25,-36,57,20,98,-100,-72],[-92,-75,86,90,-4,90,64,56,50,-63,10,-15,90,-66,-66,32,-69,-78,1,60],[21,51,-47,-43,-14,99,44,90,8,11,99,-62,57,59,69,50,-69,32,85,13],[-28,90,12,-18,23,61,-55,-97,6,89,36,26,26,-1,46,-50,79,-45,89,86],[-85,-10,49,-10,2,62,41,92,-67,85,86,27,89,-50,77,55,22,-82,-94,-98],[-50,53,-23,55,25,-22,76,-93,-7,66,-75,42,-35,-96,-5,4,-92,13,-31,-100],[-62,-78,8,-92,86,69,90,-37,81,97,53,-45,34,19,-19,-39,-88,-75,-74,-4],[29,53,-91,65,-92,11,49,26,90,-31,17,-84,12,63,-60,-48,40,-49,-48,88],[100,-69,80,11,-93,17,28,-94,52,64,-86,30,-9,-53,-8,-68,-33,31,-5,11],[9,64,-31,63,-84,-15,-30,-10,67,2,98,73,-77,-37,-96,47,-97,78,-62,-17],[-88,-38,-22,-90,54,42,-29,67,-85,-90,-29,81,52,35,13,61,-18,-94,61,-62],[-23,-29,-76,-30,-65,23,31,-98,-9,11,75,-1,-84,-90,73,58,72,-48,30,-81],[66,-33,91,-6,-94,82,25,-43,-93,-25,-69,10,-71,-65,85,28,-52,76,25,90],[-3,78,36,-92,-52,-44,-66,-53,-55,76,-7,76,-73,13,-98,86,-99,-22,61,100],[-97,65,2,-93,56,-78,22,56,35,-24,-95,-13,83,-34,-51,-73,2,7,-86,-19],[32,94,-14,-13,-6,-55,-21,29,-21,16,67,100,77,-26,-96,22,-5,-53,-92,-36],[60,93,-79,76,-91,43,-95,-16,74,-21,85,43,21,-68,-32,-18,18,100,-43,1],[87,-31,26,53,26,51,-61,92,-65,17,-41,27,-42,-14,37,-46,46,-31,-74,23],[-67,-14,-20,-85,42,36,56,9,11,-66,-59,-55,5,64,-29,77,47,44,-33,-77]]
    test(A, -1428)
    A = [[1,2,3],[4,5,6],[7,8,9]]
    test(A, 12)


if __name__ == "__main__":
    main()

    
    
"""
Intuition:

Consider this matrix:

[
    1       2       3
    4       5       6
    7       8       9
]

From eyeballing it, its fairly easy to see that the 1st column in each row is the smallest value in each row and as long as we pick that we should end up with the smallest sum.
But picking the smallest value from each row is not sufficient, because a row further down the lane might have another column which was not choosen in this path but would have had the minumum sum. Consider the below example:

[
    1       2       3
    4       5       6           # If you pick 4 here then in the next row you can only pick either 7 or 8 and thereby miss out the -100
    7       8       -100
]

This effectively means a couple of things:
1. One could parse through all possible paths and find all their sums and pick the least from it. Some paths would repeat, ergo lets add memoization to remember the answer for a path and reuse it.
2. For each row,
    For each col,
        Find the path with minimum sum encountered so far, 
   When you reach the last row, last col, find the minumum you have seen in the last row and that is your answer
   
Code:
For approach 1, the code is as given above.
For approach 2, this is a working solution:

    class Solution:
        def minFallingPathSum(self, A: List[List[int]]) -> int:
            r,c = len(A), len(A[0])
            min_paths = [ [A[R][C] if R == 0 else None for C in range(c)] for R in range(r)] #The very 1st row would have nothing above it hence we can copy it over directly.
            for row in range(1,r):
                for col in range(c):
                    min_paths[row][col] = min([ min_paths[row-1][new_col] for new_col in range(col-1, col+2) if row - 1 > -1 and new_col > -1 and new_col < c ]) + A[row][col]    
            return min(min_paths[r-1])
"""
