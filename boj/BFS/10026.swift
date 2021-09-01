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

func bfs(board: inout [[String]]) -> Int {
    var count = 0
    var queue = Queue<(Int,Int,String)>()
    let dy = [0,0,1,-1]
    let dx = [1,-1,0,0]
    for i in 0..<board.count {
        for j in 0..<board[0].count {
            if board[i][j] == "" {
                continue
            }
            queue.enqueue((i,j,board[i][j]))
            board[i][j] = ""
            count += 1
            
            while !queue.isEmpty {
                let curr = queue.dequeue()!
                for k in 0..<4 {
                    let ny = curr.0 + dy[k]
                    let nx = curr.1 + dx[k]
                    if ny < 0 || nx < 0 || ny >= board.count || nx >= board[0].count {
                        continue
                    }
                    if curr.2 != board[ny][nx] {
                        continue
                    }
                    queue.enqueue((ny,nx, board[ny][nx]))
                    board[ny][nx] = ""
                }
            }
        }
    }
    
    return count
}

func main() {
    let n = Int(readLine()!)!
    var board = (0..<n).map { _ -> [String] in Array(readLine()!).map { String($0) } }
    var board2 = board
    for i in 0..<n {
        for j in 0..<n {
            if board2[i][j] == "G" {
                board2[i][j] = "R"
            }
        }
    }
    
    print(bfs(board: &board), terminator: " ")
    print(bfs(board: &board2))
}

main()
