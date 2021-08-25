import Foundation

class Node {
    let num: Int
    var prev: Node?
    var next: Node?
    
    init(n: Int) {
        self.num = n
    }
}

let toks = readLine()!
    .split(separator: " ")
    .compactMap{ Int($0) }
let k = toks[1]
var list = Array(1...toks[0]).map { Node(n: $0) }

if toks[0] == 1 {
    print("<1>")
} else {
    list[0].next = list[1]
    list[0].prev = list[toks[0]-1]
    list[toks[0]-1].prev = list[toks[0]-2]
    list[toks[0]-1].next = list[0]

    for i in 1..<toks[0]-1 {
        list[i].next = list[i+1]
        list[i].prev = list[i-1]
    }

    var permu: [Int] = []
    var n = toks[0]
    var head: Node? = list[0]
    while n != 0 {
        for _ in 0..<k-1 {
            head = head?.next
        }
        permu.append(head!.num)
        head?.prev?.next = head?.next
        head?.next?.prev = head?.prev
        head = head?.next
        n -= 1
    }

    print("<"+permu.map { String($0) }.joined(separator: ", ")+">")
}



