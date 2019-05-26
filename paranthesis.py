def printParenthesis(str, q): 
    if(q > 0): 
        _printParenthesis(str, 0,  
                          q, 0, 0); 
    return; 
  
def _printParenthesis(str, pos, q,  
                      open, close): 
      
    if(close == q): 
        for i in str: 
            print(i, end = ""); 
        print(); 
        return; 
    else: 
        if(open > close): 
            str[pos] = '}'; 
            _printParenthesis(str, pos + 1, q,  
                              open, close + 1); 
        if(open < q): 
            str[pos] = '{'; 
            _printParenthesis(str, pos + 1, q,  
                              open + 1, close); 
q = int(input()); 
str = [""] * 2 * q; 
printParenthesis(str, q); 
