import sys
from algorithm import gale_shapley, new_gale_shapley
from util import read_input_file

def main(args):
    file = read_input_file(args[0])
    print(new_gale_shapley(file[0],file[1],file[2]))
    
    

if __name__ == "__main__":
    main(sys.argv[1:]) 