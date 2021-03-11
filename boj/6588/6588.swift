//
//  main.swift
//  ProblemSolving
//
//  Created by 채훈기 on 2021/03/07.
//

import Foundation

let maxNum = 1000001
var primeNums = Array(repeating: true, count: maxNum)

func solution(_ num: Int) {
    for i in 2..<maxNum {
        if primeNums[i] == true
            && primeNums[num - i] == true {
            print("\(num) = \(i) + \(num - i)")
            break
        }
    }
}

func submit() {
    // input
    guard let line = readLine(), var num = Int(line) else { return }
    
    //primeNums
    primeNums[0] = false
    primeNums[1] = false
    for i in 2..<maxNum {
        if primeNums[i] == false {
            continue
        }
        var j = 2
        while i * j < maxNum {
            primeNums[i*j] = false
            j += 1
        }
    }

    while num != 0 {
        
        solution(num)
        
        guard let nextLine = readLine(), let newNum = Int(nextLine) else { break }
        num = newNum
    }
}


submit()
