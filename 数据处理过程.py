#!/usr/bin/env python
# coding: utf-8

# In[145]:


import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from pylab import mpl
import seaborn as sns
mpl.rcParams['font.sans-serif'] = ['SimHei']


# In[ ]:





# In[ ]:





# In[146]:


df = pd.read_csv('./北京二手房网北京二手房出售北京二手房买卖信息.csv',encoding="utf-8")
df


# In[147]:


del df['标题链接']
del df['缩略图']


# In[148]:


df['标题']= df['标题'].apply(lambda x :x.strip().replace(' ','').replace(',','-').replace('，','-').replace('\n',''))


# In[149]:


df['picNum']=df['picNum'].apply(lambda x:int(x[:-1]))


# In[150]:


df['list-info1']=df['list-info1'].apply(lambda x : x.strip().replace('\n','').replace(',','-').replace('，','-'))


# In[151]:


df['list-info']=df['list-info'].apply(lambda x : x.strip().replace('\n','').replace(',','-').replace('，','-'))


# In[152]:


df


# In[153]:


df['jjrname-outer']=df['jjrname-outer'].apply(lambda x : x.strip().replace('\n','').replace(',','-').replace('，','-'))


# In[154]:


df


# In[155]:


df['list-info2']=df['list-info2'].apply(lambda x:float(x[:-1]))


# In[156]:


df


# In[157]:


df['sum_money']=df['sum'].apply(lambda x:float(x[:-1]))


# In[158]:


del df['sum']


# In[159]:


df['avg_mile']=df['unit'].apply(lambda x:int(x[:-3]))


# In[ ]:





# In[160]:


del df['unit']


# In[161]:


df


# In[162]:


df['list-info5']=df['list-info5'].fillna('无')


# In[163]:


df


# In[164]:


df.rename(columns={'标题':'title','list-info1':'location','jjrinfo':'company','list-info2':'area','list-info4':'floors','jjrname-outer':'broker','list-info5':'addition'},inplace=True)


# In[165]:


df.rename(columns={'sum_money':'sum_money_w','avg_mile':'avg_mile_y'},inplace=True)


# In[166]:


df.rename(columns={'list-info':'huxing'},inplace=True)
df.rename(columns={'list-info3':'direct'},inplace=True)


# In[167]:


df.to_csv('beijing_house_after.csv',encoding='utf_8_sig')


# In[168]:


df


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




