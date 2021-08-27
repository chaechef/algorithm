
public struct RingBuffer {
    fileprivate var array: [Int?]
    fileprivate var frontIndex = 0
    fileprivate var rearIndex = 0
    
    public init(count: Int) {
        array = Array((1...count))
        array.append(0)
        rearIndex = count
    }
    
    public mutating func enqueue(_ element: Int) -> Bool {
        if !isFull {
            array[rearIndex % array.count] = element
            rearIndex += 1
            return true
        } else {
            return false
        }
    }
    
    public mutating func dequeue() -> Int? {
        if !isEmpty {
            let element = array[frontIndex % array.count]
            array[frontIndex % array.count] = nil
            frontIndex += 1
            return element
        } else {
            return nil
        }
    }
    fileprivate var availableSpaceForDequeue:Int {
        return rearIndex - frontIndex
    }
    public var isEmpty:Bool {
        return availableSpaceForDequeue == 0
    }
    fileprivate var availableSpaceForEnqueue: Int {
        return array.count - availableSpaceForDequeue
    }
    public var isFull:Bool {
        return availableSpaceForEnqueue == 0
    }
}

var s = RingBuffer(count: Int(readLine()!)!)

while !s.isEmpty {
    if s.rearIndex - s.frontIndex == 1 {
        print(s.dequeue()!)
    }
    s.dequeue()
    if let ele = s.dequeue() {
        s.enqueue(ele)
    } else {
        break
    }

}
