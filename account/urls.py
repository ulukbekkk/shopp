from django.urls import path
from .views import RegisterView, SignInView, activate
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('sign_up/', RegisterView.as_view(), name='sign_up'),
    path('login/', SignInView.as_view(), name='login'),
    path('activate/<str:activation_code>/', activate, name='activate'),
    path('logout/', LogoutView.as_view(), name='logout')
]

