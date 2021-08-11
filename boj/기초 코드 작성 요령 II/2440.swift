
import Foundation

let num = Int(readLine()!)!

for i in (1...num).reversed() {
    print(String(repeating: "*", count: i))
}
