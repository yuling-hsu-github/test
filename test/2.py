import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap 
'''Facebook user analytics'''
data = pd.read_csv('pseudo_facebook.csv')
df=data.drop(columns=['userid','www_likes_received','dob_day'],axis=1)
print(df)


# #計算性別的數量 male:58574 female:40254 在facebook 上的使用占比
# df_gender = df.groupby(['gender']).size().reset_index(name='count')
# plt.figure(dpi=800,figsize=(10, 10))
# gender=['Female','Male']
# explode=[0,0]
# colors = ['#808cba','#3b5998']
# plt.title("Gender Ratio", {"fontsize" : 40})  # 設定標題及其文字大小
# plt.pie(df_gender['count'],labels=gender,explode=explode,colors=colors,autopct="%1.1f%%")
# plt.show()


# #Donut chart
# fig, ax = plt.subplots()
# size = 0.4
# colors = ['#808cba','#3b5998']
# #+legend用法
# legend = plt.legend(['female','male'], title = "Legend")
# ax.pie(df_gender['count'], labels=gender,colors=colors,
#        radius=1-size, wedgeprops=dict(width=size,edgecolor='w'))
# plt.title("Gender Ratio", {"fontsize" : 20})
# plt.show()

#years old

x=df['age'].tolist()
sum_x=[]
for i in x:
    sum_x.append(i+3)
y=df['dob_month'].tolist()
# plt.figure(figsize=(40, 30), dpi=800)
df2=pd.DataFrame({'age':sum_x,'month':df['dob_month'].tolist()})
#先把Age和month做分組 然後等等來印看看
df_Age=df2.groupby(['age']).size().reset_index(name='count')
# plt.bar(df_Age["age"],df_Age["count"],color="#3b5998",width = 1,label="Population")
# plt.xlabel('Age',fontsize=30)
# plt.ylabel("Sum of users",fontsize=30)
# plt.legend()
# plt.show()


# df3=data.drop(data[data.age>30].index)
df3=df_Age.drop(df_Age[df_Age.age>40].index)
plt.figure(figsize=(10,5), dpi=1500)
plt.rcParams['font.size']=20
plt.bar(df3["age"],df3["count"],color="#3b5998",width = 0.8,label="Population")
plt.xlabel('Age',fontsize=30)
plt.ylabel("Sum of users",fontsize=30)
plt.legend()
plt.show()

#男女朋友多寡
df_friend1=df.drop(data[data.age>40].index)
plt.figure(dpi=800,figsize=(25,5))
df_friend=df_friend1.groupby(["gender"]).sum(["close_friend"])
Female=[(df_friend['friend_count']['female']/1000000).round(3),(df_friend['friendships_initiated']['female']/1000000).round(3),(df_friend['likes']['female']/1000000).round(3),(df_friend['likes_received']['female']/1000000).round(3)]
Male=[(df_friend['friend_count']['male']/1000000).round(3),(df_friend['friendships_initiated']['male']/1000000).round(3),(df_friend['likes']['male']/1000000).round(3),(df_friend['likes_received']['male']/1000000).round(3)]
width = 0.35  # the width of the bars
labels=["Friendcount","Friendinitiated","likes","likes received"]
x = np.arange(len(labels)) 
fig, ax = plt.subplots(dpi=1200,figsize=(10,5))
rects1 = ax.bar(x - width/2, Female, width, label='Female')
rects2 = ax.bar(x + width/2, Male, width, label='Male',color="#3b5998")
# Add some text for labels, title and custom x-axis tick labels, etc.

ax.set_ylabel('User records ',fontsize=15)
ax.set_title('Female V.S. Male users len(6)',fontsize=20)
ax.set_xticks(x)
ax.set_xticklabels(labels,fontsize=15)
ax.legend(loc="center left", bbox_to_anchor=(1,0.5),fontsize=15)

ax.bar_label(rects1, padding=3,fontsize=13)
ax.bar_label(rects2, padding=3,fontsize=13)

fig.tight_layout()

plt.show()
