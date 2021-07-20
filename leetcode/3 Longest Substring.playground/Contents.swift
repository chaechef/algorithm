import Foundation

extension String {
    subscript(_ index: Int) -> Character {
        return self[self.index(self.startIndex, offsetBy: index)]
    }
}
class Solution {
    func lengthOfLongestSubstring(_ s: String) -> Int {
        //0일때 처리
        if s.count == 0 { return 0 }
        var dict: [Character: Int] = [:]
        var ret = 0
        var start = 0
        for end in 0..<s.count {
            let char = s[s.index(s.startIndex, offsetBy: end)]
            dict[char, default: 0] += 1
            if dict[char, default: 0] == 2 {
                while dict[char, default: 0] == 2 {
                    let schar = s[start]
                    dict[schar, default: 0] -= 1
                    start += 1
                }
            }
            ret = max(ret, end - start + 1)
        }
        return ret
    }
}

let a = Solution().lengthOfLongestSubstring("abcabcbb")
print(a)
