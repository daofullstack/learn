from sentinelsat import SentinelAPI, read_geojson, geojson_to_wkt
from datetime import date
from collections import OrderedDict

import json

api = SentinelAPI("daosat", "Daosat123456", "https://apihub.copernicus.eu/apihub")


# search by polygon, time, and SciHub query keywords
footprint = "POLYGON ((34.322010 0.401648,36.540989 0.876987,36.884121 -0.747357,34.664474 -1.227940,34.322010 0.401648))"
products = api.query(
    footprint,
    date=("20151011", date(2015, 12, 29)),
    platformname="Sentinel-2",
    cloudcoverpercentage=(0, 30),
)
# products_dict = dict(products)
# print(json.dumps(products, indent=4, default=str))
products_dict = []
for key in products.keys():
    products_dict.append(products[key])

# print(json.dumps(products_dict, indent=4, default=str))

for product in products_dict:
    print(product.get("title"), product.get("link"))


"""
{
        "title": "S2A_MSIL1C_20151226T074332_N0201_R092_T36NZG_20151226T075858",  (CharField)
        "link": "https://apihub.copernicus.eu/apihub/odata/v1/Products('fc65b9a7-9a21-4cf1-a90b-cfbca68545fe')/$value", (CharField)
        "link_alternative": "https://apihub.copernicus.eu/apihub/odata/v1/Products('fc65b9a7-9a21-4cf1-a90b-cfbca68545fe')/", (CharField)
        "link_icon": "https://apihub.copernicus.eu/apihub/odata/v1/Products('fc65b9a7-9a21-4cf1-a90b-cfbca68545fe')/Products('Quicklook')/$value", (CharField)
        "summary": "Date: 2015-12-26T07:43:32.029Z, Instrument: MSI, Satellite: Sentinel-2, Size: 183.48 MB", (CharField)
        "ondemand": "false",(BooleanField)
        "datatakesensingstart": "2015-12-26 07:43:32.029000", (DateTimeField)
        "beginposition": "2015-12-26 07:43:32.029000", (DateTimeField)
        "endposition": "2015-12-26 07:43:32.029000", (DateTimeField)
        "ingestiondate": "2018-12-20 04:02:44.369000", (DateTimeField)
        "orbitnumber": 2663, (IntegerField)
        "relativeorbitnumber": 92, (IntegerField)
        "cloudcoverpercentage": 17.0, (FloatgerField)
        "gmlfootprint": "<gml:Polygon srsName=\"http://www.opengis.net/gml/srs/epsg.xml#4326\" xmlns:gml=\"http://www.opengis.net/gml\">\n   <gml:outerBoundaryIs>\n      <gml:LinearRing>\n         <gml:coordinates>1.80780299,35.69617767 0.81552001,35.69511507 0.81473412,36.68040957 1.80606044,36.6818588 1.80780299,35.69617767 1.80780299,35.69617767</gml:coordinates>\n      </gml:LinearRing>\n   </gml:outerBoundaryIs>\n</gml:Polygon>", (TextField)
        "format": "SAFE", (CharField)
        "instrumentshortname": "MSI", (CharField)
        "sensoroperationalmode": "INS-NOBS", (CharField)
        "instrumentname": "Multi-Spectral Instrument", (CharField)
        "footprint": "MULTIPOLYGON (((36.68040957 0.81473412, 36.6818588 1.80606044, 35.69617767 1.80780299, 35.69511507 0.81552001, 36.68040957 0.81473412)))",  (CharField)
        "s2datatakeid": "GS2A_20151226T074332_002663_N02.01", (CharField)
        "platformidentifier": "2015-028A", (CharField)
        "orbitdirection": "DESCENDING", (CharField)
        "platformserialidentifier": "Sentinel-2A", (CharField)
        "processingbaseline": "02.01", (CharField)
        "processinglevel": "Level-1C", (CharField)
        "producttype": "S2MSI1C", (CharField)
        "platformname": "Sentinel-2", (CharField)
        "size": "183.48 MB", (CharField)
        "tileid": "36NZG", (CharField)
        "hv_order_tileid": "NG36Z", (CharField)
        "filename": "S2A_MSIL1C_20151226T074332_N0201_R092_T36NZG_20151226T075858.SAFE", (CharField)
        "identifier": "S2A_MSIL1C_20151226T074332_N0201_R092_T36NZG_20151226T075858", (CharField)
        "uuid": "fc65b9a7-9a21-4cf1-a90b-cfbca68545fe", (CharField)
        "level1cpdiidentifier": "S2A_OPER_MSI_L1C_TL_SGS__20151226T112710_A002663_T36NZG_N02.01", (CharField)
        "granuleidentifier": "S2A_OPER_MSI_L1C_TL_SGS__20151226T112710_A002663_T36NZG_N02.01", (CharField)
        "datastripidentifier": "S2A_OPER_MSI_L1C_DS_SGS__20151226T112710_S20151226T075858_N02.01" (CharField)
    }

"""
