from django.urls import path

from .views import represent_link_view

urlpatterns = [
    path('<id>/', represent_link_view,),
    
]