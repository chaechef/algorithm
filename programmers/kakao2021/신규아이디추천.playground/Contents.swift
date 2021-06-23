import Foundation



func lowerCase(_ id: String) -> String {
    return id.lowercased()
}

func removeSpecialCharacter(_ id: String) -> String {
    let condition: (Character) -> Bool = { c in
        if (c >= "a" && c <= "z") ||
            ("0" <= c && "9" >= c) ||
            "-_.".contains(c) {
            return true
        }
        return false
    }
    return id.filter(condition)
}

func recursiveReplacingDoubleDotToSingleDot(_ id: String) -> String {
    if replaceDoubleDotToSingleDot(id) == id {
        return id
    } else {
        let r = replaceDoubleDotToSingleDot(id)
        return recursiveReplacingDoubleDotToSingleDot(r)
    }
}
func replaceDoubleDotToSingleDot(_ id: String) -> String {
    return id.replacingOccurrences(of: "..", with: ".")
}

func trimDot(_ id: String) -> String {
    return id.trimmingCharacters(in: .init(charactersIn: "."))
}

func replaceEmptyToA(_ id: String) -> String {
    if id == "" {
        return "a"
    }
    return id
}

func checkIdLength(_ id: String) -> String {
    if id.count >= 16 {
        let newId = id[id.startIndex..<id.index(id.startIndex, offsetBy: 15)]
        return trimDot(String(newId))
    }
    return id
}

func recursiveAppendCharacter(_ id: String) -> String {
    if id.count < 3 {
        let newId = id + String(id[id.index(id.endIndex, offsetBy: -1)])
        return recursiveAppendCharacter(newId)
    }
    return id
}

/* 요구사항
 아이디의 길이는 3자 이상 15자 이하여야 합니다.
 아이디는 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.) 문자만 사용할 수 있습니다.
 단, 마침표(.)는 처음과 끝에 사용할 수 없으며 또한 연속으로 사용할 수 없습니다.
 
 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
      만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
 

 */


func solution(_ new_id: String) -> String {
    let newID = new_id
        .lowercased()
        .replacingOccurrences(of: #"[^\w.-]"#, with: "", options: .regularExpression)
        .replacingOccurrences(of: #"\.{2,}"#, with: ".", options: .regularExpression)
        .trimmingCharacters(in: CharacterSet(charactersIn: "."))
        .modifier { $0.isEmpty ? "a" : $0 }
        .modifier { $0.count >= 16 ?
            String($0[..<$0.index($0.startIndex, offsetBy: 15)]) : $0}
        .trimmingCharacters(in: CharacterSet(charactersIn: "."))
        .modifier {
            $0.count <= 2 ? $0.padding(toLength: 3, withPad: String($0.last!), startingAt: 0) : $0
        }
    
    return newID
}

extension String {
    func modifier(_ code: (String) -> String) -> String {
        return code(self)
    }
}

//print(solution("abcdefghijklmn.p"))


let string = "HELLO world01"
print(string.replacingOccurrences(of: "world", with: "swift"))

