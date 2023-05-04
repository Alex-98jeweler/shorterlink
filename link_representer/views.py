from django.shortcuts import render, redirect

from shorter.models import Url


def represent_link_view(request, *args, **kwargs):
    id = kwargs.get('id')
    try:
        url = Url.objects.get(pk=id)
    except Url.DoesNotExist:
        return render(request, "error.html")
    return redirect(url.long_url)
