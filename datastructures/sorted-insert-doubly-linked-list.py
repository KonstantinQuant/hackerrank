# only 4/8 testcases passing here?...
def sortedInsert(llist, data):
    head = llist
    new = DoublyLinkedListNode(data)
    
    if head is None:
        head = new
    
    while llist.next is not None and llist.next.data <= data:
        llist = llist.next
        
    new.next = llist.next
    new.prev = llist
    llist.next = new

    return head
