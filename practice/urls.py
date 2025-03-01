from django.urls import path

from .views import blog_list_and_add, delete_blog

urlpatterns = [
    path('', blog_list_and_add, name='blogs'),
    path('<int:id>/delete/', delete_blog, name='delete_blog'),
]
