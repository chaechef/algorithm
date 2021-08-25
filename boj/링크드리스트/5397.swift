import Foundation

// class Node {
//     let char: Character
//     var next: Node?
//     var prev: Node?
    
//     init(_ c: Character) {
//         self.char = c
//     }
// }

//class KeyLogger {
//
//    let head: Node
//    var curr: Node
//
//    init() {
//        head = Node(Character("?"))
//        curr = head
//    }
//
//    func moveLeft() {
//        if let left = curr.prev {
//            curr = left
//        }
//    }
//
//    func moveRight() {
//        if let right = curr.next {
//            curr = right
//        }
//    }
//
//    func input(_ c: Character) {
//        // head|A|B|C|D|
//        let newNode = Node(c)
//        newNode.next = curr.next
//        curr.next?.prev = newNode
//        newNode.prev = curr
//        curr.next = newNode
//        curr = newNode
//
//    }
//    func delete() {
//        if curr.char == Character("?") {
//            return
//        }
//        curr.prev?.next = curr.next
//        curr.next?.prev = curr.prev
//        curr = curr.prev!
//    }
//
//    func traval() {
//        var cursor = head.next
//        while let c = cursor {
//            print(c.char, terminator: "")
//            cursor = c.next
//        }
//        print()
//    }
//}

class KeyLogger {
    
    var left: [Character]
    var right: [Character]
    
    init() {
        left = []
        right = []
    }
    
    func moveLeft() {
        if let last = left.last {
            right.append(last)
            left.removeLast()
        }
    }
    
    func moveRight() {
        if let last = right.last {
            left.append(last)
            right.removeLast()
        }
    }
    
    func input(_ c: Character) {
        left.append(c)
    }
    func delete() {
        if left.last != nil {
            left.removeLast()
        }
    }
    
    func traval() {
        print(String(left + right.reversed()))
    }
}

for _ in 0..<Int(readLine()!)! {
    let stream = readLine()!
    let logger = KeyLogger()
    for c in stream {
        switch c {
        case "<":
            logger.moveLeft()
        case ">":
            logger.moveRight()
        case "-":
            logger.delete()
        default:
            logger.input(c)
        }
    }
    logger.traval()
    
}
