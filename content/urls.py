from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('create', views.createContent),
    path('addTopic', views.addTopic),
    path('api-auth-token',obtain_auth_token)
]