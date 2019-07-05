from WKAPI import WKrequest

R = "assignments"
J = WKrequest(R)
for i in J["data"][0].items():
    print(i)
    print()

print(J["object"])
print(J["url"])
print(J["pages"])
print(J["total_count"])
print(J["data_updated_at"])