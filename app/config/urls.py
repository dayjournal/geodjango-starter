from django.contrib.gis import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

#ビュー読み込み
from api.views import PointsViewSet, LinesViewSet, PolygonsViewSet

# ルーター設定
router = DefaultRouter()
router.register('points', PointsViewSet)
router.register('lines', LinesViewSet)
router.register('polygons', PolygonsViewSet)

urlpatterns = [
    # 管理画面のURLconf読み込み
    path('admin/', admin.site.urls),
    # APIのURLconf読み込み
    path('api/', include(router.urls)),
]
