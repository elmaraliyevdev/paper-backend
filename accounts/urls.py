from django.urls import path
from .views import *

urlpatterns = [
    path('login', MyTokenObtainPairView.as_view(), name='login'),
    path("register", register_user, name="register"),
    path("profile", get_user_profile, name="profile"),
    path('profile/update/', update_user_profile, name="user-profile-update"),
]