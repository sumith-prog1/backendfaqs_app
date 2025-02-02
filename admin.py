from django.contrib import admin
from .models import FAQ
from ckeditor.widgets import CKEditorWidget
from django import forms

class FAQAdminForm(forms.ModelForm):
    answer = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = FAQ
        fields = '__all__'

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    form = FAQAdminForm
    list_display = ('question', 'answer')
    fieldsets = (
        (None, {'fields': ('question', 'answer')}),
        ('Translations', {'fields': ('question_hi', 'question_bn')}),
    )