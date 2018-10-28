class ContinuousMedianHandler {
  constructor(value) {
    // Write your code here.
		this.lowers = new Heap(MAX_HEAP_FUNC, []);
		this.greaters = new Heap(MIN_HEAP_FUNC, []);
    this.median = null;
  }

  insert(number) {
    // Write your code here.
		if(!this.lowers.length || number < this.lowers.peek()) {
			this.lowers.insert(number);
		} else {
			this.greaters.insert(number);
		}
		this.rebalanceHeaps();
		this.updateMedian();
  }

	rebalanceHeaps() {
		if(this.lowers.length - this.greaters.length == 2) {
			this.greaters.insert(this.lowers.remove());
		} else if(this.greaters.length - this.lowers.length == 2) {
			this.lowers.insert(this.greaters.remove());
		}
	}

	updateMedian() {
		if(this.greaters.length == this.lowers.length) {
			this.median = (this.greaters.peek() + this.lowers.peek()) / 2;
		} else if(this.lowers.length > this.greaters.length) {
			this.median = this.lowers.peek();
		} else {
			this.median = this.greaters.peek();
		}
	}

  getMedian() {
    return this.median;
  }
}
