#!/usr/bin/env python
# coding: utf-8

# In[379]:


import pandas as pd


# In[391]:


df2018=pd.read_csv("c:\datadata\서울교통공사 2018년 일별 역별 시간대별 승하차인원(1_8호선).csv")
df2019=pd.read_csv("c:\datadata\서울교통공사 2019년 일별 역별 시간대별 승하차인원(1_8호선).csv")
df2020=pd.read_csv("c:\datadata\서울교통공사 2020년 일별 역별 시간대별 승하차인원(1_8호선).csv", encoding='cp949')
df2021=pd.read_csv("c:\datadata\서울교통공사 2021년 일별 역별 시간대별 승하차인원(1_8호선).csv", encoding='cp949')
df2022=pd.read_csv("c:\datadata\서울교통공사 2022년 역별 일별 시간대별 승하차인원 정보.csv", encoding='cp949')


# In[392]:


df2018= df2018.drop('역번호',axis=1)
df2018= df2018.drop('합 계',axis=1)
df2019= df2019.drop('역번호',axis=1)
df2019= df2019.drop('합 계',axis=1)
df2020= df2020.drop('역번호',axis=1)
df2021= df2021.drop('역번호',axis=1)
df2021= df2021.drop('합 계',axis=1) 
df2021= df2021.drop('연번',axis=1)
df2022= df2022.drop('고유역번호(외부역코드)',axis=1)
df2022= df2022.drop('연번',axis=1)


# In[393]:


df2018 = df2018.rename(columns={df2018.columns[0]: '날짜', df2018.columns[1]: '호선', df2018.columns[2]: '역명',
                                df2018.columns[3]: '승하차구분',df2018.columns[4]: '05 ~ 06',
                                df2018.columns[5]: '06 ~ 07',df2018.columns[6]: '07 ~ 08',
                                df2018.columns[7]: '08 ~ 09',df2018.columns[8]: '09 ~ 10',df2018.columns[9]: '10 ~ 11',
                                df2018.columns[10]: '11 ~ 12',df2018.columns[11]: '12 ~ 13',df2018.columns[12]: '13 ~ 14',
                                df2018.columns[13]: '14 ~ 15',df2018.columns[14]: '15 ~ 16',df2018.columns[15]: '16 ~ 17',
                                df2018.columns[16]: '17 ~ 18',df2018.columns[17]: '18 ~ 19',df2018.columns[18]: '19 ~ 20',
                                df2018.columns[19]: '20 ~ 21',df2018.columns[20]: '21 ~ 22',df2018.columns[21]: '22 ~ 23',
                                df2018.columns[22]: '23 ~ 24',df2018.columns[23]: '00 ~ 01'})

df2019 = df2019.rename(columns={df2019.columns[0]: '날짜', df2019.columns[1]: '호선', df2019.columns[2]: '역명',
                                df2019.columns[3]: '승하차구분',df2019.columns[4]: '05 ~ 06',
                                df2019.columns[5]: '06 ~ 07',df2019.columns[6]: '07 ~ 08',
                                df2019.columns[7]: '08 ~ 09',df2019.columns[8]: '09 ~ 10',df2019.columns[9]: '10 ~ 11',
                                df2019.columns[10]: '11 ~ 12',df2019.columns[11]: '12 ~ 13',df2019.columns[12]: '13 ~ 14',
                                df2019.columns[13]: '14 ~ 15',df2019.columns[14]: '15 ~ 16',df2019.columns[15]: '16 ~ 17',
                                df2019.columns[16]: '17 ~ 18',df2019.columns[17]: '18 ~ 19',df2019.columns[18]: '19 ~ 20',
                                df2019.columns[19]: '20 ~ 21',df2019.columns[20]: '21 ~ 22',df2019.columns[21]: '22 ~ 23',
                                df2019.columns[22]: '23 ~ 24',df2019.columns[23]: '00 ~ 01'})

df2020 = df2020.rename(columns={df2020.columns[0]: '날짜', df2020.columns[1]: '호선', df2020.columns[2]: '역명',
                                df2020.columns[3]: '승하차구분',df2020.columns[4]: '05 ~ 06',
                                df2020.columns[5]: '06 ~ 07',df2020.columns[6]: '07 ~ 08',
                                df2020.columns[7]: '08 ~ 09',df2020.columns[8]: '09 ~ 10',df2020.columns[9]: '10 ~ 11',
                                df2020.columns[10]: '11 ~ 12',df2020.columns[11]: '12 ~ 13',df2020.columns[12]: '13 ~ 14',
                                df2020.columns[13]: '14 ~ 15',df2020.columns[14]: '15 ~ 16',df2020.columns[15]: '16 ~ 17',
                                df2020.columns[16]: '17 ~ 18',df2020.columns[17]: '18 ~ 19',df2020.columns[18]: '19 ~ 20',
                                df2020.columns[19]: '20 ~ 21',df2020.columns[20]: '21 ~ 22',df2020.columns[21]: '22 ~ 23',
                                df2020.columns[22]: '23 ~ 24',df2020.columns[23]: '00 ~ 01'})

df2021 = df2021.rename(columns={df2021.columns[0]: '날짜', df2021.columns[1]: '호선', df2021.columns[2]: '역명',
                                df2021.columns[3]: '승하차구분',df2021.columns[4]: '05 ~ 06',
                                df2021.columns[5]: '06 ~ 07',df2021.columns[6]: '07 ~ 08',
                                df2021.columns[7]: '08 ~ 09',df2021.columns[8]: '09 ~ 10',df2021.columns[9]: '10 ~ 11',
                                df2021.columns[10]: '11 ~ 12',df2021.columns[11]: '12 ~ 13',df2021.columns[12]: '13 ~ 14',
                                df2021.columns[13]: '14 ~ 15',df2021.columns[14]: '15 ~ 16',df2021.columns[15]: '16 ~ 17',
                                df2021.columns[16]: '17 ~ 18',df2021.columns[17]: '18 ~ 19',df2021.columns[18]: '19 ~ 20',
                                df2021.columns[19]: '20 ~ 21',df2021.columns[20]: '21 ~ 22',df2021.columns[21]: '22 ~ 23',
                                df2021.columns[22]: '23 ~ 24'})


df2022 = df2022.rename(columns={df2022.columns[0]: '날짜', df2022.columns[1]: '호선', df2022.columns[2]: '역명',
                                df2022.columns[3]: '승하차구분',df2022.columns[4]: '05 ~ 06',
                                df2022.columns[5]: '06 ~ 07',df2022.columns[6]: '07 ~ 08',
                                df2022.columns[7]: '08 ~ 09',df2022.columns[8]: '09 ~ 10',df2022.columns[9]: '10 ~ 11',
                                df2022.columns[10]: '11 ~ 12',df2022.columns[11]: '12 ~ 13',df2022.columns[12]: '13 ~ 14',
                                df2022.columns[13]: '14 ~ 15',df2022.columns[14]: '15 ~ 16',df2022.columns[15]: '16 ~ 17',
                                df2022.columns[16]: '17 ~ 18',df2022.columns[17]: '18 ~ 19',df2022.columns[18]: '19 ~ 20',
                                df2022.columns[19]: '20 ~ 21',df2022.columns[20]: '21 ~ 22',df2022.columns[21]: '22 ~ 23',
                                df2022.columns[22]: '23 ~ 24',df2022.columns[23]: '00 ~ 01'})


# In[394]:


호선_mapping = {1: '1호선',  2: '2호선', 3: '3호선',  4: '4호선', 5: '5호선', 6: '6호선', 7: '7호선', 8: '8호선'}

df2021['호선'] = df2021['호선'].map(호선_mapping)
df2022['호선'] = df2022['호선'].map(호선_mapping)


# In[395]:


df1_2018 = df2018[df2018['호선'] == '1호선']
df1_2019 = df2019[df2019['호선'] == '1호선']
df1_2020 = df2020[df2020['호선'] == '1호선']
df1_2021 = df2021[df2021['호선'] == '1호선']
df1_2022 = df2022[df2022['호선'] == '1호선']

df1 = pd.concat([df1_2018, df1_2019, df1_2020,df1_2021,df1_2022])


# In[396]:


df2_2018 = df2018[df2018['호선'] == '2호선']
df2_2019 = df2019[df2019['호선'] == '2호선']
df2_2020 = df2020[df2020['호선'] == '2호선']
df2_2021 = df2021[df2021['호선'] == '2호선']
df2_2022 = df2022[df2022['호선'] == '2호선']

df2 = pd.concat([df2_2018, df2_2019, df2_2020,df2_2021,df2_2022])


# In[397]:


df3_2018 = df2018[df2018['호선'] == '3호선']
df3_2019 = df2019[df2019['호선'] == '3호선']
df3_2020 = df2020[df2020['호선'] == '3호선']
df3_2021 = df2021[df2021['호선'] == '3호선']
df3_2022 = df2022[df2022['호선'] == '3호선']

df3 = pd.concat([df3_2018, df3_2019, df3_2020,df3_2021,df3_2022])


# In[398]:


df4_2018 = df2018[df2018['호선'] == '4호선']
df4_2019 = df2019[df2019['호선'] == '4호선']
df4_2020 = df2020[df2020['호선'] == '4호선']
df4_2021 = df2021[df2021['호선'] == '4호선']
df4_2022 = df2022[df2022['호선'] == '4호선']

df4 = pd.concat([df4_2018, df4_2019, df4_2020,df4_2021,df4_2022])


# In[399]:


df5_2018 = df2018[df2018['호선'] == '5호선']
df5_2019 = df2019[df2019['호선'] == '5호선']
df5_2020 = df2020[df2020['호선'] == '5호선']
df5_2021 = df2021[df2021['호선'] == '5호선']
df5_2022 = df2022[df2022['호선'] == '5호선']

df5 = pd.concat([df5_2018, df5_2019, df5_2020,df5_2021,df5_2022])


# In[400]:


df5_2018 = df2018[df2018['호선'] == '5호선']
df5_2019 = df2019[df2019['호선'] == '5호선']
df5_2020 = df2020[df2020['호선'] == '5호선']
df5_2021 = df2021[df2021['호선'] == '5호선']
df5_2022 = df2022[df2022['호선'] == '5호선']

df5 = pd.concat([df5_2018, df5_2019, df5_2020,df5_2021,df5_2022])


# In[401]:


df6_2018 = df2018[df2018['호선'] == '6호선']
df6_2019 = df2019[df2019['호선'] == '6호선']
df6_2020 = df2020[df2020['호선'] == '6호선']
df6_2021 = df2021[df2021['호선'] == '6호선']
df6_2022 = df2022[df2022['호선'] == '6호선']

df6 = pd.concat([df6_2018, df6_2019, df6_2020,df6_2021,df6_2022])


# In[402]:


df6_2018 = df2018[df2018['호선'] == '6호선']
df6_2019 = df2019[df2019['호선'] == '6호선']
df6_2020 = df2020[df2020['호선'] == '6호선']
df6_2021 = df2021[df2021['호선'] == '6호선']
df6_2022 = df2022[df2022['호선'] == '6호선']

df6 = pd.concat([df6_2018, df6_2019, df6_2020,df6_2021,df6_2022])


# In[403]:


df7_2018 = df2018[df2018['호선'] == '7호선']
df7_2019 = df2019[df2019['호선'] == '7호선']
df7_2020 = df2020[df2020['호선'] == '7호선']
df7_2021 = df2021[df2021['호선'] == '7호선']
df7_2022 = df2022[df2022['호선'] == '7호선']

df7 = pd.concat([df7_2018, df7_2019, df7_2020,df7_2021,df7_2022])


# In[404]:


df8_2018 = df2018[df2018['호선'] == '8호선']
df8_2019 = df2019[df2019['호선'] == '8호선']
df8_2020 = df2020[df2020['호선'] == '8호선']
df8_2021 = df2021[df2021['호선'] == '8호선']
df8_2022 = df2022[df2022['호선'] == '8호선']

df8 = pd.concat([df8_2018, df8_2019, df8_2020,df8_2021,df8_2022])


# In[405]:


df1.to_csv('1호선.csv', index=False,encoding='utf-8-sig')
df2.to_csv('2호선.csv', index=False,encoding='utf-8-sig')
df3.to_csv('3호선.csv', index=False,encoding='utf-8-sig')
df4.to_csv('4호선.csv', index=False,encoding='utf-8-sig')
df5.to_csv('5호선.csv', index=False,encoding='utf-8-sig')
df6.to_csv('6호선.csv', index=False,encoding='utf-8-sig')
df7.to_csv('7호선.csv', index=False,encoding='utf-8-sig')
df8.to_csv('8호선.csv', index=False,encoding='utf-8-sig')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




