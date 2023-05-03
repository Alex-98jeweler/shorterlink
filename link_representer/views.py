from django.shortcuts import render

from shorter.models import Url


def represent_link_view(request, *args, **kwargs):
    id = kwargs.get('id')
    url = Url.objects.get(pk=id)

