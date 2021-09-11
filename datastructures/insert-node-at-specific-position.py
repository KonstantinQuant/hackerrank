def insertNodeAtPosition(llist, data, position):
    # Write your code here
    tmp = llist # Save the head of the initial linkedlist
    for _ in range(position - 1): # Traverse through the linkedlist to the position - 1
        llist = llist.next
        pos = llist.next
    llist.next = SinglyLinkedListNode(data)
    llist.next.next = pos # Link the old and new node
    
    return tmp # Return the head
