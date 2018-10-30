O(n) | O(1)

function findThreeLargestNumbers(array) {
  // Write your code here.
	let arr = [null, null, null];
	for(let num of array) {
		updateLargest(num, arr);
	}
	return arr;
}

function updateLargest(num, arr) {
	if(num > arr[2] || !arr[2]) {
		return shiftAndUpdate(num, arr, 2);
	} else if(num > arr[1] || !arr[1]) {
		return shiftAndUpdate(num, arr, 1);
	} else if(num > arr[0] || !arr[0]) {
		return shiftAndUpdate(num, arr, 0);
	}
}

function shiftAndUpdate(num, arr, idx) {
	for(let i = 0; i <= idx; i++) {
		if(i == idx) {
			arr[idx] = num;
		} else {
			arr[i] = arr[i+1];
		}
	}
	return arr;
}
