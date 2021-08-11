

import Foundation

let num = Int(readLine()!)!
if num == 1 {
    print("**")
} else {
    for i in (1...num) + (1...(num - 1)).reversed(){
        let str =
            String(repeating: "*", count: i) +
            String(repeating: " ", count: 2 * (num - i)) +
            String(repeating: "*", count: i)
        print(str)
    }

}