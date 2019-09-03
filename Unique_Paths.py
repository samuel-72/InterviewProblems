class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        r,c = len(obstacleGrid) - 1, len(obstacleGrid[0]) - 1
        if obstacleGrid[0][0] == 1 or obstacleGrid[r][c] == 1:
            return 0
        if r < 1 and c < 1:
            return 1
        mem = {}
        def find_unique_paths(cur_r, cur_c):
            if cur_r == r and cur_c == c:
                return 1
            if cur_r > r or cur_c > c or obstacleGrid[cur_r][cur_c] == 1:
                return 0
            if (cur_r, cur_c) in mem:
                return mem[(cur_r, cur_c)]
            mem[(cur_r, cur_c)] = find_unique_paths(cur_r, cur_c + 1) + find_unique_paths(cur_r + 1, cur_c)
            return mem[(cur_r, cur_c)]
        find_unique_paths(0,0)
        return mem[(0,0)]


def main():
  s = Solution()
  grid = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
  ]
  assert s.uniquePathsWithObstacles(grid) == 2, "The correct answer is 2"

if __name__ == "__main__":
  main()
