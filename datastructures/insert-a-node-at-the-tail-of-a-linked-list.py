def insertNodeAtTail(head, data):
    tmp = head
    
    # Constructing the head for the first time
    if head is None:
        head = SinglyLinkedListNode(data)
        return head
    
    while head.next is not None:
        head = head.next
    
    head.next = SinglyLinkedListNode(data)
    return tmp
