import Foundation

let num = Int(readLine()!)!

let ret = num % 400 == 0 || (num % 4 == 0 && num % 100 != 0) ? 1 : 0

print(ret)
