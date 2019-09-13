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
        queryset = CaseInfo.objects.select_related('group').all()
        page = PageNumberPagination()
        page_roles = page.paginate_queryset(queryset=queryset, request=request, view=self)
        serializer = CaseInfoSerializer(instance=page_roles, many=True)
        # return Response(serializer.data)
        return page.get_paginated_response(serializer.data)  # 使用分页返回对象，自带更详细的返回信息


@api_view(['GET'])
def getPage(request):
    platformName = request.GET.get('platformName')
    status = request.GET.get('status')

    if platformName or status:
        if platformName and status:
            queryset = CaseInfo.objects.select_related('group').filter('status', 'group__platformName')
            page = PageNumberPagination()
            page_roles = page.paginate_queryset(queryset=queryset, request=request, view=getPage)
            serializer = CaseInfoSerializer(instance=page_roles, many=True)
            return page.get_paginated_response(serializer.data)

        elif platformName:
            queryset = CaseInfo.objects.select_related('group').filter('group__platformName')
            page = PageNumberPagination()
            page_roles = page.paginate_queryset(queryset=queryset, request=request, view=getPage)
            serializer = CaseInfoSerializer(instance=page_roles, many=True)
            return page.get_paginated_response(serializer.data)

        elif status:
            queryset = CaseInfo.objects.select_related('group').filter('status')
            page = PageNumberPagination()
            page_roles = page.paginate_queryset(queryset=queryset, request=request, view=getPage)
            serializer = CaseInfoSerializer(instance=page_roles, many=True)
            return page.get_paginated_response(serializer.data)

    else:
        queryset = CaseInfo.objects.select_related('group').all()
        page = PageNumberPagination()
        page_roles = page.paginate_queryset(queryset=queryset, request=request, view=getPage)
        serializer = CaseInfoSerializer(instance=page_roles, many=True)
        return page.get_paginated_response(serializer.data)


@api_view(['POST'])
def editStatus(request):
    if request.method == 'POST':
        get_id = request.POST.get('id')
        obj = request.POST.get('status')
        queryset = CaseInfo.objects.filter(id=get_id).update(status=obj)
        serializer = CaseInfoSerializer(instance=queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(responses, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
    return Response(status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET'])
def delCaseInfo(request):
    if request.method == 'GET':
        get_id = request.GET.get('id')
        CaseInfo.objects.get(id=get_id).delete()
        return Response(responses, status.HTTP_200_OK)
    return Response(status.HTTP_405_METHOD_NOT_ALLOWED)
