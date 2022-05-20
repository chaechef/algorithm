import Foundation

let n = Int(readLine() ?? "") ?? 0
let measures = (readLine() ?? "")
    .split(separator: " ")
    .compactMap{ Int($0) }
    .sorted(by: <)

if let first = measures.first, let last = measures.last {
    print(first * last)
}

