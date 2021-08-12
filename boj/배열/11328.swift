import Foundation

func countString(str: String) -> [Int] {
    var arr = Array(repeating: 0, count: 26)
    for c in str {
        arr[Int(c.asciiValue! - Character("a").asciiValue!)] += 1
    }
    return arr
}
let num = Int(readLine()!)!


for _ in 0..<num {
    let toks = readLine()!.split(separator: " ").compactMap { String($0) }
    if countString(str: toks[0]) == countString(str: toks[1]) {
        print("Possible")
    } else {
        print("Impossible")
    }
}
