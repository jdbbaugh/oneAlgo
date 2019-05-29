
const array = [3,5,-4,8,11,1,-1,6]
const targetSum = 10

function twoNumbersSum(array, targetSum){
  let leftPointer = 0
  let rightPointer = array.length - 1
  console.log(rightPointer)
  array.sort((a,b) => a - b);
  console.log(array)
  let answerArray = []
  while (leftPointer < rightPointer){
    if (parseInt(array[leftPointer]) + parseInt(array[rightPointer]) == targetSum) {
      answerArray.push(array[leftPointer])
      answerArray.push(array[rightPointer])
      answerArray.sort((a,b) => a - b)
      console.log(answerArray)
      return answerArray
    } else if(array[leftPointer] + array[rightPointer] > targetSum){
      rightPointer--;
    } else {
      leftPointer++
    }
  }
  return answerArray
}

console.log(twoNumbersSum(array, targetSum))