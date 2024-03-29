from index.models import Group, CaseInfo

# APIView 方式生成视图
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from .serializer import CaseInfoSerializer
# Create your views here.
responses = {"code": 0, "errorCode": 0, "msg": "请求成功"}


class CaseInfoClass(APIView):
    def get(self, request):
        groupName = request.GET.get('groupName')
        case_status = request.GET.get('status')

        if groupName or case_status:
            if groupName and case_status:
                queryset = CaseInfo.objects.select_related('group').filter(status=status, group__groupName=groupName).order_by('-id')
                page = PageNumberPagination()
                page_roles = page.paginate_queryset(queryset=queryset, request=request, view=self)
                serializer = CaseInfoSerializer(instance=page_roles, many=True)
                return page.get_paginated_response(serializer.data)

            elif groupName:
                queryset = CaseInfo.objects.select_related('group').filter(group__groupName=groupName).order_by('-id')
                page = PageNumberPagination()
                page_roles = page.paginate_queryset(queryset=queryset, request=request, view=self)
                serializer = CaseInfoSerializer(instance=page_roles, many=True)
                return page.get_paginated_response(serializer.data)

            elif case_status:
                queryset = CaseInfo.objects.select_related('group').filter(status=status).order_by('-id')
                page = PageNumberPagination()
                page_roles = page.paginate_queryset(queryset=queryset, request=request, view=self)
                serializer = CaseInfoSerializer(instance=page_roles, many=True)
                return page.get_paginated_response(serializer.data)

        else:
            queryset = CaseInfo.objects.select_related('group').all().order_by('-id')
            page = PageNumberPagination()
            page_roles = page.paginate_queryset(queryset=queryset, request=request, view=self)
            serializer = CaseInfoSerializer(instance=page_roles, many=True)
            return page.get_paginated_response(serializer.data)


@api_view(['GET'])
def editStatus(request):
    get_id = request.GET.get('id')
    obj = request.GET.get('status')
    CaseInfo.objects.filter(id=get_id).update(status=obj)
    return Response(responses, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def delCaseInfo(request):
    get_id = request.GET.get('id')
    CaseInfo.objects.filter(id=get_id).update(is_deleted=1)
    return Response(responses, status.HTTP_200_OK)

