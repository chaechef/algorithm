import Foundation

func combination(_ str: String, len: Int) -> [String] {
    if str.count < len {
        return []
    }
    
    if len == 1 {
        return str.map { String($0) }
    }
    
    guard let first = str.first else { return []}
    let newString = String(str.dropFirst())
    let c = String(first)
    
    return combination(newString, len: len)
        + combination(newString, len: len - 1).map { c + $0 }
}

func solution(_ orders:[String], _ course:[Int]) -> [String] {
    
    let ret = course.map { num -> [String] in
        let counts1 = orders
            .map { combination($0, len: num) }
            .flatMap { $0 }
            .reduce(into: [:], { counts, word in
                counts[word, default: 0] += 1
            })
        print(counts1)
        let counts = orders
            .map { combination($0, len: num) }
            .flatMap { $0 }
            .map { $0.sorted().map{ String($0) }.joined() }
            .reduce(into: [:], { counts, word in
                counts[word, default: 0] += 1
            })
        guard let max = counts.values.max(), max >= 2
        else { return [] }
        let keys = counts.filter { $0.value == max }
            .map { $0.key }
        return keys
    }

    return ret.joined().sorted()
}

let a = solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5])
print(a)

