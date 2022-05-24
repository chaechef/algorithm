
import Foundation

// 5000000 이라고 치면 1~9 9개 10~99까지 90개 100~999까지 900개 1000~9999까지 9000개
// 10002 면

let line = readLine() ?? ""
let len = line.count
let num = Int(line) ?? 0

// len이 1이면 0 2이면 9
let arr = (0..<len-1).map({ n in
    return 9 * Int(pow(Double(10), Double(n))) * (n + 1)
})
var cal = Int(pow(Double(10), Double(len-1)))
var sum = arr.reduce(0, +) + (num - cal + 1) * len
print(sum)
