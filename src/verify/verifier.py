def check_validity(n: int, matching: dict[int, int]):
    if 0 in matching.values():
        return "INVALID", "All hospitals not matched to all students"
    
    has_duplicate = len(matching) != len(set(matching.values()))
    if(has_duplicate):
        return "INVALID", "Has duplicate"
    
    if(len(set(matching.keys())) != n):
        return "INVALID", "Missing/extra hospitals"
    if(len(set(matching.values())) != n):
        return "INVALID", "Missing/extra students"
    
    
    return "VALID", "All good"
    
    
def check_stability(hospital_matching: dict[int,int],
                    hospital_pref: dict[int, list[int]], 
                    student_pref: dict[int, list[int]]):
    
    
    student_matching = {s: h for h, s in hospital_matching.items()}
    
    for h_match, s_match in hospital_matching.items():
        for s in student_pref.keys():
            if s == s_match:
                continue
            
            index_unmatched_s = hospital_pref[h_match].index(s)
            index_matched_s = hospital_pref[h_match].index(hospital_matching[h_match])
            
            index_unmatched_h = student_pref[s].index(h_match)
            index_matched_h = student_pref[s].index(student_matching[s])
            
            if(index_unmatched_s < index_matched_s and index_unmatched_h < index_matched_h):
                return "NOT STABLE", (h_match, s)
           
    return "STABLE", None
