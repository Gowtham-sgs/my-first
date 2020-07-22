import requests
import pandas as pd
from datetime import datetime
from google.colab import data_table

res=requests.get('https://api.covid19india.org/states_daily.json').json()
res=res['states_daily']

l=['Confirmed','Recovered','Deceased']

ele=res[0].keys()

nl=[]
for key in ele:
    if key=='date' or key=='status' or key=='tt':
        continue
    nl.append(key)

df=pd.DataFrame(columns=l,index=nl)


for key in nl:
  j=0
  for col in l:
    s=0
    for i in range(j,len(res),3):
      s+=int(res[i][key])
    df[col][key]=s
    j+=1

df['Active']=df['Confirmed']-df['Deceased']-df['Recovered']

df.sort_values(by=['Confirmed'],ascending=False)
