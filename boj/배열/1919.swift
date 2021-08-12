
import Foundation

let word1 = readLine()!
let word2 = readLine()!

func countChar(str: String) -> [Int] {
    var arr = Array(repeating: 0, count: 26)
    for c in str {
        let idx = Int(c.asciiValue! - 97)
        arr[idx] += 1
    }
    return arr
}

let arr1 = countChar(str: word1)
let arr2 = countChar(str: word2)
var ret = 0

for (i, j) in zip(arr1, arr2) {
    ret += abs(i - j)
}
print(ret)