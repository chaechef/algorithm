import Foundation

let n = Int(readLine() ?? "") ?? 0
let arr = (readLine() ?? "").split(separator: " ").compactMap { Int($0) }
var dp = Array(repeating: 0, count: 1001)

for num in arr {
    dp[num] = (Array(dp[1..<num]).max() ?? 0) + num
}

print(dp.max() ?? 0)
