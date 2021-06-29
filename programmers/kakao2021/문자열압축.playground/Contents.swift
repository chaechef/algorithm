import Foundation

func sliceString(_ str: String, length: Int) -> [String] {
    let counts = Int(ceil(Double(str.count) / Double(length)))
    
    let subStrings = (0..<(counts)).map { num -> String in
        let leftIndex = str.index(str.startIndex, offsetBy: num * length)
        let rightIndex = str.index(leftIndex, offsetBy: length, limitedBy: str.endIndex) ?? str.endIndex
        return String(str[leftIndex..<rightIndex])
    }
    
    return subStrings
}

func compression(_ array: [String]) -> String {
    
    var ret = ""
    var prev = array[0]
    var count = 1
    
    for i in 1..<array.count {
        if array[i] == prev {
            count += 1
        } else {
            ret += count == 1 ? "\(prev)" : "\(count)\(prev)"
            prev = array[i]
            count = 1
        }
        
    }
    ret += count == 1 ? "\(prev)" : "\(count)\(prev)"

    return ret
}

func solution(_ s:String) -> Int {
    let rets = (1...Int(ceil(Double(s.count) / Double(2))))
        .map { n in compression(sliceString(s, length: n))}
        .map { $0.count }
    return rets.min()!
}

solution("a")
