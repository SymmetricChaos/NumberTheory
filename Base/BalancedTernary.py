def balanced_ternary(n):
    pass

int_form = {"+": 1, "0": 0, "-": -1}

class Bal_Tern:
    
    def __init__(self,n):
        if type(n) == int:
            self.digits = balanced_ternary(n)
        if type(n) == str:
            self.digits = [int_form(s) for s in n]