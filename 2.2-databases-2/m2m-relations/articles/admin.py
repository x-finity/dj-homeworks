from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, ArticleTag, Tag


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        tags = []
        tag_main = False
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            if form.cleaned_data['tag'] in tags:
                raise ValidationError('Тег должен быть уникальным')
            tags.append(form.cleaned_data['tag'])
            if form.cleaned_data['is_main']:
                if tag_main:
                    raise ValidationError('Основный тег должен быть один')
                tag_main = True
            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
            # raise ValidationError('Тут всегда ошибка')
        return super().clean()  # вызываем базовый код переопределяемого метода


class ArticleTagInline(admin.TabularInline):
    model = ArticleTag
    formset = RelationshipInlineFormset
    extra = 0


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'published_at', 'list_tags']
    list_filter = ['published_at']
    search_fields = ['title']
    fields = ['title', 'text', 'published_at', 'image']
    inlines = [ArticleTagInline]

    def list_tags(self, obj):
        return ', '.join([tag.name for tag in obj.tags.all()])


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


# @admin.register(ArticleTag)
# class ArticleTagAdmin(admin.ModelAdmin):
#     list_display = ['article', 'tags', 'is_main']
#     list_filter = ['is_main']
#     fields = ['article', 'tags', 'is_main']

