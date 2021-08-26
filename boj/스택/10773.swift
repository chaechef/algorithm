import Foundation

class Stack {
    var arr: [Int] = Array(repeating: 0, count: 100000)
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
            let ret = arr[pos]
            arr[pos] = 0
            return ret
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
    let line = Int(readLine()!)!
    switch line {
    case 0:
        let _ = s.pop()
    default:
        s.push(n: line)
    }
}
print(s.arr.reduce(0, +))
