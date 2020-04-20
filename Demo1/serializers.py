from rest_framework import serializers
from .models import Demo
from .import models

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model=models.Demo
        fields="__all__"