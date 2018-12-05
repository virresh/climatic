import pickle
import json

pickle_in = open("data","rb")
dict = pickle.load(pickle_in)

# print(dict)

real_dict={}
for country in dict:
    real_dict[country]={}
    for year_combo in dict[country]:
        if(isinstance(year_combo,list)):
            year=year_combo[0]
            value=year_combo[1]
            real_dict[country][year]=value
        # else:
            # print(type(year_combo))

# print(real_dict)
# print(real_dict['India'])
years=[1800,1900,1920,1950,2000,2005,2010,2013]
yearwise_data={}
for year in years:
    i = str(year)
    yearwise_data[i]={}
    for country in real_dict:
        if(i in real_dict[country]):
            yearwise_data[i][country]=real_dict[country][i]

# print(yearwise_data['2013'])
with open('./yearwise_data.json','w') as fp:
    json.dump(yearwise_data, fp)

# print(yearwise_data['1900'])

for country in yearwise_data['2013']:
    yearwise_data['2013'][country]+=10

CSV_data_2013=[]
# CSV_data_1800
for country in yearwise_data['2013']:
    new_dict={}
    new_dict['country']=country
    new_dict['temp']=yearwise_data['2013'][country]
    CSV_data_2013.append(new_dict)
    

with open('./yearwise_CSV_2050.json','w') as fp:
    json.dump(CSV_data_2013,fp)

