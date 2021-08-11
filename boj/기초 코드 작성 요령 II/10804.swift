import Foundation

var arr = Array(1...20)

for _ in 0..<10 {
    guard let line = readLine() else { continue }
    let toks = line.split(separator: " ").compactMap { Int($0) }
    if toks[0] == toks[1] { continue }

    let target: [Int] = arr[toks[0]-1...toks[1]-1].reversed()
    
    for i in (toks[0]-1)...(toks[1]-1) {
        arr[i] = target[i - toks[0] + 1]
    }
    
}
print(arr.map { String($0) }.joined(separator: " "))