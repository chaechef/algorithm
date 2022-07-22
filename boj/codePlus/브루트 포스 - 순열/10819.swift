import Foundation

let num = Int((readLine() ?? "")) ?? 0
let arr = (readLine() ?? "").split(separator: " ").compactMap { Int($0) }

func recursion(pool: [Int], picked: [Int]) -> [[Int]] {
    var ret: [[Int]] = []
    if pool.isEmpty {
        return [picked]
    }
    for i in 0..<pool.count {
        var temp = pool
        let elem = temp.remove(at: i)
        ret += recursion(pool: temp, picked: picked + [elem])
    }

    return ret
}

func calc(arr: [Int]) -> Int {
    var ret = 0
    for i in 0..<(arr.count-1) {
        ret += abs(arr[i] - arr[i+1])
    }
    return ret
}

print(recursion(pool: arr, picked: []).map(calc(arr:)).max() ?? 0)
