import Foundation

let arr = (0..<7).compactMap { _ -> Int? in
    let x = Int(readLine()!)!
    return x % 2 == 1 ? x : nil
}

print(arr.reduce(0, +))
print(arr.min()!)
