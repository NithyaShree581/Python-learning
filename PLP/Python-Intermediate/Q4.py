"""
Topic: pandas: read_csv, groupby, merge + numpy basics 
You have students.csv (student_id, name, class) and scores.csv (student_id, subject, score): 
(a) Read both into DataFrames and merge on student_id. 
(b) Use groupby to find average score per subject and per student. 
(c) Add a grade column: 'A' >= 85, 'B' >= 70, 'C' >= 55, 'F' otherwise. 
(d) Use numpy: mean, standard deviation, 75th percentile of all scores. 
(e) Predict the output: import pandas as pd data = {'name':['A','B','A','B'], 'score':[80,90,70,85]} df = pd.DataFrame(data) result = df.groupby('name')['score'].mean() print(result.to_dict()) 
"""
import pandas as pd
df1=pd.read_csv("students.csv")
df2=pd.read_csv("scores.csv")
#a
df=pd.merge(df1,df2,on='student_id')
print(df)
#b
df['total']=df.groupby('subject')['score'].mean()

#c
def get_grade(score):
    if score >= 85:
        return 'A'
    elif score >= 70:
        return 'B'
    elif score >= 55:
        return 'C'
    else:
        return 'F'
df['grade']=df['score'].apply(get_grade)    
#d Use numpy: mean, standard deviation, 75th percentile of all scores. 
import numpy as np
mean=np.mean(df['score'])
print(mean)
standard_deviation=np.std(df['score'])
print(standard_deviation)
percentile_75=np.percentile(df['score'],75)
print(percentile_75)
#e
#{'A': 75.0, 'B': 87.5}
