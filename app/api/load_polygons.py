# -*- coding: utf-8 -*-
import os
from django.contrib.gis.utils import LayerMapping
from api.models import Polygons

# マッピング
mapping = {
    'full_id' : 'full_id',
    'building' : 'building',
    'name' : 'name',
    'geom' : 'MULTIPOLYGON',
}

# ファイルパス (GeoJSONのパスを指定)
geojson_file = '/Users/ユーザー/app/db/geojson/polygon_osm.geojson'

# 実行
def run(verbose=True):
    lm = LayerMapping(Polygons, geojson_file, mapping, transform=False, encoding='UTF-8')
    lm.save(strict=True, verbose=verbose)
