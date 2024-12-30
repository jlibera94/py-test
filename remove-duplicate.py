from typing import Optional
# Definition for singly-linked list.
class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

        def __repr__(self):
            
            return f"ListNode(val={self.val})" 

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        Deletes all duplicates from a sorted linked list.

        Args:
            head: The head of the linked list.

        Returns:
            The head of the linked list after removing duplicates.
        """
        if not head:
            return head

        current = head
        while current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head

def create_linked_list(nums):
    """
  Creates a linked list from a list of integers.

  Args:
      nums: A list of integers.

  Returns:
      The head of the linked list.
  """
    if not nums:
      return None
    head = ListNode(nums[0])
    current = head
    for num in nums[1:]:
      current.next = ListNode(num)
      current = current.next
    return head

if __name__ == "__main__":
    nums = [1,1,2]
    head = create_linked_list(nums)
    solution = Solution()
    z = solution.deleteDuplicates(head)
    print(z)
