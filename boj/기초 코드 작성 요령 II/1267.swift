
import Foundation

let num = Int(readLine()!)!
let arr = readLine()!.split(separator: " ")
    .compactMap { Int($0) }

let feeRule1 = arr.map { time -> Int in
    let ceil = ceil(Double(time) / Double(30))
    let mod = time % 30
    return Int((ceil + ( mod == 0 ? 1 : 0)) * 10)
}.reduce(0, +)

let feeRule2 = arr.map { time -> Int in
    let ceil = ceil(Double(time) / Double(60))
    let mod = time % 60
    return Int((ceil + ( mod == 0 ? 1 : 0)) * 15)
}.reduce(0, +)

switch (feeRule1, feeRule2) {
case let fee where feeRule1 > feeRule2:
    print("M", fee.1)
case let fee where feeRule1 < feeRule2:
    print("Y", fee.0)
default:
    print("Y M", feeRule2)
}

