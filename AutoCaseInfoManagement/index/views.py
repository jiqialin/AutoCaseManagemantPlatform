
from index.models import CaseInfo
from .serializers import CaseInfoSerializer
from rest_framework.response import Response
import demjson
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.renderers import *
from django.db.models import Count
from rest_framework.pagination import PageNumberPagination
from datetime import datetime, date
from datetime import timedelta

# Create your views here.

page = PageNumberPagination()


def get_date(days=0):
    # 格式化为 年月日 形式 2019-02-25
    toDay = (date.today() - timedelta(days=days)).strftime("%Y-%m-%d %H:%M:%S")
    return toDay

    # # 格式化为 年月日时分秒 形式 2019-02-25 10:56:58.609985
    # print(datetime.now() - timedelta(days=days))


@api_view(['GET'])
@permission_classes([AllowAny, ])
def index(request):
    if request.COOKIES.get('user'):
        data = {'title': 'Welcome to Auto Case Info Management Platform .', 'user': request.COOKIES.get('user')}
    else:
        data = {'title': 'Welcome to Auto Case Info Management Platform .', 'user': 'Anonymous access'}
    response = demjson.encode(data)
    return Response(response, status=status.HTTP_202_ACCEPTED)


@api_view(['POST'])
def getBusinessData(request):
    body_dict = demjson.decode(request.body.decode())
    target = body_dict.get('target', '')
    if target:
        queryset = CaseInfo.objects.values(target).filter(create_time__range=(body_dict.setdefault('startTime', get_date(7)),
                                                                              body_dict.setdefault('endTime', get_date())),
                                                          caseType=body_dict.setdefault('caseType', 1),
                                                          status=body_dict.setdefault('status', 0)).annotate(caseNum=Count('id'))
        page_roles = page.paginate_queryset(queryset=queryset, request=request, view=getBusinessData)
        return page.get_paginated_response(page_roles)
    else:
        return Response('The target cannot be empty !', status=status.HTTP_400_BAD_REQUEST)



