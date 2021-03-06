"""CJST_Connector URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
# from django.contrib import admin
import xadmin
from django.views.static import serve  # 上传媒体加载包
from .settings.dev_settings import MEDIA_ROOT
from .apps.goods import tests


urlpatterns = [
    url(r'^xadmin/', include(xadmin.site.urls)),
    url(r'users/',include('user.urls')),
    url('',include('goods.urls')),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),  # 指定上传媒体位置
     url(r'^ckeditor/', include('ckeditor_uploader.urls')),

]
