def reverse(llist):
    # Write your code here
    previous = None
    head = llist
    
    while head is not None: # As long as we are not at the Null node keep advancing
        tmp = head.next # Save the next node, its our node in the next iteration
        head.next = previous # Our next is now the previous
        previous = head # The previous in the next iteration is our current node
        head = tmp # The current node in the next iteration is our next node
    
    return previous # Return the previous since we are disregarding the last Null node
