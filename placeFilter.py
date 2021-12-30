import pandas as pd
import numpy as np
from userFilter import *

tempat = pd.read_csv('Data_Place.csv')
dataTempat= pd.DataFrame(tempat)

p=dataTempat.drop([], axis=1)
p['C']=dataTempat['Jarak Pendakian (KM)']*dataTempat['Tahap kesukaran']

# def filterPlace(place):
#     q=place['V']
#     v = p[(p['C'] <=q)]
#     v.sort_values('C',ascending=True)
#     return (v)

def filterBentuk(p,bentuk):
    x=p[p["Bentuk Muka Bumi"].str.contains(bentuk, na=False)]
    return (x)

def filterNegeri(v,negeri):
    x=v[v["Negeri"].str.contains(negeri, na=False)]
    return (x)

def filterDaerah(v,Daerah):
    x=v[v["Lokasi (Daerah)"].str.contains(Daerah, na=False)]
    return (x)

def filterTahap(v,tahap):
    
    x=v[v["Tahap kesukaran"].str.contains(tahap, na=False)]
    return (x)

def filterJarak(v,jarak):
    x=v[v["Jarak Pendakian (KM)"].str.contains(jarak, na=False)]
    return (x)

def filterKhemah(v,khemah):
    x=v[v["Berkhemah"].str.contains(khemah, na=False)]
    return (x)

def filterPlace(user,negeri):
    q=user['V']
    v = p[(p['C'] <=q)]
    dataTempat=v.sort_values('C',ascending=True)
    jarakChange=dataTempat.replace({'Jarak Pendakian (KM)': {1: '<1', 2: '1 - 2', 3:'2 - 5',4:'5 - 7', 5:'8 - 10',6:'> 10'}})
    tempohChange=jarakChange.replace({'Anggaran Masa': {1: '1 Jam', 2: '1 - 2 Jam', 3:'2 - 3 Jam',4:'4 - 12 Jam', 5:'24 Jam',6:'48 Jam',7:'72 Jam(3Hari)'}})
    tempohChange=tempohChange.replace({'Tahap kesukaran': {1: '1', 2: '2', 3:'3',4:'4', 5:'5',6:'6',7:'7'}})
    r=tempohChange.drop(['C'], axis=1)
    y=r[r["Negeri"].str.contains(negeri, na=False,)]
    y=y.sort_values('Tahap kesukaran',ascending=False)
    return (y)
    
def filterNegeri1(negeri):
    jarakChange=dataTempat.replace({'Jarak Pendakian (KM)': {1: '<1', 2: '1 - 2', 3:'2 - 5',4:'5 - 7', 5:'8 - 10',6:'> 10'}})
    tempohChange=jarakChange.replace({'Anggaran Masa': {1: '1 Jam', 2: '1 - 2 Jam', 3:'2 - 3 Jam',4:'4 - 12 Jam', 5:'24 Jam',6:'48 Jam',7:'72 Jam(3Hari)'}})
    y=tempohChange[tempohChange["Negeri"].str.contains(negeri, na=False)]
    return (y)

def listDaerah(negeri):
    y=dataTempat[dataTempat["Negeri"].str.contains(negeri, na=False)]
    t=y.sort_values('Lokasi (Daerah)',ascending=True)
    t=t.drop_duplicates(subset=['Lokasi (Daerah)'])
    return (t['Lokasi (Daerah)'])

# def filterPlace1(recommender):
#     y=recommender[recommender["Negeri"].str.contains(negeri, na=False,)]
#     y=y.sort_values('Tahap kesukaran',ascending=False)
#     return (y)