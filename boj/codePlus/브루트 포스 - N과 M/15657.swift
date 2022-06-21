import Foundation

let toks = (readLine() ?? "").split(separator: " ").compactMap { Int($0) }
let n = toks[0]
let m = toks[1]
var arr = (readLine() ?? "").split(separator: " ").compactMap { Int($0) }.sorted(by: <)

func recursion(pool: [Int], selected: [Int], cindex: Int, maxCount: Int) {
    if cindex == pool.count {
        return
    }
    if selected.count == maxCount {
        print(selected)
        return
    }
    
    for i in cindex..<pool.count {
        let pick = pool[i]
        recursion(pool: pool, selected: selected + [pick], cindex: i, maxCount: maxCount)
    }
 
}

recursion(pool: arr, selected: [], cindex: 0, maxCount: m)
