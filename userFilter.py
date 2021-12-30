import pandas as pd
import numpy as np

user_data = pd.read_csv('User1.csv')
p= pd.DataFrame(user_data)
p=p.sort_values(['Tinggi','Umur']).drop_duplicates()

x=p.drop(['Jenis Tempat Tinggal','Tempoh masa pendakian yang dikehendaki.','Jenis Tempat Tinggal'], axis=1)

x['V']=x['Jarak Pendakian (KM)']*x['Tahap kesukaran']
x['BMI']=x['Berat'] /  pow(x['Tinggi']/100,2)

d=pd.DataFrame(x,columns=['Umur','BMI','V']).drop_duplicates()
d.sort_values('BMI',ascending=True).drop_duplicates()

d=pd.DataFrame(x,columns=['Umur','BMI','V'])
d.sort_values('V',ascending=False)

def recommenderUser(umur1,bmi1):
    v = d[(d['BMI'] <=bmi1) & (d['Umur'] <= umur1)]
    maxV=v.mean()
    set1=v.max()
    return (set1) 