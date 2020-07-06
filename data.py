# -*- coding: utf-8 -*-

import h3

data=[]
mylist=['86186c877ffffff']


for i, name in enumerate(['A','B','C','D','E','F']):
    mylist = [item for sublist in (h3.hex_ring(elem,5) for elem in mylist) for item in sublist]
    mylist = list(set(mylist))
    for j,myh3 in enumerate(mylist):
        data.append(["%.2d:00:00"%(j%(i+1)), myh3, name, 0.0, 0])

datasets = [{"version": "v1",
             "data": {"id": "wve3blg3s",
                      "label": "data.csv",
                      "color": [143, 47, 191],
                      "allData": data, "fields": [
                     {"name": "hour",
                      "type": "timestamp",
                      "format": "H:m:s",
                      "analyzerType": "TIME"},
                     {"name": "H3",
                      "type": "string",
                      "format": "",
                      "analyzerType": "STRING"},
                     {"name": "name",
                      "type": "string",
                      "format": "",
                      "analyzerType": "STRING"},
                     {"name": "count1",
                      "type": "real",
                      "format": "",
                      "analyzerType": "FLOAT"},
                     {"name": "count2",
                      "type": "integer",
                      "format": "",
                      "analyzerType": "INT"}]}}]

config = {"version": "v1", "config": {"visState": {"filters": [
    {"dataId": ["wve3blg3s"], "id": "xa5zqunge", "name": ["hour"], "type": "timeRange",
     "value": [1593997200000,
               1594000800000], "enlarged": True, "plotType": "histogram", "yAxis": None}], "layers": [
    {"id": "e663nl4", "type": "hexagonId",
     "config": {"dataId": "wve3blg3s", "label": "new layer", "color": [218, 112, 191], "columns": {"hex_id": "H3"},
                "isVisible": True, "visConfig": {"opacity": 0.8,
                                                 "colorRange": {"name": "Global Warming", "type": "sequential",
                                                                "category": "Uber",
                                                                "colors": ["#5A1846", "#900C3F", "#C70039", "#E3611C",
                                                                           "#F1920E", "#FFC300"]}, "coverage": 1,
                                                 "enable3d": False, "sizeRange": [0, 500], "coverageRange": [0, 1],
                                                 "elevationScale": 5}, "hidden": False, "textLabel": [
             {"field": None, "color": [255, 255, 255], "size": 18, "offset": [0, 0], "anchor": "start",
              "alignment": "center"}]},
     "visualChannels": {"colorField": {"name": "name", "type": "string"}, "colorScale": "ordinal",
                        "sizeField": None, "sizeScale": "linear", "coverageField": None, "coverageScale": "linear"}}],
    "interactionConfig": {"tooltip": {"fieldsToShow": {
        "wve3blg3s": [{"name": "hour", "format": None},
                      {"name": "H3", "format": None},
                      {"name": "name", "format": None},
                      {"name": "count1", "format": None},
                      {"name": "count2", "format": None}]},
        "enabled": True},
        "brush": {"size": 0.5, "enabled": False},
        "geocoder": {"enabled": False},
        "coordinate": {"enabled": False}},
    "layerBlending": "normal", "splitMaps": [],
    "animationConfig": {"currentTime": None, "speed": 1}},
    "mapState": {"bearing": 0, "dragRotate": False, "latitude": 47.68154776751545,
                 "longitude": 1.0317210930364384, "pitch": 0, "zoom": 5.993949061206434,
                 "isSplit": False}, "mapStyle": {"styleType": "dark", "topLayerGroups": {},
                                                 "visibleLayerGroups": {"label": True,
                                                                        "road": True,
                                                                        "border": False,
                                                                        "building": True,
                                                                        "water": True,
                                                                        "land": True,
                                                                        "3d building": False},
                                                 "threeDBuildingColor": [9.665468314072013,
                                                                         17.18305478057247,
                                                                         31.1442867897876],
                                                 "mapStyles": {}}}}