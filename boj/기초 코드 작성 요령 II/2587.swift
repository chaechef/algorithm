import Foundation

var arr = Array(repeating: 0, count: 5)

for i in 0..<5 {
    arr[i] = Int(readLine()!)!
}

print(arr.reduce(0, +) / 5)
print(arr.sorted()[2])

