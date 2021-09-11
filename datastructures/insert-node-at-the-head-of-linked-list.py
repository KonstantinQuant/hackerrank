def insertNodeAtHead(llist, data):
    new = SinglyLinkedListNode(data)
    new.next = llist
    llist = new
    return llist
