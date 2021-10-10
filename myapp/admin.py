from django.contrib import admin
from .models import Post, Like

# 管理画面でPostモデルが表示されるようにする
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
  list_display = ('id', 'author','title', 'created_at')
  list_display_links = ('title',) # 詳細に行くのにクリックする箇所
  ordering = ('-created_at',) # 並び順

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
  list_display = ('id', 'user', 'post')
  list_display_links = ('post',) # 詳細に行くのにクリックする箇所
