import Foundation

class Stack {
    typealias TYPE = (Int,Int)
    var arr: [TYPE] = Array(repeating: (0,0), count: 500000)
    var pos: Int = 0
    static let initValue = (-1,-1)
    func push(n: TYPE) {
        arr[pos] = n
        pos += 1
    }
    
    func pop() -> TYPE {
        if pos == 0 {
            return Stack.initValue
        } else {
            pos -= 1
            let ret = arr[pos]
            arr[pos] = Stack.initValue
            return ret
        }
    }
    
    func size() -> Int {
        return pos
        
    }
    
    func empty() -> Int {
        return pos == 0 ? 1 : 0
    }
    
    func top() -> TYPE {
        if pos == 0 {
            return Stack.initValue
        } else {
            return arr[pos-1]
        }
    }
}

let s = Stack()

let count = Int(readLine()!)!
let arr = readLine()!.split(separator: " ").compactMap { Int($0) }
var ret = Array(repeating: 0, count: count)
s.push(n: (0,arr[0]))

for i in 1..<count {
    if s.top().1 > arr[i] {
        ret[i] = s.top().0 + 1
        s.push(n: (i, arr[i]))
    } else {
        while s.top().1 < arr[i] && s.top().1 != -1 {
            let _ = s.pop()
        }
        if s.top().1 != -1 {
            ret[i] = s.top().0 + 1
        } else {
            ret[i] = 0
        }
        s.push(n: (i, arr[i]))
    }
}

print(ret.map { String($0) }.joined(separator: " "))