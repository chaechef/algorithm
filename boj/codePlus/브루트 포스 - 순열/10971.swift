import Foundation

let num = Int((readLine() ?? "")) ?? 0
let board = (0..<num).map { _ in (readLine() ?? "").split(separator: " ").compactMap{ Int($0) } }
var answer: Int = .max
var visited: [Bool] = Array(repeating: false, count: num)
var start = 0
visited[0] = true

func dfs(startIndex: Int, cost: Int, route: [Int]) {
    if route.count == num {
        let s = route.last ?? 0
        let e = route.first ?? 0
        if board[s][e] == 0 { return }
        let totalCost = cost + board[s][e]
        answer = min(answer, totalCost)
    }
    for i in 0..<num {
        if visited[i] == true || board[startIndex][i] == 0 { continue }
        visited[i] = true
        let newCost = board[startIndex][i]
        dfs(startIndex: i, cost: cost + newCost, route: route + [i])
        visited[i] = false
    }
}


dfs(startIndex: 0, cost: 0, route: [0])
print(answer)
