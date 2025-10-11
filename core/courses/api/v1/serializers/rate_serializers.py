from rest_framework import serializers
from courses.models import Rate


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = ["id", "score", "user", "course"]
        read_only_fields = ["user"]

    def create(self, validated_data):
        request = self.context.get("request")
        user = request.user
        validated_data["user"] = user
        return super().create(validated_data)
