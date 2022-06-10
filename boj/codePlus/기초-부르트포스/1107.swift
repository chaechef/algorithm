import Foundation

let targetNum = Int(readLine() ?? "") ?? 0
let _ = readLine()
var brokenButton: Set<Int> = Set(readLine()?.split(separator: " ").compactMap { Int($0) } ?? [])
var buttonSet = Array(Set([1,2,3,4,5,6,7,8,9,0]).subtracting(brokenButton))

func bruthForce(num: Int, idx: Int, max: Int) -> [Int] {
    if idx == max { return [num] }
    var ret: [Int] = []
    for i in 0..<buttonSet.count {
        ret += bruthForce(num: num * 10 + buttonSet[i], idx: idx + 1, max: max)
    }
    return ret
}
var arr: [Int] = []
for i in 1...6 {
    arr += bruthForce(num: 0, idx: 0, max: i)
}
let narr = arr.map { ($0, abs($0 - targetNum)) }
var ret = abs(targetNum - 100)
if let minValue = narr.min(by: {$0.1 < $1.1}).map({ String($0.0).count + $0.1 }) {
    ret = min(ret, minValue)
}
print(ret)