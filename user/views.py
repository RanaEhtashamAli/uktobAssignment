from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from user.serializers import BaseUserSerializer


class AuthedUserView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = BaseUserSerializer

    def get(self, request):
        user = request.user
        return Response(self.serializer_class(instance=user, context={'request': request}).data)
