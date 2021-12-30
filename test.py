import pandas as pd
import numpy as np
from userFilter import *
from placeFilter import *


tinggi1= 163
berat = 78
bmi2=berat/pow(tinggi1/100,2)
umur2=23


user=recommenderUser(umur2,bmi2)
tempat=filterPlace(user,"Pahang")

a="2"
tahap=filterTahap(tempat,a)
bentuk=filterBentuk(tempat,"Bukit")
negeri=filterNegeri(bentuk,"Terengganu")
print (tahap)