import Foundation
public struct Queue<T> {
  fileprivate var array = [T?]()
  fileprivate var head = 0

  public var isEmpty: Bool {
    return count == 0
  }

  public var count: Int {
    return array.count - head
  }

  public mutating func enqueue(_ element: T) {
    array.append(element)
  }

  public mutating func dequeue() -> T? {
    guard let element = array[guarded: head] else { return nil }

    array[head] = nil
    head += 1

    let percentage = Double(head)/Double(array.count)
    if array.count > 50 && percentage > 0.25 {
      array.removeFirst(head)
      head = 0
    }

    return element
  }

  public var front: T? {
    if isEmpty {
      return nil
    } else {
      return array[head]
    }
  }
}

extension Array {
    subscript(guarded idx: Int) -> Element? {
        guard (startIndex..<endIndex).contains(idx) else {
            return nil
        }
        return self[idx]
    }
}
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
var board = (0..<k).map { _ -> [Int] in
    return readLine()!.splitInt()
}
var queue = Queue<(Int,Int)>()
var visited = Array(repeating: Array(repeating: -1, count: n), count: k)

for i in 0..<k {
    for j in 0..<n {
        if board[i][j] == 1 {
            queue.enqueue((i,j))
            visited[i][j] = 0
        }
    }
}

while !queue.isEmpty {
    let curr = queue.dequeue()!
    for i in 0..<4 {
        let ny = curr.0 + dy[i]
        let nx = curr.1 + dx[i]
        if ny < 0 || nx < 0 || ny >= k || nx >= n {
            continue
        }
        // 갈수 없는곳은 패스
        if board[ny][nx] == -1 {
            continue
        }
        // 이미 방문한곳은 패스
        if visited[ny][nx] != -1 {
            continue
        }
        queue.enqueue((ny,nx))
        visited[ny][nx] = visited[curr.0][curr.1] + 1
    }
}
var flag = false
var mm = -100
for i in 0..<k {
    for j in 0..<n {
        mm = mm < visited[i][j] ? visited[i][j] : mm
        if board[i][j] == 0 && visited[i][j] == -1 {
            print(-1)
            flag = true
            break
        }
    }
    if flag {
        break
    }
}

if !flag {
    print(mm)
}
