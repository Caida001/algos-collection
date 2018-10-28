
function removeKthNodeFromEnd(head, k) {
  let node1 = head;
  let node2 = head;
  while(k > 0) {
    node2 = node2.next;
    k--;
  }

	if(node2 == null) {
		head.value = head.next.value;
		head.next = head.next.next;
		return;
	}
  while(node2.next) {
    node2 = node2.next;
    node1 = node1.next;
  }

  node1.next = node1.next.next;
}
