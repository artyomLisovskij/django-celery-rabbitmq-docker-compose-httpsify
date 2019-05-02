from django.urls import  include, path
from . import views




from .views import *

urlpatterns = [
    path("", views.index, name="index"),
]
