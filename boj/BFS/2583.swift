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

func main() {
    let mnk = readLine()!.splitInt()
    var arr = Array(repeating: Array(repeating: 0, count: mnk[1]), count: mnk[0])
    let dy = [0,0,1,-1]
    let dx = [1,-1,0,0]
    
    for _ in 0..<mnk[2] {
        let l = readLine()!.splitInt()
        for i in l[1]..<l[3] {
            for j in l[0]..<l[2] {
                arr[i][j] = 1
            }
        }
    }
    
    var count = 0
    var ret: [Int] = []
    
    for i in 0..<mnk[0] {
        for j in 0..<mnk[1] {
            if arr[i][j] != 0 {
                continue
            }
            count += 1
            var w = 0
            var queue = Queue<(Int,Int)>()
            arr[i][j] = 1
            queue.enqueue((i,j))
            while !queue.isEmpty {
                let curr = queue.dequeue()!
                w += 1
                for k in 0..<4 {
                    let ny = curr.0 + dy[k]
                    let nx = curr.1 + dx[k]
                    
                    if ny < 0 || nx < 0 || ny >= mnk[0] || nx >= mnk[1] {
                        continue
                    }
                    if arr[ny][nx] == 1 {
                        continue
                    }
                    
                    arr[ny][nx] = 1
                    queue.enqueue((ny,nx))
                }
            }
            
            ret.append(w)
            
        }
    }
    print(count)
    print(ret.sorted().map { String($0) }.joined(separator: " "))
}

main()
