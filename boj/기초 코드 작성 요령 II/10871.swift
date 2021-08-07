//
//  main.swift
//  PSCanvas
//
//  Created by 채훈기 on 2021/08/14.
//

import Foundation

let line = readLine()!
    .split(separator: " ")
    .compactMap{ Int($0) }
let n = line[0], x = line[1]
let arr = readLine()!
    .split(separator: " ")
    .compactMap{ Int($0) }

let answer = arr.filter { $0 < x }
    .map{ String($0) }
print(answer.joined(separator: " "))
