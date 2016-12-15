def sum3(nums):
  # sum_list = nums[0]
  # for number in nums:
  #   sum_list += number
  # return sum_list - nums[0]

  return sum(nums) # <-- better alternative from online


sum3([1, 2, 3]) → 6
sum3([5, 11, 2]) → 18
sum3([7, 0, 0]) → 7