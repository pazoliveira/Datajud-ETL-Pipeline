import json
import requests 

url = "https://api-publica.datajud.cnj.jus.br/api_publica_tjdft/_search"
headers = {
    "Authorization": "APIKey cDZHYzlZa0JadVREZDJCendQbXY6SkJlTzNjLV9TRENyQk1RdnFKZGRQdw==",
    "Content-Type": "application/json" }
payload = {"size": 2, "query": {"match_all": {}}}

response = requests.post(url, headers=headers,json=payload)
data = response.json()

with open("data/raw/datajud.json","w",encoding="utf-8") as file:
    json.dump(data,file,ensure_ascii=False,indent=2)

print("Extração concluída")