import Foundation

func solution(_ board:[[Int]], _ moves:[Int]) -> Int {
    var trans = (0..<board[0].count).map { i -> [Int] in
        let arr = board
            .map { line in line[i] }
            .filter { $0 != 0}
        return arr
    }
    var ret: [Int] = []
    var count = 0
    for m in moves {
        if let t = trans[m-1].first {
            if let last = ret.last {
                if last == t {
                    count += 2
                    ret.removeLast()
                } else {
                    ret.append(t)
                }
            } else {
                ret.append(t)
            }
            trans[m-1].removeFirst()
        }
        
    }
    return count
}


let b = [[0,0,0,0,0],
         [0,0,1,0,3],
         [0,2,5,0,1],
         [4,2,4,4,2],
         [3,5,1,3,1]]
let m = [1,5,3,5,1,2,1,4]

solution(b, m)
