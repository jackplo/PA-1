

def initialize_free_rankings(n) -> dict(int, int):
    '''
    Docstring for initialize_rankings
    
    :param n: number of hospitals that will be matched
    :return: dictionary of unmatched hospitals {1:0, 2:0, 3:0}
    
    ex:
        input:
        3
       
        output:
        hosp {
            1: 0,
            2: 0,
            3: 0
            
        }
        
    '''
    
    if n < 0:
        raise ValueError("n must be non-negative")
    return {i: 0 for i in range(1, n + 1)}
    