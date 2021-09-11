# Language: Python 3
# Author: Konstantin Kuchenmeister

# returns the length of a linked list
def getLength(head):
    arr = []
    
    while head is not None:
        arr.append(head.data)
        head = head.next
    
    return len(arr)
  
  
 # Intuition: Compare the two linkedlists pair/elementwise. If the number of pairs that match are equal to the length of the lists, return true, else false.

def compare_lists(llist1, llist2):
    
    counter = 0
    length = getLength(llist1)
    
    while llist1 is not None and llist2 is not None: # Advance through both LL
        if llist1.data == llist2.data:
            counter+=1
            print(llist1.data, llist2.data, counter)
        llist1 = llist1.next
        llist2 = llist2.next
    
    if counter == length:
        return 1
    else:
        return 0
