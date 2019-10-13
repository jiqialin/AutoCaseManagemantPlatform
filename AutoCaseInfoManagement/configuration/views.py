from index.models import Config, Group
from .serializers import ConfigurationSerializer, GroupSerializer, ConfigSearchSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
import demjson, json

# Create your views here.


class ConfigClass(APIView):
    responses = {"code": 0, "errorCode": 0, "msg": "请求成功"}
    errors = {"code": 1, "errorCode": 1, "msg": "Error"}
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = []

    def get(self, request):
        queryset = Config.objects.select_related('group').all().order_by('-id')
        page = PageNumberPagination()
        page_roles = page.paginate_queryset(queryset=queryset, request=request, view=self)
        serializer = ConfigSearchSerializer(instance=page_roles, many=True)
        return page.get_paginated_response(serializer.data)

    def post(self, request):
        get_id = request.GET.get('id')
        git_address = demjson.decode(request.body).get('gitAddress')

        if not git_address.startswith('http') or not git_address.endswith('.git'):
            self.errors['msg'] = 'git address formal error !'
            return Response(self.errors)

        if get_id:
            queryset = Config.objects.filter(id=get_id).first()
            if not queryset:
                self.errors['msg'] = 'unknown ID !'
                return Response(self.errors, status=status.HTTP_400_BAD_REQUEST)

            serializer = ConfigurationSerializer(instance=queryset, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(self.responses, status=status.HTTP_200_OK)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        else:
            serializer = ConfigurationSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(self.responses, status=status.HTTP_200_OK)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        obj = request.GET.get('id')
        Config.objects.filter(id=obj).update(is_deleted=1)
        return Response(self.responses, status=status.HTTP_200_OK)


@api_view()
@permission_classes([AllowAny, ])
def getGroupInfo(request):
    response = dict()
    queryset = Group.objects.values('id', 'groupName').order_by('-id').all()
    serializer = GroupSerializer(instance=queryset, many=True)
    response['group'] = serializer.data
    return Response(response, status=status.HTTP_200_OK)


