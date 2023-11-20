from rest_framework import serializers
from .models import *

class CollegeSerailizer(serializers.ModelSerializer):
    CollegeID = serializers.CharField(label="Enter CollegeID")
    College = serializers.CharField(label="Enter College")

    class Meta:
        model = College
        fields = '__all__'

    def create(self, validated_data):
        return College(**validated_data)

class CurriculumSerailizer(serializers.ModelSerializer):
    class Meta:
        model = CurriculumGuide
        fields = '__all__'