
import Foundation

let line = readLine()!
var arr = Array(repeating: 0, count: 10)

for c in line {
    let str = String(c)
    arr[Int(str)!] += 1
}
arr[6] = Int(ceil(Double(arr[6] + arr[9]) / 2))
arr[9] = 0
print(arr.max()!)
