//
//  main.swift
//  5.Longest Palindromic Substring
//
//  Created by 채훈기 on 2021/07/21.
//

import Foundation

class Solution {
    func isPalindrome(_ memo: inout [[Bool]], _ s: [Character],
                      _ start: Int, _ end: Int) -> Bool {
        if start == end {
            print("xx")
            memo[start][end] = true
            return true
        }
        if start+1 == end {
            memo[start][end] = s[start] == s[end]
            return memo[start][end]
        }
        
        if (memo[start+1][end-1] || start+1 == end - 1) && ((s[start] == s[end])) {
            memo[start][end] = true
        }

        return memo[start][end]
    }
    
    func longestPalindrome(_ s: String) -> String {
        var left = 0
        var right = 0
        var memo: [[Bool]] = Array(repeating: Array(repeating: false, count: s.count), count: s.count)
        let arr = Array(s)
        for j in 1..<s.count {
            // 단어의 길이 1~s.count
            for i in 0..<j {
                // 시작위치 for 1 ~ s.count - i
                // sub가 팰린드롬인지 체크
                if isPalindrome(&memo, arr, i, j) && right - left < j - i{
                    left = i
                    right = j
                }
            }
        }
        return String(arr[left...right])
    }
}

let s = "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"

print(Solution().longestPalindrome(s))
