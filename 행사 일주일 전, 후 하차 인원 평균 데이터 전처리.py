#!/usr/bin/env python
# coding: utf-8

# In[222]:


import pandas as pd


# In[223]:


line2_before=pd.read_csv("C:\datadata\\2호선환승역(-7).csv", encoding="utf-8")
line5_before=pd.read_csv("C:\datadata\\5호선환승역(-7).csv", encoding="utf-8")
line6_before=pd.read_csv("C:\datadata\\6호선환승역(-7).csv", encoding="utf-8")

line2_after=pd.read_csv("C:\datadata\\2호선환승역(+7).csv", encoding="utf-8")
line5_after=pd.read_csv("C:\datadata\\5호선환승역(+7).csv", encoding="utf-8")
line6_after=pd.read_csv("C:\datadata\\6호선환승역(+7).csv", encoding="utf-8")


# In[224]:


from datetime import timedelta
line2_before['행사 일주일 전 날짜'] = pd.to_datetime(line2_before['행사 일주일 전 날짜']).dt.date
line5_before['행사 일주일 전 날짜'] = pd.to_datetime(line5_before['행사 일주일 전 날짜']).dt.date
line6_before['행사 일주일 전 날짜'] = pd.to_datetime(line6_before['행사 일주일 전 날짜']).dt.date

line2_after['행사 일주일 후 날짜'] = pd.to_datetime(line2_after['행사 일주일 후 날짜']).dt.date
line5_after['행사 일주일 후 날짜'] = pd.to_datetime(line5_after['행사 일주일 후 날짜']).dt.date
line6_after['행사 일주일 후 날짜'] = pd.to_datetime(line6_after['행사 일주일 후 날짜']).dt.date

line2_before=line2_before.rename(columns={'행사 일주일 전 날짜': '날짜'})
line5_before=line5_before.rename(columns={'행사 일주일 전 날짜': '날짜'})
line6_before=line6_before.rename(columns={'행사 일주일 전 날짜': '날짜'})

line2_after=line2_after.rename(columns={'행사 일주일 후 날짜': '날짜'})
line5_after=line5_after.rename(columns={'행사 일주일 후 날짜': '날짜'})
line6_after=line6_after.rename(columns={'행사 일주일 후 날짜': '날짜'})

line2_before['날짜'] = line2_before['날짜'] + timedelta(days=7)
line5_before['날짜'] = line5_before['날짜'] + timedelta(days=7)
line6_before['날짜'] = line6_before['날짜'] + timedelta(days=7)

line2_after['날짜'] = line2_after['날짜'] - timedelta(days=7)
line5_after['날짜'] = line5_after['날짜'] - timedelta(days=7)
line6_after['날짜'] = line6_after['날짜'] - timedelta(days=7)


# In[225]:


line2_before['index']=list(range(0, len(line2_before)))
line2_after['index']=list(range(0, len(line2_after)))

line5_before['index']=list(range(0, len(line5_before)))
line5_after['index']=list(range(0, len(line5_after)))

line6_before['index']=list(range(0, len(line6_before)))
line6_after['index']=list(range(0, len(line6_after)))


# In[226]:


line2_mean = pd.concat([line2_before, line2_after])
line2_mean = line2_mean.groupby('index').mean()

line5_mean1 = pd.concat([line5_before, line5_after])
line5_mean = line5_mean1.groupby('index').mean()

line6_mean = pd.concat([line6_before, line6_after])
line6_mean = line6_mean.groupby('index').mean()


# In[227]:


line2_combined = pd.merge(line2_before, line2_mean, left_index=True, right_index=True, suffixes=('_', ''))
line5_combined = pd.merge(line5_before, line5_mean, left_index=True, right_index=True, suffixes=('_', ''))
line6_combined = pd.merge(line6_before, line6_mean, left_index=True, right_index=True, suffixes=('_', ''))


# In[228]:


line2_combined = line2_combined.drop(line2_combined.columns[8:29], axis=1)
line5_combined = line5_combined.drop(line5_combined.columns[8:29], axis=1)
line6_combined = line6_combined.drop(line6_combined.columns[8:29], axis=1)


# In[229]:


line2_combined.to_csv('2호선환승역(+-7).csv', index=False,encoding='utf-8-sig')
line5_combined.to_csv('5호선환승역(+-7).csv', index=False,encoding='utf-8-sig')
line6_combined.to_csv('6호선환승역(+-7).csv', index=False,encoding='utf-8-sig')


# In[ ]:





# In[ ]:





# In[ ]:




