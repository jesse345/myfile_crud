from django.urls import path
from . import views, profile

app_name = 'profile_app'

urlpatterns = [
    path('', views.Home.as_view()),
    path('transact/',profile.Transact.as_view({'get': 'list_profile', 'post': 'add_profile', 'put': 'update_profile' })),
    path('transact/remove/',profile.Transact.as_view({'put': 'remove_profile' })),
]
