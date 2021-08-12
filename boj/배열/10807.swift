import Foundation

let num = Int(readLine()!)!
let arr = readLine()!.split(separator: " ").compactMap { Int($0) }
var dict: [Int: Int] = [:]

for n in arr {
    dict[n, default: 0] += 1
}

print(dict[Int(readLine()!)!, default: 0])
