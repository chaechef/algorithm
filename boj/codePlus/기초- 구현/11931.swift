import Foundation

func readNumbers() -> [Int] {
    return (readLine() ?? "").split(separator: " ").compactMap { Int($0) }
}

func calcWidth(arr: [Int]) -> Int {
    var sum = arr[0]
    for i in 1..<arr.count {
        let prev = arr[i-1]
        let next = arr[i]
        sum += abs(next - prev)
    }
    sum += arr[arr.count - 1]
    return sum
}

let toks = readNumbers()
let n = toks[0]
let m = toks[1]
let board = (0..<n).map { _ -> [Int] in readNumbers() }
var tboard: [[Int]] = Array(repeating: Array(repeating: 0, count: n), count: m)
for i in 0..<n {
    for j in 0..<m {
        tboard[j][i] = board[i][j]
    }
}

let a = board.map { calcWidth(arr: $0) }.reduce(0, +)
let b = tboard.map { calcWidth(arr: $0) }.reduce(0, +)
print(a + b + (n * m * 2))
