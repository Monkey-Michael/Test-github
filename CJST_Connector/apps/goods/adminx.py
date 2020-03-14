import xadmin
from xadmin import views

from . import models


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True

xadmin.site.register(views.BaseAdminView,BaseSetting)


class GlobalSettings(object):
    site_title = '东莞市捷仕伟连接器后台管理系统'
    site_footer = '东莞市捷仕伟连接器有限公司'
    menu_style = 'accordion'

xadmin.site.register(views.CommAdminView,GlobalSettings)


class SKUAdmin(object):
    model_icon = 'fa fa-gift'
    list_display = ['id','name','price','stock','sales']
    search_fields = ['id','name']
    list_filter = ['category']
    list_editable = ['price','stock']
    show_detail_fields = ['name']
    list_export = ['xls','csv','xml']
    refresh_times = [5, 7]
    style_fields = {'content': 'ueditor'}  #配置插件效果
    show_bookmarks = True

xadmin.site.register(models.SKU, SKUAdmin)


class GoodsCateAdmin(object):
    model_icon = 'fa fa-gift'
    list_display = ['name']
    search_fields = ['name']

    show_detail_fields = ['name']
    list_export = ['xls','csv','xml']
    refresh_times = [5, 7]
    style_fields = {'content': 'ueditor'}  #配置插件效果
    show_bookmarks = True

xadmin.site.register(models.GoodsCategory, GoodsCateAdmin)


class ImageAdmin(object):
    model_icon = 'fa fa-gift'
    list_display = ['id','image']

xadmin.site.register(models.SKUImage, ImageAdmin)


class GoodsAdmin(object):
    model_icon = 'fa fa-gift'
    # list_display = ['id','image']

xadmin.site.register(models.Goods, GoodsAdmin)


class BrandAdmin(object):
    model_icon = 'fa fa-gift'
    # list_display = ['id','image']

xadmin.site.register(models.Brand, BrandAdmin)

class SeriesAdmin(object):
    model_icon = 'fa fa-gift'
    # list_display = ['id','image']

xadmin.site.register(models.Series, SeriesAdmin)

class GoodsSpecificationAdmin(object):
    model_icon = 'fa fa-gift'
    # list_display = ['id','image']

xadmin.site.register(models.GoodsSpecification, GoodsSpecificationAdmin)


class SpecificationOptionAdmin(object):
    model_icon = 'fa fa-gift'
    # list_display = ['id','image']

xadmin.site.register(models.SpecificationOption, SpecificationOptionAdmin)


class SkuSpecificsationAdmin(object):
    model_icon = 'fa fa-gift'

xadmin.site.register(models.SkuSpecificsation, SkuSpecificsationAdmin)