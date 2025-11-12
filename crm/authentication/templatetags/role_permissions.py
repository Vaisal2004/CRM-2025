# library is defined as custom tags

# django temples are used to create custom tags

# {% display_name 'Vaisal' as name %}

from django.template import Library

register = Library()

@register.simple_tag
def display_name(name):

    return name.upper()


# {% check_roles request 'Student,Admin' as allow %}

@register.simple_tag
def check_roles(request,roles):

    roles = roles.split(',')

    if request.user.is_authenticated and request.user.role in roles :

        return True
    
    return False