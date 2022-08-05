import Foundation

let line = (readLine() ?? "").split(separator: " ").compactMap { Int($0) }
let n = line[0]
let k = line[1]
var board = Array(repeating: Array(repeating: 0, count: n+1), count: k)

for i in 0..<(n+1) {
    board[0][i] = 1
}

for i in 1..<k {
    for j in 0..<(n+1) {
        for k in 0..<(j+1) {
            board[i][j] = (board[i][j] + board[i-1][k]) % 1000000000
        }
    }
}

print(board[k-1][n])