from django.contrib import admin
from .models import Post

# 管理画面でPostモデルが表示されるようにする
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'created_at')
  list_display_links = ('title',) # 詳細に行くのにクリックする箇所
  ordering = ('created_at',) # 並び順
