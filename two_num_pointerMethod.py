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
    elif array[pointer_left] + array[pointer_right] > target_sum:
      pointer_right = pointer_right - 1
    else:
      pointer_left = pointer_left + 1
  return answer_array

print(dosNumSum(array, target_sum))





