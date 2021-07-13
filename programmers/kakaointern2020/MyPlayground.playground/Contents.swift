
import Foundation

func permuteWirth<T>(_ a: [T], _ n: Int) -> [[T]] {
    if n == 0 {
        return [a]
    }
    var a = a
    var ret = permuteWirth(a, n - 1)
    for i in 0..<n {
        a.swapAt(i, n)
        ret += permuteWirth(a, n - 1)
        a.swapAt(i, n)
    }
    return ret
}

func calcOne(nums: [Int64], opers: String, prior: [String:Int]) -> Int64 {
    if nums.count == 1 {
        return nums[0]
    }
    let operToString = opers.compactMap { prior[String($0)] }
    let maxNum = operToString.max()!
    let firstIdx = operToString.firstIndex(of: maxNum)!
    let o = opers[opers.index(opers.startIndex, offsetBy: firstIdx)]
    let a = nums[firstIdx]
    let b = nums[firstIdx + 1]
    var c: Int64  = 0
    switch o {
    case "+":
        c = a + b
    case "-":
        c = a - b
    case "*":
        c = a * b
    default:
        print("error")
    }
    var newNums = nums[..<Int(firstIdx)] + [c] + nums[Int(firstIdx+2)...]
    var newOpers = opers
    newOpers.remove(at: newOpers.index(newOpers.startIndex, offsetBy: firstIdx))
    let newNumsI = newNums.compactMap { Int64($0) }
    return calcOne(nums: newNumsI, opers: newOpers, prior: prior)
}

func solution(_ expression:String) -> Int64 {

    let oper = ["+", "-", "*"]
    var prior = ["+": 0, "-": 0, "*": 0]
    var ret: [Int64] = []
    for line in permuteWirth(oper, 2) {
        let a = oper.compactMap { line.firstIndex(of: $0) }
        prior["+"] = a[0]
        prior["-"] = a[1]
        prior["*"] = a[2]
        let toks = expression.components(separatedBy: ["+","-","*"])
            .compactMap { Int64($0) }
        let operArray = expression.filter { "-+*".contains($0) }
        ret.append(calcOne(nums: toks, opers: operArray, prior: prior))
    }

    let abs = ret.map { $0 < 0 ? -$0 : $0 }
    return abs.max()!
}

print(solution("100-200*300-500+20"))
