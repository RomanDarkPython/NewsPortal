from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
    request_data = context['request'].GET.copy()
    for param, value in kwargs.items():
        request_data[param] = value
    return request_data.urlencode()