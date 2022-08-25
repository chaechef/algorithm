import Foundation

let n = Int(readLine() ?? "") ?? 0
let arr = (readLine() ?? "").split(separator: " ").compactMap { Int($0) }
var darr: [Int] = arr.reversed()
var adp = Array(repeating: 0, count: 1001)
var ascendingArr = Array(repeating: 0, count: n)
var ddp = Array(repeating: 0, count: 1001)
var descendingArr = Array(repeating: 0, count: n)

for i in 0..<arr.count {
    let num = arr[i]
    adp[num] = (Array(adp[1..<num]).max() ?? 0) + 1
    ascendingArr[i] = adp[num]
    let dnum = darr[i]
    ddp[dnum] = (Array(ddp[1..<dnum]).max() ?? 0) + 1
    descendingArr[i] = ddp[dnum]
}
print(zip(ascendingArr, descendingArr.reversed()).map { elem in elem.0 + elem.1 - 1 }.max() ?? 0)

