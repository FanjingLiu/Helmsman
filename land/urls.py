
from django.urls import path,include
from . import views
app_name = "land"
urlpatterns = [
    path("",views.homepage, name="homepage"),
    path("",views.homepage, name="homepage")
]