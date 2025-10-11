from rest_framework import serializers
from courses.models import Lesson
from rest_framework.exceptions import ValidationError


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ["id", "course", "title", "body", "published_at"]

    def create(self, validated_data):
        request = self.context.get("request")
        user = request.user
        course = validated_data.get("course")
        # بررسی اینکه آیا این درس متعلق به همین معلم است
        if course.teacher != user:
            raise ValidationError(
                {"detail": "You can only add lessons to your own courses."}
            )

        return super().create(validated_data)
