//
//  2438.swift
//  ProblemSolving
//
//  Created by 채훈기 on 2021/03/03.
//

import Foundation

let input = readLine()

if let optNum = input, let num = Int(optNum) {
    (1...num).forEach {
        let str = String(repeating: "*", count: $0)
        print(str)
    }
}

