def read_input_file(file_name: str) -> list[int, dict, dict]:
    with open(file_name, 'r') as file:
        n = file.readline().strip()

        if not n:
            raise NotImplementedError("Unhandled empty file edge case")

        if not n.isdigit():
            raise ValueError("ERROR:::FILE_FORMAT - N must be an integer")
        
        n = int(n)
        
        if n < 1:
            raise ValueError("ERROR:::FILE_FORMAT - N must be at least 1")

        prefs: list[tuple[int, list[int]]] = []
        i = 1
        for line in file:
            line = line.strip()
            if not line:
                raise ValueError("ERROR:::FILE_FORMAT - Input file contains empty lines")
            
            pref = parse_pref_line(line, n)
            prefs.append((i, pref))
            i += 1
            if i > n:
                i = 1

        if len(prefs) != 2*n:
            raise ValueError("ERROR:::FILE_FORMAT - Mismatch number of hospitals & students")
        
        hospital_prefs = dict(prefs[:n])
        student_prefs = dict(prefs[n:])

        return (n, hospital_prefs, student_prefs)


def parse_pref_line(line: str, n: int) -> list[int]:
    nums = line.split(' ')

    if len(nums) != n:
        raise ValueError(f"ERROR:::FILE_FORMAT - Preference list must be {n} digits")

    res: list[int] = []
    seen = set()
    for num in nums:
        if not num.isdigit():
            raise ValueError("ERROR:::FILE_FORMAT - Preferences must be integers")
        
        num = int(num)

        if num < 1 or num > n:
            raise ValueError(f"ERROR:::FILE_FORMAT - Preferences must be between 1 and {n}")
        
        if num in seen:
            raise ValueError("ERROR:::FILE_FORMAT - Duplicate number in preference list")
        
        res.append(int(num))
        seen.add(num)
        
    return res

def write_output_file(n, matchings: dict[int, int]):
    with open(f"output/{n}.txt", "w+") as file:
        for hospital, student in matchings.items():
            file.write(f"{hospital} {student}\n")
    


'''
File Input Format:
3 # num of hosptials and students
1 2 3 # hosp 1
2 3 1 # hosp 2
2 1 3 # hosp 3
2 1 3 # stud 1
1 2 3 # stud 2
1 2 3 # stud 3

Edge Cases:
- empty file
- doesnt follow format
- num of students or hospitals dont equal the n

ideal format for use:
hosp {
1: [1, 2, 3]
2: [2, 3, 1]
3: [2, 1, 3]
}

stud {
1: [2, 1, 3]
2: [1, 2, 3]
3: [1, 2, 3]
}
'''
