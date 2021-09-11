def reversePrint(llist):
    if llist is None:
        return
    else:
        arr = []
        while llist is not None :
            arr.append(llist.data)
            llist = llist.next
        
        for index in range(len(arr)):
            print(arr[-index-1])
