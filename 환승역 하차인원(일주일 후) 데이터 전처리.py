#!/usr/bin/env python
# coding: utf-8

# In[1156]:


import pandas as pd


# In[1157]:


df=pd.read_csv("c:\datadata\행사_승하차_데이터3.csv",encoding='utf-8')


# In[1158]:


df


# In[1159]:


print(df['호선'].unique())
print(df['가까운 지하철역'].unique())


# In[1160]:


line2 = pd.read_csv("C:/datadata/호선별 지하철 승하차/2호선.csv")
line5 = pd.read_csv("C:/datadata/호선별 지하철 승하차/5호선.csv")
line6 = pd.read_csv("C:/datadata/호선별 지하철 승하차/6호선.csv")


# In[1161]:


line2=line2[line2['승하차구분']=='하차']
line5=line5[line5['승하차구분']=='하차']
line6=line6[line6['승하차구분']=='하차']


# In[1162]:


line2['역명'] = line2['역명'].replace('동대문역사문화공원(DDP)', '동대문역사문화공원')


# In[1163]:


from datetime import timedelta
df['행사날짜'] = pd.to_datetime(df['행사날짜']).dt.date
df['행사날짜'] = df['행사날짜'] + timedelta(days=7)
df=df.rename(columns={'행사날짜': '날짜'})

line2['날짜'] = pd.to_datetime(line2['날짜']).dt.date
line5['날짜'] = pd.to_datetime(line5['날짜']).dt.date
line6['날짜'] = pd.to_datetime(line6['날짜']).dt.date


# In[1164]:


종합운동장 = df[df['가까운 지하철역']=='종합운동장역']
월드컵경기장 = df[df['가까운 지하철역']=='월드컵 경기장역']
여의나루 =df[df['가까운 지하철역']=='여의나루역']


# In[1165]:


종합운동장 = 종합운동장.drop(종합운동장.columns[6:], axis=1)
월드컵경기장 = 월드컵경기장.drop(월드컵경기장.columns[6:], axis=1)
여의나루 = 여의나루.drop(여의나루.columns[6:], axis=1)
종합운동장 = 종합운동장.drop(종합운동장.columns[4], axis=1)
월드컵경기장 = 월드컵경기장.drop(월드컵경기장.columns[4], axis=1)
여의나루 = 여의나루.drop(여의나루.columns[4], axis=1)


# In[1166]:


line2_transfer_stations = ['까치산', '신도림', '영등포구청', '당산', '합정', '홍대입구', '충정로(경기대입구)',
                           '시청', '을지로3가', '을지로4가', '동대문역사문화공원', '신당',
                           '왕십리(성동구청)', '성수', '신설동', '건대입구', '잠실(송파구청)',
                           '선릉', '강남', '교대(법원.검찰청)', '사당', '대림(구로구청)']

line6_transfer_stations = ['신내', '태릉입구', '석계', '보문', '동묘산', '신당', '청구', '약수',
                           '삼각지', '효창공원앞', '공덕', '합정', '디지털미디어시티', '불광', '연신내']

line5_transfer_stations = ['김포공항', '까치산', '영등포구청', '신길', '여의도', '공덕', '충정로',
                           '종로3가', '을지로4가', '동대문역사문화공원(DDP)', '청구', '왕십리',
                           '군자(능동)', '천호(풍납토성)', '강동', '올림픽공원(한국체대)', '개롱']


# In[1167]:


line2_transfer_stations_하차인원 = pd.DataFrame()

for i in range(len(line2_transfer_stations)):
    line2_new=line2[line2['역명']==line2_transfer_stations[i]]
    line2_transfer_stations_하차인원1 = 종합운동장.merge(line2_new, on='날짜')
    line2_transfer_stations_하차인원 = pd.concat([line2_transfer_stations_하차인원, line2_transfer_stations_하차인원1], ignore_index=True)
line2_transfer_stations_하차인원 = line2_transfer_stations_하차인원.drop(line2_transfer_stations_하차인원.index[::2])


# In[1168]:


line5_transfer_stations_하차인원 = pd.DataFrame()

for i in range(len(line5_transfer_stations)):
    line5_new=line5[line5['역명']==line5_transfer_stations[i]]
    line5_transfer_stations_하차인원1 = 여의나루.merge(line5_new, on='날짜')
    line5_transfer_stations_하차인원 = pd.concat([line5_transfer_stations_하차인원, line5_transfer_stations_하차인원1], ignore_index=True)
line5_transfer_stations_하차인원 = line5_transfer_stations_하차인원.drop(line5_transfer_stations_하차인원.index[::2])


# In[1169]:


line6_transfer_stations_하차인원 = pd.DataFrame()

for i in range(len(line6_transfer_stations)):
    line6_new=line6[line6['역명']==line6_transfer_stations[i]]
    line6_transfer_stations_하차인원1 = 월드컵경기장.merge(line6_new, on='날짜')
    line6_transfer_stations_하차인원 = pd.concat([line6_transfer_stations_하차인원, line6_transfer_stations_하차인원1], ignore_index=True)
line6_transfer_stations_하차인원 = line6_transfer_stations_하차인원.drop(line6_transfer_stations_하차인원.index[::2])


# In[1170]:


line2_transfer_stations_하차인원.rename(columns={'역명': '환승역'}, inplace=True)
line5_transfer_stations_하차인원.rename(columns={'역명': '환승역'}, inplace=True)
line6_transfer_stations_하차인원.rename(columns={'역명': '환승역'}, inplace=True)
line2_transfer_stations_하차인원.rename(columns={'날짜': '행사 일주일 후 날짜'}, inplace=True)
line5_transfer_stations_하차인원.rename(columns={'날짜': '행사 일주일 후 날짜'}, inplace=True)
line6_transfer_stations_하차인원.rename(columns={'날짜': '행사 일주일 후 날짜'}, inplace=True)


# In[ ]:





# In[1171]:


line2_transfer_stations_하차인원.to_csv('2호선환승역(+7).csv', index=False,encoding='utf-8-sig')
line5_transfer_stations_하차인원.to_csv('5호선환승역(+7).csv', index=False,encoding='utf-8-sig')
line6_transfer_stations_하차인원.to_csv('6호선환승역(+7).csv', index=False,encoding='utf-8-sig')


# In[1172]:


line2_transfer_stations_하차인원


# In[1173]:


line5_transfer_stations_하차인원


# In[1174]:


line6_transfer_stations_하차인원


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




