//
//  main.swift
//  ProblemSolving
//
//  Created by 채훈기 on 2021/03/07.
//

import Foundation

func solution(_ nums: [Int]) {
    var years = 1
    var earthNum = 1
    var sunNum = 1
    var moonNum = 1
    
    while earthNum != nums[0]
            || sunNum != nums[1]
            || moonNum != nums[2] {
        earthNum = earthNum == 15 ? 1 : earthNum + 1
        sunNum = sunNum == 28 ? 1 : sunNum + 1
        moonNum = moonNum == 19 ? 1 : moonNum + 1

        years += 1
    }
    
    print(years)
}

func submit() {
    guard let line = readLine() else { return }
    let nums = line.components(separatedBy: " ").compactMap { Int($0) }
    
    solution(nums)
    
}


submit()
