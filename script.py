import pandas as pd 
import os

path = '/home/fatim/Downloads/earth_dataset'

# print(path)
# print("new line")
# print(os.listdir(path))

file_names = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
data = []
for file_name in file_names:
    with open(os.path.join(path, file_name), 'r') as file:
        #print(file.read())
        data.append(file.read().strip())


df = pd.DataFrame({'data': data})
print(df)
##3B-HHR.MS.MRG.3IMERG.20210815-S113000-E115959.0690.V06B.HDF5