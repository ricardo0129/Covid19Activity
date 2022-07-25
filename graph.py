import json
all_data = []
def split(data):
    if type(data[0][0])==type(1.1):
        all_data.append(data)
        return 
    for i in range(len(data)):
        split(data[i])
    
bad = ["Guam","Commonwealth of the Northern Mariana Islands","Diamond Princess","Grand Princess","Northern Mariana Islands","Virgin Islands","Puerto Rico","United States Virgin Islands","American Samoa","Alaska","Hawaii"]
print(len(bad))
f = open('us-state-boundaries.json')
data = json.load(f)
for i in range(len(data)):
    if data[i]["fields"]["name"] in bad:
        continue
    split(data[i]["fields"]["st_asgeojson"]["coordinates"])
    print(data[i]["fields"]["name"])

f.close()

f = open("usa_map.txt","w")
x_cords = []
y_cords = []
for d in all_data:
    for points in d:
        x_cords.append(points[0])
        y_cords.append(points[1])

f.write(str(min(x_cords))+" "+str(min(y_cords))+" ")
f.write(str(max(x_cords))+" "+str(max(y_cords))+"\n")
for d in all_data:
    f.write(str(len(d))+"\n")
    for points in d:
        f.write(str(points[0])+" "+str(points[1])+"\n")
print(min(x_cords),max(x_cords))
print(min(y_cords),max(y_cords))
