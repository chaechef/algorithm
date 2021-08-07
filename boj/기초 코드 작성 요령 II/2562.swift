import Foundation

let arr = (0..<9).map { _ -> Int in
    let x = Int(readLine()!)!
    return x
}

print(arr.max()!)
print(arr.firstIndex(of: arr.max()!)! + 1)
