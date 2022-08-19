import Foundation

let tc = Int(readLine() ?? "") ?? 0
var arr = Array(repeating: 0, count: 1000001)
arr[1] = 1
arr[2] = 2
arr[3] = 4

for i in 4..<arr.count {
    arr[i] = (arr[i-1] + arr[i-2] + arr[i-3]) % 1000000009
}

for _ in 0..<tc {
    let num = Int(readLine() ?? "") ?? 0
    print(arr[num])
}

