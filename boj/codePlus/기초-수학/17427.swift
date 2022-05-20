
import Foundation


let n = Int(readLine() ?? "") ?? 1
let ret = (1...n).map { num -> Int in
    var mul = 1
    var sum = 0
    while num * mul <= n {
        sum += num
        mul += 1
    }
    return sum
}
print(ret.reduce(0, +))
