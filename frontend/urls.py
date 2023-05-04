from django.urls import path

from .views import MainView, ResultShortenerView


urlpatterns = [
    path('', MainView.as_view()),
    path('result/<id>/', ResultShortenerView.as_view()),

]