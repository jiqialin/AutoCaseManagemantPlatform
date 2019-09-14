from index.models import Group

# APIView 方式生成视图
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from .serializer import GroupSerializer

# Create your views here.


@api_view(['GET'])
def groupInfo(request):
    queryset = Group.objects.all()
    page = PageNumberPagination()
    page_roles = page.paginate_queryset(queryset=queryset, request=request, view=groupInfo)
    serializer = GroupSerializer(instance=page_roles, many=True)
    return page.get_paginated_response(serializer.data)
