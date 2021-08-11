import Foundation

let num = Int(readLine()!)!

for i in (1...num).reversed() {
    let str = String(repeating: " ", count: num - i) + String(repeating: "*", count: i)
    print(str)
}
