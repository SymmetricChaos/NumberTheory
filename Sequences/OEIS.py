import requests
import json

# https://oeis.org/wiki/JSON_Format,_Compressed_Files

def get_OEIS_JSON(A):

    if A > 999999:
        raise Exception("All A-Numbers are less than 1000000")
    
    Astr = str(A)
    
    while len(Astr) < 6:
        Astr = "0"+Astr
    
    resp = requests.get(f"https://oeis.org/search?q=id:A{Astr}&fmt=json")
    
    J = json.loads(resp.content.decode('utf-8'))
    if "error" in J:
        raise Exception(f"Error {J['code']} {J['error']}\nRequest: {sfurl+S}")
    return J

A = get_OEIS_JSON(1)

print(A)