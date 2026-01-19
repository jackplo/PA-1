import sys
from algorithm import initialize_free_rankings

def main(args):
    print("hospital unmatch init ", initialize_free_rankings(int(args[0])))
    
    

if __name__ == "__main__":
    main(sys.argv[1:]) 