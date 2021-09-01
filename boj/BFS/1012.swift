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

let tc = Int(readLine()!)!
let dy = [0,0,1,-1]
let dx = [1,-1,0,0]

for _ in 0..<tc {
    let mnk = readLine()!.splitInt()
    var queue = Queue<(Int,Int)>()
    let m = mnk[0]
    let n = mnk[1]
    let k = mnk[2]
    var arr = Array(repeating: Array(repeating: 0, count: m), count: n)
    var count = 0
    for _ in 0..<k {
        let coor = readLine()!.splitInt()
        arr[coor[1]][coor[0]] = 1
    }
    
    for i in 0..<n {
        for j in 0..<m {
            if arr[i][j] == 1 {
                count += 1
                arr[i][j] = 0
                queue.enqueue((i,j))
                while !queue.isEmpty {
                    let curr = queue.dequeue()!
                    for i in 0..<4 {
                        let ny = curr.0 + dy[i]
                        let nx = curr.1 + dx[i]
                        
                        if ny < 0 || nx < 0 || ny >= n || nx >= m {
                            continue
                        }
                        
                        if arr[ny][nx] == 0 {
                            continue
                        }
                        arr[ny][nx] = 0
                        queue.enqueue((ny,nx))
                    }
                }
                
            }
        }
    }
    
    print(count)
    
}
