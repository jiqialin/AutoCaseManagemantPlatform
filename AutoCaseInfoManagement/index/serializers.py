
from rest_framework import serializers
from index.models import CaseInfo


class CaseInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseInfo
        fields = '__all__'

