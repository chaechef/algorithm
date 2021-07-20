import Foundation

class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        for i in 0..<nums.count {
            for j in i+1..<nums.count {
                if nums[i] + nums[j] == target {
                    return [i, j]
                }
            }
        }
        return []
    }
}

class Solution2 {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        var table: [Int:Int] = [:]
        for i in 0..<nums.count {
            if let index = table[target - nums[i]] {
                return [index, i]
            }
            table[nums[i]] = i
        }
        return []
    }
}


Solution().twoSum([1,2,3,4,5,6], 10)
