
from rest_framework import serializers
from index.models import CaseInfo, Group


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        # fields = '__all__'
        fields = ('id', 'groupName')


class CaseInfoSerializer(serializers.ModelSerializer):
    # group = GroupSerializer()

    class Meta:
        model = CaseInfo
        fields = '__all__'
        # fields = ('id', 'caseName', 'type', 'userName', 'status', 'modify_time')

