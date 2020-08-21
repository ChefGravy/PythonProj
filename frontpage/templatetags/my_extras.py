#django custom template tags is where this is all at!!!
from django import template


register = template.Library()
#or using decorators
@register.filter(name='cut')
def cut(value,arg):
    """
    this cuts out all values of 'arg' from the string!
    """
    return value#.replace(arg,'')
#you'll need to register this after done.

#pass what you want to call it and call to function.
#register.filter('cut',cut)
#don't forget to load with {% load my_templates %} at the top of the html
