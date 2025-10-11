from rest_framework import serializers
from accounts.models import *
from courses.models import *


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "user", "course", "comment"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get("request")

        # اگر کاربر ادمین هست، اجازه بده user رو انتخاب کنه
        if request:
            if request.user.role == "admin":
                self.fields["user"].read_only = False
            else:
                # برای معلم یا سایر کاربران، user read_only بمونه
                self.fields["user"].read_only = True

    def create(self, validated_data):
        request = self.context.get("request")

        # اگر کاربر ادمین هست و user انتخاب شده بود، از خودش استفاده کن
        if request.user.role != "admin":
            # برای معلم، user خودش باشه
            validated_data["user"] = request.user

        return super().create(validated_data)
