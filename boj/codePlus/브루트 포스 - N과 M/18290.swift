import Foundation

let toks = (readLine() ?? "").split(separator: " ").compactMap { Int($0) }
let n = toks[0]
let m = toks[1]
let k = toks[2]
let board = (0..<n).map { _ -> [Int] in (readLine() ?? "").split(separator: " ").compactMap { Int($0) } }
var answer: Int = .min

func recursion(picked: [(Int,Int)], ci: Int, maxCount: Int) {
    if picked.count == maxCount {
        let ret = picked.map { y, x in board[y][x] }.reduce(0, +)
        answer = max(answer, ret)
        return
    }
    let ban = picked.map { ($0.0, $0.1 + 1) } + picked.map { ($0.0 + 1, $0.1) }
    for i in ci..<n*m {
        let y = i / m
        let x = i % m
        if ban.contains(where: { $0.0 == y && $0.1 == x}) {
            continue
        }
        recursion(picked: picked + [(y, x)], ci: i+1, maxCount: maxCount)
        
    }

}

recursion(picked: [], ci: 0, maxCount: k)

print(answer)
