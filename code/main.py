from satelite import Satelite

newstatelite = Satelite()

datas = newstatelite.get_data_by_period("2020-06-01", "2020-06-30")

print(datas)
print(len(datas))

for data in datas:
    data = data['data']
    norm_factor = data["userdata.json"]["norm_factor"]
    img = data["default.tif"]
    print(norm_factor)