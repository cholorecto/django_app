from django.urls import path

from .views import LoginView, LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login', LoginView.as_view(), name='signin'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('password_reset/', auth_views.password_reset, name='password_reset'),
    path('password_reset/done/', auth_views.password_reset_done, name='password_reset_done'),
    path('reset/<str:uidb64>/<slug:token>/',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    path('reset/done/', auth_views.password_reset_complete, name='password_reset_complete'),
]