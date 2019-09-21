
from rest_framework import serializers
from index.models import Group


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
        # fields = ('userName', 'gitUrl', 'starId', 'caseType')
