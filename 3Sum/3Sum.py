"""
Great! Let's move on to another coding problem. Here's a medium-level question that will test your problem-solving and algorithmic skills:

### Problem: 3Sum

Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set must not contain duplicate triplets.
--------------------------------

Example:
1. Input: `nums = [-1,0,1,2,-1,-4]`
   Output: `[[-1,-1,2],[-1,0,1]]`
   
2. Input: `nums = []`
   Output: `[]`
   
3. Input: `nums = [0]`
   Output: `[]`
--------------------------------

Constraints:
- `0 <= nums.length <= 3000`
- `-10^5 <= nums[i] <= 10^5`
--------------------------------

Function Signature:
```python
def three_sum(nums: List[int]) -> List[List[int]]:
    # Your implementation here
```

 Task:
Implement the `three_sum` function and provide your solution. Once you're done, send your code, and I'll review it for you.
"""

# My Solution
"""
def three_sum(nums):
    solution = set()
    d = {}
    for i , num in enumerate(nums):
        d[num] = i

    for i in range (len(nums)):
        for j in range (i+1 , len(nums)):
            check_element = - (nums[i] + nums[j])
            if check_element in d and d[check_element] != i and d[check_element] != j:
                three_sum_array = sorted([check_element, nums[i], nums[j]])
                three_sum_array = tuple(three_sum_array)
                solution.add(three_sum_array)
    return list(solution)

"""

# Optimmized solution
def three_sum(nums):
    nums.sort()
    result = []
    
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
    
    return result

nums = [-1,0,1,2,-1,-4]
print(three_sum(nums))