from django.conf.urls import url
from . import views
from rest_framework.routers import DefaultRouter
from . import tests

router = DefaultRouter()
router.register('sku/search',views.SKUSearchViewSet,base_name='sku_search')

urlpatterns = [
    # url()
    url(r'^categories/$',views.Cate.as_view()),
    url(r'^categories/goodsdetail$',views.GoodsCate.as_view()),
    url(r'^categories/(?P<category>\d+)/goods/$',views.GoodsListView.as_view()),
    url(r'^categories/(?P<category>\d+)/skus/$',views.SKUListView.as_view()),
    url(r'^goods/(?P<goods>\d+)/$',views.SPUModelListView.as_view()),
    url(r'^goods/$',views.GoodsIdView.as_view()),
    url(r'^specifications/(?P<specification>\d+)/$', views.SpecOptionView.as_view()),
    url(r'^sku/(?P<sku>\d+)/$',views.SkuView.as_view()),
    url(r'^sku/(?P<sku>\d+)/specifications/(?P<spec>\d+)/option/(?P<option>\d+)/$',views.SkuSpecView.as_view())

]

urlpatterns += router.urls