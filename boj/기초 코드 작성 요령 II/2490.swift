
import Foundation

for _ in 0..<3 {
    let sum = readLine()!.split(separator: " ").map { Int($0)!}
        .reduce(0, +)

    switch sum {
    case 0:
        print("D")
    case 1:
        print("C")
    case 2:
        print("B")
    case 3:
        print("A")
    case 4:
        print("E")
    default:
        print("x")
    }
}
