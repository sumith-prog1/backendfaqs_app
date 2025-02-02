from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator

translator = Translator()

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()
    question_hi = models.TextField(blank=True)
    question_bn = models.TextField(blank=True)

    def get_translated_question(self, lang):
        return getattr(self, f'question_{lang}', None) or self.question

    def save(self, *args, **kwargs):
        if not self.pk:
            for lang in ['hi', 'bn']:
                try:
                    translated = translator.translate(self.question, dest=lang).text
                    setattr(self, f'question_{lang}', translated)
                except Exception:
                    pass
        super().save(*args, **kwargs)