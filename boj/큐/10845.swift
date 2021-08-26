
import Foundation

class Queue {
    
    var arr: [Int] = Array(repeating: -100000, count: 100001)
    var head = 0
    var tail = 0
    
    func push(n: Int) {
        // [] [] [] []
        arr[head] = n
        head += 1
    }
    
    func pop() -> Int? {
        if tail == head {
            return nil
        }
        let ret = arr[tail]
        tail += 1
        return ret

    }
    
    func size() -> Int {
        return head - tail
    }
    
    func empty() -> Int {
        return size() == 0 ? 1 : 0
    }
    
    func front() -> Int? {
        if head > tail {
            return arr[tail]
        } else {
            return nil
        }
    }
    
    func back() -> Int? {
        if head > tail {
            return arr[head - 1]
        } else {
            return nil
        }
    }
}

let s = Queue()

for _ in 0..<Int(readLine()!)! {
    let line = readLine()!
    let op = String(Array(line)[0..<2])
    
    switch op {
    case "pu":
        let toks = line.split(separator: " ")
        s.push(n: Int(toks[1])!)
    case "po":
        print(s.pop() ?? -1)
    case "si":
        print(s.size())
    case "em":
        print(s.empty())
    case "fr":
        print(s.front() ?? -1)
    case "ba":
        print(s.back() ?? -1)
    default:
        print()
    }
}
