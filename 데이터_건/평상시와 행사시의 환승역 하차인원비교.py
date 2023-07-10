#!/usr/bin/env python
# coding: utf-8

# In[40]:


import pandas as pd


# In[41]:


df2=pd.read_csv("C:\datadata\\2호선환승역.csv", encoding="utf-8")
df5=pd.read_csv("C:\datadata\\5호선환승역.csv", encoding="utf-8")
df6=pd.read_csv("C:\datadata\\6호선환승역.csv", encoding="utf-8")


# In[42]:


df2_week=pd.read_csv("C:\datadata\\2호선환승역(+-7).csv", encoding="utf-8")
df5_week=pd.read_csv("C:\datadata\\5호선환승역(+-7).csv", encoding="utf-8")
df6_week=pd.read_csv("C:\datadata\\6호선환승역(+-7).csv", encoding="utf-8")


# In[43]:


import matplotlib.pyplot as plt


# In[44]:


plt.rcParams['font.family'] = 'Malgun Gothic'

print("행사장소 : 종합운동장역(2호선)")
for i in range(8,28):
    plt.bar(df2['환승역'],df2.iloc[:,i])
    plt.xlabel('환승역')
    plt.ylabel('하차 인원') 
    plt.title(df2.iloc[:,i].name)
    plt.xticks(rotation = 80)
   

    plt.bar(df2_week['환승역'],df2_week.iloc[:,i])
    plt.xlabel('환승역')
    plt.ylabel('하차 인원') 
    plt.title(df2_week.iloc[:,i].name)
    plt.xticks(rotation = 80)
    
    plt.show()


# In[45]:


for i in range(8,28):
    plt.bar(df['환승역'],df.iloc[:,i])
    plt.xlabel('환승역')
    plt.ylabel('하차 인원') 
    plt.title(df.iloc[:,i].name)
    plt.xticks(rotation = 80)
   

    plt.bar(df_week['환승역'],df_week.iloc[:,i])
    plt.xlabel('환승역')
    plt.ylabel('하차 인원') 
    plt.title(df_week.iloc[:,i].name)
    plt.xticks(rotation = 80)
    
    plt.show()


# In[46]:


print("행사장소 : 여의나루역(5호선)")
for i in range(8,28):
    plt.bar(df5['환승역'],df5.iloc[:,i])
    plt.xlabel('환승역')
    plt.ylabel('하차 인원') 
    plt.title(df5.iloc[:,i].name)
    plt.xticks(rotation = 80)
   

    plt.bar(df5_week['환승역'],df5_week.iloc[:,i])
    plt.xlabel('환승역')
    plt.ylabel('하차 인원') 
    plt.title(df5_week.iloc[:,i].name)
    plt.xticks(rotation = 80)
    
    plt.show()


# In[47]:


print("행사장소 : 월드컵경기장(6호선)")
for i in range(8,28):
    plt.bar(df6['환승역'],df6.iloc[:,i])
    plt.xlabel('환승역')
    plt.ylabel('하차 인원') 
    plt.title(df6.iloc[:,i].name)
    plt.xticks(rotation = 80)
   

    plt.bar(df6_week['환승역'],df6_week.iloc[:,i])
    plt.xlabel('환승역')
    plt.ylabel('하차 인원') 
    plt.title(df6_week.iloc[:,i].name)
    plt.xticks(rotation = 80)
    
    plt.show()

