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


def get_OEIS_JSON(A):

    if A > 999999:
        raise Exception("All A-Numbers are less than 1000000")
    
    Astr = str(A)
    
    while len(Astr) < 6:
        Astr = "0"+Astr
    
    rqsrting = f"https://oeis.org/search?q=id:A{Astr}&fmt=json"
    
    resp = requests.get(rqsrting)
    
    J = json.loads(resp.content.decode('utf-8'))
    if "error" in J:
        raise Exception(f"Error {J['code']} {J['error']}\nRequest: {rqsrting}")
    return J

A = get_OEIS_JSON(5)

# show_dict(A)
print(f"name: {A['results'][0]['name']}")
print(f"data: {A['results'][0]['data']}")