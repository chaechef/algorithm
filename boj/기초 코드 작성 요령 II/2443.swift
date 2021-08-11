import Foundation

let num = Int(readLine()!)!

for i in (1...num).reversed() {
    let str = String(repeating: " ", count: num - i) + String(repeating: "*", count: 2 * i - 1)
    print(str)
}
