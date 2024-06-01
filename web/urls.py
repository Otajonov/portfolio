from django.urls import include, path
from .views import index_view


urlpatterns = [
    path('', index_view, name='index'),
]