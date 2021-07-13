import Foundation

func solution(_ gems:[String]) -> [Int] {
    let gemSet = Set(gems)
    let gemNum = gemSet.count
    var dict = Dictionary(uniqueKeysWithValues: gemSet.map { ($0, 0) })
    
    var lo = 0
    var ret: (Int, Int) = (1,gems.count)
    var nonZeroCount = 0

    for hi in 0..<gems.count {
        let gem = gems[hi]
        if dict[gem]! == 0 {
            nonZeroCount += 1
        }
        dict[gem]! += 1
        
        while lo <= hi {
            if nonZeroCount < gemNum {
                break
            }
            if ret.1 - ret.0 > (hi+1) - (lo+1) {
                ret = (lo+1, hi+1)
            }
            let key = gems[lo]
            if dict[key] == 1 {
                nonZeroCount -= 1
            }
            dict[key]! -= 1
            lo += 1
        }
        
    }
    
    return [ret.0, ret.1]
}

let a = solution(["a", "a", "a", "a", "b"])
print(a)
