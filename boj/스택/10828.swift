import Foundation

class Stack {
    var arr: [Int] = Array(repeating: 0, count: 20000)
    var pos: Int = 0
    
    func push(n: Int) {
        arr[pos] = n
        pos += 1
    }
    
    func pop() -> Int {
        if pos == 0 {
            return -1
        } else {
            pos -= 1
            return arr[pos]
        }
    }
    
    func size() -> Int {
        return pos
        
    }
    
    func empty() -> Int {
        return pos == 0 ? 1 : 0
    }
    
    func top() -> Int {
        if pos == 0 {
            return -1
        } else {
            return arr[pos-1]
        }
    }
}

let s = Stack()
for _ in 0..<Int(readLine()!)! {
    let line = readLine()!
    let oper = String(Array(line)[0..<2])
    
    switch oper {
    case "pu":
        let toks = line.split(separator: " ")
        s.push(n: Int(toks[1])!)
    case "to":
        print(s.top())
    case "si":
        print(s.size())
    case "em":
        print(s.empty())
    case "po":
        print(s.pop())
    default:
        print("")
    }
}
