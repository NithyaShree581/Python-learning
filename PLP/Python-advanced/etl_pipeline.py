"""
Topic: ETL Pipeline: API -> pandas -> File Output 
Build a complete ETL pipeline in etl_pipeline.py: 
Extract: Fetch from /users and /posts at jsonplaceholder.typicode.com. 
Transform: (a) Create users DataFrame. (b) Add word_count column to posts. (c) Merge on userId/id. (d) Filter word_count > 30. (e) Add category: Short/Medium/Long. 
Load: Save to output/etl_result.csv. Create directory if missing. 
Add main() and print a summary line with counts. 
(e) Predict the output: import pandas as pd posts = [{'userId':1,'body':'hello world foo bar'},{'userId':1,'body':'hi'},{'userId':2,'body':'a b c d e f g h'}] df = pd.DataFrame(posts) df['wc'] = df['body'].apply(lambda x: len(x.split())) print(df['wc'].tolist()) print(len(df[df['wc'] > 3])) 
"""
import pandas as pd
import requests
import os
posts="https://jsonplaceholder.typicode.com/posts"
users="https://jsonplaceholder.typicode.com/users"
response_posts=requests.get(posts,timeout=5)
response_users=requests.get(users,timeout=5)
posts_dic=response_posts.json()
users_dic=response_users.json()
#a
df_posts=pd.DataFrame(posts_dic)
df_users=pd.DataFrame(users_dic)
print(df_posts)

#b
print("after adding word count")
df_posts['word_count'] = df_posts['body'].apply(lambda x: len(x.split()))
print(df_posts)

#c
print(df_users)
df=pd.merge(df_users,df_posts,on='id')
print(df)

#d filter word count>30
print("filterring on word coutn")
df1=df[df['word_count']>30]
print(df1)

#e  Add category: Short/Medium/Long. 
print(set(df['word_count']))
df['Category'] = df['word_count'].apply(
    lambda x: 'Short' if x <= 10 else 'Medium' if x <= 30 else 'Long'
)

#f
os.makedirs("output", exist_ok=True)
df1.to_csv("output/etl_result.csv", index=False)

    # Summary
print(
        f"ETL completed! Users: {len(df_users)}, "
        f"Posts fetched: {len(df_posts)}, "
        f"Posts after filtering: {len(df1)}"
    )
