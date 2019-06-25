from Tournament import Tournament

players = ["PHI","LDN","NYE","BOS","SEO","GLA","SHD","HZS",
           "TOR","HOU","ATL","FLA","DAL","SFS","CHD","GZC",
           "PAR","WAS","VAL","VAN"]
T = Tournament(players,start_score=1000,K=32)

    
T.update("PHI","LDN",3,1)
T.update("NYE","BOS",2,1)
T.update("SEO","GLA",3,1)

T.update("SHD","HZS",1,3)
T.update("TOR","HOU",3,2)
T.update("ATL","FLA",4,0)
T.update("DAL","SFS",0,4)

T.update("CHD","GZC",3,2)
T.update("LDN","PAR",1,3)
T.update("WAS","NYE",1,3)
T.update("VAL","HZS",2,3)
T.update("VAN","SHD",4,0)

T.update("HOU","BOS",2,3)
T.update("PHI","ATL",3,2)
T.update("SFS","GLA",2,3)
T.update("SEO","DAL",1,3)

T.update("WAS","LDN",2,3)
T.update("PHI","FLA",1,2)
T.update("GZC","DAL",4,0)

T.update("SEO","CHD",4,0)
T.update("ATL","TOR",3,1)
T.update("NYE","VAL",3,2)
T.update("SHD","BOS",3,1)

print(T)

print(T.predict("ATL","DAL"))