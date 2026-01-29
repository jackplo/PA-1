import copy
import sys
from algorithm import gale_shapley
from util import read_input_file
from verifier import check_stability, check_validity
def main(args):
    file = read_input_file(args[0])
    #print(file[1])
    #print(file[2])
  
    print("file[1] ", file[1])
    print("file[2] ", file[2])
    matching = gale_shapley(file[0],copy.deepcopy(file[1]),copy.deepcopy(file[2]))
    print(matching)
    matching = {
        1:1,
        2:3,
        3:2
    }
    print("file[1] after g-s ", file[1])
    result = check_stability(matching,file[1],file[2])
   
    print(result)

if __name__ == "__main__":
    main(sys.argv[1:]) 