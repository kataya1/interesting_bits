class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def has_cycle(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next 
        fast = fast.next.next
        if slow == fast: 
            return slow
    return False

def break_cycle(head):
    slow = has_cycle(head)
    if not slow:
        return
    # Getting the cycle beginning node
    fast = head
    while fast != slow: 
        fast = fast.next
        slow = slow.next
    # Getting the cycle ending node
    while fast.next != slow:
        fast = fast.next
    # breaking the cycle
    fast.next = None
    

def reverse_linked_list(head):
    prev = None 
    while head:
        head.next, prev, head = prev, head, head.next 
    return prev

def print_ll(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    else:
        print("null")
# Test functions 
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next =  head.next # point at the second node


print(f"has_cycle -> {True if has_cycle(head) else False}") #  True
break_cycle(head) 
print(f"has_cycle -> {True if has_cycle(head) else False}") #  False
print_ll(head)
reverse_head = reverse_linked_list(head)  
print_ll(reverse_head)
