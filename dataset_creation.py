import pandas as pd
import os

all_dir=os.listdir("C:/Users/Euelpis/Desktop/agroknow/downloads")
dataset=pd.read_excel(all_dir[0], header=1)

for i in range(1,len(all_dir)):
    new_file=pd.read_excel(all_dir[i], header=1)
    frames=[dataset, new_file]
    dataset=pd.concat(frames)

#dataset.to_csv("C:/Users/Euelpis/Desktop/agroknow/uncleaned_dataset.txt", index=False)


#removed files named: 
#000736651.xls, 000701286.xls, 000692124.xls 
#because japanese
