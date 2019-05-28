array = [3,5,-4,8,11,1,-1,6]
target_sum = 10
# print(target_sum)


def two_number_sum(array_nums, target):
  # print(len(array_nums) -1, target)

  array_count = len(array_nums)
  i = 0

  finalArray = []
  while i < array_count:
    # print(i)
    for num in array_nums:
      if num != array_nums[i]:
        test_for_target = num + array_nums[i]
        if test_for_target == target:
          print(f'{num} and {array_nums[i]} equal target number {target} ')
          newArray = [num,array_nums[i]]
          finalArray.append(newArray)
    i = i + 1

  return finalArray

for item in two_number_sum(array,target_sum):
  print(item)




