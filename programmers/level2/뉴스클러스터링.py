import re
import math

def solution(str1, str2):
    str1 = [str1[i:i+2].lower() for i in range(len(str1)-1) if not re.findall('[^a-zA-Z]+',str1[i:i+2])]
    str2 = [str2[i:i+2].lower() for i in range(len(str2)-1) if not re.findall('[^a-zA-Z]+',str2[i:i+2])]
    hap = set(str1) | set(str2)
    gyo = set(str1) & set(str2)

    if len(hap) == 0:
        return 65536
    gyosum = sum([min(str1.count(gy), str2.count(gy)) for gy in gyo])
    hapsum = sum([max(str1.count(ha), str2.count(ha)) for ha in hap])
    return math.floor((gyosum / hapsum) * 65536)


print(solution('FRANCE', 'french'))
print(solution('handshake', 'shake hands'))
print(solution('aa1+aa2', 'AAAA12'))
print(solution('E=M*C^2', 'e=m*c^2'))