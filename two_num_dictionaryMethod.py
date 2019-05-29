array = [3,5,-4,8,11,1,-1,6]
targetSum = 10
# print(target_sum)

def dosNumSum(array, targetSum):
  nums = {}
  for num in array:
    potential_num = targetSum - num
    if potential_num in nums:
      return sorted([potential_num, num])
    else:
      nums[num] = True
  return []


print(dosNumSum(array, targetSum))