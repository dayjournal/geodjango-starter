from django.contrib.gis import admin
# モデル読み込み
from api.models import Points, Lines, Polygons

# 管理画面に追加
admin.site.register(Points, admin.GeoModelAdmin)
admin.site.register(Lines, admin.GeoModelAdmin)
admin.site.register(Polygons, admin.GeoModelAdmin)
