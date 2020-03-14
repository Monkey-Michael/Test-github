from drf_haystack.serializers import HaystackSerializer
from rest_framework import serializers
from .models import SKU,GoodsSpecification,GoodsCategory,Goods,SpecificationOption,SkuSpecificsation
from .search_indexes import SKUIndex


class CateSerializer(serializers.ModelSerializer):
    class Meta:
        model= GoodsCategory
        fields = '__all__'

class SpecOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model= SpecificationOption
        fields = '__all__'

class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model= Goods
        fields = '__all__'


class SPU_ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsSpecification
        fields = '__all__'


class SKUSerializer(serializers.ModelSerializer):
    class Meta:
        model = SKU
        fields = '__all__'


class SKUIndexSerializer(HaystackSerializer):
    object = SKUSerializer(read_only=True)

    class Meta:
        index_classes = [SKUIndex]
        fields = ('text','object')


class SKUSpecSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkuSpecificsation
        fields = '__all__'


