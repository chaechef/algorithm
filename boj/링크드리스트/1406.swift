import Foundation


class Node {
    let char: String
    var next: Node?
    var prev: Node?
    
    init(char: String, next: Node? = nil, prev: Node? = nil) {
        self.char = char
        self.next = next
        self.prev = prev
    }
}

class Editor {
    // (h)ABCDE
    let head = Node(char: "head")
    var curr: Node
    
    init() {
        curr = head
    }
    
    func leftCursor() {
        if let left = curr.prev {
            curr = left
        }
    }
    
    func rightCursor() {
        if let right = curr.next {
            curr = right
        }
    }
    
    func insert(new: Node) {
        // | A| B| C| D|
        // prev curr| next
        new.next = curr.next
        new.prev = curr
        if let next = curr.next {
            next.prev = new
        }
        curr.next = new
        curr = new
    }
    
    func delete() {
        // | A| B| C| D|
        // prev curr| next
        if let left = curr.prev {
            left.next = curr.next
            curr.next?.prev = left
            curr = left
        } else {
            
        }
    }
    
    func traval() {
        var cursor: Node? = head.next
        while let c = cursor {
            print(c.char, terminator: "")
            cursor = cursor?.next
        }
        print()
    }
}

let initString = Array(readLine()!)
let operCount = Int(readLine()!)!

var head = Node(char: "")
var curr = head
let editor = Editor()
for c in initString {
    let newNode = Node(char: String(c))
    editor.insert(new: newNode)
}


for _ in 0..<operCount {
    let line = readLine()!
    
    switch line.first! {
    case "L":
        editor.leftCursor()
    case "D":
        editor.rightCursor()
    case "B":
        editor.delete()
    default:
        let p = String(line.last!)
        let newNode = Node(char: p)
        editor.insert(new: newNode)
    }

}

editor.traval()
