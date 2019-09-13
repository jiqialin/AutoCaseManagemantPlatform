
from rest_framework import serializers
from index.models import Group


class MySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    platformName = serializers.CharField(required=True, allow_null=False, max_length=100)
    businessLine = serializers.CharField(required=True, allow_null=False, max_length=100)
    groupName = serializers.CharField(required=True, allow_null=False, max_length=100)

    def create(self, validated_data):
        return Group.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.platformName = validated_data.get('platformName', instance.platformName)
        instance.businessLine = validated_data.get('businessLine', instance.businessLine)
        instance.groupName = validated_data.get('groupName', instance.groupName)
        instance.sava()
        return instance


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
        # fields = ('userName', 'gitUrl', 'starId', 'caseType')
