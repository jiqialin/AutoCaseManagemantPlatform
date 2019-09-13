
from rest_framework import serializers
from index.models import Config, Group, Department, BusinessLine


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessLine
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        # fields = '__all__'
        fields = ('id', 'groupName')


class ConfigurationSerializer(serializers.ModelSerializer):
    group = GroupSerializer()  # 实例化外键关联表

    class Meta:
        model = Config
        # fields = '__all__'
        fields = ('id', 'moduleName', 'gitAddress', 'modifier', 'caseType', 'modify_time', 'group')
