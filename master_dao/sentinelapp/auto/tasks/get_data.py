from .satelite import Satelite
from sentinelapp.models import SentinelData
from numpngw import write_png
import numpy, PIL
from sentinelapp.auto.tasks.satelite.utilsn import plot_image

newstatelite = Satelite()


def get_sentinel_datad():
    print("start...")
    datas = newstatelite.get_data_by_period("2020-06-01", "2020-06-30")
    for data in datas:
        data = data["data"]
        norm_factor = data["userdata.json"]["norm_factor"]
        img = data["default.tif"]
        # plot_image(img, factor=norm_factor, clip_range=(0,1))
        # imgs = write_png("example.png", img)
        # print(imgs)
        print(norm_factor)
        im = PIL.Image.fromarray(numpy.uint8(img))

        print(im)
        # sd = SentinelData(data=data, norm_factor=norm_factor)

    print("end")
