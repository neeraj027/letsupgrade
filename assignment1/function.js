function findMax(numbers) {
    let max = numbers[0];
    for (let i = 1; i < numbers.length; i++) {
      if (numbers[i] > max) {
        max = numbers[i];
      }
    }
  
    return max;
  }
  
const numbers = [5, 10, 2, 8, 11, 54, 99, 105];
const maxNumber = findMax(numbers);
console.log(maxNumber);
