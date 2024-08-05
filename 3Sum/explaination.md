Let's walk through an example step-by-step to illustrate how this block of code works.

Consider the input array:

```
nums = [-1, 0, 1, 2, -1, -4]
```

First, we sort the array:

```
sorted nums = [-4, -1, -1, 0, 1, 2]
```

Now, let's see how the block of code works with this sorted array:

### Initial Setup:

- We initialize the result list: `result = []`.
- We start iterating with the outer loop, fixing one element at a time and using two pointers (`left` and `right`) to find the other two elements.

### Detailed Walkthrough:

#### 1. First Iteration (i = 0):

- `nums[i] = -4`
- Initialize `left` and `right` pointers:
  - `left = 1` (pointing to `-1`)
  - `right = 5` (pointing to `2`)

#### While Loop:

- Calculate the sum: `-4 + (-1) + 2 = -3` (which is less than 0)
- Increment `left`: `left = 2` (still pointing to `-1`)
- Calculate the sum: `-4 + (-1) + 2 = -3` (still less than 0)
- Increment `left`: `left = 3` (pointing to `0`)
- Calculate the sum: `-4 + 0 + 2 = -2` (still less than 0)
- Increment `left`: `left = 4` (pointing to `1`)
- Calculate the sum: `-4 + 1 + 2 = -1` (still less than 0)
- Increment `left`: `left = 5` (pointing to `2`)

Now, `left` is not less than `right`, so we exit the loop.

#### 2. Second Iteration (i = 1):

- `nums[i] = -1`
- Initialize `left` and `right` pointers:
  - `left = 2` (pointing to `-1`)
  - `right = 5` (pointing to `2`)

#### While Loop:

- Calculate the sum: `-1 + (-1) + 2 = 0` (which is equal to 0)
- Append triplet to the result: `result.append([-1, -1, 2])`

  - `result = [[-1, -1, 2]]`
- Skip duplicates:

  - `while left < right and nums[left] == nums[left + 1]`: This is false because `nums[2]` is `-1` and `nums[3]` is `0`.
  - `while left < right and nums[right] == nums[right - 1]`: This is false because `nums[5]` is `2` and `nums[4]` is `1`.
- Move pointers:

  - `left += 1` (now pointing to `0`)
  - `right -= 1` (now pointing to `1`)
- Calculate the sum: `-1 + 0 + 1 = 0` (which is equal to 0)
- Append triplet to the result: `result.append([-1, 0, 1])`

  - `result = [[-1, -1, 2], [-1, 0, 1]]`
- Skip duplicates:

  - `while left < right and nums[left] == nums[left + 1]`: This is false because `nums[3]` is `0` and `nums[4]` is `1`.
  - `while left < right and nums[right] == nums[right - 1]`: This is false because `nums[4]` is `1` and `nums[3]` is `0`.
- Move pointers:

  - `left += 1` (now pointing to `1`)
  - `right -= 1` (now pointing to `0`)

Now, `left` is not less than `right`, so we exit the loop.

#### 3. Third Iteration (i = 2):

- `nums[i] = -1`
- Skip this iteration since `nums[i]` is the same as `nums[i-1]`.

#### 4. Fourth Iteration (i = 3):

- `nums[i] = 0`
- Initialize `left` and `right` pointers:
  - `left = 4` (pointing to `1`)
  - `right = 5` (pointing to `2`)

#### While Loop:

- Calculate the sum: `0 + 1 + 2 = 3` (which is greater than 0)
- Decrement `right`: `right = 4` (pointing to `1`)

Now, `left` is not less than `right`, so we exit the loop.

### Final Result:

The final list of unique triplets is:

```
result = [[-1, -1, 2], [-1, 0, 1]]
```

### Key Points:

- **Appending the triplet**: When a valid triplet is found, it is appended to the result list.
- **Skipping duplicates**: After finding a valid triplet, the `while` loops skip any duplicate elements to avoid duplicate triplets in the result.
- **Moving pointers**: The `left` and `right` pointers are moved inward to continue searching for other potential triplets.

This approach ensures that the function efficiently finds all unique triplets that sum to zero while avoiding duplicates.
