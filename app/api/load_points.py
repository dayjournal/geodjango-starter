# -*- coding: utf-8 -*-
import os
from django.contrib.gis.utils import LayerMapping
from api.models import Points

# マッピング
mapping = {
    'full_id' : 'full_id',
    'name' : 'name',
    'shop' : 'shop',
    'geom'    : 'POINT',
}

# ファイルパス (GeoJSONのパスを指定)
geojson_file = '/Users/ユーザー/app/db/geojson/point_osm.geojson'

# 実行
def run(verbose=True):
    lm = LayerMapping(Points, geojson_file, mapping, transform=False, encoding='UTF-8')
    lm.save(strict=True, verbose=verbose)
