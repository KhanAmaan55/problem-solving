def top_k_frequent(nums, k):
    frequency = {}
    for element in nums:
        if element not in frequency:
            frequency[element] = 0
        frequency[element] = frequency[element] + 1
    
    # freq_list = sorted(frequency, key=frequency.get)
    # return freq_list[-k:] 
    freq_list = sorted(frequency, key=frequency.get, reverse=True)
    return freq_list[:k]


nums = [1,1,1,1,2,2,3,3,3]
k = 2
print(top_k_frequent(nums, k))