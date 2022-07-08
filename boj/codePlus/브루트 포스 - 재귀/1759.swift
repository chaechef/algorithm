import Foundation

let line1 = (readLine() ?? "").split(separator: " ").compactMap { Int($0) }
let L = line1[0]
let C = line1[1]
let chars = (readLine() ?? "").split(separator: " ").compactMap { String($0) }
let vowel = ["a", "e", "i", "o", "u"]
let vchars = chars.filter(vowel.contains(_:))
let cchars = chars.filter { !vowel.contains($0) }
var ret: [String] = []
func combination(index: Int, topick: Int, picked: [String], arr: [String]) -> [[String]] {
    if topick == 0 {
        return [picked]
    }
    var ret: [[String]] = []
    for i in index..<arr.count {
        ret += combination(index: i+1, topick: topick - 1, picked: picked + [arr[i]], arr: arr)
    }
    return ret
}

for vcount in 1...vchars.count {
    let ccount = L - vcount
    if ccount < 2 { continue }
    let vpicked = combination(index: 0, topick: vcount, picked: [], arr: vchars)
    let cpicked = combination(index: 0, topick: ccount, picked: [], arr: cchars)
    for v in vpicked {
        for c in cpicked {
            ret += [(v + c).sorted(by: <).joined(separator: "")]
        }
    }
}

print(ret.sorted(by: <).joined(separator: "\n"))
