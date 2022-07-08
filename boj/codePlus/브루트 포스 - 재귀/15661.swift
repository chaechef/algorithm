import Foundation

let N: Int = readLine().map { Int($0) ?? 0 } ?? 0
let board: [[Int]] = (0..<N).map { _ in
    let line = readLine()?.split(separator: " ") ?? []
    return line.map { Int($0) ?? 0 }
}
let minPlayerCount = 1
let maxPlayerCount = Int(N / 2)
var ret: Int = .max

func combination(index: Int, topick: Int, picked: [Int]) -> [[Int]] {
    if topick == 0 {
        return [picked]
    }
    var ret: [[Int]] = []
    for i in index..<N {
        let r = combination(index: i + 1, topick: topick - 1, picked: picked + [i])
        ret += r
    }
    return ret
}

func teamAbility(_ team: [Int]) -> Int {
    let count = team.count
    var ability = 0
    for i in 0..<count {
        for j in 0..<count {
            if i == j { continue }
            let p1 = team[i]
            let p2 = team[j]
            ability += board[p1][p2]
        }
    }
    return ability
}

for curr in minPlayerCount...maxPlayerCount {
    let pool = Set(0..<N)
    let r = combination(index: 0, topick: curr, picked: [])
    for leftTeam in r {
        let rightTeam: [Int] = Array(pool.subtracting(Set(leftTeam)))
        let lability = teamAbility(leftTeam)
        let rability = teamAbility(rightTeam)
        let diff = abs(lability - rability)
        ret = min(ret, diff)
    }
}
print(ret)
