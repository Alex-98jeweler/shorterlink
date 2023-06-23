from django.shortcuts import render
from django.views import View

from shorter.models import Url


class MainView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'frontend/index.html')


class ResultShortenerView(View):

    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')
        try:
            obj = Url.objects.get(pk=id)
        except Url.DoesNotExist:
            return render(request, 'error.html',)
        host = f"https://{request.get_host()}"
        return render(request, 'frontend/result.html', context={'url': obj, 'host': host})
