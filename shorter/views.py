from django.shortcuts import render
from django.http import HttpRequest
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .serializers import UrlSerializer
from .models import Url


class UrlView(ModelViewSet):

    serializer_class = UrlSerializer
    queryset = Url.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        host = request.get_host()
        protocol = 'http'
        if serializer.is_valid():
            obj = serializer.save()
            url = f"{protocol}://{host}/{serializer.data.get('id')}"
            return Response({'id': obj.id, "short_url": url})
        return Response(serializer.errors, status=400)
