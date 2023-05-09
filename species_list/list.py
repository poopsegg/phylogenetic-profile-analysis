import requests
import re
import pandas as pd
import time

def catch_organism_list(name):
    url = "https://www.genome.jp/kegg-bin/show_organism"
    param = {
        "category": f"{name}",
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15",
    }
    resp = requests.get(url=url, params=param, headers=headers)
    page_content = resp.text
    obj = re.compile(r"<a href='/kegg-bin/show_organ.*?org=(?P<organism>.*?)'>", re.S)
    result = obj.finditer(page_content)
    with open ("/Users/user/Desktop/Fusobacteria.txt", "a") as f:
        for it in result:
            f.write(it.group("organism")+'\n')
            print(it.group("organism"))
        f.close()
    resp.close()
    return

    #print(page_content)
#Test=catch_organism_list()
organism_list= pd.read_excel('/Users/user/Desktop/生物分類/cls_archaea/Archaea.xlsx')
organism_kegg_list = organism_list.values.tolist()
organism_name=[]
for i in organism_kegg_list:
    organism_name.append(i[0])

for t in range(1):
    print(organism_name[t])
    catch_organism_list(organism_name[t])
    time.sleep(3)

print("over")

