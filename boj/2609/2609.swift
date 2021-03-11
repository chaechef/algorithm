//
//  main.swift
//  ProblemSolving
//
//  Created by 채훈기 on 2021/03/02.
// 2609

import Foundation

func gcd(num1: Int, num2: Int) -> Int {
    var n1 = num1
    var n2 = num2
    
    while n2 > 0 {
        let q = n1 / n2
        let r = n1 - q * n2
        n1 = n2
        n2 = r
    }
    
    return n1
}

let input = readLine()

if let optNums = input {
    let nums = optNums.components(separatedBy: " ")
        .compactMap { Int($0) }
    let n1 = nums[0]
    let n2 = nums[1]
    print(gcd(num1: n1, num2: n2))
    print(n1 * n2 / gcd(num1: n1, num2: n2))
}

