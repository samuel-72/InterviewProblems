#! /usr/bin/env python3

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Intuition behind problem - Simple solution would be O(n^2), 2 for loops calculate all areas, return max area
        Could we do better? - If yes at what complexity?
        O(n) - Have 2 pointers, one at left and one at right end, based on whose height is lesser move the pointer away, 
        the intution is that moving the pointer pointing to lesser height will result in us able to find a container with more area 
        rather than moving the pointer pointing to greater height.
        Formal Proof - In Description
        """
        max_area = -1
        l,r = 0,len(height)-1
        while l < r:
            max_area = max(max_area, (r - l) * min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area


def main():
  s = Solution()
  assert s.maxArea([1,8,6,2,5,4,8,3,7]) == 49, "Max Area of container should be 49"

if __name__ == "__main__":
  main()
