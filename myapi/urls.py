from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from . import views


# Wire API using automatic URL routing.
urlpatterns = [
    path('', views.CustomerApiView.as_view()),
    path('<str:id>', views.CustomerApiDetailView.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'), 
]