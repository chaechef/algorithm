import Foundation

let line = readLine()!
let toks = line
    .split(separator: " ")
    .compactMap { Int($0)}
print(toks[0] + toks[1])