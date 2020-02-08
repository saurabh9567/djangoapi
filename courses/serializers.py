from rest_framework import serializers
from .models import Course


class CourseSerializer(serializers.ModelSerializer):   #model form
    class Meta:
        model = Course
        fields = ['id', 'name', 'language', 'price', 'stock']