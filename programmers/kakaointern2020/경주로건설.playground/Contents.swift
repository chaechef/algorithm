import UIKit

struct Node {
    let x: Int
    let y: Int
    let direct: Int
}

func solution(_ board:[[Int]]) -> Int {
    let n = board.count - 1, m = board[0].count - 1
    let dy = [-1, 0, 1, 0]
    let dx = [0, 1, 0, -1]
    var queue: [Node] = [Node(x: 0, y: 0, direct: -1)]
    var costBoard = Array.init(repeating: Array(repeating: Int.max, count: m + 1), count: n + 1)
    let boundCheck: (Int, Int) -> Bool = { y, x in
        return y >= 0 && x >= 0 && y <= n && x <= m
    }
    while !queue.isEmpty {
        let node = queue.removeFirst()
        for i in 0..<4 {
            let ny = node.y + dy[i]
            let nx = node.x + dx[i]
            if !boundCheck(ny, nx) || board[ny][nx] == 1
                || (i+2) % 4 == node.direct  {
                continue // 밖을 벗어나거나 벽이거나 왔던 반대편 길이면 패스
            }
            
            let next = Node(x: nx, y: ny, direct: i)
            
        }
        
    }
    
    return 0
}


let b = [[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]

solution(b)
