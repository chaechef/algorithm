//
//  main.swift
//  ProblemSolving
//
//  Created by 채훈기 on 2021/03/12.
//

import Foundation

func solution(_ num: Int) -> Int {
    
    let arr = [1,2,4,7,13,24,44,81,149,274]
    
    return num > 10 ? 0 : arr[num-1]
}


func submit() {
    guard let line = readLine(), let tc = Int(line) else { return }
    
    for _ in 0..<tc {
        if let l = readLine(), let num = Int(l){
            print(solution(num))
        }
    }
}

submit()
