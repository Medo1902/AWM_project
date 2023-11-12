from django.urls import path

from . import views
urlpatterns = [
    path ('', views.index, name='index'),

    path('earthquake_likelihood.html', views.likelihood, name='likelihood')
]