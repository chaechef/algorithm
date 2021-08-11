
import Foundation

let arr = readLine()!
    .split(separator: " ")
    .compactMap { Int64($0) }
    .sorted()

if arr[0] == arr[1] {
    print(0)
} else {
    print(arr[1] - arr[0] - 1 )
    for i in ((arr[0]+1)..<arr[1]) {
        print(i, terminator: " ")
    }
    print()
}

