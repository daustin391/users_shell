from django.urls import path
from users_app import views

urlpatterns = [path("", views.index), path("add-user", views.add_user)]
