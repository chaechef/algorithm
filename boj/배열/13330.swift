import Foundation

let line = readLine()!.split(separator: " ").compactMap { Int($0) }
let n = line[0]
let k = line[1]
var arr = Array(repeating: 0, count: 12)

for _ in 0..<n {
    let l = readLine()!.split(separator: " ").compactMap { Int($0) }
    let idx = 2 * (l[1] - 1) + l[0]
    arr[idx] += 1
}

let ret = arr.map { Int(ceil(Double($0) / Double(k))) }
    .reduce(0, +)
print(ret)