import Foundation

let num = Int(readLine()!)!
if num == 1 {
    print("*")
} else {
    for i in (1...num).reversed() + (2...num) {
        let str = String(repeating: " ", count: num - i) + String(repeating: "*", count: 2 * i - 1)
        print(str)
    }

}
