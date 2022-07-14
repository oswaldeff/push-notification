from django.http import HttpResponseRedirect
from django.urls import reverse

'''
user authorization
'''


def authorization(function):
    def wrapper(request, *args, **kwargs):
        if request.user.is_anonymous:
            return HttpResponseRedirect(reverse('core:home'))
        return function(request, *args, **kwargs)
    return wrapper
