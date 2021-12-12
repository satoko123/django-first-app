from django.contrib import admin
from .models import SiteConfig
from django.contrib.sites.models import Site

# 管理画面でPostモデルが表示されるようにする
@admin.register(SiteConfig)
class SiteConfig(admin.ModelAdmin):
  list_display = ('id', 'meta_title')
  list_display_links = ('meta_title',) # 詳細に行くのにクリックする箇所
