import numpy
import pandas

header_row = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'num',]
url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.cleveland.data'
heart_data = pandas.read_csv(url, header=0, na_values='?')
heart_data.columns = header_row


#1
print len[heart_data[heart_data['sex'==0]]

#2          
gender_groups=heart_data.groupby('sex')
print gender_groups.agg('count')
print gender_groups.size()
print heart_data.groupby('sex').count()

#3
print heart_data.describe()
print gender_groups.describe()

#4
heart_data.fillna(int(heart_data['thal'].mode()))
heart_data['thal'].ffill()
heart_data['thal'].bfill()
