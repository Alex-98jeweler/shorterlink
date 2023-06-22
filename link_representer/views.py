from django.shortcuts import render, redirect
from django.views import View

from shorter.models import Url
from .utils import get_url_obj


class RepresentLinkView(View):

    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')
        url = get_url_obj(id)
        if not url:
            return render(request, 'error.html')
        return redirect(url.long_url)
