from django.urls import path

from .views import RepresentLinkView

urlpatterns = [
    path('redirect/<str:id>/', RepresentLinkView.as_view(),),

]
