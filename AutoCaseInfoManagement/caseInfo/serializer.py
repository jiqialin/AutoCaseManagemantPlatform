
from rest_framework import serializers
from index.models import CaseInfo, Group


class MySerializer(serializers.Serializer):  # 反序列化
    id = serializers.IntegerField(read_only=True)
    moduleName = serializers.CharField(required=True, allow_null=False, max_length=100)
    caseName = serializers.CharField(required=True, allow_null=False, max_length=100)
    casePath = serializers.CharField(required=True, allow_null=False, max_length=100)
    caseType = serializers.CharField(required=True, allow_null=False, max_length=100)
    status = serializers.CharField(required=True, allow_null=False, max_length=100)
    userName = serializers.CharField(required=True, allow_null=False, max_length=100)
    group_id = serializers.IntegerField(read_only=True)

    def create(self, validated_data):
        return Group.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.moduleName = validated_data.get('moduleName', instance.moduleName)
        instance.caseName = validated_data.get('caseName', instance.caseName)
        instance.caseType = validated_data.get('caseType', instance.caseType)
        instance.casePath = validated_data.get('casePath', instance.casePath)
        instance.status = validated_data.get('status', instance.status)
        instance.userName = validated_data.get('modifier', instance.userName)
        instance.group_id = validated_data.get('group_id', instance.group_id)
        instance.sava()
        return instance


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        # fields = '__all__'
        fields = ('id', 'groupName', 'businessLine')


class CaseInfoSerializer(serializers.ModelSerializer):
    group = GroupSerializer()

    class Meta:
        model = CaseInfo
        fields = '__all__'
        # fields = ('id', 'caseName', 'type', 'userName', 'status', 'modify_time')

