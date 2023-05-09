# profile_vision_LI
import requests
import re
import pandas as pd
import time


def catch_OC_ID(name):
    url = f"http://rest.genome.jp/oc/{name}"

    headers = {
         "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15"
    }

    resp = requests.get(url=url,headers=headers)
    page_content = resp.text
    obj=re.compile(r'OC..*?\d.+?\s(?P<OC_ID>\w*?):.*?\n',re.S)
    result=obj.finditer(page_content)
    identification=[]
    for it in result:
        it.group("OC_ID")
        identification.append(it.group("OC_ID"))
    #print(identification )
        #print(it.group("OC_ID"))
    resp.close()
    time.sleep(3)
    return identification
#a="hsa:362"
#p=catch_OC_ID(a)

#kegg_ID_list
kegg_ID=open('/Users/user/Desktop/group1/原核/細菌/kegg_ID.txt')
KEGG_ID=kegg_ID.read()
KEGG_ID_list=KEGG_ID.split("\n")

#species_ID_list
species_ID=open('/Users/user/Desktop/group1/原核/細菌/seibutushu.txt')
SPECIES_ID=species_ID.read()
SPECIES_ID_list=SPECIES_ID.split("\n")

#pannas_and_csv_format
li_df=pd.DataFrame()
li_df=pd.DataFrame(columns=SPECIES_ID_list)
li_df.to_csv('/Users/user/Desktop/group1/原核/細菌/LI_profile_list.csv')


for n in KEGG_ID_list :
    catch=catch_OC_ID(n)
    #print(catch)
    print(n)
    li_df.loc[n]=0
    for x in catch:
        for u in SPECIES_ID_list:
            if x==u:
                li_df.loc[n,u]=1
            else:
                pass
li_df.to_csv('/Users/user/Desktop/group1/原核/細菌/LI_profile_list.csv', mode='a+', header=False)



print(li_df)
print("over")



