
from collections import deque

def gale_shapley(n: int, hospital_pref: dict[int, list[int]], student_pref: dict[int, list[int]]) -> dict[int, int]:
    hospital_match = {i: 0 for i in range(1, n + 1)}
    student_match = {i: 0 for i in range(1, n + 1)}

    unmatched = deque(list(hospital_match.keys()))
    while unmatched:
        h = unmatched[0]
        a = hospital_pref[h][0]
        
        if student_match[a] == 0:
            hospital_match[h] = a
            student_match[a] = h
            unmatched.popleft()
        else:
            h_prime = student_match[a]

            prefs = list(student_pref[a])
            idx_h = prefs.index(h)
            idx_h_prime = prefs.index(h_prime)

            if (idx_h < idx_h_prime):
                unmatched.popleft()
                hospital_match[h_prime] = 0
                unmatched.append(h_prime)
                student_match[a] = h
                hospital_match[h] = a
                
            else:
                continue
                
                
    print(hospital_match)
