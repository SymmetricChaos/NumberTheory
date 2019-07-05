from WKAPI import WKrequest

R = "reviews"
J = WKrequest(R)
for i in J["data"][0].items():
    print(i)
    print()

            
for i in J.items():
    print(i)
    print()