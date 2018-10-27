function selectionSort(arr) {
  let j;
  for(let i = 0; i < arr.length; i++) {
    j = i + 1;
    let min = i;
    while(j < arr.length) {
      if(arr[j] < arr[min]) min = j;
      j++;
    }
    let temp = arr[min];
    arr[min] = arr[i];
    arr[i] = temp;
  }
  return arr;
}


array = [12, 3, 1, 66, 34, 2];
array1 = [3, 5, 10, 6, 23, 4];
array2 = [11, 3, 45, 6, 8, 5];
array3 = [11, -3, -45, 6, 8, 5];

console.log(selectionSort(array));
console.log(selectionSort(array1));
console.log(selectionSort(array2));
console.log(selectionSort(array3));
