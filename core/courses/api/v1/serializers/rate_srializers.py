from rest_framework import serializers
from courses.models import Rate

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = ['id' ,'score']