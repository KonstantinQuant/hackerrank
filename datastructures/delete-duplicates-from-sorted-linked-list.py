def removeDuplicates(llist):
    head = llist
    while head.next is not None:
        if head.data == head.next.data:
            head.next = head.next.next
        else:
            head = head.next
        
    return llist
