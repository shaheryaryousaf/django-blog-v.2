from django.urls import path
from . import views

urlpatterns = [
	path('<slug>', views.index, name='index'),
	path('category/<slug>', views.category, name='category'),
	path('search/s', views.search, name="search"),
]