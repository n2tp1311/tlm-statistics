#!/usr/bin/env python
# coding: utf-8

# In[8]:


import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import datetime as dt
import time
import random
url = 'http://www.awstats.io/mining/pools/'
while(True):
  data = pd.DataFrame({'date': [], 'planet': [], 'max_minerable': []})
  times = 50
  for i in range(0, times):
    page = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(page)
    planet_html = soup.select('table')[0].select('tr > td:nth-child(1)')
    planet = [planet.text for planet in planet_html]
    max_minerable_html = soup.select('table')[0].select('td:nth-child(4)')
    max_minerable = [float(i.text) for i in max_minerable_html]
    small_data = pd.DataFrame({'date': dt.datetime.today(), 'planet': planet, 'max_minerable': max_minerable})
    data = pd.concat([data,small_data], ignore_index=True)
    print(str(i+1)+'/'+str(times))
    time.sleep(4)
  data.to_csv('minedata/'+str(random.random())+'.csv',index=False)




# In[ ]:




