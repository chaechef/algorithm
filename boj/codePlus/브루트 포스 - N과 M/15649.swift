import Foundation

let toks = (readLine() ?? "").split(separator: " ").compactMap { Int($0) }
let n = toks[0]
let m = toks[1]
var arr = Array(1...n)

func recursion(arr1: [Int], arr2: [Int], current: Int, total: Int) {
    if current == total {
        print(arr2.map { String($0)}.joined(separator: " ") )
        return
    }
    for i in 0..<arr1.count {
        var tempArr = arr1
        let temp = tempArr.remove(at: i)
        recursion(arr1: tempArr, arr2: arr2 + [temp], current: current + 1, total: total)
    }
}

recursion(arr1: arr, arr2: [], current: 0, total: m)