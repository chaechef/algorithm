import Foundation


public class ListNode {
    public var val: Int
    public var next: ListNode?
    public init() { self.val = 0; self.next = nil; }
    public init(_ val: Int) { self.val = val; self.next = nil; }
    public init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next; }
}

class Solution {
    func addTwoNumbers(_ l1: ListNode?, _ l2: ListNode?) -> ListNode? {
        var left = l1
        var right = l2
        var carry = 0
        let head = ListNode()
        var curr = head
        
        while left != nil || right != nil {
            let lvalue = left?.val ?? 0
            let rvalue = right?.val ?? 0
            var sum = lvalue + rvalue + carry
            carry = sum >= 10 ? 1 : 0
            sum = sum >= 10 ? sum - 10 : sum
            let newNode = ListNode(sum)
            curr.next = newNode
            curr = newNode
            left = left?.next
            right = right?.next
        }
        if carry == 1 {
            curr.next = ListNode(1)
        }
        return head.next
    }
}

let a = Solution().addTwoNumbers(ListNode(0), ListNode(0))
print(a?.val)
