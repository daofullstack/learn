import utils
import os
import datetime
import numpy as np
import matplotlib.pyplot as plt
from sentinelhub import SHConfig


from sentinelhub import (
    MimeType,
    CRS,
    BBox,
    SentinelHubRequest,
    SentinelHubDownloadClient,
    DataCollection,
    bbox_to_dimensions,
    DownloadRequest,
)

from .utilsn import plot_image
from numpngw import write_png


class Satelite:
    def __init__(self, *args):
        self.evalscript = """
            //VERSION=3

            function setup() {
                return {
                    input: [{
                        bands: ["B02", "B03", "B04"],
                        units: "DN"
                    }],
                    output: {
                        bands: 3,
                        sampleType: "INT16"
                    }
                };
            }

            function updateOutputMetadata(scenes, inputMetadata, outputMetadata) {
                outputMetadata.userData = { "norm_factor":  inputMetadata.normalizationFactor }
            }

            function evaluatePixel(sample) {
                return [sample.B04, sample.B03, sample.B02];
            }
        """
        self.config = SHConfig()
        self.betsiboka_coords_wgs84 = [46.16, -16.15, 46.51, -15.58]
        self.resolution = 60
        self.betsiboka_bbox = BBox(bbox=self.betsiboka_coords_wgs84, crs=CRS.WGS84)
        self.betsiboka_size = bbox_to_dimensions(
            self.betsiboka_bbox, resolution=self.resolution
        )

    def get_all_sentinelle(self):
        data_collection = []
        for collection in DataCollection.get_available_collections():
            data_collection.append(collection)

        return data_collection

    def get_data_by_period(self, start, end):
        datas = []
        collections = self.get_all_sentinelle()

        for collection in collections:
            try:
                request_multitype = SentinelHubRequest(
                    evalscript=self.evalscript,
                    input_data=[
                        SentinelHubRequest.input_data(
                            data_collection=collection,
                            time_interval=(start, end),
                            mosaicking_order="leastCC",
                        )
                    ],
                    responses=[
                        SentinelHubRequest.output_response("default", MimeType.TIFF),
                        SentinelHubRequest.output_response("userdata", MimeType.JSON),
                    ],
                    bbox=self.betsiboka_bbox,
                    size=self.betsiboka_size,
                    config=self.config,
                )
                multi_data = request_multitype.get_data()[0]
                data = multi_data.keys()

                output = {}
                output["start"] = start
                output["end"] = end
                #output["collection"] = collection
                output["data"] = multi_data

                datas.append(output)
            except Exception as e:
                #print(str(e))
                pass

        return datas
