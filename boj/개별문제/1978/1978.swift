//
//  main.swift
//  ProblemSolving
//
//  Created by 채훈기 on 2021/03/05.
//

import Foundation

let maxNum = 1001
func solution(_ nums: [Int]) -> Int{
    
    var isPrimeNumber : [Bool] = Array(repeating: true, count: maxNum)
    
    isPrimeNumber[0] = false
    isPrimeNumber[1] = false
    
    for i in 2..<maxNum {
        if isPrimeNumber[i] == false {
            continue
        }
        var j = 2
        while i * j < maxNum {
            isPrimeNumber[i * j] = false
            j += 1
        }
    }
    
    return nums.map { isPrimeNumber[$0] }.filter { $0 == true }.count
}

func submit() {
    guard let _ = readLine(),
          let line = readLine() else { return }
    
    let toks = line.components(separatedBy: " ").compactMap { Int($0) }
    
    print(solution(toks))
    
}

submit()
