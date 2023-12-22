from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    UserRegisterView,
    UserLoginView,
    UserLogoutView,
    UserListView,
    UserCreateView,
    UserRetrieveView,
    UserUpdateView,
    UserDestroyView,
)

urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="user-register"),
    path("login/", UserLoginView.as_view(), name="user-login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
    path("logout/", UserLogoutView.as_view(), name="user-logout"),
    path("", UserListView.as_view(), name="user-list"),
    path("create/", UserCreateView.as_view(), name="user-create"),
    path("<int:pk>/", UserRetrieveView.as_view(), name="user-retrieve"),
    path("<int:pk>/update/", UserUpdateView.as_view(), name="user-update"),
    path("<int:pk>/delete/", UserDestroyView.as_view(), name="user-destroy"),
]
