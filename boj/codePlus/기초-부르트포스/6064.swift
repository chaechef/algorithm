
import Foundation

let tc = Int(readLine() ?? "") ?? 0
(0..<tc).forEach { _ in
    let toks = (readLine() ?? "").split(separator: " ").compactMap { Int($0) }
    let m = toks[0]
    let n = toks[1]
    let x = toks[2]
    let y = toks[3]
    var count = x
    let mod = x % n
    var cy = mod == 0 ? n : mod // x만큼 가야하는데 한계는 n임 mod 연산이 필요한데 세부 수치 조절해야함
    while true {
        if cy == y {
            print(count)
            return
        }
        if count > n * m {
            print(-1)
            return
        }
        let tmod = (cy + m) % n
        cy = tmod == 0 ? n : tmod
        count += m
    }
}
