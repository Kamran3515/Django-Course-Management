from rest_framework import serializers
from accounts.models import *
from courses.models import *

class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id' ,'teacher' ,'title', 'category','body','image' ,'published_at']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get('request')

        # اگر کاربر ادمین هست، اجازه بده user رو انتخاب کنه
        if request.user and request.user.is_authenticated:
            if request.user.role == 'admin':
                self.fields['teacher'].read_only = False
            else:
                # برای معلم یا سایر کاربران، user read_only بمونه
                self.fields['teacher'].read_only = True

    
    def create(self, validated_data):
        request = self.context.get('request')

        # اگر کاربر ادمین هست و user انتخاب شده بود، از خودش استفاده کن
        if request.user.role != 'admin':
            # برای معلم، user خودش باشه
            validated_data['teacher'] = request.user

        return super().create(validated_data)
