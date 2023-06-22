from django.urls import path

from .views import RepresentLinkView

urlpatterns = [
    path('<str:id>/', RepresentLinkView.as_view(),),

]
