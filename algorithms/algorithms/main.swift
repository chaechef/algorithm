//
//  main.swift
//  algorithms
//
//  Created by 채훈기 on 2021/04/30.
//

import Foundation



extension String {
    subscript(index: Int) -> Character? {
        if index < 0 || index >= self.count {
            return nil
        }
        let charIdx = self.index(self.startIndex, offsetBy: index)
        
        return self[charIdx]
    }
    
    subscript(range: Range<Int>) -> String? {
        if range.lowerBound < 0 || range.upperBound >= self.count {
            return nil
        }
        
        let sIdx = self.index(startIndex, offsetBy: range.lowerBound)
        let eIdx = self.index(startIndex, offsetBy: range.upperBound)
        return String(self[sIdx..<eIdx])
    }

}
