from django.db import models
from CJST_Connector.utools.Bmodel import BaseModel
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class GoodsCategory(BaseModel):
    name = models.CharField(max_length=20,verbose_name='产品类别')

    class Meta:
        db_table = 'tb_category'
        verbose_name = '产品类别'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Brand(BaseModel):
    name = models.CharField(max_length=20,verbose_name='品牌名称',db_index=True)
    logo = models.ImageField(verbose_name='Logo图片',upload_to='media/brand',null=True)
    first_letter = models.CharField(max_length=1,verbose_name='品牌首字母')

    class Meta:
        db_table = 'tb_brand'
        verbose_name = '品牌'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Series(BaseModel):
    name = models.CharField(max_length=20, verbose_name="系列")

    class Meta:
        db_table = 'tb_series'
        verbose_name = '系列'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name



class Goods(BaseModel):
    '''SPU'''
    name = models.CharField(max_length=50, verbose_name='产品目录')
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, verbose_name='品牌')
    category = models.ForeignKey(GoodsCategory, on_delete=models.PROTECT, verbose_name='类别')
    series = models.ForeignKey(Series, on_delete=models.PROTECT, verbose_name='系列')
    sales = models.IntegerField(default=0, verbose_name='销量')
    class Meta:
        db_table = 'tb_spu'
        verbose_name = '产品目录'
        verbose_name_plural = verbose_name

    def get_spu(self):
        return '%s/%s'%(self.category,self.name,)

    def __str__(self):
        return self.name


class GoodsSpecification(BaseModel):
    '''产品规格分类'''
    goods = models.ForeignKey(Goods,on_delete=models.CASCADE,verbose_name='产品规格')
    name = models.CharField(max_length=20,verbose_name='产品规格类别')

    class Meta:
        db_table = 'tb_goods_specification'
        verbose_name = '产品规格类别'
        verbose_name_plural = verbose_name

    def get_name(self):
        return  self.name

    def __str__(self):
        return '%s : %s '%(self.goods.name,self.name)


class SpecificationOption(BaseModel):
    '''
    规格选项
    '''
    spec = models.ForeignKey(GoodsSpecification,on_delete=models.CASCADE,verbose_name='规格名称')
    value = models.CharField(max_length=20,verbose_name='规格选项值')

    class Meta:
        db_table = 'tb_specification_option'
        verbose_name = '规格选项'
        verbose_name_plural = verbose_name

    def get_value(self):
        return self.value

    def __str__(self):
        return '%s - %s'%(self.spec,self.value)


class SKU(BaseModel):
    name = models.CharField(max_length=50,verbose_name='名称')
    caption = models.CharField(max_length=100,verbose_name='副标题')
    goods = models.ForeignKey(Goods,on_delete=models.CASCADE,verbose_name='产品系列')
    category = models.ForeignKey(GoodsCategory,on_delete=models.PROTECT,verbose_name='从属类别')
    price = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='单价')
    cost_price = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='进价')
    market_price = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='市场价')
    stock = models.IntegerField(default=0,verbose_name='库存')
    sales = models.IntegerField(default=0,verbose_name='销量')
    is_launched = models.BooleanField(default=True, verbose_name='是否上架销售')
    default_image = models.ImageField(default='',verbose_name='默认图片',null=True,upload_to='sku/sku_default_image')
    desc_detail = RichTextUploadingField(default='', verbose_name='详细介绍')
    desc_pack = RichTextField(default='', verbose_name='包装信息')
    desc_service = RichTextUploadingField(default='', verbose_name='售后服务')

    class Meta:
        db_table = 'tb_sku'
        verbose_name = '产品详情'
        verbose_name_plural = verbose_name

    def get_name(self):
        return self.name

    def __str__(self):
        return self.name


class SKUImage(BaseModel):
    sku = models.ForeignKey(SKU,on_delete=models.CASCADE,verbose_name='sku')
    image = models.ImageField(verbose_name='图片',upload_to='sku/sku_images')

    class Meta:
        db_table = 'tb_sku_image'
        verbose_name = '产品图片'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.sku.name


class SKUFile(BaseModel):
    sku = models.ForeignKey(SKU,on_delete=models.CASCADE,verbose_name='sku')
    image = models.FileField(verbose_name='图片',upload_to='static')

    class Meta:
        db_table = 'tb_sku_pdf'
        verbose_name = '产品文件'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.sku.name


class SkuSpecificsation(BaseModel):
    '''sku具体规格'''
    sku = models.ForeignKey(SKU,on_delete=models.CASCADE,verbose_name='sku')
    spec = models.ForeignKey(GoodsSpecification,on_delete=models.PROTECT,verbose_name='规格名称')
    option = models.ForeignKey(SpecificationOption,on_delete=models.PROTECT,verbose_name='规格值')

    class Meta:
        db_table = 'tb_sku_specification'
        verbose_name = '产品详细规格'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s: %s - %s'%(self.sku,self.spec.name,self.option.value)
