
from collections import deque

from src.verify.verifier import check_stability
import time 

def gale_shapley(n: int, hospital_pref: dict[int, list[int]], student_pref: dict[int, list[int]]) -> dict[int, int]:
    start_time = time.perf_counter()
    
    hospital_match = {i: 0 for i in range(1, n + 1)}
    student_match = {i: 0 for i in range(1, n + 1)}

    unmatched = deque(list(hospital_match.keys()))
    

    while unmatched:
        h = unmatched[0]
        a = hospital_pref[h][0]
    
        if student_match[a] == 0:
            hospital_match[h] = a
            student_match[a] = h
            hospital_pref[h].pop(0)
            unmatched.popleft()
        else:
            
            h_prime = student_match[a]
            idx_h = student_pref[a].index(h)
            idx_h_prime = student_pref[a].index(h_prime)

            if idx_h <= idx_h_prime:
                
                hospital_match[h] = a
                student_match[a] = h

                hospital_pref[h].pop(0)
                unmatched.popleft()

                hospital_match[h_prime] = 0
                unmatched.appendleft(h_prime)
            else:
                hospital_pref[h].pop(0)
                
                
    #print(hospital_match)
    #check_stability(hospital_match,hospital_match,student_match)

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"Execution time: {elapsed_time} seconds")
    return hospital_match
