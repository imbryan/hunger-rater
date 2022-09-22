from . import views
from django.urls import path

app_name = 'hunger-rater'

urlpatterns = [
    path('', views.hungerrater, name='hunger-rater')
]
