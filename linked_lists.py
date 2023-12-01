#2 pointers, to return node n from the end.

def nth_last_node(linked_list, n):
 
    current = linked_list.head
    nth_pointer = None
    count = 1

    while current:
        current = current.next
        count += 1

        if count >= n + 1:
            if nth_pointer == None:
                nth_pointer = linked_list.head
            else:
                nth_pointer = nth_pointer.next

    return nth_pointer


#Reverse linked list in place
def reverse_linked_list_inplace(llist):

    current = llist.head
    previous = None

    while current:
        next = current.next
        current.next = previous
        previous = current
        current = next
    
    return previous   #return new head of reversed list

# 2 pointers, one double fast, one single fast.  Return middle of linked list node. Moves twice as fast so when end reached slow will be in middle.
def find_middle(linked_list):
    fast_pointer = linked_list.head
    slow_pointer = linked_list.head

    while fast_pointer.next.next:
        fast_pointer = fast_pointer.next.next
        slow_pointer = slow_pointer.next

    return slow_pointer