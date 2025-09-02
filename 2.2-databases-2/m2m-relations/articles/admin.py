from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Tag, Scope
from .models import Article

class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_scopes = 0
        for form in self.forms:
            if form.cleaned_data and 'is_main' in form.cleaned_data and form.cleaned_data['is_main']:
                main_scopes += 1
        if main_scopes > 1:
            raise ValidationError('Нельзя отметить более одного Тега как основной для одной Статьи.')
        return super().clean()

class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset
    extra = 1 # Количество дополнительных полей для добавления новых связей

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]

@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    pass