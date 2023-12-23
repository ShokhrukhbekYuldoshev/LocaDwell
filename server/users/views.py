from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth.hashers import make_password
from users.models import CustomUser
from .serializers import TokenObtainPairSerializer, CustomUserSerializer
from rest_framework_simplejwt.tokens import RefreshToken


class UserRegisterView(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            token = {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }
            return Response(status=status.HTTP_201_CREATED, data=token)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)


class UserLoginView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer


class UserLogoutView(APIView):
    permission_classes = [IsAuthenticated]

    # blacklist the refresh token, and revoke
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(
                status=status.HTTP_205_RESET_CONTENT,
                data={"message": "Logout successful"},
            )
        except Exception as e:
            print(e)
            return Response(
                status=status.HTTP_400_BAD_REQUEST, data={"message": e.__str__()}
            )


class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    # permission_classes = [IsAuthenticated]


class UserCreateView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdminUser]
    # hash password when create

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # Hash the password
        password = make_password(request.data["password"])
        serializer.validated_data["password"] = password
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )


class UserRetrieveView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    # permission_classes = [IsAuthenticated]


class UserUpdateView(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", True)
        instance = self.get_object()
        # check if the user is the current user (or is an admin)
        if not request.user == instance and not request.user.is_staff:
            print(request.user)
            print(instance)
            return Response(
                status=status.HTTP_403_FORBIDDEN,
                data={"message": "You are not authorized to perform this action."},
            )
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        # Hash the password if it is being updated
        if "password" in request.data:
            password = make_password(request.data["password"])
            serializer.validated_data["password"] = password
        self.perform_update(serializer)
        if getattr(instance, "_prefetched_objects_cache", None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserDestroyView(generics.DestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        # check if the user is the current user (or is an admin)
        if not request.user == instance and not request.user.is_staff:
            return Response(
                status=status.HTTP_403_FORBIDDEN,
                data={"message": "You are not authorized to perform this action."},
            )
        self.perform_destroy(instance)
        return Response(
            status=status.HTTP_204_NO_CONTENT,
            data={"message": "User deleted successfully."},
        )
