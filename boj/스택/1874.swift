import Foundation

class Stack {
    var arr: [Int] = Array(repeating: 0, count: 100001)
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
let container = Stack()
let arr = (0..<Int(readLine()!)!).map { _ in return Int(readLine()!)! }

Array(1...arr.count).reversed().forEach {
    container.push(n: $0)
}
var oper: [String] = []
var flag = true
for a in arr {
    // 4
    //[3, 2, 1], top: [4,5,6,7], bottom
    if a >= container.top() && container.top() != -1 {
        while container.top() != a && container.top() != -1 {
            s.push(n: container.pop())
            oper.append("+")
        }
        container.pop()
        oper.append("+")
        oper.append("-")
    } else {
        if s.top() == a {
            s.pop()
            oper.append("-")
        } else {
            print("NO")
            flag = false
            break
        }
    }
}

if flag {
    print(oper.joined(separator: "\n"))

}
