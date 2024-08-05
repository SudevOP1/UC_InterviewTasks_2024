from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("django_unchained_details/", views.django_unchained_details, name="django_unchained_details"),
    path("search_results/", views.search_results, name="search_results"),
]
