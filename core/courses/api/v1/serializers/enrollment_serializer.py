# courses/serializers.py
from rest_framework import serializers
from courses.models import Enrollment, Course

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = ['id', 'student', 'course', 'enrolled_at']
        read_only_fields = ['student', 'enrolled_at']

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        validated_data['student'] = user
        return super().create(validated_data)
