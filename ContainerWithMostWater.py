"""
Problem: Container With Most Water

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `i-th` line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

 Example:
1. Input: `height = [1,8,6,2,5,4,8,3,7]`
   Output: `49`
   Explanation: The vertical lines are represented by the array `[1,8,6,2,5,4,8,3,7]`. In this case, the maximum area of water (49 units) can be obtained by the lines at indices 1 and 8 (0-based index).

2. Input: `height = [1,1]`
   Output: `1`

 Constraints:
- `n == height.length`
- `2 <= n <= 10^5`
- `0 <= height[i] <= 10^4`

Function Signature:

def max_area(height: List[int]) -> int:
    # Your implementation here

Task:
Implement the `max_area` function and provide your solution. Once you're done, send your code, and I'll review it for you.

"""


# First solution

"""
def max_area(height):
    max_area = 0
    for i in range(len(height) - 1):
        for j in range(i+1, len(height)):
            h_cont = min(height[i],height[j])
            w_cont = j - i
            area = h_cont * w_cont
            if area > max_area:
                max_area = area
    
    return max_area
"""

# second solution

def max_area(height):
    max_area = 0
    left = 0
    right = len(height)-1
    while left < right:
        area = min(height[left], height[right]) * (right - left)
        max_area = max(max_area, area)
        if height[left] < height[right]:
            left +=1
        else:
            right-=1
    
    return max_area


# height = [1,2,6,2,8,4,8,3,7]
height = [1,8,6,2,5,4,8,3,7]
print(max_area(height))