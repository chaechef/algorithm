//
//  main.swift
//  ProblemSolving
//
//  Created by 채훈기 on 2021/03/03.
//

import Foundation

func solution(num1: Int, num2: Int) {
    var n1 = num1
    var n2 = num2
    
    while n2 > 0 {
        let q = n1 / n2
        let r = n1 - q * n2
        n1 = n2
        n2 = r
    }
    
    print(num1 * num2 / n1 )
}


func submit() {
    guard let input = readLine(),
          let testCase = Int(input) else { return }
    
    for _ in 0..<testCase {
        guard let line = readLine() else { continue }
        let toks = line.components(separatedBy: " ")
            .compactMap { Int($0) }
        
        if toks.count != 2 {
            continue
        }
        let num1 = toks[0]
        let num2 = toks[1]
        
        solution(num1: num1, num2: num2)
    }

}

submit()

