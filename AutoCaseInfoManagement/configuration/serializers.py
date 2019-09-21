
from rest_framework import serializers
from index.models import Config, Group


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        # fields = '__all__'
        fields = ('id', 'groupName')


class ConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Config
        # fields = '__all__'
        fields = ('id', 'moduleName', 'gitAddress', 'caseType', 'creator', 'modifier', 'group')


class ConfigSearchSerializer(ConfigurationSerializer):
    group = GroupSerializer()  # 实例化外键关联表

