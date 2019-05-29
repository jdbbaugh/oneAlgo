
const array = [3,5,-4,8,11,1,-1,6]
const targetSum = 10

function twoNumbersSum(array, targetSum){
  const nums = {};
  for (const num of array){
    const potentialMatch = targetSum - num;
    if (potentialMatch in nums) {
      return [potentialMatch, num].sort((a, b) => a - b);
    } else {
      nums[num] = true;
    }
  }
  return [];
}

console.log(twoNumbersSum(array, targetSum))