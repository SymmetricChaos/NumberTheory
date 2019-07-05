from WKAPI import WKrequest

for i in range(440,450):

    J = WKrequest(f"subjects/{i}")
    
    ch = J["data"]["characters"]
    rd = J["data"]["readings"][0]["reading"]
    print(ch,rd)