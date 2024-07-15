from django import template
from django.template.defaultfilters import stringfilter
from markdown import markdown
from posts.models import Category

register = template.Library()

@register.filter()
@stringfilter
def markdown(value):
    return markdown.markdown(value,extention=['markdown.extentions.fancy_code'])

@register.simple_tag
def get_categories():
    return Category.objects.all()[0:3]
