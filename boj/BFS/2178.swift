import Foundation

extension String {
    func splitInt() -> [Int] {
        self.split(separator: " ").compactMap { Int($0) }
    }
}

let nk = readLine()!.splitInt()
let n = nk[0]
let k = nk[1]
let dy = [0,0,1,-1]
let dx = [1,-1,0,0]
var board = (0..<n).map { _ -> [Int] in
    return readLine()!.map { Int(String($0))!}}
var dst = Array(repeating: Array(repeating: -1, count: k), count: n)
var queue: [(Int,Int)] = []
queue.append((0,0))

dst[0][0] = 1

while !queue.isEmpty {
    let curr = queue.removeLast()
    for i in 0..<4 {
        let ny = curr.0 + dy[i]
        let nx = curr.1 + dx[i]
        if !((0..<n) ~= ny) || !((0..<k) ~= nx)
            || board[ny][nx] == 0 {
            continue
        }
        if dst[ny][nx] == -1 || dst[ny][nx] > dst[curr.0][curr.1] + 1 {
        dst[ny][nx] = dst[curr.0][curr.1] + 1
        queue.append((ny,nx))
        }
    }
}

print(dst[n-1][k-1])
