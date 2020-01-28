from django.contrib.gis.db import models

# ポイントモデル
class Points(models.Model):
    full_id = models.CharField(max_length=256, null=True)
    name = models.CharField(max_length=256, null=True)
    shop = models.CharField(max_length=256, null=True)
    geom = models.PointField(srid=4326)

# ラインモデル
class Lines(models.Model):
    full_id = models.CharField(max_length=256, null=True)
    highway = models.CharField(max_length=256, null=True)
    name = models.CharField(max_length=256, null=True)
    geom = models.MultiLineStringField(srid=4326)

# ポリゴンモデル
class Polygons(models.Model):
    full_id = models.CharField(max_length=256, null=True)
    building = models.CharField(max_length=256, null=True)
    name = models.CharField(max_length=256, null=True)
    geom = models.MultiPolygonField(srid=4326)
