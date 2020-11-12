import requests
import json

# https://oeis.org/wiki/JSON_Format,_Compressed_Files

def show_dict(D,superdict=""):
    """
    Recursively show the contents of a dictionary or iterable that make contain
    other dictionaries or iterables
    """
    if type(D) == dict:
        if len(D) == 0:
            print(f"{superdict}: {D}")
        
        for key,val in D.items():
            show_dict(val,superdict=f"{superdict}['{key}']")
    
    elif type(D) in (list,tuple):
        if len(D) == 0:
            print(f"{superdict}: {D}")
        
        for n,i in enumerate(D):
            show_dict(i,superdict=f"{superdict}[{n}]")
    
    else:
        print(f"{superdict}: {D}")


def OEIS_A(A):
    
    Astr = str(A)
    rqsrting = f"https://oeis.org/search?q=id:A{Astr}&fmt=json"
    
    resp = requests.get(rqsrting)
    J = json.loads(resp.content.decode('utf-8'))
    
    if "error" in J:
        raise Exception(f"Error {J['code']} {J['error']}\nRequest: {rqsrting}")
    
    return J


def OEIS_search(search,start=0):
    
    search = str(search)
    rqsrting = f"https://oeis.org/search?q={search}&fmt=json&start={start}"
    
    resp = requests.get(rqsrting)
    J = json.loads(resp.content.decode('utf-8'))
    
    if "error" in J:
        raise Exception(f"Error {J['code']} {J['error']}\nRequest: {rqsrting}")
    
    return J


def make_A(num):
    
    if num > 999999:
        raise ValueError("OEIS A numbers are less than 999999")
        
    return f'A{num:06}'


def pisot_sequences():
    
    E = []
    L = []
    P = []
    T = []
    
    s = 0
    
    while True:
        
        S = "name: 'pisot sequence'"
        A = OEIS_search(S,s)
        R = A['results']
        
        if len(R) == 0:
            break
        
        s += len(R)
        
        for r in R:
            name = r['name']
            number = make_A(r['number'])
            
            if "E(" in name:
                E.append(number)
            if "L(" in name:
                L.append(number)
            if "P(" in name:
                P.append(number)
            if "T(" in name:
                T.append(number)
    
    print("E=",", ".join(E))
    print("L=",", ".join(L))
    print("P=",", ".join(P))
    print("T=",", ".join(T))