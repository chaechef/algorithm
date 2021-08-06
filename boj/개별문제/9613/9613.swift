//
//  main.swift
//  ProblemSolving
//
//  Created by 채훈기 on 2021/03/04.
//

import Foundation

func gcd(_ num1: Int, _ num2: Int) -> Int {
    var n1 = num1
    var n2 = num2
    
    while n2 > 0 {
        let r = n1 % n2
        n1 = n2
        n2 = r
    }
    
    return n1
}

func solution(_ nums: [Int]) -> Int {
    var sum = 0
    for i in 0..<nums.count {
        for j in i+1..<nums.count {
            sum += gcd(nums[i], nums[j])
        }
    }
    
    return sum
}

func submit() {
    guard let testCase = readLine(),
          let tc = Int(testCase) else { return }
    
    for _ in 0..<tc {
        guard let line = readLine() else { continue }
        let toks = line.components(separatedBy: " ")
            .compactMap { Int($0) }
        print(solution(Array(toks[1...])))
        
    }
}

submit()

