import pandas as pd
import numpy as np
import math, re
from collections import Counter
from sklearn.preprocessing import OrdinalEncoder

def text_to_vector(text):
    words = re.compile(r"\w+").findall(text)
    words=[word for word in words if not word.isnumeric()]
    words=[word.lower() for word in words]
    return words

#load dataset
df=pd.read_csv("uncleaned_dataset.txt", sep=",")

################# violations/CLASS #####################
violations=df['CONTENTS OF VIOLATION']

#vectorize sentences
violvec=[text_to_vector(violations[i]) for i in range(len(violations))]

#create bag of words to determine most used words
flat_list = [item for sublist in violvec for item in sublist]
flv=Counter(flat_list)
bag={k: v for k, v in sorted(flv.items(), key=lambda item: item[1])}

#based on results, manually create groups
#to determine in which group to classify each violation
class_names=['standard', 'compositional', 'bacteria', 
             'mycotoxin', 'aflatoxin', 'sanitation', 
             'mold', 'smell', 'nasty', 'additive'] 
groups=[]
for i in range(len(violvec)):
    if class_names[1] in violvec[i]: groups.append(1)
    elif class_names[2] in violvec[i]: groups.append(2)
    elif class_names[3] in violvec[i]: groups.append(3)
    elif class_names[4] in violvec[i]: groups.append(4)
    elif class_names[5] in violvec[i]: groups.append(5)
    elif class_names[6] in violvec[i]: groups.append(6)
    elif class_names[7] in violvec[i]: groups.append(7)
    elif class_names[8] in violvec[i]: groups.append(8)
    elif class_names[9] in violvec[i]: groups.append(9)
    else: groups.append(0)

################# item #####################
items=df['ITEM'] #item.unique() gives 2.5k unique items...needs refining

#vectorize sentences
itemvec=[text_to_vector(items[i]) for i in range(len(items))]

#create bag of words to determine most used words
flat_list = [item for sublist in itemvec for item in sublist]
flv=Counter(flat_list)
bag={k: v for k, v in sorted(flv.items(), key=lambda item: item[1])}

#based on results, manually create groups
#to determine in which group to classify each item
class_names=['frozen', 'food', 'heated', 'immediately',
             'fish', 'beans', 'peanuts', 'dried',
             'raw', 'cacao', 'shrimp',
             'rice', 'almonds', 'beverages', 'nuts',
             'meat', 'chocolate', 'corn', 'wheat']
class_names.reverse()
groups_item=[]
for i in range(len(items)):
    if class_names[0] in itemvec[i]: groups_item.append(0)
    elif class_names[1] in itemvec[i]: groups_item.append(1)
    elif class_names[2] in itemvec[i]: groups_item.append(2)
    elif class_names[3] in itemvec[i]: groups_item.append(3)
    elif class_names[4] in itemvec[i]: groups_item.append(4)
    elif class_names[5] in itemvec[i]: groups_item.append(5)
    elif class_names[6] in itemvec[i]: groups_item.append(6)
    elif class_names[7] in itemvec[i]: groups_item.append(7)
    elif class_names[8] in itemvec[i]: groups_item.append(8)
    elif class_names[9] in itemvec[i]: groups_item.append(9)
    elif class_names[10] in itemvec[i]: groups_item.append(10)
    elif class_names[11] in itemvec[i]: groups_item.append(11)
    elif class_names[12] in itemvec[i]: groups_item.append(12)
    elif class_names[13] in itemvec[i]: groups_item.append(13)
    elif class_names[14] in itemvec[i]: groups_item.append(14)
    elif class_names[15] in itemvec[i]: groups_item.append(15)
    elif class_names[16] in itemvec[i]: groups_item.append(16)
    elif class_names[17] in itemvec[i]: groups_item.append(17)
    elif class_names[18] in itemvec[i]: groups_item.append(18)
    else: groups_item.append(19)

################# country #####################
country=OrdinalEncoder().fit_transform(df[['EXPORTING COUNTRY']])
country=country.tolist()
country=[item for sublist in country for item in sublist]

################# shipper #####################
shipper=OrdinalEncoder().fit_transform(df[['SHIPPER']].fillna("0"))
shipper=shipper.tolist()
shipper=[item for sublist in shipper for item in sublist]

################# station #####################
station=OrdinalEncoder().fit_transform(df[['QUARANTIN STATION']].fillna("0"))
station=station.tolist()
station=[item for sublist in station for item in sublist]

################# importers #####################
importers=OrdinalEncoder().fit_transform(df[['NAME OF IMPORTERS']].fillna("0"))
importers=importers.tolist()
importers=[item for sublist in importers for item in sublist]

################# cause of violation #####################
cause=OrdinalEncoder().fit_transform(df[['CAUSE OF VIOLATION']].fillna("0"))
cause=cause.tolist()
cause=[item for sublist in cause for item in sublist]

################# cargo #####################
cargo=OrdinalEncoder().fit_transform(df[['DISPOSAL OF THE CARGO']].fillna("0"))
cargo=cargo.tolist()
cargo=[item for sublist in cargo for item in sublist]

################# remarks #####################
remarks=OrdinalEncoder().fit_transform(df[['DISPOSAL OF THE CARGO']].fillna("0"))
remarks=remarks.tolist()
remarks=[item for sublist in remarks for item in sublist]

################# article #####################
article=OrdinalEncoder().fit_transform(df[['ARTICLE']].fillna("0"))
article=article.tolist()
article=[item for sublist in article for item in sublist]

################# manufacturers #####################
manufacturers=OrdinalEncoder().fit_transform(df[['NAME OF MANUFACTURERS']].fillna("0"))
manufacturers=manufacturers.tolist()
manufacturers=[item for sublist in manufacturers for item in sublist]

################# datetime ######################
date=df['Publication day']
year=[]
month=[]
day=[]
for i in range(len(df)):
    year.append(int(date[i][0:4])-2016)
    month.append(date[i][5:7])
    day.append(date[i][8:])
    
    
#################### CREATE FINAL CLEANED DATASET ##################
complete={'violation':groups, 
          'item':groups_item,
          'country':country,
          'shipper':shipper,
          'station':station,
          'importers':importers,
          'cause':cause,
          'cargo':cargo,
          'remarks':remarks,
          'article':article,
          'manufacturers':manufacturers,
          'year':year,
          'month':month,
          'day':day}    

dataset=pd.DataFrame(complete)
#dataset.to_csv("ready_for_ml.txt", index=False)

