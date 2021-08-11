import Foundation

let num = Int(readLine()!)!

for i in 0..<num {
    for _ in 0..<(num - i - 1) {
        print(" ", terminator: "")
    }
    for _ in 0..<(i+1) {
        print("*", terminator: "")
    }
    print()
}
