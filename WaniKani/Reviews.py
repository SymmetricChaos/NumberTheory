from WKAPI import WKrequest

R = "reviews"
J = WKrequest(R)
print(J["data"][0])