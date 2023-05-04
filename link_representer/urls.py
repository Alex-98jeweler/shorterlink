from django.urls import path

from .views import RepresentLinkView

urlpatterns = [
    path('<id>/', RepresentLinkView.as_view(),),
    
]