func solution() {
    let n = Int(readLine()!)!
    var ret = 0
    var sum = 0
    var i = 1
    while true {
        let temp = sum + i
        if temp > n {
            break
        } else {
            sum = temp
            i += 1
            ret += 1
        }
    }
    print(ret)
    
}

solution()