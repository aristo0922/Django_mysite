from rest_framework import serializers
from .models import user

class UserSerializer(serializers.ModelSerializer) :
    class Meta :
        model = user        # user 모델 사용
        fields = '__all__'            # 모든 필드 포함