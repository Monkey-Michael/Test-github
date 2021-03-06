import datetime
from haystack import indexes
from .models  import SKU
from .models import GoodsCategory


class SKUIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True,use_template=True)   #创建一个text字段

    num = indexes.IntegerField(model_attr='id')
    # author = indexes.CharField(model_attr='user')
    #
    # pub_date = indexes.DateTimeField(model_attr='pub_date')

    def get_model(self):
        return SKU

    def index_queryset(self, using=None):
        # return self.get_model().objects.filter(is_launched=True)
        return self.get_model().objects.filter(is_launched = True)




