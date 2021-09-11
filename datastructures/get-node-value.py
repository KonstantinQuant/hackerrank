def getLength(llist):
    arr = list()
    
    while llist is not None:
        arr.append(llist.data)
        llist = llist.next
    print(arr)
    return len(arr)

def getNode(llist, positionFromTail):
    tmp = llist
    print(getLength(llist), positionFromTail)
    
    for _ in range(getLength(llist)-positionFromTail-1):
        llist = llist.next
    return llist.data
