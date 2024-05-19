def twoNumberSum(array, targetSum):
    nums = {}
    for num in array:
        match = targetSum - num
        if match in nums:
            return [match, num]
        else:
            nums[num] = True
    return []