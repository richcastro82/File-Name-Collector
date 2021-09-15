#RICHARD Castro
#CRAWL DIRECTORY AND COLLECT FILE NAMES

import os
import pathlib
import pandas as pd
path=pathlib.Path().resolve()
files=os.listdir(path)
yourFiles=[]
for f in files:
  yourFiles.append(f)

df=pd.DataFrame(yourFiles)
df.to_csv('yourFileList.csv')
