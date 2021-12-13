func solution() {
    let toks = readLine()!.split(separator: " ").compactMap({Int($0)})
    let n = toks[0]
    var m = toks[1]
    var coins: [Int] = []
    var ret = 0
    for _ in 0..<n {
        let coin = Int(readLine()!)!
        coins.append(coin)
    }
    
    while m > 0 {
        let candi = coins.filter({$0 <= m}).last!
        let mok = m / candi
        ret += mok
        m -= mok * candi
    }
    
    print(ret)
    
}
solution()