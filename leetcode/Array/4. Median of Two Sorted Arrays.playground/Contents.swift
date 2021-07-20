import UIKit

class Solution {
    func findMedianSortedArrays(_ nums1: [Int], _ nums2: [Int]) -> Double {
        let mid = (nums1.count + nums2.count) / 2
        var arr1 = nums1
        var arr2 = nums2
        var prev = 0
        var curr = 0
        for _ in 0...mid {
            prev = curr
            if arr1.first == nil {
                curr = arr2.removeFirst()
                continue
            }
            if arr2.first == nil {
                curr = arr1.removeFirst()
                continue
            }
            if arr1[0] < arr2[0] {
                curr = arr1.removeFirst()
            } else {
                curr = arr2.removeFirst()
            }
        }
        if (nums1.count + nums2.count) % 2  == 0{
            return Double((prev + curr)) / 2.0
        } else {
            return Double(curr)
        }
    }
}

let n1 = [0,0]
let n2 = [0,0]
let a = Solution().findMedianSortedArrays(n1, n2)
