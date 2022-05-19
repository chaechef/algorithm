
import Foundation

func getNumberOfDigit(num: Int) -> Int {
    var dividend = 1
    var count = 1
    while true {
        if dividend % num == 0 {
            return count
        }
        dividend = ((dividend * 10) % num + 1 % num) % num
        count += 1
    }
}

while let input = Int(readLine() ?? "") {
    print(getNumberOfDigit(num: input))
}