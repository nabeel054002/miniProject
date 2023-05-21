import os
import pandas as pd

folder = '/home/fatim/Downloads/earth_dataset'

# Get a list of all the filenames in the folder
filenames = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]

lon = ['72.25', '72.35', '72.45', '72.55', '72.65', '72.75', '72.85', '72.95', '73.05', '73.15', '73.25', '73.35', '73.45', '73.55', '73.65', '73.75', '73.85']
lat = ['18.05', '18.15', '18.25', '18.35', '18.45', '18.55', '18.65', '18.75', '18.85', '18.95', '19.05', '19.15', '19.25', '19.35', '19.45', '19.55', '19.65', '19.75', '19.85', '19.95', '20.05']
idx=[]
for i in range(len(lon)):
    lon[i] = float(lon[i])
for j in range(len(lon)): 
    lat[j] = float(lat[j])
print(lat)
print(lon)
time = []
precipitation = []
jidx = 0
# Read each file and store the data in the lists
for filename in filenames:
    df_arr = []
    with open(os.path.join(folder, filename)) as file:
        lines = file.readlines()
        #print(lines[18])
        time_local = lines[len(lines)-1]
        time_local = time_local[5:-1]
        time_local = int(time_local)
        print(time_local)
        time.append(time_local)
        lines = lines[1:len(lines)-3]#har ek row 21 ka aur cols 17 hai
        for i in lines: 
            row = i.split(', ')[1:]
            if(len(row)):
                row[-1] = row[-1][:-1]
                # print("idx is ", j)
                for k in range(len(row)):
                    row[k] = float(row[k])
                #print(row)
                df_arr.append(row)
        df = pd.DataFrame(df_arr, index = lat, columns=lon)
        data = []
        for i in df.index:
            for j in df.columns:
                if jidx==0: 
                    idx.append((i,j))
                    print("idx has length", len(idx))
                data.append(df.loc[i,j])
        precipitation.append(data)
    jidx +=1
    print(jidx)
print("rows in precipitation are", len(precipitation))
print("cols in precipitation are", len(precipitation[0]))
print("columns we have", len(time))
print("idx has length", len(idx))

df_prep = pd.DataFrame(precipitation, index = time, columns=idx)
df_prep.to_csv("PrecipitationData.csv")
print(df_prep)
        # print(len(df_arr[0]))
        # print(len(lat))
        # print("len of lat is", len(lat))
        # print("len of lon is", len(lon))`

    # break#to only operate on the very first file
