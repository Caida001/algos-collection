class LRUCache {
  constructor(maxSize) {
		this.cache = {};
    this.maxSize = maxSize || 1;
		this.currentSize = 0;
		this.list = new DoublyLinkedList();
  }

  insertKeyValuePair(key, value) {
    // Write your code here.
		if(!(key in this.cache)) {
			if(this.currentSize == this.maxSize) {
				this.evictLeastRecent();

			} else {
				this.currentSize++;
			}
			this.cache[key] = new DoublyLinkedListNode(key, value);
		} else {
			this.replaceKey(key, value);
		}
		this.updateMostRecent(this.cache[key]);
  }

  getValueFromKey(key) {
    // Write your code here.
		if(!(key in this.cache)) return null;
		this.updateMostRecent(this.cache[key]);
		return this.cache[key].value;
  }

  getMostRecentKey() {
    // Write your code here.
		return this.list.head.key;
  }

	evictLeastRecent() {
		let keyToRemove = this.list.tail.key;
		this.list.removeTail();
		delete this.cache[keyToRemove];
	}

	updateMostRecent(node) {
		this.list.setHeadTo(node);
	}

	replaceKey(key, value) {
		this.cache[key].value = value;
	}

}

class DoublyLinkedList {
	constructor() {
		this.head = null;
		this.tail = null;
	}

	setHeadTo(node) {
		if(node === this.head) {
			return;
		} else if(this.head == null) {
			this.head = node;
			this.tail = node;
		} else if(this.head == this.tail) {
			this.tail.prev = node;
			this.head = node;
			this.head.next = this.tail;
		} else {
			node.removeBindings();
			this.head.prev = node;
			node.next = this.head;
			this.head = node;
		}

	}

	removeTail() {
		if(this.tail == null) return;
		if(this.tail == this.head) {
			this.tail = null;
			this.head = null;
			return;
		}
		this.tail = this.tail.prev;
		this.tail.next = null;
	}

}

class DoublyLinkedListNode {
	constructor(key, value) {
		this.key = key;
		this.value = value;
		this.prev = null;
		this.next = null;
	}

	removeBindings() {
		if(this.next != null) this.next.prev = this.prev;
		if(this.prev != null) this.prev.next = this.next;
		this.prev = null;
		this.next = null;
	}

}
