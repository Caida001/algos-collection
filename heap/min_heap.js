class MinHeap {
  constructor(array) {
    this.heap = this.buildHeap(array);
  }

  buildHeap(array) {
    // Write your code here.
		let parentIdx = Math.floor((array.length-2)/2);
		for(let currentIdx = parentIdx; currentIdx >= 0; currentIdx--) {
			this.siftDown(currentIdx, array.length-1, array);
		}
		return array;
  }

  siftDown(currentIdx, endIdx, heap) {
    // Write your code here.
		let childIdx1 = currentIdx * 2 + 1;
		let childIdx2 = currentIdx * 2 + 2;
		while(childIdx1 <= endIdx || childIdx2 <= endIdx) {
			if(heap[childIdx2] < heap[childIdx1] && childIdx2 <= endIdx) {
				if(heap[childIdx2] < heap[currentIdx]) {
					this.swap(currentIdx, childIdx2, heap);
					currentIdx = childIdx2;
					childIdx1 = currentIdx * 2 + 1;
					childIdx2 = currentIdx * 2 + 2;
				} else {
					return;
				}

			} else if(heap[childIdx2] > heap[childIdx1] && childIdx2 <= endIdx) {
				if(heap[childIdx1] < heap[currentIdx]) {
					this.swap(currentIdx, childIdx1, heap);
					currentIdx = childIdx1;
					childIdx1 = currentIdx * 2 + 1;
					childIdx2 = currentIdx * 2 + 2;
				} else {
					return;
				}
			} else {
				if(heap[childIdx1] < heap[currentIdx]) {
					this.swap(currentIdx, childIdx1, heap);
				} else {
					return;
				}
			}
		}
		return;
  }

  siftUp(currentIdx, heap) {
    // Write your code here.
		let parentIdx = Math.floor((currentIdx - 1)/2);
		while(parentIdx >= 0) {
			if(heap[parentIdx] > heap[currentIdx]) {
				this.swap(parentIdx, currentIdx, heap);
			}
			currentIdx = parentIdx;
			parentIdx = Math.floor((currentIdx - 1)/2);
		}
  }

  peek() {
    // Write your code here.
		return this.heap[0];
  }

  remove() {
    // Write your code here.
		this.swap(0, this.heap.length-1, this.heap);
		let itemToRemove = this.heap.pop();
		this.siftDown(0, this.heap.length-1, this.heap);
		return itemToRemove;
  }

  insert(value) {
    // Write your code here.
		this.heap.push(value);
		this.siftUp(this.heap.length-1, this.heap);
  }

	swap(i, j, heap) {
		let temp = heap[i];
		heap[i] = heap[j];
		heap[j] = temp;
	}
}
