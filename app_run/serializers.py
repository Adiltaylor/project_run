from django.contrib.auth.models import User
from rest_framework import serializers
from app_run.models import Run


class UserSerializer(serializers.ModelSerializer):
    type=serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['id','username','last_name','first_name','type','date_joined']

    def get_type(self,obj):
        if obj.is_staff == True:
            type='coach'
        elif obj.is_staff == False:
            type = 'athlete'
        return type


class UserSerializerRun(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','last_name','first_name']


class RunSerializer(serializers.ModelSerializer):
    athlete = UserSerializerRun(source="athlete",read_only=True)
    class Meta:
        model = Run
        fields = ['id','created_at','comment','athlete']
