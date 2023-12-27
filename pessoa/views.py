from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from pessoa.models import Pessoa


class Logout(APIView):
    queryset = Pessoa.objects.all()

    def post(self, request, *args, **kwargs):
        request.user.auth_token.delete()
        return Response({'message': 'Deslogado com sucesso!'}, status=status.HTTP_200_OK)
