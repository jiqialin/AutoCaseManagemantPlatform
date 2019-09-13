
from rest_framework import serializers
from index.models import CaseInfo, Group


class MySerializer(serializers.Serializer):  # 反序列化
    id = serializers.IntegerField(read_only=True)
    caseName = serializers.CharField(required=True, allow_null=False, max_length=100)
    type = serializers.CharField(required=True, allow_null=False, max_length=100)
    status = serializers.CharField(required=True, allow_null=False, max_length=100)
    userName = serializers.CharField(required=True, allow_null=False, max_length=100)
    group_id = serializers.IntegerField(read_only=True)

    def create(self, validated_data):
        return Group.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.caseName = validated_data.get('caseName', instance.caseName)
        instance.type = validated_data.get('type', instance.type)
        instance.status = validated_data.get('status', instance.status)
        instance.userName = validated_data.get('userName', instance.userName)
        instance.group_id = validated_data.get('group_id', instance.group_id)
        instance.sava()
        return instance


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
        # fields = ('id', 'caseName', 'type', 'userName', 'status', 'modify_time')


class CaseInfoSerializer(serializers.ModelSerializer):
    group = GroupSerializer()

    class Meta:
        model = CaseInfo
        fields = '__all__'
        # fields = ('id', 'caseName', 'type', 'userName', 'status', 'modify_time')

