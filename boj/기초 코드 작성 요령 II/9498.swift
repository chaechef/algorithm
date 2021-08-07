import Foundation

let num = Int(readLine()!)!


switch num {
case let x where (90...100) ~= x:
    print("A")
case let x where (80...89) ~= x:
    print("B")
case let x where (70...79) ~= x:
    print("C")
case let x where (60...69) ~= x:
    print("D")
default:
    print("F")
}