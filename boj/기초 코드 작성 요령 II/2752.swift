import Foundation

let line = readLine()!.split(separator: " ").compactMap{ Int($0) }
    .sorted()
    .map { String($0) }
    .joined(separator: " ")

print(line)