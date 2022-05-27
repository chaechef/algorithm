import Foundation

let n = Int(readLine() ?? "") ?? 0
var board = (0..<n).map { _ in
    return Array(readLine() ?? "")
}
var isItRange: (Int,Int) -> Bool = { y, x -> Bool in
    if y < 0 || y >= n || x < 0 || x >= n {
        return false
    }
    return true
}
var transpose: ([[Character]]) -> [[Character]] = { board in
    let col = board.count
    let row = board[0].count
    var ret: [[Character]] = Array(repeating: Array(repeating: Character("a"), count: col), count: row)
    for i in 0..<board.count {
        for j in 0..<board.count {
            ret[i][j] = board[j][i]
        }
    }
    return ret
}
func calcMaxContinuousValue(board: [[Character]]) -> Int {
    let len = board.count
    var ret = 1
    for i in 0..<len {
        var continueNum = 1
        var currValue = board[i][0]
        for j in 1..<len {
            if currValue == board[i][j] {
                continueNum += 1
            } else {
                ret = max(ret, continueNum)
                currValue = board[i][j]
                continueNum = 1
            }
        }
        ret = max(ret, continueNum)
    }
    
    return ret
}
var ret = 0
for i in 0..<n {
    for j in 0..<n {
        if isItRange(i + 1, j) && board[i][j] != board[i+1][j] {
            var tempBoard = board
            let temp = tempBoard[i][j]
            tempBoard[i][j] = tempBoard[i+1][j]
            tempBoard[i+1][j] = temp
            ret = max(ret, calcMaxContinuousValue(board: tempBoard))
            ret = max(ret, calcMaxContinuousValue(board: transpose(tempBoard)))
        }
        if isItRange(i, j + 1) && board[i][j] != board[i][j+1] {
            var tempBoard = board
            let temp = tempBoard[i][j]
            tempBoard[i][j] = tempBoard[i][j+1]
            tempBoard[i][j+1] = temp
            ret = max(ret, calcMaxContinuousValue(board: tempBoard))
            ret = max(ret, calcMaxContinuousValue(board: transpose(tempBoard)))
        }
    }
}
print(ret)