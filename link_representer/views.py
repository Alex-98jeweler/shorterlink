from django.shortcuts import render, redirect
from django.views import View

from shorter.models import Url


class RepresentLinkView(View):

    def get(request, *args, **kwargs):
        id = kwargs.get('id')
        try:
            url = Url.objects.get(pk=id)
        except Url.DoesNotExist:
            return render(request, "error.html")
        return redirect(url.long_url)
