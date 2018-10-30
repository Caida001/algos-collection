write a function that takes in an array of distinct integers as well as an
integer k and returns the kth smallest number in that array in linear time on
average. The array is not sorted.


O(n) | O(1)

function quickselect(array, k) {
  // Write your code here.
	let pos = k - 1;
	return helper(array, 0, array.length-1, pos);
}

function helper(array, startIdx, endIdx, pos) {
	while(true) {
		let pivot = startIdx;
		let leftIdx = startIdx + 1;
		let rightIdx = endIdx;

		while(leftIdx <= rightIdx) {
			if(array[leftIdx] > array[pivot] && array[rightIdx] < array[pivot]) {
				swap(leftIdx, rightIdx, array);
			}

			if(array[leftIdx] <= array[pivot]) leftIdx++;
			if(array[rightIdx] >= array[pivot]) rightIdx--;
		}
		swap(pivot, rightIdx, array);
		if(rightIdx == pos) {
			return array[pos];
		} else if(rightIdx < pos){
			startIdx = rightIdx + 1;
		} else {
			endIdx = leftIdx - 1;
		}
	}
}


function swap(i, j, array) {
	let temp = array[i];
	array[i] = array[j];
	array[j] = temp;
}
