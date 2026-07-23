'''
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted linked list and return the head of the new sorted linked list.
The new list should be made up of nodes from list1 and list2.
Example 1: Input: list1 = [1,2,4], list2 = [1,3,5]
Output: [1,1,2,3,4,5]

Example 2: Input: list1 = [], list2 = [1,2]
Output: [1,2]

Example 3:Input: list1 = [], list2 = []
Output: []

Constraints: 0 <= The length of the each list <= 100.
-100 <= Node.val <= 100
'''

# list1 = [1,2,4]
# list2 = [1,3,5]
# list1 = []
# list2= [1,2]
# list1 = []
# list2 = []


class solution:
    def mergetwolist(self,l1: Listnode,l2 : Listnode):
        dummy= Listnode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
                tail = tail.next
            if l1:
                tail.next = l1
            elif l2:
                tail.next = 12

            return dummy.next



l1 = [1,2,4]
l2 = [1,3,5]

x = solution()
x.mergetwolist(l1,l2)
print(x)
