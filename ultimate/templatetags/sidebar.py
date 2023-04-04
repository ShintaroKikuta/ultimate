from django import template
from blog.models import BlogPost
register = template.Library()

@register.inclusion_tag('sidebar.html')
def sidebar():
    if BlogPost.objects.count() != 0:
        return {'blogpost': BlogPost.objects.latest('date_posted')}
    else:
        return None

# @register.filter('rep')
# def rep(string):
#     return string.replace("a", "b")

