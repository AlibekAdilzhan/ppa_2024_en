cap = {"Kazakhstan": "Astana", "USA": "Washington", "Japan": "Tokyo", "France": "Paris"}
# print(cap["Korea"])
# print(cap.get("USA", "Such element does not exist"))
country = "USA"
if country in cap:
    print(cap[country])
else:
    print(-1)