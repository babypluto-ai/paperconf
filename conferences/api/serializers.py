from rest_framework import serializers

from conferences import models

class ConferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Conference
        fields = '__all__'
        read_only_fields = ('submission_link',)