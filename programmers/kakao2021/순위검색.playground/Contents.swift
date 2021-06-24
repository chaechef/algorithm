import Foundation

struct Applicant {
    let language: String
    let position: String
    let career: String
    let food: String
    let score: Int
}

func solution(_ info:[String], _ query:[String]) -> [Int] {
    let applicants = info.map { line -> Applicant in
        let toks = line.split(separator: " ").map { String($0) }
        return Applicant(language: toks[0], position: toks[1],
                         career: toks[2], food: toks[3], score: Int(toks[4])!)
    }
    
    let conditions = query.map { q -> Applicant in
        let a = q.components(separatedBy: " and ").map { String($0) }
        let toks = a[3].split(separator: " ")
        let food = String(toks[0])
        let score = Int(toks[1])!
        return Applicant(language: a[0], position: a[1], career: a[2], food: food, score: score)
    }
    let ret = conditions.map { con -> Int in
        applicants.filter { a in
            (a.language == con.language || con.language == "-") &&
                (a.position == con.position || con.position == "-") &&
                (a.career == con.career || con.career == "-") &&
                (a.food == con.food || con.food == "-") &&
                (a.score >= con.score)
        }.count
    }
    return ret
}


let info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]

let query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

let a = solution(info, query)
print(a)
