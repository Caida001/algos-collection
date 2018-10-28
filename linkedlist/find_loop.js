function findLoop(head) {
  // Write your code here.
	let node1 = head.next;
	let node2 = head.next.next;
	while(node1 != node2) {
		node1 = node1.next;
		node2 = node2.next.next;
	}
	node1 = head;
	while(node1 != node2) {
		node1 = node1.next;
		node2 = node2.next;
	}
	return node1;
}
