from bs4 import BeautifulSoup as bs
import json
import pandas as pd
import requests

r = requests.get('https://www.youtube.com/playlist?list=PLpj8MXRvW1q7-u6Yu4vMatTjRrtWTWula')
page = r.text
soup=bs(page,'html.parser')
res=soup.find_all('a',{'class':'pl-video-title-link'})

# print(res)

df1 = pd.read_html(str(res), thousands='dorya')

# for l in res:
#     print(l.get("href"))

print(df1[0])

# <iframe width="560" height="315" src="https://www.youtube.com/embed//watch?v=Wjyl6v-S-rY&t=0s&index=1&list=PLpj8MXRvW1q7-u6Yu4vMatTjRrtWTWula" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>