from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create', views.create),
    path('panda/<int:panda_id>', views.panda_profile),
    path('post/create', views.create_post),
    path('date/create', views.create_date)
]