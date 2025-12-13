from rest_framework import status
from rest_framework.response import Response
from .serializers import SignupSerializer,ProfileSerializer
from rest_framework.generics import CreateAPIView,RetrieveAPIView
from .models import User
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated


# Create your views here.
class SignupViewSet(CreateAPIView):
    serializer_class = SignupSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = Token.objects.create(user=user)
        return Response({'token': token.key},status=status.HTTP_201_CREATED)

class ProfileViewSet(RetrieveAPIView):
    serializer_class = ProfileSerializer
    lookup_field = 'username'
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        username = self.kwargs['username']
        queryset = User.objects.filter(username=username)
        return queryset




