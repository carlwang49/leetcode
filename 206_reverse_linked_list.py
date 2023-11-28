from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        new_head = ListNode()
        new_head = self.reverseList(head.next)  # 遞迴"反轉 Link list"
        head.next.next = head                   # 反轉過後，head 的 next 變成最後一個節點，將其最後一個節點指向自己，成為新的最後一個節點
        head.next = None                        # 自己成為最後一個節點後，將最後一個節點指向 None
        return new_head                         # 返回"已反轉的 Link list"

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None 
        new_head = None
        while head is not None:
            rear = head.next        # 保存 head 的下一個
            head.next = new_head    # 斷掉右邊的鏈結，將新鏈結指向左邊
            new_head = head         # new_head 往右移動一個  
            head = rear             # head 往右移動一個
        return new_head
        