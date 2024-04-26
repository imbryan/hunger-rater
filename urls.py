from . import views
from django.urls import path

app_name = 'hungerrater'

urlpatterns = [
    path('', views.hungerrater, name='hungerrater')
]
