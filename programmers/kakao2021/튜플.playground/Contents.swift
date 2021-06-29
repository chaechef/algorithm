import Foundation

func solution(_ s:String) -> [Int] {
    let trimed = s.dropLast().dropFirst()
    let toks = trimed.components(separatedBy: ",{")
    let array = toks.map { tok -> [Int] in
        let t = tok.trimmingCharacters(in: CharacterSet(charactersIn: "{}") )
        return t.split(separator: ",").map { Int($0)! } }
        .sorted { $0.count < $1.count }
    var ret = [array[0][0]]
    for i in 1..<array.count {
        let prev = Set(array[i-1])
        let curr = Set(array[i])
        ret.append(contentsOf: curr.subtracting(prev))
    }
    return ret
}

let str = "{{2},{2,1},{2,1,3},{2,1,3,4}}"

solution(str)
