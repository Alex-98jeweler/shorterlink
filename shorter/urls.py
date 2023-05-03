from django.urls import path

from .views import UrlView


urlpatterns = [
    path('create_short_link/', UrlView.as_view({'get': "list", 'post': 'create'}), ),

]