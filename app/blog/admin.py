from django.contrib import admin
from .models import Category, Tags, Article
from ckeditor.widgets import CKEditorWidget
from django import forms


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    pass


class PostAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Article
        fields = ['title', 'text', 'short_text', 'category', 'Tags', 'user', 'image']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ('title', 'short_text', 'created')
