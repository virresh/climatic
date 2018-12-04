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

with open('./data.json','w') as fp:
    json.dump(real_dict, fp)