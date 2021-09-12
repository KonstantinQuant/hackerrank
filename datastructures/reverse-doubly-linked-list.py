def reverse(llist):
    prev = None
    while llist is not None:
        buf = llist.next
        llist.next = prev
        prev = llist
        llist = buf
        
    return prev
