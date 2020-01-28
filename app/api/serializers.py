from rest_framework import serializers
# モデル読み込み
from .models import Points, Lines, Polygons

# ポイントシリアライザ
class PointsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Points
        fields = ('__all__')

# ラインシリアライザ
class LinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lines
        fields = ('__all__')

# ポリゴンシリアライザ
class PolygonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Polygons
        fields = ('__all__')
