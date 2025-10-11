# courses/serializers.py
from rest_framework import serializers
from courses.models import Enrollment
from rest_framework.exceptions import ValidationError

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = ['id', 'student', 'course', 'enrolled_at']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get('request')

        if request.user and request.user.is_authenticated:
            if request.user.role == 'admin':
                self.fields['student'].read_only = False
            else:
                self.fields['student'].read_only = True

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        course = validated_data.get('course')
        validated_data['student'] = user

        if Enrollment.objects.filter(student=user, course=course).exists():
            raise ValidationError({'detail': 'You are already registered for this course.'})
        
        return super().create(validated_data)
        
