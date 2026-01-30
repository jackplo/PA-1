import copy
import sys
from src.matching.algorithm import gale_shapley
from util import read_input_file, write_output_file, check_file_validity
from src.graph.grapher import generate_plot
from src.verify.verifier import check_stability
from pathlib import Path
import time 

def run_gale_shapley_suite(args):
    test_dir = Path(args[0])

    files = sorted(
        [file for file in test_dir.iterdir() if file.is_file()],
        key=lambda path: int(path.stem)
    )

    data: tuple[list[int], list[int]] = ([], [])

    for file in files:
        file_data = read_input_file(file)
        n = file_data[0]

        start_time = time.perf_counter()
        matching = gale_shapley(n ,copy.deepcopy(file_data[1]), copy.deepcopy(file_data[2]))
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time

        print(f"GS Execution Time: {elapsed_time:0.5f} seconds")
    
        data[0].append(n), data[1].append(elapsed_time)

        write_output_file(n, matching)

    generate_plot(data, "gs") 

def run_gale_shapley(pref_file_path):
    pref_dir = Path(pref_file_path)

    file_data = read_input_file(pref_dir)
    n = file_data[0]

    start_time = time.perf_counter()
    matching = gale_shapley(n ,copy.deepcopy(file_data[1]), copy.deepcopy(file_data[2]))
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time

    #print(f"GS Execution Time: {elapsed_time:0.5f} seconds")

    write_output_file(n, matching)

def run_verifier(pref_file_path, match_file_path):
    pref_dir = Path(pref_file_path)
    match_dir = Path(match_file_path)

    match_data = check_file_validity(match_dir)
    if not match_data:
        return
    
    pref_data = read_input_file(pref_dir)

    start_time = time.perf_counter()
    result = check_stability(match_data, pref_data[1], pref_data[2])
    
    if(result):
        print(f"Test with n = {pref_data[0]} ")
        print("UNSTABLE ", result)
        
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    
    if(match_data and not result):
        print(f"Test with n = {pref_data[0]} ")
        print("VALID STABLE")
    #print(f"Verifier Execution Time: {elapsed_time:0.5f} seconds")

def run_verifier_suite(pref_path, match_path):
    pref_dir = Path(pref_path)
    match_dir = Path(match_path)

    pref_files = sorted(
        [file for file in pref_dir.iterdir() if file.is_file()],
        key=lambda path: int(path.stem)
    )

    match_files = sorted(
        [file for file in match_dir.iterdir() if file.is_file()],
        key=lambda path: int(path.stem)
    )

    data: tuple[list[int], list[int]] = ([], [])

    for pref_file, match_file in zip(pref_files, match_files):
        pref_data = read_input_file(pref_file)
        match_data = check_file_validity(match_file)
        
        n = pref_data[0]

        if not match_data:
            continue
        
        start_time = time.perf_counter()
        result = check_stability(match_data, pref_data[1], pref_data[2])
        
        if(result):
            print(f"Test with n = {n} ")
            print("UNSTABLE ", result)
            print()
            
            
        end_time = time.perf_counter()
        
        elapsed_time = end_time - start_time
        
        print(f"Verifier Execution Time: {elapsed_time:0.5f} seconds")
        
        if(match_data and not result):
            print(f"Test with n = {n} ")
            print("VALID STABLE")
            print()
        

        data[0].append(n), data[1].append(elapsed_time)

    generate_plot(data, 'verifier') 

if __name__ == "__main__":

    mode = sys.argv[1]

    if mode == "--gs":
        run_gale_shapley(sys.argv[2])
    elif mode == "--verify":
        run_verifier(sys.argv[2], sys.argv[3])
    elif mode == "--gs-suite":
        run_gale_shapley_suite(sys.argv[2:]) 
    elif mode == "--verify-suite":
        run_verifier_suite(sys.argv[2], sys.argv[3])

