from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('create_link/', views.createLink, name="create link"),
    path('trace/<int:link_id>', views.trace, name="trace"),

]