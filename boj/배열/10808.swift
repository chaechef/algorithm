import Foundation

let word = readLine()!

var dict: [Character: Int] = [:]

for c in word {
    dict[c, default: 0] += 1
}

for i in (97...122).map({Character(UnicodeScalar($0))}) {
    print(dict[i] ?? 0, terminator: " ")
}
