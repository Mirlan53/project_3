from django.urls import path
from .views import blog_list, blog_create


urlpatterns = [
	path('blog_list', blog_list, name='blog_list'),
	path('blog_create', blog_create, name='blog_create')
]