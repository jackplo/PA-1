import copy
import sys
from src.matching.algorithm import gale_shapley
from util import read_input_file
from src.graph.grapher import generate_plot
from pathlib import Path
import time 

def run_comparison_test(args):
    test_dir = Path(args[0])

    files = [file for file in test_dir.iterdir() if file.is_file()]

    data: tuple[list[int], list[int]] = ([], [])

    for file in files:
        file_data = read_input_file(file)

        start_time = time.perf_counter()
        matching = gale_shapley(file_data[0],copy.deepcopy(file_data[1]),copy.deepcopy(file_data[2]))
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
    
        data[0].append(file_data[0]), data[1].append(elapsed_time)

    generate_plot(data) 


if __name__ == "__main__":
    run_comparison_test(sys.argv[1:]) 