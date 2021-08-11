
import Foundation

let num1 = Int(readLine()!)!
let num2 = Int(readLine()!)!
let num3 = Int(readLine()!)!
let mul = num1 * num2 * num3
var dict: [Int:Int] = [:]

for i in 0..<10 {
    dict[i] = 0
}
for c in String(mul) {
    dict[Int(String(c))!]! += 1
}

let ret = dict.sorted { $0.key < $1.key}
    .reduce("", { $0 + "\n" + String($1.value) })
print(ret.dropFirst())
