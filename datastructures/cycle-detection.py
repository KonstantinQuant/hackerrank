def has_cycle(head):
    iter_ = head
    cycle = False
    arr = []
    
    if head is None:
        return 0
    
    while head is not None:
        arr.append(head)
        head = head.next
    
    while iter_ is not None:
        if arr.count(iter_) > 1:
            cycle = True
            break
        iter_ = iter_.next
    
    return cycle
