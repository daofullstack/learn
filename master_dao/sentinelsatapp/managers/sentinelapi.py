from sentinelsat import SentinelAPI, read_geojson, geojson_to_wkt
from datetime import date
from collections import OrderedDict


def get_sentinel_api_data(
    polygon, start, end, sentinel, cloudcoverpercentage_start, cloudcoverpercentage_end
):
    """GET sentinel data

    Args:
        polygon ([str])
        start ([date])
        end ([date])
        sentinel ([choice])
        cloudcoverpercentage_start ([int])
        cloudcoverpercentage_end ([int])

    Returns:
        [json array]
    """
    # search by polygon, time, and SciHub query keywords
    api = SentinelAPI("daosat", "Daosat123456", "https://apihub.copernicus.eu/apihub")
    footprint = polygon
    products = api.query(
        footprint,
        date=(start, end),  # optional
        platformname=sentinel,  # optional
        cloudcoverpercentage=(
            cloudcoverpercentage_start,
            cloudcoverpercentage_end,
        ),  # optional
    )

    products_dict = []
    for key in products.keys():
        products_dict.append(products[key])

    return products_dict
