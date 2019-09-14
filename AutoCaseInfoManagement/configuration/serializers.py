
from rest_framework import serializers
from index.models import Config, Group


# class MySerializer(serializers.Serializer):  # 反序列化
#     id = serializers.IntegerField(read_only=True)
#     moduleName = serializers.CharField(required=True, allow_null=False, max_length=100)
#     gitAddress = serializers.CharField(required=True, allow_null=False, max_length=100)
#     caseType = serializers.CharField(required=True, allow_null=False, max_length=100)
#     creator = serializers.CharField(required=True, allow_null=False, max_length=100)
#     modifier = serializers.CharField(required=True, allow_null=False, max_length=100)
#     group = serializers.IntegerField(read_only=True)
#
#     def create(self, validated_data):
#         return Group.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.moduleName = validated_data.get('moduleName', instance.moduleName)
#         instance.gitAddress = validated_data.get('gitAddress', instance.gitAddress)
#         instance.caseType = validated_data.get('caseType', instance.caseType)
#         instance.creator = validated_data.get('creator', instance.creator)
#         instance.modifier = validated_data.get('modifier', instance.modifier)
#         instance.group = validated_data.get('group', instance.group)
#         instance.sava()
#         return instance


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        # fields = '__all__'
        fields = ('id', 'groupName')


class ConfigurationSerializer(serializers.ModelSerializer):
    group = GroupSerializer()  # 实例化外键关联表

    class Meta:
        model = Config
        fields = '__all__'
        # fields = ('id', 'moduleName', 'gitAddress', 'modifier', 'caseType', 'modify_time', 'group')
