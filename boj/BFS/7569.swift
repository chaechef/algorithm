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

let xyz = readLine()!.splitInt()
let dy = [0,0,1,-1,0,0]
let dx = [1,-1,0,0,0,0]
let dz = [0,0,0,0,1,-1]
let x = xyz[0]
let y = xyz[1]
let z = xyz[2]
var queue = Queue<(Int,Int,Int)>()

var arr = (0..<z).map { _ -> [[Int]] in
    (0..<y).map { _ -> [Int] in
        readLine()!.splitInt()
    }
}
var dst = (0..<z).map { _ -> [[Int]] in
    (0..<y).map { _ -> [Int] in
        Array(repeating: Int.max, count: x)
    }
}

for i in 0..<z {
    for j in 0..<y {
        for k in 0..<x {
            if arr[i][j][k] == 1 {
                queue.enqueue((i,j,k))
                dst[i][j][k] = 0
            }
        }
    }
}

while !queue.isEmpty {
    
    let curr = queue.dequeue()!
    
    for i in 0..<6 {
        let nz = curr.0 + dz[i]
        let ny = curr.1 + dy[i]
        let nx = curr.2 + dx[i]
        if nz < 0 || ny < 0 || nx < 0 || nz >= z || ny >= y || nx >= x {
            continue
        }
        
        if arr[nz][ny][nx] == -1 {
            continue
        }
        
        if dst[nz][ny][nx] > dst[curr.0][curr.1][curr.2] + 1 {
            dst[nz][ny][nx] = dst[curr.0][curr.1][curr.2] + 1
            queue.enqueue((nz,ny,nx))
        }
    }
}

var flag = false
for i in 0..<z {
    if flag {
        break
    }
    for j in 0..<y {
        if flag {
            break
        }
        for k in 0..<x {
            if arr[i][j][k] == 0 && dst[i][j][k] == Int.max {
                print(-1)
                flag = true
                break
            }
        }
    }
}

if !flag {
    var mm = Int.min
    for i in 0..<z {
        for j in 0..<y {
            for k in 0..<x {
                if dst[i][j][k] != Int.max {
                    mm = max(mm, dst[i][j][k])
                }
            }
        }
    }
    if mm == Int.min {
        print(-1)
    } else {
        print(mm)

    }
    
    
}
