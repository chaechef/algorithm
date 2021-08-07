import Foundation

var arr = readLine()!.split(separator: " ").map { Int($0)!}
    .sorted()

switch (arr[0], arr[1], arr[2]) {
case let x where x.0 == x.1 && x.1 == x.2:
    print(10000 + x.0 * 1000)
case let x where x.0 == x.1:
    print(1000 + x.0 * 100)
case let x where x.1 == x.2:
    print(1000 + x.1 * 100)
default:
    print(arr[2] * 100)
}