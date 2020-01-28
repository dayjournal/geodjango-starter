# -*- coding: utf-8 -*-
import os
from django.contrib.gis.utils import LayerMapping
from api.models import Lines

# マッピング
mapping = {
    'full_id': 'full_id',
    'highway': 'highway',
    'name': 'name',
    'geom': 'MULTILINESTRING',
}

# ファイルパス (GeoJSONのパスを指定)
geojson_file = '/Users/ユーザー/app/db/geojson/line_osm.geojson'

# 実行
def run(verbose=True):
    lm = LayerMapping(Lines, geojson_file, mapping, transform=False, encoding='UTF-8')
    lm.save(strict=True, verbose=verbose)
