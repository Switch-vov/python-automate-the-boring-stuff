import json

stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0,"felineIQ": null}'

jsonData = json.loads(stringOfJsonData)
print(jsonData)

jsonString = json.dumps(jsonData)
print(jsonString)