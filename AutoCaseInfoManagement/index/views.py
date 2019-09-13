
from rest_framework.response import Response
from rest_framework import status
import demjson
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes


# Create your views here.


@api_view(['GET'])
@permission_classes([AllowAny, ])
def index(request):
    if request.COOKIES.get('user'):
        data = {'title': 'Welcome to Auto Case Info Management Platform .', 'user': request.COOKIES.get('user')}
    else:
        data = {'title': 'Welcome to Auto Case Info Management Platform .', 'user': 'Anonymous access'}
    response = demjson.encode(data)
    return Response(response, status=status.HTTP_202_ACCEPTED)
