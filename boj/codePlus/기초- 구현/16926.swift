import Foundation

func readNumbers() -> [Int] {
    return (readLine() ?? "").split(separator: " ").compactMap { Int($0) }
}

let toks = readNumbers()
let n = toks[0]
let m = toks[1]
let r = toks[2]
var board = (0..<n).map { _ -> [Int] in readNumbers() }

for i in 0..<(min(n,m) / 2) {
    // 껍질 순서 겉껍질 -> 속껍질
    let minX = i
    let minY = i
    let maxX = m - i - 1
    let maxY = n - i - 1
    var tempArr: [Int] = []
    var mapping: [(Int,Int)] = []
    
    for j in minX...maxX {
        mapping.append((minY,j))
        tempArr.append(board[minY][j])
    }
    for j in (minY+1)...maxY {
        mapping.append((j,maxX))
        tempArr.append(board[j][maxX])
    }
    
    for j in (minX...(maxX-1)).reversed() {
        mapping.append((maxY, j))
        tempArr.append(board[maxY][j])
    }
    
    for j in ((minY)...(maxY-1)).reversed() {
        if j == minY { continue }
        mapping.append((j,minX))
        tempArr.append(board[j][minX])
    }
    let rotateCount = r % tempArr.count
    let a1 = tempArr[0..<rotateCount]
    let a2 = tempArr[rotateCount..<tempArr.count]
    let rotatedArray = Array(a2 + a1)
    for j in 0..<mapping.count {
        let y = mapping[j].0
        let x = mapping[j].1
        board[y][x] = rotatedArray[j]
    }
}
board.forEach {
    print($0.map { String($0 )}.joined(separator: " "))
}
