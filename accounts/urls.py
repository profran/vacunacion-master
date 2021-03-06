from django.urls import path
from .views import signup_user, signup_medic, login_account, logout_account

urlpatterns = [
    path('signup/user', signup_user, name='signup_user'),
    path('signup/medic', signup_medic, name='signup_medic'),
    path('login', login_account, name='login_account'),
    path('logout', logout_account, name='logout_account')
]