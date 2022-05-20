import Foundation

var cache: [Bool] = Array(repeating: true, count: 1_000_001)
cache[0] = false
cache[1] = false

(2...1_000_000).forEach { num in
    if !cache[num] {
        return
    }
    var mul = 2
    while num * mul <= 1_000_000 {
        cache[num * mul] = false
        mul += 1
    }
}

let toks = readLine()?.split(separator: " ").compactMap { Int($0) } ?? []

print(cache[toks[0]...toks[1]]
        .enumerated()
        .filter { $0.element }
        .map { String($0.offset + toks[0] )}
        .joined(separator: "\n"))