class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  def addTwoNumbers(self, l1, l2, c = 0):
    p = l1
    q = l2
    carry = 0
    res = n = ListNode(0)
    while p or q:
        if not p:
            i=0
        else:
            i=p.val
        if not q:
            j=0
        else:
            j=q.val

        s = i+j+carry
        if s >= 10:
            carry = 1
            rem=s%10
            n.next = n = ListNode(rem)
        else:
            carry = 0
            n.next = n = ListNode(s)
        if p:
            p=p.next
        if q:
            q=q.next
    return res.next
l1 = ListNode(4)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
while result:
  print(result.val)
  result = result.next
# 7 0 8
