from django.db import models

# Create your models here.
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles
from pygments.formatters.html import HtmlFormatter
from django.contrib.auth import get_user_model
from pygments import highlight

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

class Snippet(models.Model):
    title  = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    code = models.TextField()
    line_numbering = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    owner = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE, related_name="snippets")
    highlighted = models.TextField()

    class Meta:
        ordering = ['created',]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        lexer = get_lexer_by_name(self.language, )
        linenos = 'table' if self.line_numbering else False
        options = {'title': self.title} if self.title else {}
        formatter = HtmlFormatter(style = self.style, lineos=linenos, full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super().save(*args, **kwargs)