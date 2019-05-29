array = [3,5,-4,8,11,1,-1,6]
target_sum = 10
# print(target_sum)

def dosNumSum(array, target_sum):
  pointer_left = 0
  pointer_right = len(array) - 1
  # print(pointer_right, pointer_left)
  answer_array = []
  array.sort()
  # print(array)
  while pointer_left < pointer_right:
    # print(pointer_left)
    if array[pointer_left] + array[pointer_right] == target_sum:
      answer_array = [array[pointer_left], array[pointer_right]]
      return answer_array
    else:
      pointer_left = pointer_left + 1


# def two_number_sum(array_nums, target):
#   # print(len(array_nums) -1, target)

#   array_count = len(array_nums)
#   i = 0

#   finalArray = []
#   while i < array_count:
#     # print(i)
#     for num in array_nums:
#       if num != array_nums[i]:
#         test_for_target = num + array_nums[i]
#         if test_for_target == target:
#           print(f'{num} and {array_nums[i]} equal target number {target} ')
#           newArray = [num,array_nums[i]]
#           newArray.sort()
#           finalArray.append(newArray)
#     i = i + 1

#   return finalArray

# for item in two_number_sum(array,target_sum):
#   print(item)

print(dosNumSum(array, target_sum))





