import copy
import sys
from src.matching.algorithm import gale_shapley
from util import read_input_file
from src.verify.verifier import check_stability, check_validity

def main(args):
    file = read_input_file(args[0])

    matching = gale_shapley(file[0],copy.deepcopy(file[1]),copy.deepcopy(file[2]))
   
    validity = check_validity(file[0], matching)
    print(validity)

    result = check_stability(matching,file[1],file[2])
    print(result)

if __name__ == "__main__":
    main(sys.argv[1:]) 