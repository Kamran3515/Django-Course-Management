from rest_framework import serializers
from accounts.models import *
from ...models import *

class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id','user','title', 'category','body','published_at']
        
    def create(self, validated_data):
        
        validated_data['user'] = Profile.objects.get(user__id = self.context.get('request').user.id)
        return super().create(validated_data)

    