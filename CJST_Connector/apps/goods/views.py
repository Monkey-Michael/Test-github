from django.shortcuts import render
from drf_haystack.viewsets import HaystackViewSet
from .serializers import SKUIndexSerializer,SKUSerializer,SPU_ModelSerializer,CateSerializer,GoodsSerializer,SpecOptionSerializer,SKUSpecSerializer
from rest_framework.generics import ListAPIView
from .models import SKU,GoodsCategory,GoodsSpecification,Goods,SpecificationOption,SkuSpecificsation
from rest_framework.views import APIView
from rest_framework.response import Response

class Cate(ListAPIView):
    serializer_class = CateSerializer
    queryset = GoodsCategory.objects.all()


class GoodsListView(ListAPIView):
    serializer_class = GoodsSerializer

    def get_queryset(self):
        category = self.kwargs['category']
        return Goods.objects.filter(category=category)


class GoodsCate(APIView):
    '''获取目录'''
    def get(self,request):
        try:
            categoires = GoodsCategory.objects.all()
        except Exception:
            return Response({'Error':'DatabaseError'},status=500)

        Content_Data = {}

        for cate in categoires:
            Content_Data[cate.name] = {}
            for good in  cate.goods_set.all():
                Content_Data[cate.name].setdefault('goods',[]).append(good.name)
                Content_Data[cate.name][good.name + 'stock'] = good.sku_set.all().count()
        return Response(Content_Data)


class SKUListView(ListAPIView):
    '''
    sku信息
    '''
    serializer_class = SKUSerializer

    def get_queryset(self):
        category = self.kwargs['category']
        return SKU.objects.filter(category = category,is_launched = True)


class SPUModelListView(APIView):
    '''
    SPU 型号信息
    '''

    serializer_class = SPU_ModelSerializer

    def get(self,request,goods):
        Data = { }
        goods_query = Goods.objects.filter(id=goods)[0]
        Data['spu_name'] = goods_query.get_spu()
        sepcs = goods_query.goodsspecification_set.all()
        for spec in sepcs:
            sepc_name = spec.get_name()
            options = spec.specificationoption_set.all()
            sepcvaluelist = []
            for opt_value in options:
                sepcvaluelist.append(opt_value.get_value())
            Data[sepc_name] = sepcvaluelist
        return Response(Data)


class SpecOptionView(ListAPIView):
    '''
    SPU 型号信息
    '''

    serializer_class = SpecOptionSerializer

    def get_queryset(self):
        specification = self.kwargs['specification']
        return SpecificationOption.objects.filter(spec = specification )


class SKUSearchViewSet(HaystackViewSet):
    '''
    sku搜索
    '''
    index_models = [SKU]
    serializer_class = SKUIndexSerializer


class SkuSpecView(APIView):
    serializer_class =  SKUSpecSerializer

    def get(self,request,sku,spec,option):
        Data = {}
        sku_query = SKU.objects.filter(id=sku)[0]
        Data['sku'] = sku_query.get_name()
        Data['sepc'] =GoodsSpecification.objects.filter(id=spec)[0].get_name()
        Data['option'] = SpecificationOption.objects.filter(id=option)[0].get_value()
        return Response(Data)


class SkuView(APIView):
    def get(self,request,sku):
        Data = {}
        sku_query = SKU.objects.filter(id=sku)[0]
        Data['sku_name'] = sku_query.get_name()
        sepcs = sku_query.skuspecificsation_set.all()
        params = {}

        for spec in sepcs:
            print(spec)
            params[spec.spec.get_name()] = spec.option.get_value()
        Data['params']= params
        return Response(Data)



class GoodsIdView(ListAPIView):
    serializer_class = GoodsSerializer

    def get_queryset(self):
        return Goods.objects.all()
