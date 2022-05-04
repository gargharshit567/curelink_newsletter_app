from django.urls import path
from .views import subscribeUser
urlpatterns = [
    path('subscribe', subscribeUser),

]