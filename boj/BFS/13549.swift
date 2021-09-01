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

var queue = Queue<Int>()
var arr = Array(repeating: -1, count: 200001)

queue.enqueue(n)
arr[n] = 0

while !queue.isEmpty {
    let curr = queue.dequeue()!
    if curr == k {
        print(arr[curr])
        break
    }
    if 2 * curr < 200001 && (arr[2 * curr] == -1 || arr[2 * curr] > arr[curr] ) {
        arr[2 * curr] = arr[curr]
        queue.enqueue(curr * 2)
    }
    
    if curr + 1 < 200001 && (arr[curr + 1] == -1 || arr[curr + 1] > arr[curr] + 1) {
        arr[curr + 1] = arr[curr] + 1
        queue.enqueue(curr + 1)
    }
    if curr - 1 >= 0 && (arr[curr - 1] == -1 || arr[curr - 1] > arr[curr] + 1){
        arr[curr - 1] = arr[curr] + 1
        queue.enqueue(curr - 1)

    }

}
