import Foundation

var cache: [Int] = Array(repeating: 0, count: 1_000_001)
var cache2: [Int] = Array(repeating: 0, count: 1_000_001)

(1...1_000_000).forEach { num in
    var mul = 1
    while num * mul <= 1000000 {
        cache[num * mul] += num
        mul += 1
    }
}
(1...1_000_000).forEach { num in
    cache2[num] = cache2[num-1] + cache[num]
}

let tc = Int(readLine() ?? "") ?? 0

(0..<tc).forEach { _ in
    let n = Int(readLine() ?? "") ?? 1
    print(cache2[n])
}

