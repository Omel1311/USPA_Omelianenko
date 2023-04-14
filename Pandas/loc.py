import pandas as pd
import openpyxl
q = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%204/Datasets/TopSellingAlbums.xlsx'
qq = pd.read_excel(q)
print(qq)
q.to_excel('hii.xlsx')
print(qq.loc[4,'Artist'])