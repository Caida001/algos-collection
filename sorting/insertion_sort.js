function insertionSort(arr) {
  let j;
  for(let i = 1; i < arr.length; i++){
    j = i;
    while(j > 0 && arr[j] < arr[j-1]){
      let temp = arr[j];
      arr[j] = arr[j-1];
      arr[j-1] = temp;
      j--;
    }
  }
  return arr;
}


array = [12, 3, 1, 66, 34, 2];
array1 = [3, 5, 10, 6, 23, 4];
array2 = [11, 3, 45, 6, 8, 5];
array3 = [11, -3, -45, 6, 8, 5];

console.log(insertionSort(array));
console.log(insertionSort(array1));
console.log(insertionSort(array2));
console.log(insertionSort(array3));
