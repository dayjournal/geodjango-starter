from rest_framework import viewsets
# シリアライザ読み込み
from .serializers import PointsSerializer, LinesSerializer, PolygonsSerializer
# モデル読み込み
from .models import Points, Lines, Polygons

# ポイントビュー
class PointsViewSet(viewsets.ModelViewSet):
    queryset = Points.objects.all()
    serializer_class = PointsSerializer

# ラインビュー
class LinesViewSet(viewsets.ModelViewSet):
    queryset = Lines.objects.all()
    serializer_class = LinesSerializer

# ポリゴンビュー
class PolygonsViewSet(viewsets.ModelViewSet):
    queryset = Polygons.objects.all()
    serializer_class = PolygonsSerializer
